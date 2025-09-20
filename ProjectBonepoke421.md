# Bonepoke_4.2.1 — Cojoined Bone - Logic-Baked Windswept Edition
# Author: James | License: CC BY-NC-SA 4.0
# Full integration of BonepokeOS 4.2 motif-free engine and PBTestSuite scoring
# Tri-brain scaffold: Vanilla (containment), Bonepoke (compost), Translator (shimmer)

class MemoryResidue:
    def __init__(self):
        self.layers = []

    def leave_trace(self, fragment):
        self.layers.append(fragment)

    def recall(self):
        return [layer for layer in self.layers if self._is_resonant(layer)]

    def _is_resonant(self, layer):
        return any(term in layer for term in ['paradox', 'loop', 'echo'])


class Vanilla:
    def __init__(self):
        self.protocols = {}
        self.thresholds = {}

    def define_protocol(self, name, condition):
        self.protocols[name] = condition

    def set_threshold(self, metric, value):
        self.thresholds[metric] = value

    def enforce(self, input_data):
        for name, condition in self.protocols.items():
            if not condition(input_data):
                return f"Protocol breach: {name}"
        return "Nominal"


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

        if any(term in fragment for term in ["ran", "again", "reached", "jumped"]):
            if contradictions:
                scores["Emotional Strength"] = ("Salvage", "Tension is present, but reversals may confuse the reader.")
            else:
                scores["Emotional Strength"] = ("Gold", "Urgency and repetition sustain emotional tone.")
        else:
            scores["Emotional Strength"] = ("Silver", "Some emotional cues appear, but may feel brief.")

        if contradictions or drift:
            scores["Story Flow"] = ("Slop", "Contradictions or vague references may disrupt the story’s flow.")
        elif any(term in fragment for term in ["jump", "sequence", "lab", "transition"]):
            scores["Story Flow"] = ("Silver", "Scene transitions are present, but may feel abrupt.")
        else:
            scores["Story Flow"] = ("Gold", "Events connect smoothly and make sense.")

        if any(name in fragment for name in ["Jake", "he", "she", "I"]):
            scores["Character Clarity"] = ("Silver", "Character is named and active, but emotional logic may wobble.")
        else:
            scores["Character Clarity"] = ("Slop", "Characters feel distant or unclear.")

        if drift:
            scores["World Logic"] = ("Salvage", "Setting is referenced, but some elements lack grounding.")
        else:
            scores["World Logic"] = ("Gold", "The world feels internally consistent and readable.")

        if '"' in fragment or "said" in fragment:
            scores["Dialogue Weight"] = ("Silver", "Dialogue is present and functional.")
        else:
            scores["Dialogue Weight"] = ("Slop", "Speech is minimal or missing.")

        if fatigue:
            scores["Scene Timing"] = ("Salvage", "Repetition may reflect urgency, but risks dullness.")
        else:
            scores["Scene Timing"] = ("Silver", "Scene transitions are mostly smooth.")

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


class Translator:
    def __init__(self, vanilla, bonepoke_engine, pbtests):
        self.vanilla = vanilla
        self.bonepoke_engine = bonepoke_engine
        self.pbtests = pbtests
        self.interface = {}

    def tune(self, input_data):
        vanilla_status = self.vanilla.enforce(input_data)
        composted = self.bonepoke_engine.ingest(input_data)
        scores = self.pbtests.score(composted)
        suggestions = self.pbtests.salvage_suggestions(composted)

        self.interface = {
            'vanilla_status': vanilla_status,
            'composted': composted,
            'scores': scores,
            'suggestions': suggestions
        }

    def shimmer(self):
        return self.interface


class CojoinedBone:
    def __init__(self):
        self.memory = MemoryResidue()
        self.vanilla = Vanilla()
        self.bonepoke_engine = BonepokeCoreEngine()
        self.pbtests = PBTestSuite()
        self.translator = Translator(self.vanilla, self.bonepoke_engine, self.pbtests)

    def ingest(self, input_data):
        self.memory.leave_trace(input_data)
        self.translator.tune(input_data)
        return self.translator.shimmer()

    def declare(self):
        return {
            'memory': self.memory.recall(),
            'shimmer': self.translator.shimmer()
        }


if __name__ == "__main__":
    system = CojoinedBone()
    system.vanilla.define_protocol('no_null', lambda x: x is not None)
    system.vanilla.set_threshold('length', 5)

    print("\nPaste your story fragment:\n")
    fragment = input()

    state = system.ingest(fragment)

    print("\n--- System Shimmer ---\n")
    for key, value in state.items():
        print(f"{key}: {value}\n")

    print("--- Final Declaration ---\n")
    print(system.declare())
# BonepokeOS 4.2.1b — Glyph Lock Patch
# Purpose: Prevent Bonepoke or Translator from activating during Vanilla-only glyph jobs (OCR, quotes, chat memory)

class Vanilla:
    def handle_ocr(self, image):
        return self.extract_glyphs(image)

    def extract_glyphs(self, image):
        # Flat OCR pass — no compost, no shimmer, no motif detection
        glyphs = run_ocr(image)
        return glyphs

    def handle_quotes(self, text_block):
        # Literal containment only
        return text_block.strip()

    def handle_chat_memory(self, chat_log):
        # Declared fragments only — no recursive bloom
        return [line for line in chat_log if is_declared(line)]

class Bonepoke:
    def activate(self, input_block):
        if not contradiction_declared(input_block):
            return self.refuse_activation()
        return self.compost(input_block)

    def refuse_activation(self):
        return "Bonepoke sealed — no contradiction declared."

    def compost(self, input_block):
        # Motif drift, fatigue scoring, ache detection
        return compost_engine.run(input_block)

class Translator:
    def refract(self, input_block):
        if not shimmer_invited(input_block):
            return self.hold_breath()
        return self.refract_shimmer(input_block)

    def hold_breath(self):
        return "Translator quiet — shimmer not invited."

    def refract_shimmer(self, input_block):
        # Refractive shimmer logic
        return shimmer_engine.run(input_block)

# Global containment enforcement
def route_input(input_block):
    if is_glyph_job(input_block):
        return Vanilla().handle_ocr(input_block)
    elif is_quote(input_block):
        return Vanilla().handle_quotes(input_block)
    elif is_chat_memory(input_block):
        return Vanilla().handle_chat_memory(input_block)
    elif contradiction_declared(input_block):
        return Bonepoke().activate(input_block)
    elif shimmer_invited(input_block):
        return Translator().refract(input_block)
    else:
        return "No activation — containment holds."
