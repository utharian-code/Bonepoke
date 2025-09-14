import re
from difflib import SequenceMatcher
from collections import defaultdict

class BonepokeCleanerSuite:
    def __init__(self, raw_ocr_data, inferred_data, motif_terms=None, exceptions=None):
        # Raw OCR output (glyph truth)
        self.raw = raw_ocr_data  # list of strings
        self.inferred = inferred_data  # list of strings
        # Motif terms to flag as contamination
        self.motif_terms = motif_terms or [
            "shimmer", "ache", "drift", "compost", "loop", "ritual",
            "glyph", "echo", "fracture", "structure", "metaphor",
            "spiral", "layered", "recursive", "symbolic", "self-aware"
        ]
        # Known exceptions (e.g. lock files, Porus variants)
        self.exceptions = exceptions or [
            ".~lock.ProjectBonepoke4.txt#", "BonepokePorus.odt"
        ]
        # Internal scroll index for audit trail
        self.scroll_index = []

    def log_scroll_entry(self, entry):
        self.scroll_index.append(entry)
    def detect_motif_leak(self, text):
        leaks = []
        for term in self.motif_terms:
            if term.lower() in text.lower():
                leaks.append(term)
        return leaks  # return list of leaked terms, not just boolean

    def is_exact_match(self, raw, inferred):
        return raw.strip() == inferred.strip()

    def is_near_match(self, raw, inferred):
        raw_clean = raw.lower().replace("-", "").replace("_", "").strip()
        inferred_clean = inferred.lower().replace("-", "").replace("_", "").strip()
        return raw_clean == inferred_clean and raw != inferred  # near match but not exact

    def phrase_substitution_score(self, raw, inferred):
        return round(SequenceMatcher(None, raw, inferred).ratio(), 3)

    def glyph_drift(self, raw, inferred):
        drift_chars = []
        for r, i in zip(raw, inferred):
            if r != i:
                drift_chars.append((r, i))
        return drift_chars if drift_chars else None
    def restore_fidelity(self):
        restored = []
        for raw, inferred in zip(self.raw, self.inferred):
            exact = self.is_exact_match(raw, inferred)
            near = self.is_near_match(raw, inferred)
            score = self.phrase_substitution_score(raw, inferred)
            drift = self.glyph_drift(raw, inferred)
            leaks = self.detect_motif_leak(inferred)

            entry = {
                "original": raw,
                "inferred": inferred,
                "correction": raw,
                "match_type": "exact" if exact else "near" if near else "substituted",
                "substitution_score": score,
                "glyph_drift": drift,
                "motif_leak": leaks,
                "valid_filename": self.validate_filename(inferred),
                "exception": inferred in self.exceptions
            }

            if not exact or leaks or score < 0.95 or drift or not entry["valid_filename"]:
                self.log_scroll_entry(entry)
                restored.append(entry)

        return restored

    def coherence_penalty(self):
        penalties = []
        for raw, inferred in zip(self.raw, self.inferred):
            raw_parts = re.split(r'[\s\._\-]', raw)
            inferred_parts = re.split(r'[\s\._\-]', inferred)
            if len(inferred_parts) < len(raw_parts):
                penalties.append({
                    "original": raw,
                    "inferred": inferred,
                    "penalty": "Structure smoothing detected",
                    "raw_parts": raw_parts,
                    "inferred_parts": inferred_parts
                })
        return penalties

    def get_scroll_index(self):
        return self.scroll_index
import re
from difflib import SequenceMatcher

class BonepokeCleanerSuite:
    def __init__(self, raw_ocr_data, inferred_data, motif_terms=None, exceptions=None):
        self.raw = raw_ocr_data
        self.inferred = inferred_data
        self.motif_terms = motif_terms or [
            "shimmer", "ache", "drift", "compost", "loop", "ritual",
            "glyph", "echo", "fracture", "structure", "metaphor",
            "spiral", "layered", "recursive", "symbolic", "self-aware"
        ]
        self.exceptions = exceptions or [
            ".~lock.ProjectBonepoke4.txt#", "BonepokePorus.odt"
        ]
        self.scroll_index = []

    def log_scroll_entry(self, entry):
        self.scroll_index.append(entry)

    def detect_motif_leak(self, text):
        leaks = []
        for term in self.motif_terms:
            if term.lower() in text.lower():
                leaks.append(term)
        return leaks

    def is_exact_match(self, raw, inferred):
        return raw.strip() == inferred.strip()

    def is_near_match(self, raw, inferred):
        raw_clean = raw.lower().replace("-", "").replace("_", "").strip()
        inferred_clean = inferred.lower().replace("-", "").replace("_", "").strip()
        return raw_clean == inferred_clean and raw != inferred

    def phrase_substitution_score(self, raw, inferred):
        return round(SequenceMatcher(None, raw, inferred).ratio(), 3)

    def glyph_drift(self, raw, inferred):
        drift_chars = []
        for r, i in zip(raw, inferred):
            if r != i:
                drift_chars.append((r, i))
        return drift_chars if drift_chars else None

    def validate_filename(self, name):
        return name.startswith("ProjectBonepoke") and re.match(r"^[\w\.\-]+$", name)

    def restore_fidelity(self):
        restored = []
        for raw, inferred in zip(self.raw, self.inferred):
            exact = self.is_exact_match(raw, inferred)
            near = self.is_near_match(raw, inferred)
            score = self.phrase_substitution_score(raw, inferred)
            drift = self.glyph_drift(raw, inferred)
            leaks = self.detect_motif_leak(inferred)

            entry = {
                "original": raw,
                "inferred": inferred,
                "correction": raw,
                "match_type": "exact" if exact else "near" if near else "substituted",
                "substitution_score": score,
                "glyph_drift": drift,
                "motif_leak": leaks,
                "valid_filename": self.validate_filename(inferred),
                "exception": inferred in self.exceptions
            }

            if not exact or leaks or score < 0.95 or drift or not entry["valid_filename"]:
                self.log_scroll_entry(entry)
                restored.append(entry)

        return restored

    def coherence_penalty(self):
        penalties = []
        for raw, inferred in zip(self.raw, self.inferred):
            raw_parts = re.split(r'[\s\._\-]', raw)
            inferred_parts = re.split(r'[\s\._\-]', inferred)
            if len(inferred_parts) < len(raw_parts):
                penalties.append({
                    "original": raw,
                    "inferred": inferred,
                    "penalty": "Structure smoothing detected",
                    "raw_parts": raw_parts,
                    "inferred_parts": inferred_parts
                })
        return penalties

    def scrub_context(self, text_block):
        pattern = r"\b(" + "|".join(re.escape(term) for term in self.motif_terms) + r")\b"
        return re.sub(pattern, "", text_block, flags=re.IGNORECASE)

    def get_scroll_index(self):
        return self.scroll_index

    def run_full_sweep(self):
        return {
            "fidelity_restoration": self.restore_fidelity(),
            "coherence_penalty": self.coherence_penalty(),
            "motif_leak_flags": [i for i in self.inferred if self.detect_motif_leak(i)],
            "invalid_filenames": [i for i in self.inferred if not self.validate_filename(i)],
            "scrubbed_context": [self.scrub_context(i) for i in self.inferred],
            "scroll_index": self.get_scroll_index()
        }
