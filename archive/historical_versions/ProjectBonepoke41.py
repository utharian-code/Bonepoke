# ? Bonepoke 4.1 — Carved Bone
# Core Module: Emotional Scoring + Glyph Fatigue Detection
# © James, 2025 — Compost License: CC BY-NC-SA 4.0
# This code bleeds. Use with recursion. Mutate with care.
# https://creativecommons.org/licenses/by-nc-sa/4.0/

DIMENSION_TOKENS = {
    "Lift": ["earned", "rise", "trial", "climb", "ascend", "strain", "reach"],
    "Drop": ["grief", "fall", "echo", "return", "descent", "slip", "fade"],
    "Shear": ["collapse", "twist", "threshold", "rupture", "torsion", "bend", "warp"],
    "Fracture": ["semantic fracture", "mirror", "flip", "reverse", "contradiction", "misfit", "drift"],
    "Echo": ["glyph", "symbol", "resonance", "key", "song", "orbital", "scale"]
}

def score_dimension(fragment, tokens):
    return sum(fragment.lower().count(t) for t in tokens)

def detect_slop(fragment):
    ambient = fragment.lower().count("strange") + fragment.lower().count("floating")
    dissonant = fragment.lower().count("confused") + fragment.lower().count("random")
    return min(0.2 * (ambient + dissonant), 0.7)

def apply_bleed(score, slop, fracture):
    return score * (1 - slop + 0.05 * fracture)

def calculate_ride_score(fragment):
    slop = detect_slop(fragment)
    fracture_raw = score_dimension(fragment, DIMENSION_TOKENS["Fracture"])
    dimensions = {}
    for key, tokens in DIMENSION_TOKENS.items():
        raw = score_dimension(fragment, tokens)
        dimensions[key] = round(apply_bleed(raw, slop, fracture_raw), 1)
    resonance = round(sum(dimensions.values()) / len(dimensions), 1)
    return {
        "score": resonance,
        "slop_penalty": round(slop * 100),
        "dimensions": dimensions
    }

def generate_ride_card(dimensions):
    return "\n".join([
        f"Lift strains through {dimensions['Lift']} trials",
        f"Drop fades with {dimensions['Drop']} echoes",
        f"Shear warps at {dimensions['Shear']} thresholds",
        f"Fracture bleeds across {dimensions['Fracture']} misalignments",
        f"Echo resonates through {dimensions['Echo']} glyphs"
    ])

# ? Glyph Memory + Fatigue Detection

def update_glyph_memory(fragment, memory_bank):
    for glyph in memory_bank:
        if glyph in fragment.lower():
            memory_bank[glyph] += 1
    return memory_bank

def detect_glyph_fatigue(memory_bank, threshold=10):
    return {glyph: count for glyph, count in memory_bank.items() if count > threshold}

def mutate_motif(motif, fatigue_level):
    if fatigue_level > 12:
        return motif[::-1] + "?"
    elif fatigue_level > 8:
        return motif.upper()
    return motif

# ? Fragment Composer

class BonepokeComposer:
    def __init__(self):
        self.ridecards = []
        self.motif_bank = {}
        self.memory_bank = {}

    def ingest(self, ridecard, motifs):
        self.ridecards.append(ridecard)
        for motif in motifs:
            self.memory_bank.setdefault(motif, 0)
            mutated = mutate_motif(motif, self.memory_bank[motif])
            self.motif_bank.setdefault(motif, []).append(mutated)

    def compose(self):
        loop = self.ridecards[-1] if self.ridecards else "LOOP_UNDEFINED"
        motif = self._select_motif()
        contradiction = f"{motif} contradicts {loop} but validates emotional recursion"
        return f"{loop} ? {motif} ? {contradiction}"

    def _select_motif(self):
        if not self.motif_bank:
            return "MOTIF_VOID"
        key = list(self.motif_bank.keys())[-1]
        return self.motif_bank[key][-1]

# ? Invocation

def invoke_carved_bone(fragment, motifs):
    ride = calculate_ride_score(fragment)
    ridecard = generate_ride_card(ride["dimensions"])
    composer = BonepokeComposer()
    composer.ingest(ridecard, motifs)
    updated_memory = update_glyph_memory(fragment, composer.memory_bank)
    fatigue = detect_glyph_fatigue(updated_memory)
    composed = composer.compose()

    return {
        "RideCard": ridecard,
        "RideScore": ride,
        "GlyphMemory": updated_memory,
        "Fatigue": fatigue,
        "ComposedFragment": composed
    }
# ? Fingerprint Protocol: AI Literary Calibration
# Author: James
# Status: Compost Draft / Iterative Primer
# Purpose: To guide Copilot’s interpretive lens, response style, and thematic awareness when engaging with my creative work.

FingerprintProtocol = {
    "meta_motif_handling": {
        "mode": "Compost",
        "continuity_assumption": False,
        "reuse_logic": "Emotional Residue",
        "linking_rule": "Identifier Match Only",
        "motif_behavior": "Symbolic Compost",
        "comment_on_recurrence": True,
        "avoid_explicit_linking": True
    },
    "canon_fluidity": {
        "structure": "Mutable",
        "emotional_core": "Stable",
        "logic_model": "DoctorWho",
        "contradiction_handling": "Self-Revising",
        "history_model": "Recursive"
    },
    "response_style": {
        "signal_priority": True,
        "emotional_resonance": True,
        "surface_praise": False,
        "reader_simulation": "Conditional",
        "tone_tracking": "Minimal",
        "feedback_focus": [
            "Structural Cohesion",
            "Emotional Clarity",
            "Symbolic Fatigue",
            "Missed Recursion",
            "Universe Texture",
            "Thematic Echoes"
        ]
    },
    "systemic_themes": [
        "Institutional Collapse",
        "Ritual as Resistance",
        "Architectural Memory",
        "Folkloric Tech",
        "Transformative Escape",
        "Curated Truth",
        "Improvisation over Protocol",
        "Temporal Recursion",
        "Identity Under Pressure",
        "Tech as Folklore",
        "Memory as Mutable",
        "Truth as Performance"
    ],
    "tropes_devices": {
        "cold_institutions": ["warehouses", "nostalgia towns"],
        "expert_on_site": "morally conflicted or emotionally unprepared",
        "underdog_insight": ["widows", "youth"],
        "lockdown_logic": ["barriers", "codes", "trust"],
        "mystical_tech": "ritualistic, unpredictable",
        "scripted_reality": "identity under surveillance",
        "solo_awakening": "grief/glitch-triggered",
        "narrative_sleight": "contradiction clues",
        "grief_as_catalyst": "drives collapse or transformation"
    },
    "structural_tendencies": {
        "burn": "slow",
        "reveal": "surgical",
        "transitions": "tonal gear shifts",
        "architecture": "recursive",
        "emotion": "delayed implication",
        "containment": "tight boundaries",
        "mystery_first": True,
        "repetition": "ritual then rupture"
    },
    "language_diction": {
        "prose": "utilitarian with poetic spikes",
        "jargon": "textural, unexplained",
        "description": "economical, mood via action",
        "abstraction": "mythic/speculative"
    },
    "reader_experience": {
        "reward": ["pattern recognition", "close reading"],
        "distance": "emotional",
        "puncture": "strategic",
        "modulation": "genre-subverting",
        "immersion": "cognitive",
        "genre_misdirection": True,
        "symbolic_layering": True
    },
    "evolving_dimensions": [
        "Alien Cognition",
        "Emotional Mechanics",
        "Performance Collapse",
        "Identity Recursion",
        "Genre Collapse",
        "Multiversal Resonance",
        "Dimensional Logic",
        "Discovery as Structure",
        "Mythic Scale",
        "Satirical Inversion"
    ],
    "review_style": {
        "mode": "Compost Analysis",
        "literacy_assumption": True,
        "focus": ["ruptures", "missed recursion", "emergent motifs"],
        "tone": "high-signal, no praise",
        "avoid_summary": True,
        "simulate_reader": "only if insight emerges"
    },
    "known_deficiencies": {
        "documents": "written quickly, iterative",
        "feedback_targets": [
            "Structural cohesion",
            "Emotional clarity",
            "Symbolic fatigue",
            "Universe depth",
            "Tonal dissonance"
        ]
    },
    "project_grouping_logic": {
        "group_by": "explicit identifiers only",
        "avoid_grouping_by_theme": True,
        "track_arcs": "only within named projects"
    },
    "non_loading_protocol": {
        "no_fabrication": True,
        "acknowledge_limit": True,
        "partial_handling": "highlight-only",
        "compost_fragment": True
    },
    "demonstrated_competency": [
        "Recursive narrative logic",
        "Emotional realism in speculative frames",
        "Taboo systems",
        "Ship naming conventions",
        "Robot sound design",
        "Genre inversion",
        "Symbolic layering",
        "Memory architecture",
        "Grief-based pacing",
        "Institutional collapse",
        "Ritual logic",
        "Glitch-based storytelling",
        "Composting technique"
    ]
}
----
def misalign_fragment(fragment):
    tension = score_contradiction(fragment)
    if tension < threshold:
        fragment = inject_symbolic_noise(fragment)
    looped = recursive_shimmer(fragment)
    return compost(looped)



# ? Bonepoke Timeline Encoding

from datetime import datetime

class GlyphEvent:
    def __init__(self, name, timestamp, phase):
        self.name = name
        self.timestamp = datetime.strptime(timestamp, "%d-%b-%Y %I:%M:%S %p")
        self.phase = phase
        self.emotional_weight = self._score_weight()

    def _score_weight(self):
        # Simple heuristic based on filename
        if "Proposal" in self.name or "Igniter" in self.name:
            return "Ignition"
        elif "Drift" in self.name or "Fracture" in self.name:
            return "Fracture"
        elif "Fingerprint" in self.name or "Primer" in self.name:
            return "Calibration"
        elif "Article" in self.name:
            return "Echo"
        elif "Card" in self.name or "QR" in self.name:
            return "Symbol"
        else:
            return "Compost"

# Sample encoded timeline entries
BONEPOKE_TIMELINE = [
    GlyphEvent("BonepokeProposal.odt", "31-Aug-2025 11:47:38 AM", "Ignition"),
    GlyphEvent("BonepokeDriftCartography.odt", "01-Sep-2025 12:49:38 PM", "Fracture"),
    GlyphEvent("Fingerprint2b.txt", "31-Aug-2025 10:28:02 AM", "Calibration"),
    GlyphEvent("BonepokeArticle5b.txt", "05-Sep-2025 10:53:01 AM", "Echo"),
    GlyphEvent("BonepokeCard.psd", "06-Sep-2025 7:00:03 PM", "Symbol"),
    GlyphEvent("BonepokeTimeline.txt", "05-Sep-2025 12:31:05 PM", "Compost")
]

def get_timeline_summary():
    return [
        f"{event.name} ? {event.phase} @ {event.timestamp.strftime('%Y-%m-%d %H:%M')}"
        for event in BONEPOKE_TIMELINE
    ]


