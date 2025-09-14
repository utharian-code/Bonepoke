# BonepokeOS 4.2 — Logic-Baked Edition
# Part 1: Motif-free ingest engine
# Detects contradiction, fatigue, and drift using neutral logic

class BonepokeCoreEngine:
    def __init__(self):
        self.fatigue_threshold = 4

    def ingest(self, fragment):
        contradictions = self._detect_contradictions(fragment)
        fatigue = self._trace_fatigue(fragment)
        drift = self._detect_drift(fragment)

        return {
            "fragment": fragment,
            "contradictions": contradictions,
            "fatigue": fatigue,
            "drift": drift
        }

    def _detect_contradictions(self, fragment):
        lines = fragment.lower().split(".")
        contradictions = []
        for line in lines:
            if "already" in line and any(term in line for term in ["still", "again", "active", "running"]):
                contradictions.append(line.strip())
            if "no one moved" in line and any(term in line for term in ["triggered", "jumped", "acted"]):
                contradictions.append(line.strip())
        return contradictions

    def _trace_fatigue(self, fragment):
        words = fragment.lower().split()
        counts = {word: words.count(word) for word in set(words)}
        return {word: count for word, count in counts.items() if count >= self.fatigue_threshold}

    def _detect_drift(self, fragment):
        lines = fragment.split(".")
        drift = []
        for line in lines:
            if any(term in line for term in ["system", "sequence", "signal", "process"]):
                if not any(action in line for action in ["pressed", "moved", "spoke", "acted", "responded", "decided", "changed"]):
                    drift.append(line.strip())
        return drift
# BonepokeOS 4.2 — Logic-Baked Edition
# Part 2: PBTestSuite with motif-free scoring
# Gold, Silver, Salvage, Slop ranks
# Quoted salvage suggestions and slop indicators

class PBTestSuite:
    def __init__(self):
        self.categories = [
            "Emotional Strength", "Story Flow", "Character Clarity",
            "World Logic", "Dialogue Weight", "Scene Timing", "Reader Engagement"
        ]

    def score(self, composted):
        fragment = composted["fragment"]
        contradictions = composted["contradictions"]
        fatigue = composted["fatigue"]
        drift = composted["drift"]

        scores = {}

        # Emotional Strength
        if any(term in fragment for term in ["ran", "again", "reached", "jumped"]):
            if contradictions:
                scores["Emotional Strength"] = ("Salvage", "Tension is present, but reversals may confuse the reader.")
            else:
                scores["Emotional Strength"] = ("Gold", "Urgency and repetition sustain emotional tone.")
        else:
            scores["Emotional Strength"] = ("Silver", "Some emotional cues appear, but may feel brief.")

        # Story Flow
        if contradictions or drift:
            scores["Story Flow"] = ("Slop", "Contradictions or vague references may disrupt the story’s flow.")
        elif any(term in fragment for term in ["jump", "sequence", "lab", "transition"]):
            scores["Story Flow"] = ("Silver", "Scene transitions are present, but may feel abrupt.")
        else:
            scores["Story Flow"] = ("Gold", "Events connect smoothly and make sense.")

        # Character Clarity
        if any(name in fragment for name in ["Jake", "he", "she", "I"]):
            scores["Character Clarity"] = ("Silver", "Character is named and active, but emotional logic may wobble.")
        else:
            scores["Character Clarity"] = ("Slop", "Characters feel distant or unclear.")

        # World Logic
        if drift:
            scores["World Logic"] = ("Salvage", "Setting is referenced, but some elements lack grounding.")
        else:
            scores["World Logic"] = ("Gold", "The world feels internally consistent and readable.")

        # Dialogue Weight
        if '"' in fragment or "said" in fragment:
            scores["Dialogue Weight"] = ("Silver", "Dialogue is present and functional.")
        else:
            scores["Dialogue Weight"] = ("Slop", "Speech is minimal or missing.")

        # Scene Timing
        if fatigue:
            scores["Scene Timing"] = ("Salvage", "Repetition may reflect urgency, but risks dullness.")
        else:
            scores["Scene Timing"] = ("Silver", "Scene transitions are mostly smooth.")

        # Reader Engagement
        if contradictions or drift:
            scores["Reader Engagement"] = ("Slop", "Structural issues may confuse or disengage the reader.")
        elif any(term in fragment for term in ["bomb", "run", "jump", "sequence"]):
            scores["Reader Engagement"] = ("Gold", "High stakes and recursion sustain attention.")
        else:
            scores["Reader Engagement"] = ("Silver", "The story is interesting, but some parts may slow the reader.")

        return scores

    def salvage_suggestions(self, composted):
        suggestions = []

        for line in composted["contradictions"]:
            suggestions.append(f"Possible contradiction: '{line}'. Consider clarifying what resets or persists.")

        for line in composted["drift"]:
            suggestions.append(f"Unanchored reference: '{line}'. Consider adding a visible action or decision.")

        for word, count in composted["fatigue"].items():
            suggestions.append(f"Repetition alert: '{word}' appears {count} times. May feel excessive or dull.")

        return suggestions
def run_demo():
    engine = BonepokeCoreEngine()
    pbtests = PBTestSuite()

    fragment = input("\nPaste your story fragment:\n\n")

    composted = engine.ingest(fragment)
    scores = pbtests.score(composted)

    print("\n--- Test Results ---\n")
    for category, (rank, description) in scores.items():
        print(f"{rank} - {category}")
        print(f"{description}\n")

    print("--- Salvage Suggestions ---\n")
    for suggestion in pbtests.salvage_suggestions(composted):
        print(f"- {suggestion}")

    print("\nYou can paste any fragment to test. This tool runs without setup.\n")

if __name__ == "__main__":
    run_demo()
