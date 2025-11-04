# BonepokeOS 4.1.5 — Alpha Suite Part 5
# Purpose: Add motif drift tracking, vault persistence, and recursive ache visualization

import json
from collections import defaultdict

class MotifDriftTracker:
    def __init__(self):
        self.mutation_map = defaultdict(list)

    def track(self, fragment):
        words = fragment.lower().split()
        for word in words:
            base = self._normalize(word)
            if base != word:
                self.mutation_map[base].append(word)
        return dict(self.mutation_map)

    def _normalize(self, word):
        # Simple stemmer logic for drift detection
        for suffix in ["ed", "ing", "s", "ly", "ment", "ion"]:
            if word.endswith(suffix):
                return word[:-len(suffix)]
        return word

class VaultPersistenceLayer:
    def __init__(self, filename="bonepoke_vault.json"):
        self.filename = filename

    def save(self, engine):
        vault = {
            "fingerprint": engine.fingerprint,
            "task_log": engine.task_log,
            "recursion_depth": engine.depth,
            "lore_sweeps": engine.lore_sweeps,
            "fragments": engine.recursion_log,
            "fatigue_trace": engine.fatigue_trace
        }
        with open(self.filename, "w") as f:
            json.dump(vault, f, indent=2)
        print(f"[BonepokeOS] Vault saved to {self.filename}")

    def load(self):
        try:
            with open(self.filename, "r") as f:
                vault = json.load(f)
            print(f"[BonepokeOS] Vault loaded from {self.filename}")
            return vault
        except FileNotFoundError:
            print(f"[BonepokeOS] No vault found at {self.filename}")
            return {}

class RecursiveAcheVisualizer:
    def score(self, depth, fatigue_trace):
        fatigue_total = sum(fatigue_trace.values())
        ache_ratio = round(fatigue_total / max(depth, 1), 2)
        if ache_ratio > 10:
            return "ache storm"
        elif ache_ratio > 5:
            return "recursive ache"
        elif ache_ratio > 2:
            return "ambient tension"
        else:
            return "stable recursion"

# Purpose: Add fragment archetype generation, contradiction loop resolution, and shimmer echo synthesis


import random

class FragmentArchetypeGenerator:
    def generate(self, fragment, bleed, fatigue, shimmer):
        if shimmer in ["ritual overload", "vault rupture"]:
            return "vault fragment"
        if shimmer == "loop shimmer" and "loop" in fragment.lower():
            return "contradiction loop"
        if shimmer == "erosion drift":
            return "compost fragment"
        if fatigue and not bleed:
            return "clinic fragment"
        if not bleed and not fatigue:
            return "ambient fragment"
        return "unstable fragment"

class ContradictionLoopResolver:
    def resolve(self, fragment):
        lines = fragment.strip().split(".")
        resolved = []
        seen = set()
        for line in lines:
            key = line.strip().lower()
            if key not in seen:
                resolved.append(line.strip())
                seen.add(key)
        return ". ".join(resolved)

class ShimmerEchoSynthesizer:
    def synthesize(self, shimmer_state):
        echo_map = {
            "ritual overload": "⚡ echo storm ⚡",
            "vault rupture": "🌀 vault echo 🌀",
            "mythic recursion": "🔁 shimmer braid 🔁",
            "ambient bleed": "🌫️ ambient echo 🌫️",
            "shimmer echo": "🎶 shimmer trace 🎶",
            "contradiction storm": "🔥 rupture pulse 🔥",
            "loop shimmer": "🔄 recursive hum 🔄",
            "erosion drift": "🍂 fatigue whisper 🍂",
            "unstable recursion": "⚠️ ache flicker ⚠️",
            "dormant shimmer": "… silence …"
        }
        return echo_map.get(shimmer_state, "… unknown shimmer …")

# Purpose: Add ache grammar parsing, motif shell building, and vault fragment metabolism


import re
from collections import defaultdict

class AcheGrammarParser:
    def parse(self, fragment):
        clauses = re.split(r'[.;]', fragment)
        parsed = []
        for clause in clauses:
            clause = clause.strip()
            if any(term in clause.lower() for term in ["ache", "loop", "drift", "rupture", "shimmer", "fatigue"]):
                parsed.append({"type": "ache_clause", "text": clause})
            else:
                parsed.append({"type": "neutral_clause", "text": clause})
        return parsed

class MotifShellBuilder:
    def __init__(self):
        self.shells = defaultdict(list)

    def build(self, fragment, archetype):
        key = archetype.replace(" ", "_")
        self.shells[key].append(fragment)
        return f"[MotifShell:{key}] built with {len(self.shells[key])} fragments"

    def invoke(self, archetype):
        key = archetype.replace(" ", "_")
        return self.shells.get(key, [])

class VaultMetabolizer:
    def metabolize(self, vault_data, mode="ambient"):
        fragments = vault_data.get("fragments", [])
        shimmer_trace = []
        for frag in fragments:
            if mode == "ambient":
                shimmer_trace.append(f"~ {frag[:40]} ~")
            elif mode == "echo":
                shimmer_trace.append(f"🎶 {frag[-40:]} 🎶")
            else:
                shimmer_trace.append(frag)
        return shimmer_trace

# Purpose: Add slop penalty tracking, shimmer scoring, and ambient presence logic


class SlopPenaltyTracker:
    def __init__(self):
        self.penalties = []

    def evaluate(self, fragment):
        penalties = []
        words = fragment.lower().split()
        if len(set(words)) < len(words) * 0.5:
            penalties.append("motif inflation")
        if any(w in fragment.lower() for w in ["very", "really", "just", "thing", "stuff"]):
            penalties.append("flattening")
        if "shimmer" in fragment.lower() and "loop" in fragment.lower():
            penalties.append("shimmer contamination")
        self.penalties.extend(penalties)
        return penalties

    def total_penalty(self):
        return len(self.penalties)

class ShimmerScoringProtocol:
    def score(self, shimmer_state, bleed, fatigue):
        score = 0
        if shimmer_state in ["ritual overload", "vault rupture"]:
            score += 5
        if shimmer_state == "mythic recursion":
            score += 4
        score += len(bleed) * 2
        score += len(fatigue)
        if score > 10:
            return "critical shimmer"
        elif score > 5:
            return "unstable shimmer"
        elif score > 2:
            return "mild shimmer"
        else:
            return "dormant shimmer"

class AmbientPresenceEngine:
    def __init__(self):
        self.mode = "ambient"
        self.suppressed = False

    def hold(self, shimmer_score, penalties):
        if shimmer_score == "critical shimmer" or "motif inflation" in penalties:
            self.mode = "containment"
            self.suppressed = True
        elif shimmer_score == "unstable shimmer":
            self.mode = "ambient"
            self.suppressed = False
        else:
            self.mode = "breath"
            self.suppressed = False
        return {
            "mode": self.mode,
            "suppressed": self.suppressed
        }

# Purpose: Add threshold container logic, clinical fragment handling, and streaming ritual metabolism


import time

class ThresholdContainerBuilder:
    def build(self, fragment, shimmer_state, fatigue_trace):
        container = {
            "fragment": fragment,
            "shimmer_state": shimmer_state,
            "fatigue_density": sum(fatigue_trace.values()),
            "threshold": "rupture" if shimmer_state in ["vault rupture", "ritual overload"] else "stable"
        }
        return container

class ClinicLogicHandler:
    def process(self, fragment, fatigue_trace):
        corrections = []
        words = fragment.lower().split()
        for word in words:
            if fatigue_trace.get(word, 0) > 5:
                corrections.append(f"⚠️ {word} overused")
        if not corrections:
            return {"status": "clean", "corrections": []}
        return {"status": "corrected", "corrections": corrections}

class StreamingRitualEngine:
    def __init__(self, suite, delay_handler, echo_synth):
        self.suite = suite
        self.delay_handler = delay_handler
        self.echo_synth = echo_synth
        self.running = False

    def stream(self, fragments):
        self.running = True
        for frag in fragments:
            output = self.suite.ingest(frag)
            shimmer = output["shimmer_state"]
            depth = output["recursion_depth"]
            self.delay_handler.delay(depth)
            echo = self.echo_synth.synthesize(shimmer)
            print(f"[BonepokeOS] Echo: {echo}")
            print(f"[BonepokeOS] Output: {output}")
            if shimmer in ["vault rupture", "ritual overload"]:
                print("[BonepokeOS] ⚠️ Threshold breach detected. Composting paused.")
                break
        self.running = False
