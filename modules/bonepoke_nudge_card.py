from typing import List

class NudgeCardModule:
    def generate_nudge_card(self, fragment: str) -> str:
        """
        Generates a micro-ritual mutation idea ?60 words.
        """
        if "princess" in fragment:
            return "Let the princess rewrite her own quest using silence as a weapon."
        elif "knight" in fragment:
            return "Let the knight doubt his sword before he lifts it."
        elif "vault" in fragment:
            return "Let the vault shimmer not from light, but from memory."
        return "Let the fragment compost itself into myth before it answers."

