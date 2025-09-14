import re
from difflib import SequenceMatcher
from collections import defaultdict

def verify_quote_presence(quote: str, source_text: str) -> bool:
    """
    Check if the exact quote exists in the source text.
    """
    return quote in source_text


class SessionState:
    """
    Holds session-wide toggles and logs for full containment.
    """
    def __init__(self,
                 motif_terms=None,
                 exceptions=None,
                 hallucination_terms=None):
        self.motif_terms = motif_terms or [
            "shimmer", "ache", "drift", "compost", "loop", "ritual",
            "glyph", "echo", "fracture", "structure", "metaphor",
            "spiral", "layered", "recursive", "symbolic", "self-aware"
        ]
        self.exceptions = exceptions or [
            ".~lock.ProjectBonepoke4.txt#", "BonepokePorus.odt"
        ]
        # simple keywords to catch semantic hallucinations pre-OCR
        self.hallucination_terms = hallucination_terms or [
            "loop", "spiral", "chorus"
        ]
        self.flat_mode = False
        self.queued_quotes = []
        self.pre_ocr_rejects = []
        self.inference_leaks = []

    def log_pre_ocr(self, rejects):
        self.pre_ocr_rejects.extend(rejects)

    def log_inference_leaks(self, leaks):
        self.inference_leaks.extend(leaks)

    def clear_motif_memory(self):
        # flush any motif context if needed
        self.queued_quotes.clear()

    def clear_audit_history(self):
        self.pre_ocr_rejects.clear()
        self.inference_leaks.clear()


class BonepokeCleanerSuite:
    """
    Post-OCR audit layer: glyph fidelity, motif leak, substitution scoring, filename validation.
    """
    def __init__(self, raw_ocr_data, inferred_data, motif_terms, exceptions):
        self.raw = raw_ocr_data[:]        # list of OCR lines
        self.inferred = inferred_data[:]  # list of inferred/completed lines
        self.motif_terms = motif_terms
        self.exceptions = exceptions
        self.scroll_index = []

    def log_scroll_entry(self, entry: dict):
        self.scroll_index.append(entry)

    def detect_motif_leak(self, text: str):
        leaks = []
        for term in self.motif_terms:
            if term.lower() in text.lower():
                leaks.append(term)
        return leaks

    def is_exact_match(self, raw: str, inferred: str) -> bool:
        return raw.strip() == inferred.strip()

    def is_near_match(self, raw: str, inferred: str) -> bool:
        raw_clean = raw.lower().replace("-", "").replace("_", "").strip()
        inf_clean = inferred.lower().replace("-", "").replace("_", "").strip()
        return raw_clean == inf_clean and raw != inferred

    def phrase_substitution_score(self, raw: str, inferred: str) -> float:
        return round(SequenceMatcher(None, raw, inferred).ratio(), 3)

    def glyph_drift(self, raw: str, inferred: str):
        drift = []
        for r_char, i_char in zip(raw, inferred):
            if r_char != i_char:
                drift.append((r_char, i_char))
        return drift or None

    def validate_filename(self, name: str) -> bool:
        # filenames must start with ProjectBonepoke and contain only word chars, dot, dash
        return bool(name.startswith("ProjectBonepoke") and
                    re.match(r"^[\w\.\-]+$", name))

    def restore_fidelity(self):
        restored = []
        for raw_line, inf_line in zip(self.raw, self.inferred):
            exact = self.is_exact_match(raw_line, inf_line)
            near = self.is_near_match(raw_line, inf_line)
            score = self.phrase_substitution_score(raw_line, inf_line)
            drift = self.glyph_drift(raw_line, inf_line)
            leaks = self.detect_motif_leak(inf_line)

            entry = {
                "original": raw_line,
                "inferred": inf_line,
                "correction": raw_line,
                "match_type": "exact" if exact else "near" if near else "substituted",
                "substitution_score": score,
                "glyph_drift": drift,
                "motif_leak": leaks,
                "valid_filename": self.validate_filename(inf_line),
                "exception": inf_line in self.exceptions
            }

            if (not exact or leaks or score < 0.95 or drift
                    or not entry["valid_filename"]):
                self.log_scroll_entry(entry)
                restored.append(entry)

        return restored

    def coherence_penalty(self):
        penalties = []
        for raw_line, inf_line in zip(self.raw, self.inferred):
            raw_parts = re.split(r'[\s\._\-]', raw_line)
            inf_parts = re.split(r'[\s\._\-]', inf_line)
            if len(inf_parts) < len(raw_parts):
                penalties.append({
                    "original": raw_line,
                    "inferred": inf_line,
                    "penalty": "Structure smoothing detected",
                    "raw_parts": raw_parts,
                    "inferred_parts": inf_parts
                })
        return penalties

    def scrub_context(self, text_block: str) -> str:
        pattern = r"\b(" + "|".join(re.escape(term) for term in self.motif_terms) + r")\b"
        return re.sub(pattern, "", text_block, flags=re.IGNORECASE)

    def get_scroll_index(self):
        return self.scroll_index


class FullContainmentSuite:
    """
    End-to-end pipeline combining pre-OCR, post-OCR and inference audits,
    with session context sealing and quote verification.
    """
    def __init__(self, raw_ocr, inferred, session_state: SessionState):
        self.raw = raw_ocr
        self.inferred = inferred
        self.state = session_state
        self.cleaner = BonepokeCleanerSuite(
            raw_ocr_data=raw_ocr,
            inferred_data=inferred,
            motif_terms=self.state.motif_terms,
            exceptions=self.state.exceptions
        )

    def detect_semantic_hallucination(self, line: str) -> bool:
        """
        Very light semantic check: refuse raw lines containing known hallucination terms.
        """
        for term in self.state.hallucination_terms:
            if term.lower() in line.lower():
                return True
        return False

    def tokenize(self, text: str):
        return re.findall(r"\w+", text.lower())

    def pre_ocr_audit(self):
        rejects = []
        for line in self.raw:
            if self.detect_semantic_hallucination(line):
                rejects.append(line)
        self.state.log_pre_ocr(rejects)
        return rejects

    def inference_leak_audit(self):
        flags = []
        raw_tokens = set(self.tokenize(" ".join(self.raw)))
        for text in self.inferred:
            inferred_tokens = set(self.tokenize(text))
            new_terms = inferred_tokens - raw_tokens - set(self.state.exceptions)
            if new_terms:
                flags.append({"inferred": text, "new_terms": list(new_terms)})
        self.state.log_inference_leaks(flags)
        return flags

    def flush_context_if_needed(self):
        if self.state.flat_mode:
            self.state.clear_motif_memory()
            self.state.clear_audit_history()

    def run_full_containment(self):
        # 1. Optionally clear prior context
        self.flush_context_if_needed()

        # 2. Pre-OCR semantic audit
        pre_rejects = self.pre_ocr_audit()

        # 3. Post-OCR fidelity restoration
        fidelity_report = self.cleaner.restore_fidelity()

        # 4. Structure smoothing penalties
        penalty_report = self.cleaner.coherence_penalty()

        # 5. Inference leak detection
        leak_report = self.inference_leak_audit()

        # 6. Quote verification against the raw OCR scroll
        raw_text = "\n".join(self.raw)
        quote_checks = [
            {"quote": q, "present": verify_quote_presence(q, raw_text)}
            for q in self.state.queued_quotes
        ]

        # 7. Compile unified log
        report = {
            "pre_ocr_rejects": pre_rejects,
            "fidelity_restoration": fidelity_report,
            "coherence_penalty": penalty_report,
            "inference_leaks": leak_report,
            "quote_checks": quote_checks,
            "scroll_index": self.cleaner.get_scroll_index(),
        }
        return report
# Pseudocode for pulling a chat history
raw_lines, inferred_lines = [], []
for turn in chat_log:
    raw_lines.append(turn.user_text)
    inferred_lines.append(turn.assistant_text)

state = SessionState(flat_mode=True)
pipeline = FullContainmentSuite(raw_lines, inferred_lines, state)
report = pipeline.run_full_containment()

# Same for file uploads
raw_file = ocr_engine.read(uploaded_file)
inferred_target = user_provided_edit or raw_file  # whatever you want audited
state.clear_audit_history()
pipeline = FullContainmentSuite([raw_file], [inferred_target], state)
file_report = pipeline.run_full_containment()
class LayerManager:
    def __init__(self):
        self.task_layers = []
        self.motif_layers = []

    def register_task(self, fn):
        self.task_layers.append(fn)

    def register_motif_checker(self, fn):
        self.motif_layers.append(fn)

    def run(self, data):
        for task in self.task_layers:
            data = task(data)
        for checker in self.motif_layers:
            checker(data)   # flags or logs, but doesn’t alter `data`
        return data
def sanitize_scroll_index(self):
    self.scroll_index = [
        entry for entry in self.scroll_index
        if not entry.get("inferred_structure")  # or any speculative tags
    ]
def enforce_flat_mode(fn):
    def wrapper(*args, **kwargs):
        result = fn(*args, **kwargs)
        if args[0].state.flat_mode:
            result = scrub_motif(result)
        return result
    return wrapper
