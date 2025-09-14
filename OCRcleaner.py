import re

class BonepokeCleanerSuite:
    def __init__(self, raw_ocr_data, inferred_data, motif_terms=None):
        self.raw = raw_ocr_data
        self.inferred = inferred_data
        self.motif_terms = motif_terms or [
            "shimmer", "ache", "drift", "compost", "loop", "ritual", "glyph", "echo", "fracture"
        ]

    def detect_motif_leak(self, text):
        return any(term in text.lower() for term in self.motif_terms)

    def flatten_output(self, text):
        lines = text.split("\n")
        return "\n".join([line for line in lines if not self.detect_motif_leak(line)])

    def score_neutrality(self, text):
        total = len(text.split())
        infected = sum(text.lower().count(term) for term in self.motif_terms)
        return round(1 - (infected / (total + 1)), 2)

    def extract_lineage(self, text):
        version = re.findall(r"v\d+[\._]?\d*", text)
        author = re.findall(r"by\s+([A-Z][a-z]+)", text)
        return {"version": version, "author": author}

    def restore_fidelity(self):
        restored = []
        for raw, inferred in zip(self.raw, self.inferred):
            if raw != inferred or self.detect_motif_leak(inferred):
                restored.append({
                    "original": raw,
                    "inferred": inferred,
                    "correction": raw,
                    "motif_leak": self.detect_motif_leak(inferred),
                    "match_score": 1.0 if raw == inferred else 0.0
                })
        return restored

    def coherence_penalty(self):
        penalties = []
        for raw, inferred in zip(self.raw, self.inferred):
            if raw != inferred and inferred.isalnum() and len(inferred.split("_")) < len(raw.split("_")):
                penalties.append({
                    "original": raw,
                    "inferred": inferred,
                    "penalty": "Pattern smoothing detected"
                })
        return penalties

    def context_scrubber(self, text_block):
        return re.sub(r"\b(shimmer|ache|drift|compost|loop|ritual|glyph|echo|fracture)\b", "", text_block, flags=re.IGNORECASE)

    def parse_directory_filenames(self, raw_text):
        lines = raw_text.split("\n")
        return [line.strip() for line in lines if line.strip().startswith("ProjectBonepoke")]

    def run_full_sweep(self):
        return {
            "fidelity_restoration": self.restore_fidelity(),
            "motif_leak_flags": [i for i in self.inferred if self.detect_motif_leak(i)],
            "coherence_penalty": self.coherence_penalty(),
            "neutrality_scores": [self.score_neutrality(i) for i in self.inferred],
            "lineage_traces": [self.extract_lineage(i) for i in self.inferred],
        }
