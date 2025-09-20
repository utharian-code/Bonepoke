# BonepokeOS 4.1.9 — Brainless Tools
# Static scoring engine with Gold, Silver, Salvage, and Slop ranks
# Input-agnostic, motif-free, plain English output
# Includes salvage suggestions and slop indicators

import random

class PBTestSuite:
    def __init__(self):
        self.categories = [
            "Emotional Strength", "Story Flow", "Character Clarity",
            "World Logic", "Dialogue Weight", "Scene Timing", "Reader Engagement"
        ]
        self.fatigue_threshold = 4

    def score(self, fragment):
        scores = {}
        fatigue = self._trace_fatigue(fragment)
        for category in self.categories:
            scores[category] = self._score_category(fragment, category, fatigue)
        return scores, fatigue

    def _score_category(self, fragment, category, fatigue):
        length = len(fragment.split())
        has_dialogue = '"' in fragment or "said" in fragment
        has_action = any(word in fragment for word in ["ran", "moved", "opened", "closed", "looked"])
        has_emotion = any(word in fragment for word in ["felt", "cried", "shouted", "trembled"])
        has_setting = any(word in fragment for word in ["room", "hall", "door", "light", "floor"])

        if category == "Emotional Strength":
            if has_emotion and length > 40:
                return ("Gold", "The emotional tone is strong and sustained.")
            elif has_emotion:
                return ("Silver", "Some emotional moments land, but may feel brief.")
            return ("Salvage", "Emotion is present but underdeveloped.")

        if category == "Story Flow":
            if length > 60 and has_action:
                return ("Gold", "Events connect smoothly and make sense.")
            elif has_action:
                return ("Silver", "The story mostly flows, but some transitions may feel abrupt.")
            return ("Slop", "The story feels disjointed or hard to follow.")

        if category == "Character Clarity":
            if "he" in fragment or "she" in fragment or "I" in fragment:
                return ("Silver", "Characters are present, but emotional logic may wobble.")
            return ("Slop", "Characters feel distant or unclear.")

        if category == "World Logic":
            if has_setting and length > 50:
                return ("Gold", "The world feels internally consistent and grounded.")
            elif has_setting:
                return ("Silver", "Setting is present but may lack clarity.")
            return ("Salvage", "Setting is vague or abstract.")

        if category == "Dialogue Weight":
            if has_dialogue and length > 40:
                return ("Silver", "Dialogue is present and functional.")
            elif has_dialogue:
                return ("Salvage", "Dialogue appears but may lack impact.")
            return ("Slop", "Speech is minimal or missing.")

        if category == "Scene Timing":
            if fatigue:
                return ("Salvage", "Repetition may reflect urgency, but risks dullness.")
            elif length > 60:
                return ("Silver", "Scene transitions are mostly smooth.")
            return ("Slop", "Scene pacing may feel abrupt or unclear.")

        if category == "Reader Engagement":
            if length > 70 and not fatigue:
                return ("Gold", "The fragment holds attention and reads smoothly.")
            elif length > 40:
                return ("Silver", "The story is interesting, but some parts may slow the reader.")
            return ("Salvage", "The fragment may struggle to hold attention.")

        return ("Slop", "Needs major revision.")

    def _trace_fatigue(self, fragment):
        words = fragment.lower().split()
        counts = {word: words.count(word) for word in set(words)}
        return {word: count for word, count in counts.items() if count >= self.fatigue_threshold}

    def salvage_suggestions(self, fragment, fatigue):
        suggestions = []
        lines = fragment.split(".")
        for line in lines:
            if any(term in line for term in ["system", "signal", "threshold", "protocol"]):
                if not any(action in line for action in ["pressed", "moved", "spoke", "acted", "responded"]):
                    suggestions.append(f"Unanchored reference: '{line.strip()}'. Consider adding a visible action or response.")
        for word, count in fatigue.items():
            suggestions.append(f"Repetition alert: '{word}' appears {count} times. May feel excessive or dull.")
        return suggestions

def generate_fragment():
    fragments = [
        "Jake ran through the mall again. The bomb had already been defused, but the timer was active. He triggered the jump. In the lab, the protocol was still running. No one moved.",
        "The council met in silence. The threshold was crossed, but no action followed. A scar remained on the floor, faint but visible.",
        "She repeated the phrase three times. The echo didn’t return. The vault was sealed. No one remembered the gesture.",
        "He looked at the door. The door was closed. He looked again. The door was still closed. He turned. The door remained closed."
    ]
    return random.choice(fragments)

def run_demo():
    pbtests = PBTestSuite()
    fragment = generate_fragment()

    print("\n--- Input Fragment ---\n")
    print(fragment)

    scores, fatigue = pbtests.score(fragment)

    print("\n--- Test Results ---\n")
    for category, (rank, description) in scores.items():
        print(f"{rank} - {category}")
        print(f"{description}\n")

    print("--- Salvage Suggestions ---\n")
    for suggestion in pbtests.salvage_suggestions(fragment, fatigue):
        print(f"- {suggestion}")
    print("\nYou can paste your own fragment to test. This tool runs without setup.\n")

if __name__ == "__main__":
    run_demo()
