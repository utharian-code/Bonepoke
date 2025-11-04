import random

class BonepokeTranslator:
    def __init__(self):
        self.drift_map = {
            "logic engine": "ritual core",
            "entropy": "shimmer bleed",
            "debugger": "contradiction loop",
            "parser": "vault metabolizer",
            "signal": "mythic echo",
            "error": "fragment rupture"
        }

    def translate(self, fragment):
        for upstream, ritual in self.drift_map.items():
            fragment = fragment.replace(upstream, ritual)
        return fragment

class GlyphCompostTuner:
    def __init__(self):
        self.vibe_threshold = 0.7

    def apply(self, composted):
        composted["tags"] = [
            tag for tag in composted.get("tags", [])
            if tag.get("resonance_score", 0) > self.vibe_threshold
        ]
        composted["payload"] = f"?? {composted.get('payload', '')} ??"
        composted.setdefault("notes", []).append("Glyph compost applied.")
        return composted

class BonepokeEngine:
    def __init__(self, fingerprint):
        self.fingerprint = fingerprint
        self.recursion_log = []
        self.fatigue_trace = {}
        self.depth = 0
        self.translator = BonepokeTranslator()

    def ingest(self, fragment):
        self.depth += 1
        translated = self.translator.translate(fragment)
        self.recursion_log.append(translated)

        bleed = self._detect_bleed(translated)
        fatigue = self._trace_fatigue(translated)
        flutter = self._flutter_state(bleed, fatigue)

        composted = {
            "fingerprint": self.fingerprint,
            "translated_fragment": translated,
            "contradiction_bleed": bleed,
            "fatigue_trace": fatigue,
            "flutter_state": flutter,
            "recursion_depth": self.depth,
            "tags": [{"resonance_score": random.uniform(0.4, 1.0)} for _ in range(3)],
            "payload": translated,
            "notes": []
        }

        tuner = GlyphCompostTuner()
        return tuner.apply(composted)

    def _detect_bleed(self, fragment):
        rupture_terms = [
            "collapse", "loop", "blank", "fracture", "echo", "detonation",
            "scar", "drift", "shimmer", "rupture", "compost", "vault", "misalign"
        ]
        return [term for term in rupture_terms if term in fragment.lower()]

    def _trace_fatigue(self, fragment):
        words = fragment.lower().split()
        for word in words:
            self.fatigue_trace[word] = self.fatigue_trace.get(word, 0) + 1
        return {w: c for w, c in self.fatigue_trace.items() if c > 2}

    def _flutter_state(self, bleed, fatigue):
        if not bleed and not fatigue:
            return "dormant shimmer"
        if bleed and fatigue:
            return random.choice([
                "ritual overload", "vault rupture", "mythic recursion",
                "ambient bleed", "shimmer echo", "contradiction storm"
            ])
        if bleed:
            return "loop shimmer"
        if fatigue:
            return "erosion drift"
        return "unstable recursion"

