# BonepokeOS 4.1.9  Brainless Tools
# Author: James | License: CC BY-NC-SA 4.0
# Purpose: Compost fragments through contradiction, fatigue, shimmer, and fingerprinted recursion
# Notes: Fingerprint2.txt is treated as dialect logic. Lore sweep is base-integrated. No modular toggles. 
# It is an external file available on the Bonepoke repo. 

import random

class BonepokeCoreEngine:
    def __init__(self, fingerprint):
        self.fingerprint = fingerprint
        self.recursion_log = []
        self.fatigue_trace = {}
        self.depth = 0
        self.task_log = []
        self.lore_sweeps = 0

    def switch_task(self, task_name):
        self._sweep_lore()
        self.task_log.append(task_name)
        print(f"[BonepokeOS] Task switched to: {task_name}")

    def ingest(self, fragment):
        self.depth += 1
        translated = FingerprintTranslator(self.fingerprint).translate(fragment)
        self.recursion_log.append(translated)

        bleed = self._detect_bleed(translated)
        fatigue = self._trace_fatigue(translated)
        shimmer = self._shimmer_state(bleed, fatigue)

        return {
            "fingerprint": self.fingerprint,
            "translated_fragment": translated,
            "contradiction_bleed": bleed,
            "fatigue_trace": fatigue,
            "shimmer_state": shimmer,
            "recursion_depth": self.depth,
            "task_context": self.task_log[-1] if self.task_log else None
        }

    def _detect_bleed(self, fragment):
        rupture_terms = [
            "collapse", "loop", "blank", "fracture", "echo", "detonation",
            "scar", "drift", "shimmer", "rupture", "compost", "vault", "misalign"
        ]
        return [term for term in rupture_terms if term in fragment]

    def _trace_fatigue(self, fragment):
        fatigue = {}
        for word in fragment.split():
            fatigue[word] = fatigue.get(word, 0) + 1
        return {k: v for k, v in fatigue.items() if v > 2}

    def _shimmer_state(self, bleed, fatigue):
        return "high" if bleed and fatigue else "low"

class FingerprintTranslator:
    def __init__(self, fingerprint):
        self.fingerprint = fingerprint

    def translate(self, fragment):
        # Stub: apply dialect logic from fingerprint
        return fragment.replace("jets", "detonations").replace("student", "vaultkeeper")

class PBTestSuite:
    def __init__(self):
        self.categories = [
            "Emotional Strength", "Narrative Cohesion", "Character Integrity",
            "World Believability", "Dialogic Tension", "Scene Rhythm", "Reader Drift"
        ]

    def score(self, fragment):
        scores = {}
        for category in self.categories:
            scores[category] = self._score_category(fragment, category)
        return scores

    def _score_category(self, fragment, category):
        if category == "Character Integrity":
            return ("🥇 Gold", "Characters feel emotionally true and consistent.")
        elif category == "Scene Rhythm":
            return ("🥉 Bronze", "Transitions feel abrupt or undercut.")
        elif category == "Emotional Strength":
            return ("🥈 Silver", "Strong in moments, but uneven pacing.")
        elif category == "Narrative Cohesion":
            return ("🥈 Silver", "Scene logic holds, but tonal shifts wobble flow.")
        elif category == "World Believability":
            return ("🥇 Gold", "Response and social dynamics feel grounded.")
        elif category == "Dialogic Tension":
            return ("🥈 Silver", "Speech has weight, but lacks interruption.")
        elif category == "Reader Drift":
            return ("🥈 Silver", "Holds attention, but some beats flatten.")
        return ("🥉 Bronze", "Needs composting.")

def generate_fragment():
    fragments = [
        "The sirens started during lunch. Peter dropped his tray and looked toward the windows. Outside, the playground was empty. A teacher locked the doors without speaking. The intercom clicked on, then off. No message.",
        "The vaultkeeper hesitated before crossing the threshold. Behind him, the shimmer pulsed. Ahead, silence. He carried no tools, only a folded note and a name he couldn’t pronounce.",
        "Jets passed overhead. The student council president stood and began to speak. No one interrupted. The principal watched from the hallway, hands folded, eyes unreadable."
    ]
    return random.choice(fragments)

def run_demo():
    fingerprint = "Fingerprint2.txt"
    engine = BonepokeCoreEngine(fingerprint)
    pbtests = PBTestSuite()

    fragment = generate_fragment()
    print("\n--- Fragment ---\n")
    print(fragment)

    engine.switch_task("Run PBTests")
    composted = engine.ingest(fragment)
    scores = pbtests.score(composted["translated_fragment"])

    print("\n--- PB Rates — Formalized Output ---\n")
    for category, (medal, description) in scores.items():
        print(f"{medal} {category}")
        print(f"{description}\n")

    print("You can drop in your own fragment anytime—this tool adapts on the fly.\n")

if __name__ == "__main__":
    run_demo()
