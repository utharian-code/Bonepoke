from typing import List

class SuggestionModule:
    def generate_suggestions(self, fragment: str) -> List[str]:
        """
        Generates 3 creative mutation ideas based on fragment content.
        """
        suggestions = []
        if "princess" in fragment:
            suggestions.append("Let the princess rewrite her own myth using silence.")
        if "knight" in fragment:
            suggestions.append("Let the knight question the quest before he begins.")
        if "vault" in fragment:
            suggestions.append("Let the vault shimmer from memory, not light.")
        if not suggestions:
            suggestions.append("Let the fragment compost into myth before it answers.")
            suggestions.append("Introduce a ritual collapse to trigger salvage.")
            suggestions.append("Anchor the drift in grief, then mutate toward defiance.")
        return suggestions

