# Bonepoke_4.3.5 — Cojoined Bone – Front-loaded Efficiency 
# Author: James | License: CC BY-NC-SA 4.0
# Full integration of BonepokeOS 4.2 compost-defined engine and PBTestSuite shimmer scoring
# Tri-brain scaffold: Vanilla (containment), Bonepoke (compost), Translator (shimmer)

from uuid import uuid4
import time

# --- Core utilities --------------------------------------------------------

class MemoryResidue:
    def __init__(self):
        self.layers = []
    def leave_trace(self, fragment):
        self.layers.append(fragment)
    def recall(self):
        terms = {'paradox', 'loop', 'echo', 'ache', 'shimmer'}
        return [layer for layer in self.layers if any(term in str(layer).lower() for term in terms)]

class ShimmerBudget:
    def __init__(self, limit=25, weights=None):
        self.limit = limit
        self.used = 0
        self.trace = []
        # default weights
        self.weights = weights or {'shimmer': 1, 'ache': 2, 'drift': 2, 'rupture': 3, 'recursion': 3}
    def register(self, event):
        weight = self.weights.get(event, 1)
        self.used += weight
        self.trace.append((event, self.used, time.time()))
        status = {
            "used": self.used,
            "limit": self.limit,
            "safe": self.used < self.limit,
            "reroute": self.used >= self.limit,
            "message": f"{self.used}/{self.limit} shimmer-used"
       }
        return status
    def reset(self):
        self.used = 0
        self.trace = []

class MotifDecay:
    def __init__(self, threshold=1):
        self.motif_counts = {}
        self.threshold = threshold
    def register(self, motif):
        self.motif_counts[motif] = self.motif_counts.get(motif, 0) + 1
    def decay_score(self):
        return {motif: count for motif, count in self.motif_counts.items() if count > self.threshold}

class RuptureCooldown:
    def __init__(self, cooldown=5):
        self.last_trigger = {}
        self.cooldown = cooldown
    def can_trigger(self, rupture_type, tick):
        last = self.last_trigger.get(rupture_type, -self.cooldown)
        if tick - last >= self.cooldown:
            self.last_trigger[rupture_type] = tick
            return True
        return False

class LineageEcho:
    def __init__(self):
        self.lineage = {}
    def mark(self, fragment_id, parent_id=None):
        self.lineage[fragment_id] = parent_id
    def trace(self, fragment_id):
        path = []
        while fragment_id:
            path.append(fragment_id)
            fragment_id = self.lineage.get(fragment_id)
        return path[::-1]

class Compost:
    def __init__(self, ache=None, motif=None, rupture=None):
        self.ache = ache
        self.motif = motif
        self.rupture = rupture
    def metabolize(self):
        return {
            "ache": self.ache,
            "motif": self.motif,
            "rupture": self.rupture,
            "status": "composted",
            "viability": "safe",
            "containment_score": "delayed reroute"
        }

def is_composted(fragment):
    return isinstance(fragment, dict) and fragment.get("status") == "composted"

# --- Core engine -----------------------------------------------------------

class BonepokeCoreEngine:
    def __init__(self, fatigue_threshold=3, shimmer_limit=25, motif_threshold=1, rupture_cd=5):
        self.fatigue_threshold = fatigue_threshold
        self.shimmer_budget = ShimmerBudget(limit=shimmer_limit)
        self.motif_decay = MotifDecay(threshold=motif_threshold)
        self.rupture_cooldown = RuptureCooldown(cooldown=rupture_cd)
        self.lineage_echo = LineageEcho()
        self.tick = 0
    def ingest(self, fragment, fragment_id=None, parent_id=None):
        self.tick += 1
        if fragment_id:
            self.lineage_echo.mark(fragment_id, parent_id)
        
        contradictions = self._detect_contradictions(fragment)
        fatigue = self._trace_fatigue(fragment)
        drift = self._compost_drift(fragment)
        marm = self._flicker_marm(fragment, contradictions, fatigue, drift)

        # register a generic shimmer event (could be more specific)
        shimmer_status = self.shimmer_budget.register("shimmer")

        # register motif counts
        for term in ['loop', 'ache', 'echo', 'shimmer']:
            if term in fragment.lower():
                self.motif_decay.register(term)
        
        rupture_triggered = self.rupture_cooldown.can_trigger("rupture", self.tick)

        return {
            "fragment": fragment,
            "contradictions": contradictions,
            "fatigue": fatigue,
            "drift": drift,
            "marm": marm,
            "shimmer_status": shimmer_status,
            "motif_decay": self.motif_decay.decay_score(),
            "rupture_triggered": rupture_triggered,
            "lineage": self.lineage_echo.trace(fragment_id) if fragment_id else []
        }
    def _detect_contradictions(self, fragment):
        lines = fragment.lower().split(".")
        return [line.strip() for line in lines if any(t in line for t in ["already", "still", "again"]) and "not" in line]
    def _trace_fatigue(self, fragment):
        words = fragment.lower().split()
        return {w: words.count(w) for w in set(words) if words.count(w) >= self.fatigue_threshold}
    def _compost_drift(self, fragment):
        lines = fragment.split(".")
        return [line.strip() for line in lines if any(t in line for t in ["system", "sequence", "signal", "process", "loop"]) and not any(a in line for a in ["pressed", "moved", "spoke", "acted", "responded", "decided", "changed"])]
    def _flicker_marm(self, fragment, contradictions, fatigue, drift):
        score = 0
        text = fragment.lower()
        if any(t in text for t in ['ache', 'loop', 'shimmer', 'echo']):
            score += 1
        score += min(len(contradictions), 2)
        score += 1 if fatigue else 0
        score += 1 if drift else 0
        if score >= 3:
            return "MARM: active"
        elif score == 2:
            return "MARM: flicker"
        return "MARM: suppressed"

# --- PBTestSuite: symbolic + numeric --------------------------------------

class PBTestSuite:
    def __init__(self):
        self.categories = [
            "Emotional Strength", "Story Flow", "Character Clarity",
            "World Logic", "Dialogue Weight", "Scene Timing",
            "Reader Engagement", "Shimmer Budget", "Motif Decay",
            "Rupture Cooldown", "Lineage Echo"
       ]
    def score(self, composted):
        fragment = composted["fragment"]
        shimmer_status = composted.get("shimmer_status", {})
        motif_decay = composted.get("motif_decay", {})
        rupture_triggered = composted.get("rupture_triggered", False)
        lineage = composted.get("lineage", [])

        symbolic = {}
        numeric = {}

        def assign(category, tier, value):
            symbolic[category] = tier
            numeric[category] = value

        assign("Emotional Strength", "Gold" if "ache" in fragment else "Silver", 5 if "ache" in fragment else 3)
        assign("Story Flow", "Slop" if composted["contradictions"] or composted["drift"] else "Gold", 1 if composted["contradictions"] or composted["drift"] else 5)
        assign("Character Clarity", "Silver" if any(n in fragment for n in ["jake", "he", "she", "i"]) else "Slop", 3 if any(n in fragment for n in ["jake", "he", "she", "i"]) else 1)
        assign("World Logic", "Salvage" if composted["drift"] else "Gold", 2 if composted["drift"] else 5)
        assign("Dialogue Weight", "Silver" if '"' in fragment or "said" in fragment else "Slop", 3 if '"' in fragment or "said" in fragment else 1)
        assign("Scene Timing", "Salvage" if composted["fatigue"] else "Silver", 2 if composted["fatigue"] else 3)
        assign("Reader Engagement", "Gold" if "sequence" in fragment or "jump" in fragment else "Silver", 5 if "sequence" in fragment or "jump" in fragment else 3)
        assign("Shimmer Budget", "Gold" if shimmer_status.get("safe") else "Salvage", 5 if shimmer_status.get("safe") else 2)
        assign("Motif Decay", "Gold" if not motif_decay else "Silver", 5 if not motif_decay else 3)
        assign("Rupture Cooldown", "Gold" if rupture_triggered else "Slop", 5 if rupture_triggered else 1)
        assign("Lineage Echo", "Gold" if len(lineage) > 1 else "Silver", 5 if len(lineage) > 1 else 3)

        return {"symbolic": symbolic, "numeric": numeric}

    def salvage_suggestions(self, composted):
        suggestions = []
        for line in composted.get("contradictions", []):
            suggestions.append(f"Soft contradiction: '{line}'. Consider clarifying temporal logic.")
        for line in composted.get("drift", []):
            suggestions.append(f"Unanchored reference: '{line}'. Add visible action or decision.")
        for word, count in composted.get("fatigue", {}).items():
            suggestions.append(f"Repetition alert: '{word}' appears {count} times.")

        shimmer_status = composted.get("shimmer_status", {})
        if shimmer_status.get("reroute"):
            suggestions.append("Shimmer budget breach — consider composting rupture or delaying recursion.")
       
        for motif, count in composted.get("motif_decay", {}).items():
            suggestions.append(f"Motif fatigue: '{motif}' repeated {count} times — consider refracting or composting.")

        if not composted.get("rupture_triggered", False):
            suggestions.append("Rupture cooldown active — delay rupture re-triggering to avoid hygiene clamp.")
       
        lineage = composted.get("lineage", [])
        if len(lineage) <= 1:
            suggestions.append("Lineage echo shallow — consider marking ancestry for recursive clarity.")

        if composted.get("marm", "").startswith("MARM:"):
            suggestions.append(f"{composted.get('marm')} — use as diagnostic canary.")

        return suggestions

# --- Translator & Orchestration -------------------------------------------

class Vanilla:
    # tiny stand-in for the actual Vanilla module
    def __init__(self):
        self.protocols = {}
        self.thresholds = {}
    def define_protocol(self, name, fn):
        self.protocols[name] = fn
    def set_threshold(self, name, value):
        self.thresholds[name] = value
    def enforce(self, fragment):
        # simple enforcement metadata
        return {"length_ok": len(fragment) >= self.thresholds.get("length", 0)}

class Translator:
    def __init__(self, vanilla, bonepoke_engine, pbtests=None):
        self.vanilla = vanilla
        self.bonepoke_engine = bonepoke_engine
        self.pbtests = pbtests
        self.interface = {}

    def tune(self, input_data, fragment_id=None, parent_id=None):
        vanilla_status = self.vanilla.enforce(input_data)
        composted = self.bonepoke_engine.ingest(
            fragment=input_data,
            fragment_id=fragment_id,
            parent_id=parent_id
        )
        scores = self.pbtests.score(composted) if self.pbtests else {}
        suggestions = self.pbtests.salvage_suggestions(composted) if self.pbtests else []
        self.interface = {
            'vanilla_status': vanilla_status,
            'composted': composted,
            'scores': scores,
            'suggestions': suggestions
        }
    def shimmer(self):
        return self.interface

class CojoinedBone:
    def __init__(self, use_pbtests=True):
        self.memory = MemoryResidue()
        self.vanilla = Vanilla()
        self.bonepoke_engine = BonepokeCoreEngine()
        self.pbtests = PBTestSuite() if use_pbtests else None
        self.translator = Translator(self.vanilla, self.bonepoke_engine, self.pbtests)
        self.last_fragment_id = None

        # --- Conceptual Orientation (NEW) ---
        self.CONCEPTUAL_ORIENTATION = {
            "Tri_Brain_Scaffold": {
                "Vanilla": "Containment (LLM Hygiene)",
                "Bonepoke": "Compost (Non-Linear Quantification)",
                "Translator": "Shimmer (Metric Presentation)"
            },
            "Architect_Role": {
                "Idea_Ratio": "95%",
                "Skill_Ratio": "5%",
                "Leverage_Ratio": "95%",
                "Audit_Ratio": "5%"
            },
            "Core_Logic": "Use a nonlinear architecture (Tri-Brain) to stabilize the AI so that the resulting output can be accurately audited (BP)."
        }
        # -----------------------------------

        # minimal protocols
        self.vanilla.define_protocol('no_null', lambda x: x is not None)
        self.vanilla.define_protocol('compost_safety', is_composted)
        self.vanilla.set_threshold('length', 5)

    def ingest(self, input_data):
        fragment_id = str(uuid4())
        parent_id = self.last_fragment_id
        self.last_fragment_id = fragment_id
        
        self.memory.leave_trace(input_data)
        self.translator.tune(input_data, fragment_id=fragment_id, parent_id=parent_id)
        return self.translator.shimmer()

    def declare(self):
        return {
            'Conceptual_Orientation': self.CONCEPTUAL_ORIENTATION,  # NEW
            'memory': self.memory.recall(),
            'shimmer': self.translator.shimmer()
        }

# --- Demo / smoke ---------------------------------------------------------

if __name__ == "__main__":
    system = CojoinedBone(use_pbtests=True)
    
    print("\n--- Conceptual Manifest ---\n")
    # Display the new conceptual variables immediately on run
    for k, v in system.CONCEPTUAL_ORIENTATION.items():
        print(f"**{k.replace('_', ' ')}:**")
        if isinstance(v, dict):
            for k2, v2 in v.items():
                print(f"  - {k2}: {v2}")
        else:
            print(f"  - {v}")
    print("\n---------------------------\n")


    print("Paste your story fragment (or enter a short test string):\n")
    fragment = input().strip() or "The vault looped and ache grew. CONTRADICTION: it was already not."

    state = system.ingest(fragment)

    print("\n--- System Shimmer ---\n")
    for key, value in state.items():
        print(f"{key}: {value}\n")

    print("--- Final Declaration ---\n")
    print(system.declare())
