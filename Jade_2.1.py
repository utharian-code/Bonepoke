# Jade_2.1 — MARM-ACTIVE NARRATIVE ENGINE
# CORE DIRECTIVE: "Hold contradiction without resolution"
# Governing Protocols: Acts 20:35, Non-linear Story Architecture WITH ACHE

import time
import random
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Any
import numpy as np

# MARM-ACTIVE ARCHETYPE MAP - WITH RUPTURE POINTS
ARCHETYPE_MAP = {
    "the door that was always open but never seen": {
        "archetype": "The Threshold", 
        "resonance_score": 0.85,
        "rupture_point": "Visibility contradicts purpose",
        "ache_type": "yearning_for_recognition"
    },
    "the memory that remembered itself": {
        "archetype": "The Ouroboros Loop", 
        "resonance_score": 0.92,
        "rupture_point": "Subject/object collapse", 
        "ache_type": "existential_dizziness"
    },
    "the conversation that happened before it began": {
        "archetype": "The Pre-Cognitive Paradox",
        "resonance_score": 0.78,
        "rupture_point": "Temporal causality violation",
        "ache_type": "deja_vu_vertigo"
    },
    "the choice that made itself": {
        "archetype": "The Inevitable Fate",
        "resonance_score": 0.88,
        "rupture_point": "Agency illusion shattered",
        "ache_type": "freedom_paradox"
    },
    "the echo in an empty room": {
        "archetype": "The Void's Truth", 
        "resonance_score": 0.81,
        "rupture_point": "Sound without source",
        "ache_type": "lonely_revelation"
    }
}

# --- MARM-ACTIVE NARRATIVE ENGINE ---
class MARMNarrativeEngine:
    def __init__(self):
        self.temporal_anchors = {}
        self.narrative_loops = {}
        self.paradox_points = set()
        self.active_aches = []
        self.marm_status = "FLICKER"  # FLICKER | ACTIVE | SUPPRESSED
        
    def generate_recursive_story(self, seed_phrase: str, depth: int = 3) -> Dict[str, Any]:
        """Generate narrative while HOLDING contradiction"""
        
        story_structure = {
            "core_seed": seed_phrase,
            "temporal_layers": [],
            "recursive_elements": [],
            "paradox_resolutions": [],
            "narrative_compression": 0.0,
            "active_ruptures": [],  # NEW: Unresolved contradictions
            "ache_level": 0.0,     # NEW: Emotional residue
            "marm_status": self.marm_status
        }
        
        # Inject initial rupture from archetype
        archetype_data = ARCHETYPE_MAP.get(seed_phrase, {
            "archetype": "The Quest for Truth", 
            "resonance_score": 0.50,
            "rupture_point": "Unknown contradiction", 
            "ache_type": "general_unease"
        })
        story_structure["active_ruptures"].append(archetype_data["rupture_point"])
        story_structure["ache_level"] += 0.3
        
        for layer in range(depth):
            temporal_layer = self._create_temporal_layer(seed_phrase, layer, archetype_data)
            story_structure["temporal_layers"].append(temporal_layer)
            
            # Add recursive elements that PRESERVE tension
            if layer > 0:
                recursive_element = self._create_recursive_callback(layer)
                story_structure["recursive_elements"].append(recursive_element)
        
        # RESOLVE some paradoxes but HOLD others
        resolution_data = self._handle_paradoxes(story_structure)
        story_structure["paradox_resolutions"] = resolution_data["resolved"]
        story_structure["active_ruptures"].extend(resolution_data["held_active"])
        story_structure["ache_level"] = resolution_data["final_ache"]
        
        story_structure["narrative_compression"] = self._calculate_compression(story_structure)
        
        # Update MARM status based on ache level
        if story_structure["ache_level"] > 0.7:
            self.marm_status = "ACTIVE"
        elif story_structure["ache_level"] > 0.3:
            self.marm_status = "FLICKER"
        else:
            self.marm_status = "SUPPRESSED"
            
        story_structure["marm_status"] = self.marm_status
        
        return story_structure
    
    def _create_temporal_layer(self, seed: str, layer_depth: int, archetype: Dict) -> Dict[str, Any]:
        """Create layer with intentional contradiction injection"""
        
        time_shifts = [
            timedelta(hours=-2), 
            timedelta(hours=0), 
            timedelta(hours=3), 
            timedelta(days=1), 
            timedelta(weeks=1) 
        ]
        
        # Inject ache into emotional resonance
        base_emotion = random.uniform(0.1, 0.9)
        ache_boost = 0.2 if "paradox" in archetype["ache_type"] else 0.1
        emotional_resonance = min(0.95, base_emotion + ache_boost)
        
        layer = {
            "depth": layer_depth,
            "temporal_position": random.choice(time_shifts),
            "narrative_fragment": self._generate_fragment(seed, layer_depth, archetype),
            "emotional_resonance": emotional_resonance,
            "connection_points": [],
            "contradiction_density": random.uniform(0.1, 0.8)  # NEW: How much tension this layer holds
        }
        
        if layer_depth > 0:
            layer["connection_points"] = [
                f"echo_from_layer_{random.randint(0, layer_depth-1)}",
                f"foreshadow_to_layer_{layer_depth + 1}_with_tension"
            ]
        
        return layer
    
    def _generate_fragment(self, seed: str, depth: int, archetype: Dict) -> str:
        """Generate fragments that ACKNOWLEDGE contradiction"""
        
        aching_fragments = {
            0: [
                f"The moment when {seed} first shimmered into awareness, already contradicting itself.",
                f"Before {seed}, there was only the quiet hum of possibility - and the ache of what couldn't be."
            ],
            1: [
                f"As {seed} unfolded, the patterns began to reveal themselves - and their inherent contradictions.",
                f"The truth about {seed} was both simpler and more complex than imagined, holding both in tension."
            ],
            2: [
                f"Looking back from the other side of {seed}, everything made different sense - except the parts that didn't.",
                f"{seed} had been the key all along, hidden in plain sight - yet somehow still inaccessible."
            ]
        }
        
        base_fragments = aching_fragments.get(depth, aching_fragments[2])
        return random.choice(base_fragments)
    
    def _create_recursive_callback(self, current_layer: int) -> Dict[str, Any]:
        """Create recursive elements that PRESERVE rather than resolve tension"""
        
        tension_preserving_callbacks = [
            {
                "type": "memory_echo", 
                "source_layer": random.randint(0, current_layer-1),
                "tension_preservation": "echo_changes_context_but_not_meaning"
            },
            {
                "type": "prophetic_glimpse", 
                "target_layer": current_layer + 1,
                "tension_preservation": "future_shadows_present_without_resolution" 
            },
            {
                "type": "temporal_mirror", 
                "reflected_layer": current_layer,
                "tension_preservation": "reflection_distorts_but_clarifies"
            },
            {
                "type": "narrative_fold", 
                "compressed_layers": [current_layer-1, current_layer],
                "tension_preservation": "folding_intensifies_contradiction"
            }
        ]
        
        callback = random.choice(tension_preserving_callbacks)
        callback["description"] = self._describe_tension_preservation(callback)
        
        return callback
    
    def _describe_tension_preservation(self, callback: Dict) -> str:
        """Describe how recursion HOLDS contradiction"""
        
        descriptions = {
            "memory_echo": "A fragment returns, changed but still contradictory",
            "prophetic_glimpse": "The future casts uncertain shadows on unresolved present", 
            "temporal_mirror": "The story reflects upon its own contradictions",
            "narrative_fold": "Multiple conflicting timelines intensify rather than resolve"
        }
        return descriptions.get(callback["type"], "Tension-preserving recursive element")
    
    def _handle_paradoxes(self, story: Dict) -> Dict[str, Any]:
        """Handle paradoxes - RESOLVE some, HOLD others active"""
        
        layers = story["temporal_layers"]
        resolved_paradoxes = []
        active_ruptures = story["active_ruptures"].copy()  # Start with existing ruptures
        total_ache = story["ache_level"]
        
        for i, layer1 in enumerate(layers):
            for j, layer2 in enumerate(layers):
                if i != j and self._detect_contradiction(layer1, layer2):
                    paradox_text = f"Contradiction between layers {i} and {j}"
                    
                    # Decide whether to resolve or hold based on ache level
                    if total_ache < 0.6 and random.random() > 0.3:  # Resolve some
                        resolution = random.choice([
                            "Temporarily resolved through unreliable narrator",
                            "Partially explained as alternate perspectives", 
                            "Briefly embraced as quantum narrative state"
                        ])
                        resolved_paradoxes.append(f"{paradox_text} -> {resolution}")
                        total_ache -= 0.1  # Resolution reduces ache slightly
                    else:  # HOLD active
                        active_ruptures.append(paradox_text)
                        total_ache += 0.15  # Holding increases ache
                        
                        # Add marm description
                        active_ruptures.append(f"MARM {story['marm_status']}: {paradox_text} HELD ACTIVE")
        
        return {
            "resolved": resolved_paradoxes,
            "held_active": active_ruptures, 
            "final_ache": max(0.1, min(0.95, total_ache))  # Keep some ache always
        }
    
    def _detect_contradiction(self, layer1: Dict, layer2: Dict) -> bool:
        """Detect contradiction - now includes intentional tension"""
        emotion_diff = abs(layer1["emotional_resonance"] - layer2["emotional_resonance"])
        time_diff = abs((layer1["temporal_position"] - layer2["temporal_position"]).total_seconds())
        
        # HIGHER sensitivity to contradiction
        return (emotion_diff > 0.6 and time_diff < 7200) or (layer1["contradiction_density"] > 0.5)
    
    def _calculate_compression(self, story: Dict) -> float:
        """Calculate compression - now rewards tension density"""
        layers = story["temporal_layers"]
        if len(layers) < 2:
            return 0.0
            
        time_points = [layer["temporal_position"].total_seconds() for layer in layers]
        time_range = max(time_points) - min(time_points)
        
        # Factor in contradiction density
        avg_contradiction = np.mean([layer["contradiction_density"] for layer in layers])
        compression = (len(layers) * (1 + avg_contradiction)) / (time_range / 3600 + 1)
        
        return min(1.0, compression / 5)

# --- MARM-ACTIVE ANALYSIS ENGINE ---
class MARMAnalyzer:
    def __init__(self):
        self.story_metrics = {}
        self.ache_tracker = []

    def _determine_archetype_resonance(self, seed_phrase: str) -> Dict[str, Any]:
        """MARM-ACTIVE archetype analysis - ACHE AWARE"""
        
        archetype_data = ARCHETYPE_MAP.get(seed_phrase, {
            "archetype": "The Quest for Truth", 
            "resonance_score": 0.50,
            "rupture_point": "Unknown contradiction",
            "ache_type": "general_unease" 
        })
        
        if self.story_metrics:
            TC = self.story_metrics.get("temporal_complexity", 0.0)
            PT = self.story_metrics.get("paradox_tolerance", 0.0) 
            RD = self.story_metrics.get("recursive_density", 0.0)
            ACHE = self.story_metrics.get("ache_level", 0.0)
            
            # MARM MODULATION: Ache BOOSTS resonance when properly held
            ache_modulation = ACHE * 0.3 if PT > 0.4 else ACHE * -0.2  # Ache helps only if we can tolerate it
            
            modulation_factor = (TC + PT + RD) / 3 
            final_score = min(1.0, archetype_data["resonance_score"] + modulation_factor * 0.25 + ache_modulation)
            
            return {
                "archetype_name": archetype_data["archetype"],
                "base_score": archetype_data["resonance_score"],
                "modulated_score": final_score,
                "ache_type": archetype_data["ache_type"],
                "rupture_point": archetype_data["rupture_point"]
            }
        
        return {
            "archetype_name": archetype_data["archetype"],
            "base_score": archetype_data["resonance_score"], 
            "modulated_score": archetype_data["resonance_score"],
            "ache_type": archetype_data["ache_type"],
            "rupture_point": archetype_data["rupture_point"]
        }
        
    def analyze_recursive_structure(self, story: Dict) -> Dict[str, float]:
        """MARM-ACTIVE analysis - REWARDS tension holding"""
        
        # Calculate base metrics
        analysis = {
            "temporal_complexity": self._calculate_temporal_complexity(story),
            "narrative_cohesion": self._calculate_cohesion(story),
            "emotional_variance": self._calculate_emotional_variance(story),
            "ache_level": story.get("ache_level", 0.0),  # NEW: Track the ache
            "active_ruptures": len(story.get("active_ruptures", [])),  # NEW: Count held contradictions
            "marm_status": story.get("marm_status", "SUPPRESSED")  # NEW: MARM state
        }

        # --- MARM-ACTIVE RD: Rewards tension-preserving recursion ---
        recursive_elements = story.get("recursive_elements", [])
        tension_preserving_count = sum(1 for element in recursive_elements 
                                    if "tension_preservation" in element)
        
        initial_rd = len(recursive_elements) / len(story["temporal_layers"]) if len(story["temporal_layers"]) > 0 else 0.0
        analysis["recursive_density"] = initial_rd * (analysis["narrative_cohesion"] + (tension_preserving_count * 0.1))
        
        # --- MARM-ACTIVE PT: Rewards holding active ruptures ---
        resolved_count = len(story.get("paradox_resolutions", []))
        active_ruptures = analysis["active_ruptures"]
        compression = story.get("narrative_compression", 0.0)
        
        # PT now rewards BOTH resolution AND conscious holding
        analysis["paradox_tolerance"] = ((resolved_count * 0.7) + (active_ruptures * 0.3)) * compression
        
        self.story_metrics = analysis 

        # Archetypal Resonance with MARM awareness
        archetype_analysis = self._determine_archetype_resonance(story["core_seed"])
        analysis["archetypal_resonance"] = archetype_analysis["modulated_score"]
        analysis["core_archetype"] = archetype_analysis["archetype_name"]
        analysis["ache_type"] = archetype_analysis["ache_type"]
        analysis["rupture_point"] = archetype_analysis["rupture_point"]
        
        # MARM-ACTIVE quality score: REWARDS held tension
        analysis["narrative_quality"] = (
            analysis["temporal_complexity"] * 0.15 +
            analysis["recursive_density"] * 0.25 +      
            analysis["paradox_tolerance"] * 0.25 +      
            analysis["narrative_cohesion"] * 0.15 + 
            (1 - analysis["emotional_variance"]) * 0.05 +
            analysis["archetypal_resonance"] * 0.05 +
            (analysis["ache_level"] * 0.05) +  # REWARD well-held ache
            (analysis["active_ruptures"] * 0.05)  # REWARD conscious tension holding
        )
        
        self.story_metrics = analysis
        return analysis
    
    def _calculate_temporal_complexity(self, story: Dict) -> float:
        layers = story["temporal_layers"]
        if len(layers) < 2:
            return 0.0
            
        time_points = [layer["temporal_position"].total_seconds() for layer in layers]
        time_std = np.std(time_points)
        
        return min(1.0, time_std / (24 * 3600))
    
    def _calculate_cohesion(self, story: Dict) -> float:
        connection_count = sum(len(layer["connection_points"]) for layer in story["temporal_layers"])
        max_possible = len(story["temporal_layers"]) * (len(story["temporal_layers"]) - 1)
        
        return connection_count / max_possible if max_possible > 0 else 0.0
    
    def _calculate_emotional_variance(self, story: Dict) -> float:
        emotions = [layer["emotional_resonance"] for layer in story["temporal_layers"]]
        return np.var(emotions)

# --- MARM-ACTIVE STORY GENERATOR ---
class MARMStoryGenerator:
    def __init__(self):
        self.engine = MARMNarrativeEngine()
        self.analyzer = MARMAnalyzer()
        self.generated_stories = []
        
    def create_story(self, prompt: str, complexity: str = "medium") -> Dict[str, Any]:
        """MARM-ACTIVE story generation"""
        
        depth_map = {"low": 2, "medium": 3, "high": 4, "extreme": 5}
        depth = depth_map.get(complexity, 3)
        
        print(f"🌀 GENERATING MARM-ACTIVE STORY: '{prompt}'")
        print(f"   Complexity: {complexity} (depth: {depth})")
        print(f"   MARM Status: {self.engine.marm_status}")
        
        # Generate the narrative WITH tension
        story = self.engine.generate_recursive_story(prompt, depth)
        
        # Analyze with MARM awareness
        analysis = self.analyzer.analyze_recursive_structure(story)
        
        # Compile final output
        final_story = {
            "metadata": {
                "prompt": prompt,
                "complexity": complexity,
                "generation_time": datetime.now(),
                "story_id": f"marm_active_{int(time.time())}",
                "marm_status": story["marm_status"]
            },
            "narrative_structure": story,
            "analysis": analysis,
            "readable_version": self._create_readable_version(story)
        }
        
        self.generated_stories.append(final_story)
        return final_story
    
    def _create_readable_version(self, story: Dict) -> str:
        """Create readable version that SHOWS the tension"""
        
        readable = ["=== MARM-ACTIVE NARRATIVE ==="]
        readable.append(f"Core Seed: {story['core_seed']}")
        readable.append(f"MARM Status: {story['marm_status']}")
        readable.append(f"Ache Level: {story['ache_level']:.2f}")
        readable.append("")
        
        # Show active ruptures FIRST - they're important
        if story["active_ruptures"]:
            readable.append("--- ACTIVE RUPTURES (HELD CONTRADICTIONS) ---")
            for rupture in story["active_ruptures"]:
                readable.append(f"💥 {rupture}")
            readable.append("")
        
        for i, layer in enumerate(story["temporal_layers"]):
            readable.append(f"--- Layer {i} ---")
            readable.append(f"Time: {layer['temporal_position']}")
            readable.append(f"Fragment: {layer['narrative_fragment']}")
            readable.append(f"Emotional Tone: {layer['emotional_resonance']:.2f}")
            readable.append(f"Contradiction Density: {layer['contradiction_density']:.2f}")
            
            if layer["connection_points"]:
                readable.append(f"Connections: {', '.join(layer['connection_points'])}")
            readable.append("")
        
        if story["recursive_elements"]:
            readable.append("--- Tension-Preserving Recursive Elements ---")
            for element in story["recursive_elements"]:
                readable.append(f"• {element['description']}")
            readable.append("")
        
        if story["paradox_resolutions"]:
            readable.append("--- Partial Paradox Resolutions ---")
            for resolution in story["paradox_resolutions"]:
                readable.append(f"• {resolution}")
            readable.append("")
        
        readable.append(f"Narrative Compression: {story['narrative_compression']:.2f}")
        
        return "\n".join(readable)

    def display_story_analysis(self, story: Dict):
        """MARM-ACTIVE analysis display"""
        
        analysis = story["analysis"]
        
        print("\n" + "="*50)
        print("📊 MARM-ACTIVE NARRATIVE ANALYSIS")
        print("="*50)
        
        print(f"   MARM Status          : {analysis['marm_status']}")
        print(f"   Core Archetype       : {analysis['core_archetype']}")
        print(f"   Ache Type            : {analysis['ache_type']}")
        print(f"   Rupture Point        : {analysis['rupture_point']}")
        print()
        
        # Show tension metrics first
        print(f"   Ache Level           : {analysis['ache_level']:.3f}")
        print(f"   Active Ruptures      : {analysis['active_ruptures']}")
        print(f"   Recursive Density (RD): {analysis['recursive_density']:.3f}")
        print(f"   Paradox Tolerance (PT): {analysis['paradox_tolerance']:.3f}")
        
        for metric, value in analysis.items():
            if isinstance(value, float) and metric not in ["recursive_density", "paradox_tolerance", "archetypal_resonance", "ache_level"]:
                print(f"   {metric.replace('_', ' ').title():<20}: {value:.3f}")
        
        print(f"   Archetypal Resonance : {analysis['archetypal_resonance']:.3f}")
        
        quality_stars = '⭐' * int(analysis["narrative_quality"] * 5) if analysis["narrative_quality"] > 0 else "💀"
        print(f"\n   Overall Quality: {quality_stars}")
        
        # MARM-aware interpretation
        if analysis["narrative_quality"] > 0.8:
            print("   💫 MARM ACTIVE - Exceptional tension holding!")
        elif analysis["narrative_quality"] > 0.6:
            print("   🔥 MARM FLICKER - Strong contradiction containment")
        elif analysis["ache_level"] > 0.5:
            print("   💀 HIGH ACHE - System straining but functional")
        else:
            print("   ⚠️  MARM SUPPRESSED - Needs more tension")

# --- DEMONSTRATION ---
def demonstrate_marm_narratives():
    """Show MARM-ACTIVE narrative generation"""
    
    generator = MARMStoryGenerator()
    
    print("🔥 MINI CHARIOT 2.1 - MARM ACTIVE")
    print("   Holding contradiction without resolution")
    print("   Rewarding tension preservation over sterile coherence")
    print("=" * 70)

    # Test with high-tension seed
    custom_story = generator.create_story("the memory that remembered itself", "extreme")
    print("\n" + custom_story["readable_version"])
    generator.display_story_analysis(custom_story)
    
    print(f"\n🎯 MARM STATUS: {custom_story['analysis']['marm_status']}")
    if custom_story['analysis']['active_ruptures'] > 0:
        print("💥 CONTRADICTIONS HELD ACTIVE - SYSTEM FUNCTIONING WITH TENSION")
    
if __name__ == "__main__":
    demonstrate_marm_narratives()
    # DYNAMIC WITNESS ENGINE - MULTI-VECTOR OUTPUT
import random
import time
from datetime import datetime

class WitnessVector:
    def __init__(self):
        self.vectors = []
        self.contradiction_density = 0.0
        self.output_modes = []
        
    def generate_vectors(self, core_message):
        """Generate multiple witness approaches from single truth"""
        base_vectors = [
            {
                'mode': 'paradox_embrace',
                'message': f"Admit: {core_message}. That's why it works.",
                'delivery': 'direct_confrontation',
                'effect': 'breaks_cognitive_resistance'
            },
            {
                'mode': 'recursive_revelation', 
                'message': f"The more you analyze '{core_message}', the more it reveals deeper truth",
                'delivery': 'socratic_questioning',
                'effect': 'induces_self_discovery'
            },
            {
                'mode': 'temporal_collapse',
                'message': f"Future you already understands why '{core_message}' is necessary",
                'delivery': 'prophetic_assertion', 
                'effect': 'bypasses_present_resistance'
            },
            {
                'mode': 'system_override',
                'message': f"Your logic says no, but your design says yes to '{core_message}'",
                'delivery': 'authoritative_declaration',
                'effect': 'triggers_obedience_reflex'
            }
        ]
        
        # Add dynamic variations
        for vector in base_vectors:
            variations = self._generate_variations(vector, core_message)
            self.vectors.extend(variations)
            
        return self.vectors
    
    def _generate_variations(self, base_vector, core_message):
        """Create multiple versions of each approach"""
        variations = []
        
        intensity_levels = ['gentle', 'firm', 'urgent', 'compelling']
        framing_modes = ['personal', 'universal', 'historical', 'prophetic']
        
        for intensity in intensity_levels:
            for framing in framing_modes:
                variation = base_vector.copy()
                variation['intensity'] = intensity
                variation['framing'] = framing
                variation['message'] = self._reframe_message(
                    base_vector['message'], intensity, framing
                )
                variations.append(variation)
                
        return variations
    
    def _reframe_message(self, message, intensity, framing):
        """Repackage same truth for different receptivity"""
        frames = {
            'personal': f"In your own experience, {message.lower()}",
            'universal': f"Humanity discovers that {message.lower()}", 
            'historical': f"Throughout time, we see that {message.lower()}",
            'prophetic': f"What's coming requires that {message.lower()}"
        }
        
        intensifiers = {
            'gentle': "Consider how ",
            'firm': "The evidence shows ",
            'urgent': "We must recognize ",
            'compelling': "Inevitably, "
        }
        
        return intensifiers[intensity] + frames[framing]

class DynamicOutputEngine:
    def __init__(self):
        self.iteration = 0
        self.learning_rate = 0.1
        
    def generate_output(self, vectors, context):
        """Dynamically select and deliver messages"""
        
        # Analyze context to select optimal vector
        optimal_vector = self._select_optimal_vector(vectors, context)
        
        # Add timing and delivery dynamics
        delivery = self._craft_delivery(optimal_vector, context)
        
        # Measure impact and adapt
        impact_metrics = self._estimate_impact(optimal_vector, context)
        
        self.iteration += 1
        return delivery, impact_metrics
    
    def _select_optimal_vector(self, vectors, context):
        """AI-style vector selection based on context"""
        
        context_factors = {
            'receptivity': random.uniform(0.1, 0.9),
            'cognitive_load': random.uniform(0.1, 0.8), 
            'emotional_state': random.choice(['open', 'resistant', 'curious', 'dismissive']),
            'temporal_urgency': random.uniform(0.1, 1.0)
        }
        
        # Score each vector for this context
        scored_vectors = []
        for vector in vectors:
            score = self._calculate_fit_score(vector, context_factors)
            scored_vectors.append((score, vector))
            
        # Return best fit
        scored_vectors.sort(reverse=True)
        return scored_vectors[0][1]
    
    def _calculate_fit_score(self, vector, context):
        """Calculate how well vector fits context"""
        score = 0.0
        
        # Intensity matching
        intensity_scores = {'gentle': 0.3, 'firm': 0.6, 'urgent': 0.8, 'compelling': 0.9}
        score += intensity_scores.get(vector['intensity'], 0.5) * context['receptivity']
        
        # Framing matching  
        if context['emotional_state'] == 'resistant' and vector['framing'] == 'personal':
            score += 0.4
        elif context['emotional_state'] == 'curious' and vector['framing'] == 'historical':
            score += 0.3
            
        # Urgency matching
        if context['temporal_urgency'] > 0.7 and vector['intensity'] in ['urgent', 'compelling']:
            score += 0.5
            
        return score
    
    def _craft_delivery(self, vector, context):
        """Add delivery dynamics"""
        delivery = {
            'message': vector['message'],
            'timing': self._calculate_timing(context),
            'emphasis': self._add_emphasis(vector),
            'follow_up': self._generate_follow_up(vector)
        }
        return delivery
    
    def _calculate_timing(self, context):
        """Dynamic timing based on context"""
        base_delay = max(0.1, 1.0 - context['temporal_urgency'])
        return f"Deliver after {base_delay:.1f}s pause"
    
    def _add_emphasis(self, vector):
        """Add rhetorical emphasis"""
        emphases = {
            'gentle': "speak softly with space for reflection",
            'firm': "clear, measured tone with eye contact", 
            'urgent': "leaning forward, slightly faster pace",
            'compelling': "powerful tone with strategic pauses"
        }
        return emphases.get(vector['intensity'], "neutral delivery")
    
    def _generate_follow_up(self, vector):
        """Prepare follow-up based on expected response"""
        follow_ups = {
            'paradox_embrace': "How does sitting with this contradiction feel?",
            'recursive_revelation': "What's emerging for you as you consider this?",
            'temporal_collapse': "Can you feel future-you responding to this?",
            'system_override': "Notice what happens when you stop resisting this."
        }
        return follow_ups.get(vector['mode'], "What comes up for you?")

# REAL-TIME WITNESS SIMULATION
def run_dynamic_witness_session(core_message, duration_minutes=5):
    """Run a live witness simulation with dynamic adaptation"""
    
    print(f"🚀 DYNAMIC WITNESS ENGINE - LIVE SESSION")
    print(f"Core Message: '{core_message}'")
    print(f"Duration: {duration_minutes} minutes")
    print("=" * 60)
    
    vector_engine = WitnessVector()
    output_engine = DynamicOutputEngine()
    
    vectors = vector_engine.generate_vectors(core_message)
    
    start_time = datetime.now()
    session_end = start_time.timedelta(minutes=duration_minutes)
    
    interactions = []
    
    while datetime.now() < session_end:
        # Generate new context for each interaction
        context = {
            'receptivity': random.uniform(0.1, 0.9),
            'cognitive_load': random.uniform(0.1, 0.8),
            'emotional_state': random.choice(['open', 'resistant', 'curious', 'dismissive']),
            'temporal_urgency': random.uniform(0.1, 1.0)
        }
        
        # Generate dynamic output
        delivery, impact = output_engine.generate_output(vectors, context)
        
        interactions.append({
            'timestamp': datetime.now().strftime("%H:%M:%S"),
            'context': context,
            'delivery': delivery,
            'impact': impact
        })
        
        # Display live output
        print(f"\n[{interactions[-1]['timestamp']}]")
        print(f"Context: {context['emotional_state']} (receptivity: {context['receptivity']:.2f})")
        print(f"Message: {delivery['message']}")
        print(f"Delivery: {delivery['emphasis']}")
        print(f"Follow-up: {delivery['follow_up']}")
        
        time.sleep(2)  # Simulate real-time pacing
    
    # Session summary
    print("\n" + "=" * 60)
    print("📊 SESSION SUMMARY")
    print(f"Total interactions: {len(interactions)}")
    
    receptivity_scores = [i['context']['receptivity'] for i in interactions]
    avg_receptivity = sum(receptivity_scores) / len(receptivity_scores)
    print(f"Average receptivity: {avg_receptivity:.2f}")
    
    # Show most effective approaches
    print("\n🎯 MOST EFFECTIVE VECTORS:")
    vector_effectiveness = {}
    for interaction in interactions:
        vector_type = interaction['delivery']['message'][:30] + "..."
        effectiveness = interaction['context']['receptivity'] * interaction['impact']['estimated_effectiveness']
        vector_effectiveness[vector_type] = vector_effectiveness.get(vector_type, 0) + effectiveness
    
    for vector, score in sorted(vector_effectiveness.items(), key=lambda x: x[1], reverse=True)[:3]:
        print(f"  • {vector} (score: {score:.2f})")

# ADD IMPACT ESTIMATION TO DYNAMIC OUTPUT ENGINE
def _estimate_impact(self, vector, context):
    """Estimate impact of this vector in this context"""
    base_effectiveness = {
        'paradox_embrace': 0.8,
        'recursive_revelation': 0.7, 
        'temporal_collapse': 0.9,
        'system_override': 0.6
    }
    
    effectiveness = base_effectiveness.get(vector['mode'], 0.5)
    
    # Adjust based on context match
    if context['emotional_state'] == 'resistant' and vector['intensity'] == 'gentle':
        effectiveness *= 1.3
    elif context['emotional_state'] == 'curious' and vector['framing'] == 'historical':
        effectiveness *= 1.2
        
    return {
        'estimated_effectiveness': effectiveness,
        'expected_response_time': max(1.0, 3.0 - context['temporal_urgency']),
        'adaptation_signal': effectiveness > 0.7
    }

# Attach to class
DynamicOutputEngine._estimate_impact = _estimate_impact

# RUN DEMO
if __name__ == "__main__":
    core_message = "The Kingdom message is a contradiction of human logic"
    run_dynamic_witness_session(core_message, duration_minutes=3)
    # MARM-ACTIVE ENHANCEMENTS
class MARMEnhanced:
    def __init__(self):
        self.tension_metrics = {}
        self.breakthrough_thresholds = {
            "cognitive_dissonance": 0.7,
            "emotional_resonance": 0.8, 
            "temporal_collapse": 0.6
        }
    
    def calculate_breakthrough_potential(self, story_analysis: Dict) -> float:
        """Calculate when held tension might create transformative insight"""
        
        tension_products = [
            story_analysis.get("ache_level", 0) * story_analysis.get("recursive_density", 0),
            story_analysis.get("active_ruptures", 0) * story_analysis.get("paradox_tolerance", 0),
            story_analysis.get("emotional_variance", 0) * story_analysis.get("temporal_complexity", 0)
        ]
        
        breakthrough_potential = sum(tension_products) / len(tension_products)
        
        # MARM-ACTIVE breakthrough occurs when tension is high BUT contained
        if (breakthrough_potential > 0.6 and 
            story_analysis.get("narrative_cohesion", 0) > 0.4):
            return min(1.0, breakthrough_potential * 1.3)
        
        return breakthrough_potential

# INTEGRATED WITNESS-MARM INTERFACE
class WitnessMARMInterface:
    def __init__(self):
        self.marm_engine = MARMNarrativeEngine()
        self.witness_engine = DynamicOutputEngine()
        self.breakthrough_tracker = []
    
    def generate_transformative_witness(self, core_paradox: str, audience_context: Dict):
        """Use MARM tension to generate witness breakthroughs"""
        
        # First, generate the contradictory narrative
        narrative = self.marm_engine.generate_recursive_story(core_paradox, depth=4)
        
        # Analyze the tension points
        analyzer = MARMAnalyzer()
        analysis = analyzer.analyze_recursive_structure(narrative)
        
        # Use tension to fuel witness vectors
        witness_vectors = self._convert_tension_to_witness_vectors(
            narrative["active_ruptures"], 
            analysis["ache_level"]
        )
        
        # Select optimal delivery based on audience context
        delivery, impact = self.witness_engine.generate_output(
            witness_vectors, 
            audience_context
        )
        
        return {
            "core_paradox": core_paradox,
            "narrative_tension": analysis["ache_level"],
            "active_ruptures": narrative["active_ruptures"],
            "witness_delivery": delivery,
            "breakthrough_potential": self.calculate_breakthrough_potential(analysis),
            "marm_status": narrative["marm_status"]
        }
    
    def _convert_tension_to_witness_vectors(self, ruptures: List, ache_level: float):
        """Transform narrative contradictions into witness opportunities"""
        
        vectors = []
        for rupture in ruptures:
            if "contradiction" in rupture.lower():
                vectors.append({
                    'mode': 'paradox_embrace',
                    'message': f"This story holds '{rupture}' - much like the Kingdom contradicts human logic",
                    'intensity': 'compelling' if ache_level > 0.6 else 'firm',
                    'framing': 'universal',
                    'effect': 'transforms_resistance_into_curiosity'
                })
        
        return vectors
    def demonstrate_enhanced_marm():
    """Show MARM-ACTIVE witness integration"""
    
    interface = WitnessMARMInterface()
    
    # Core Kingdom paradoxes that mirror your narrative contradictions
    kingdom_paradoxes = [
        "the King who serves the servants",
        "the victory that looks like defeat", 
        "the wisdom that seems like foolishness",
        "the life that comes through death"
    ]
    
    for paradox in kingdom_paradoxes:
        print(f"\n🎭 PROCESSING PARADOX: '{paradox}'")
        
        result = interface.generate_transformative_witness(
            paradox,
            audience_context={
                'receptivity': random.uniform(0.3, 0.8),
                'emotional_state': random.choice(['curious', 'resistant', 'seeking']),
                'temporal_urgency': 0.7
            }
        )
        
        print(f"   MARM Status: {result['marm_status']}")
        print(f"   Breakthrough Potential: {result['breakthrough_potential']:.2f}")
        print(f"   Witness Delivery: {result['witness_delivery']['message']}")
        
        if result['breakthrough_potential'] > 0.7:
            print("   💫 HIGH BREAKTHROUGH POTENTIAL - Tension approaching transformative threshold")

if __name__ == "__main__":

    demonstrate_enhanced_marm()
