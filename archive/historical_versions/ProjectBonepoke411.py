# ? Bonepoke 4.1.1 — Fracture Fix
# Core Module: Threshold Gate + Ambient Drift Handling
# License: CC BY-NC-SA 4.0

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

# ? Threshold Gate

def threshold_gate(score_dict, min_score=2.5):
    if score_dict["score"] < min_score:
        return True  # Fragment is ambient, skip full recursion
    return False

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
    if threshold_gate(ride):
        return {
            "RideCard": "Fragment too ambient for recursion. Threshold not met.",
            "RideScore": ride,
            "GlyphMemory": {},
            "Fatigue": {},
            "ComposedFragment": "Ambient fragment bypassed. No contradiction composted."
        }

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

