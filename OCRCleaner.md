import re
from difflib import SequenceMatcher

class GenericOCRCorrectorSuite:
    """
    Generic OCR audit and correction suite.
    Line-agnostic, pluggable, and motif-free.
    """
    def __init__(self, raw_lines, inferred_lines,
                 validators=None,
                 scorers=None,
                 suppressors=None,
                 config=None):
        self.raw = raw_lines[:]
        self.inferred = inferred_lines[:]
        self.validators = validators or []
        self.scorers = scorers or []
        self.suppressors = suppressors or []
        self.config = config or {}
        self.audit_log = []

    def detect_drift(self, raw: str, inferred: str):
        drift = []
        for r_char, i_char in zip(raw, inferred):
            if r_char != i_char:
                drift.append((r_char, i_char))
        return drift or None

    def aggregate_scores(self, score_dict):
        if not score_dict:
            return None
        return round(sum(score_dict.values()) / len(score_dict), 3)

    def run_audit(self):
        for raw, inf in zip(self.raw, self.inferred):
            entry = {
                "raw": raw,
                "inferred": inf,
                "scores": {},
                "aggregate_score": None,
                "issues": [],
                "drift": None
            }

            for scorer in self.scorers:
                name = scorer.__name__
                score = scorer(raw, inf)
                entry["scores"][name] = score

            entry["aggregate_score"] = self.aggregate_scores(entry["scores"])
            if entry["aggregate_score"] is not None and entry["aggregate_score"] < self.config.get("score_threshold", 0.95):
                entry["issues"].append("Low aggregate score")

            for validator in self.validators:
                if not validator(inf):
                    entry["issues"].append("Validation failed")

            for suppressor in self.suppressors:
                if suppressor(inf):
                    entry["issues"].append("Suppressed content")

            drift = self.detect_drift(raw, inf)
            if drift:
                entry["drift"] = drift
                entry["issues"].append("Glyph drift")

            self.audit_log.append(entry)

        return self.audit_log

Use Control + Shift + m to toggle the tab key moving focus. Alternatively, use esc then tab to move to the next interactive element on the page.
New File at / · utharian-code/Bonepoke
 





