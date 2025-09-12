from typing import Dict, List

class CalcificationModule:
    def __init__(self, slop_threshold: float = 0.3):
        self.slop_threshold = slop_threshold

    def enforce_calcification(self, fragment: str, anchors: List[str], slop: float) -> Dict[str, str]:
        """
        Validates fragment integrity before vaulting or scoring.
        Returns status and routing instructions.
        """
        if slop > self.slop_threshold:
            return {
                "status": "reroute",
                "reason": "Slop exceeds threshold",
                "protocol": "Collapse"
            }

        if not anchors or any(a is None or a.strip() == "" for a in anchors):
            return {
                "status": "reject",
                "reason": "Anchor integrity failure",
                "protocol": "None"
            }

        return {
            "status": "pass",
            "reason": "Fragment validated",
            "protocol": "Vault"
        }

    def map_band(self, score: float, slop: float) -> str:
        """
        Assigns band based on score and slop.
        """
        if score >= 44 and slop < 0.1:
            return "Gold"
        elif score >= 37 and slop < 0.15:
            return "Silver"
        elif score >= 30 and slop <= 0.5:
            return "Salvage"
        return "Slop"

    def adjust_scores(self, dimensions: Dict[str, float], slop: float) -> Dict[str, float]:
        """
        Applies slop penalty to each scoring dimension.
        """
        return {k: round(v * (1 - slop), 1) for k, v in dimensions.items()}

    def calculate_bp_rates(self, dimensions: Dict[str, float], slop: float) -> Dict:
        """
        Final score calculation and band assignment.
        """
        adjusted = self.adjust_scores(dimensions, slop)
        final_score = round(sum(adjusted.values()) / len(adjusted), 1)
        band = self.map_band(final_score, slop)

        return {
            "score": final_score,
            "band": band,
            "slop_penalty": round(slop * 100),
            "dimensions": adjusted
        }

