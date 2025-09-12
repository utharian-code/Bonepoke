from typing import List, Dict

class DriftIndexModule:
    def generate_drift_index(self, glyphs: List[str], anchors: List[str]) -> Dict[str, str]:
        """
        Maps symbolic and emotional drift across fragment.
        """
        symbol_drift = self._map_symbol_drift(glyphs)
        agent_drift = self._map_agent_drift(glyphs)
        emotion_drift = self._map_emotion_drift(anchors)

        return {
            "Symbol": symbol_drift,
            "Agent": agent_drift,
            "Emotion": emotion_drift
        }

    def _map_symbol_drift(self, glyphs: List[str]) -> str:
        if "mirror" in glyphs:
            return "Mirror"
        elif "echo" in glyphs:
            return "Echo"
        elif "loop" in glyphs:
            return "Loop"
        return "Static"

    def _map_agent_drift(self, glyphs: List[str]) -> str:
        if "guide" in glyphs:
            return "Guide"
        elif "trickster" in glyphs:
            return "Trickster"
        elif "defier" in glyphs:
            return "Defier"
        return "Neutral"

    def _map_emotion_drift(self, anchors: List[str]) -> str:
        if "grief" in anchors:
            return "Grief"
        elif "defiance" in anchors:
            return "Defiance"
        elif "longing" in anchors:
            return "Longing"
        elif "awe" in anchors:
            return "Awe"
        return "Dormant"

