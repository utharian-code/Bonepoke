class SymbolicTestModule:
    def run_symbolic_tests(self, fragment: str) -> dict:
        """
        Returns scores and bands for 5 symbolic-emotional dimensions.
        """
        return {
            "Comedic": self._score_band(self._test_comedic(fragment)),
            "Mythic": self._score_band(self._test_mythic(fragment)),
            "Emotional": self._score_band(self._test_emotional(fragment)),
            "Speculative": self._score_band(self._test_speculative(fragment)),
            "Reflective": self._score_band(self._test_reflective(fragment))
        }

    def _score_band(self, score: float) -> dict:
        band = (
            "Slop" if score < 30 else
            "Salvage" if score < 37 else
            "Silver" if score < 44 else
            "Gold"
        )
        return {"score": round(score, 1), "band": band}

    def _test_comedic(self, fragment: str) -> float:
        return 42.0 if "absurd" in fragment else 33.0

    def _test_mythic(self, fragment: str) -> float:
        return 45.0 if "ritual" in fragment else 36.0

    def _test_emotional(self, fragment: str) -> float:
        return 44.0 if "grief" in fragment else 35.0

    def _test_speculative(self, fragment: str) -> float:
        return 43.0 if "future" in fragment else 32.0

    def _test_reflective(self, fragment: str) -> float:
        return 40.0 if "memory" in fragment else 34.0

