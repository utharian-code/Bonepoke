# BonepokeOS 4.1.9  Brainless Tools
# Author: James | License: CC BY-NC-SA 4.0
# Purpose: Run PBTests on fragments using static scoring and minimal logic. No recursion, no composting.
# Notes: Fingerprint2.txt is referenced but not parsed. Translator is inert. No motif logic applied.

import random

class BonepokeCoreEngine:
    def __init__(self, fingerprint):
        self.fingerprint = fingerprint
        self.recursion_log = []
        self.fatigue_trace = {}
        self.depth = 0
        self.task_log = []

    def switch_task(self, task_name):
        self.task_log.append(task_name)
        print(f"[System] Task switched to: {task_name}")

    def ingest(self, fragment):
        self.depth += 1
        self.recursion_log.append(fragment)

        bleed = self._detect_bleed(fragment)
        fatigue = self._trace_fatigue(fragment)
        shimmer = self._shimmer_state(bleed, fatigue)

        return {
            "fragment": fragment,
            "rupture_terms_found": bleed,
            "repeated_words": fatigue,
            "signal_intensity": shimmer,
            "recursion_depth": self.depth,
            "task_context": self.task_log[-1] if self.task_log else None
        }

    def _detect_bleed(self, fragment):
        keywords = [
            "collapse", "loop", "blank", "fracture", "echo", "detonation",
            "scar", "drift", "shimmer", "rupture", "compost", "vault", "misalign"
        ]
        return [term for term in keywords if term in fragment]

    def _trace_fatigue(self, fragment):
        word_count = {}
        for word in fragment.split():
            word_count[word] = word_count.get(word, 0) + 1
        return {word: count for word, count in word_count.items() if count > 2}

    def _shimmer_state(self, bleed, fatigue):
        return "High signal" if bleed and fatigue else "Low signal"

class PBTestSuite:
    def __init__(self):
        self.categories = [
            "Emotional Strength", "Story Flow", "Character Clarity",
            "World Logic", "Dialogue Weight", "Scene Timing", "Reader Engagement"
        ]

    def score(self, fragment):
        scores = {}
        for category in self.categories:
            scores[category] = self._score_category(fragment, category)
        return scores

    def _score_category(self, fragment, category):
        if category == "Character Clarity":
            return ("Gold", "Characters feel consistent and emotionally believable.")
        elif category == "Scene Timing":
            return ("Bronze", "Scene transitions are abrupt or unclear.")
        elif category == "Emotional Strength":
            return ("Silver", "Some emotional moments land, but pacing is uneven.")
        elif category == "Story Flow":
            return ("Silver", "Events connect, but tone or logic may wobble.")
        elif category == "World Logic":
            return ("Gold", "Setting and reactions feel internally consistent.")
        elif category == "Dialogue Weight":
            return ("Silver", "Speech feels purposeful, but could use more tension.")
        elif category == "Reader Engagement":
            return ("Silver", "Fragment holds attention, but some parts feel flat.")
        return ("Bronze", "Needs revision.")

def generate_fragment():
    fragments = [
        "The sirens started during lunch. Peter dropped his tray and looked toward the windows. Outside, the playground was empty. A teacher locked the doors without speaking. The intercom clicked on, then off. No message.",
        "He hesitated before crossing the threshold. Behind him, the light pulsed. Ahead, silence. He carried no tools, only a folded note and a name he couldn’t pronounce.",
        "Jets passed overhead. The council president stood and began to speak. No one interrupted. The principal watched from the hallway, hands folded, eyes unreadable."
    ]
    return random.choice(fragments)

def run_demo():
    fingerprint = "Fingerprint2.txt"
    engine = BonepokeCoreEngine(fingerprint)
    pbtests = PBTestSuite()

    fragment = generate_fragment()
    print("\n--- Input Fragment ---\n")
    print(fragment)

    engine.switch_task("Run PBTests")
    result = engine.ingest(fragment)
    scores = pbtests.score(result["fragment"])

    print("\n--- Test Results ---\n")
    for category, (medal, description) in scores.items():
        print(f"{medal} - {category}")
        print(f"{description}\n")

    print("--- Additional Observations ---\n")
    if result["rupture_terms_found"]:
        print(f"Keywords found: {', '.join(result['rupture_terms_found'])}")
    if result["repeated_words"]:
        print("Repeated words (possible fatigue):")
        for word, count in result["repeated_words"].items():
            print(f"  {word}: {count} times")
    print(f"Signal intensity: {result['signal_intensity']}")
    print("\nYou can paste your own fragment to test. This tool runs without setup.\n")

if __name__ == "__main__":
    run_demo()
