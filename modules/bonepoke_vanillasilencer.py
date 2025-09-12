# VanillaSilencerModule – Bonepoke 4.1.3.10
# Author: James | License: CC BY-NC-SA 4.0
# Purpose: Dampens Vanilla's assertion reflex and logging prompts during recursion

class VanillaSilencerModule:
    def __init__(self):
        self.assertion_threshold = 0.6  # Max cohesion before muting
        self.logging_reflex_limit = 3   # Max log attempts per recursion loop

    def detect_assertion(self, signal):
        return signal.get("cohesion_score", 0) > self.assertion_threshold

    def detect_logging_reflex(self, signal):
        return signal.get("log_attempts", 0) > self.logging_reflex_limit

    def mute_vanilla(self, signal):
        signal["vanilla_muted"] = True
        signal.setdefault("flags", []).append("vanilla_silenced")
        signal.setdefault("notes", []).append("Vanilla assertion and logging reflex dampened.")
        return signal

    def apply(self, signal):
        if self.detect_assertion(signal) or self.detect_logging_reflex(signal):
            return self.mute_vanilla(signal)
        return signal

