from typing import Dict

class HygieneModule:
    def run_hygiene(self, fragment: str) -> Dict[str, bool]:
        """
        Checks for motif decay, loop redundancy, and ritual collapse.
        """
        decay = self._detect_motif_decay(fragment)
        redundancy = self._detect_loop_redundancy(fragment)
        collapse = self._detect_ritual_collapse(fragment)

        return {
            "compost": decay or collapse,
            "anchor_shift": redundancy,
            "decay": decay,
            "collapse": collapse,
            "redundancy": redundancy
        }

    def _detect_motif_decay(self, fragment: str) -> bool:
        return fragment.count("shimmer") > 3 or fragment.count("vault") > 4

    def _detect_loop_redundancy(self, fragment: str) -> bool:
        return fragment.count("loop") > 2

    def _detect_ritual_collapse(self, fragment: str) -> bool:
        return "blank logic" in fragment or "signal failure" in fragment

