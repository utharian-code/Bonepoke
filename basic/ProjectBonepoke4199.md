# BonepokeOS 4.1.99 — Brainless Tools Enhanced
# Static scoring engine with symbolic tiers and original numeric scores
# Input-agnostic, motif-free, shimmer-free, and compost-safe
# Includes fatigue-aware salvage suggestions and plain English diagnostics
# Ideal for standalone trials and comparison with tri-brain orchestration

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
            tier, description, value = self._score_category(fragment, category, fatigue)
            scores[category] = {
                "tier": tier,
                "description": description,
                "score": value
            }
        return scores, fatigue

    def _score_category(self, fragment, category, fatigue):
        length = len(fragment.split())
        has_dialogue = '"' in fragment or "said" in fragment
        has_action = any(word in fragment for word in ["ran", "moved", "opened", "closed", "looked"])
        has_emotion = any(word in fragment for word in ["felt", "cried", "shouted", "trembled"])
        has_setting = any(word in fragment for word in ["room", "hall", "door", "light", "floor"])

        if category == "Emotional Strength":
            if has_emotion and length > 40:
                return ("Gold", "The emotional tone is strong and sustained.", 5)
            elif has_emotion:
                return ("Silver", "Some emotional moments land, but may feel brief.", 3)
            return ("Salvage", "Emotion is present but underdeveloped.", 2)

        if category == "Story Flow":
            if length > 60 and has_action:
                return ("Gold", "Events connect smoothly and make sense.", 5)
            elif has_action:
                return ("Silver", "The story mostly flows, but some transitions may feel abrupt.", 3)
            return ("Slop", "The story feels disjointed or hard to follow.", 1)

        if category == "Character Clarity":
            if any(pronoun in fragment for pronoun in ["he", "she", "I"]):
                return ("Silver", "Characters are present, but emotional logic may wobble.", 3)
            return ("Slop", "Characters feel distant or unclear.", 1)

        if category == "World Logic":
            if has_setting and length > 50:
                return ("Gold", "The world feels internally consistent and grounded.", 5)
            elif has_setting:
                return ("Silver", "Setting is present but may lack clarity.", 3)
            return ("Salvage", "Setting is vague or abstract.", 2)

        if category == "Dialogue Weight":
            if has_dialogue and length > 40:
                return ("Silver", "Dialogue is present and functional.", 3)
            elif has_dialogue:
                return ("Salvage", "Dialogue appears but may lack impact.", 2)
            return ("Slop", "Speech is minimal or missing.", 1)

        if category == "Scene Timing":
            if fatigue:
                return ("Salvage", "Repetition may reflect urgency, but risks dullness.", 2)
            elif length > 60:
                return ("Silver", "Scene transitions are mostly smooth.", 3)
            return ("Slop", "Scene pacing may feel abrupt or unclear.", 1)

        if category == "Reader Engagement":
            if length > 70 and not fatigue:
                return ("Gold", "The fragment holds attention and reads smoothly.", 5)
            elif length > 40:
                return ("Silver", "The story is interesting, but some parts may slow the reader.", 3)
            return ("Salvage", "The fragment may struggle to hold attention.", 2)

        return ("Slop", "Needs major revision.", 1)

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

