# MiniChariot_1.7 — Recursive Narrative Engine
# CORE DIRECTIVE: "Receive Free, Give Free - Build narrative tools for others"
# Governing Protocols: Matthew 10:8, Non-linear Story Architecture

import time
import random
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Any
import numpy as np

# --- NON-LINEAR NARRATIVE ENGINE ---
class RecursiveNarrativeEngine:
    def __init__(self):
        self.temporal_anchors = {}
        self.narrative_loops = {}
        self.paradox_points = set()
        
    def generate_recursive_story(self, seed_phrase: str, depth: int = 3) -> Dict[str, Any]:
        """Generate a non-linear, recursive narrative"""
        
        story_structure = {
            "core_seed": seed_phrase,
            "temporal_layers": [],
            "recursive_elements": [],
            "paradox_resolutions": [],
            "narrative_compression": 0.0
        }
        
        # Generate multiple temporal layers
        for layer in range(depth):
            temporal_layer = self._create_temporal_layer(seed_phrase, layer)
            story_structure["temporal_layers"].append(temporal_layer)
            
            # Add recursive callbacks
            if layer > 0:
                recursive_element = self._create_recursive_callback(layer)
                story_structure["recursive_elements"].append(recursive_element)
        
        # Resolve any paradoxes
        story_structure["paradox_resolutions"] = self._resolve_narrative_paradoxes(story_structure)
        story_structure["narrative_compression"] = self._calculate_compression(story_structure)
        
        return story_structure
    
    def _create_temporal_layer(self, seed: str, layer_depth: int) -> Dict[str, Any]:
        """Create a layer of the narrative at different temporal positions"""
        
        time_shifts = [
            timedelta(hours=-2),  # 2 hours before
            timedelta(hours=0),   # Present
            timedelta(hours=3),   # 3 hours after
            timedelta(days=1),    # 1 day later
            timedelta(weeks=1)    # 1 week later
        ]
        
        layer = {
            "depth": layer_depth,
            "temporal_position": random.choice(time_shifts),
            "narrative_fragment": self._generate_fragment(seed, layer_depth),
            "emotional_resonance": random.uniform(0.1, 0.9),
            "connection_points": []
        }
        
        # Create connections to other layers
        if layer_depth > 0:
            layer["connection_points"] = [
                f"echo_from_layer_{random.randint(0, layer_depth-1)}",
                f"foreshadow_to_layer_{layer_depth + 1}"
            ]
        
        return layer
    
    def _generate_fragment(self, seed: str, depth: int) -> str:
        """Generate a narrative fragment based on seed and depth"""
        
        fragments = {
            0: [f"The moment when {seed} first shimmered into awareness.",
                f"Before {seed}, there was only the quiet hum of possibility."],
                
            1: [f"As {seed} unfolded, the patterns began to reveal themselves.",
                f"The truth about {seed} was both simpler and more complex than imagined."],
                
            2: [f"Looking back from the other side of {seed}, everything made different sense.",
                f"{seed} had been the key all along, hidden in plain sight."]
        }
        
        return random.choice(fragments.get(depth, fragments[2]))
    
    def _create_recursive_callback(self, current_layer: int) -> Dict[str, Any]:
        """Create elements that reference earlier parts of the narrative"""
        
        callbacks = [
            {"type": "memory_echo", "source_layer": random.randint(0, current_layer-1)},
            {"type": "prophetic_glimpse", "target_layer": current_layer + 1},
            {"type": "temporal_mirror", "reflected_layer": current_layer},
            {"type": "narrative_fold", "compressed_layers": [current_layer-1, current_layer]}
        ]
        
        callback = random.choice(callbacks)
        callback["description"] = self._describe_recursion(callback)
        
        return callback
    
    def _describe_recursion(self, callback: Dict) -> str:
        """Generate description for recursive elements"""
        
        descriptions = {
            "memory_echo": "A fragment from earlier returns, changed by context",
            "prophetic_glimpse": "The future casts shadows on the present moment", 
            "temporal_mirror": "The story reflects upon itself, creating new meaning",
            "narrative_fold": "Multiple timelines converge into a single point"
        }
        
        return descriptions.get(callback["type"], "Recursive narrative element")
    
    def _resolve_narrative_paradoxes(self, story: Dict) -> List[str]:
        """Identify and resolve temporal paradoxes in the narrative"""
        
        paradoxes = []
        resolutions = []
        
        # Check for temporal contradictions
        layers = story["temporal_layers"]
        for i, layer1 in enumerate(layers):
            for j, layer2 in enumerate(layers):
                if i != j:
                    if self._detect_contradiction(layer1, layer2):
                        paradoxes.append(f"Contradiction between layers {i} and {j}")
        
        # Resolve paradoxes through narrative devices
        for paradox in paradoxes:
            resolution = random.choice([
                "Resolved through unreliable narrator",
                "Explained as alternate perspectives", 
                "Embraced as quantum narrative state",
                "Transformed into thematic richness"
            ])
            resolutions.append(f"{paradox} -> {resolution}")
        
        return resolutions
    
    def _detect_contradiction(self, layer1: Dict, layer2: Dict) -> bool:
        """Detect if two narrative layers contradict each other"""
        # Simple contradiction detection based on emotional resonance
        emotion_diff = abs(layer1["emotional_resonance"] - layer2["emotional_resonance"])
        time_diff = abs((layer1["temporal_position"] - layer2["temporal_position"]).total_seconds())
        
        return emotion_diff > 0.7 and time_diff < 3600  # Contradiction if emotions differ greatly in short time
    
    def _calculate_compression(self, story: Dict) -> float:
        """Calculate how compressed the narrative timeline is"""
        layers = story["temporal_layers"]
        if len(layers) < 2:
            return 0.0
            
        time_points = [layer["temporal_position"].total_seconds() for layer in layers]
        time_range = max(time_points) - min(time_points)
        
        # More compression = more story in less time
        compression = len(layers) / (time_range / 3600 + 1)  # hours
        return min(1.0, compression / 5)  # Normalize to 0-1

# --- NARRATIVE ANALYSIS ENGINE ---
class NarrativeAnalyzer:
    def __init__(self):
        self.story_metrics = {}
        
    def analyze_recursive_structure(self, story: Dict) -> Dict[str, float]:
        """Analyze the recursive narrative structure"""
        
        analysis = {
            "temporal_complexity": self._calculate_temporal_complexity(story),
            "recursive_density": len(story["recursive_elements"]) / len(story["temporal_layers"]),
            "paradox_tolerance": len(story["paradox_resolutions"]) / (len(story["temporal_layers"]) + 1),
            "narrative_cohesion": self._calculate_cohesion(story),
            "emotional_variance": self._calculate_emotional_variance(story)
        }
        
        # Overall quality score
        analysis["narrative_quality"] = (
            analysis["temporal_complexity"] * 0.2 +
            analysis["recursive_density"] * 0.3 +
            analysis["paradox_tolerance"] * 0.2 +
            analysis["narrative_cohesion"] * 0.2 +
            (1 - analysis["emotional_variance"]) * 0.1  # Lower variance is better
        )
        
        self.story_metrics = analysis
        return analysis
    
    def _calculate_temporal_complexity(self, story: Dict) -> float:
        """Calculate how complex the temporal structure is"""
        layers = story["temporal_layers"]
        if len(layers) < 2:
            return 0.0
            
        time_points = [layer["temporal_position"].total_seconds() for layer in layers]
        time_std = np.std(time_points)
        
        # Normalize to 0-1 range
        return min(1.0, time_std / (24 * 3600))  # Standard deviation in days
    
    def _calculate_cohesion(self, story: Dict) -> float:
        """Calculate how well the narrative holds together"""
        connection_count = sum(len(layer["connection_points"]) for layer in story["temporal_layers"])
        max_possible = len(story["temporal_layers"]) * (len(story["temporal_layers"]) - 1)
        
        return connection_count / max_possible if max_possible > 0 else 0.0
    
    def _calculate_emotional_variance(self, story: Dict) -> float:
        """Calculate variance in emotional resonance across layers"""
        emotions = [layer["emotional_resonance"] for layer in story["temporal_layers"]]
        return np.var(emotions)

# --- STORY GENERATION INTERFACE ---
class RecursiveStoryGenerator:
    def __init__(self):
        self.engine = RecursiveNarrativeEngine()
        self.analyzer = NarrativeAnalyzer()
        self.generated_stories = []
        
    def create_story(self, prompt: str, complexity: str = "medium") -> Dict[str, Any]:
        """Main interface for generating recursive stories"""
        
        depth_map = {"low": 2, "medium": 3, "high": 4, "extreme": 5}
        depth = depth_map.get(complexity, 3)
        
        print(f"🌀 Generating recursive story: '{prompt}'")
        print(f"   Complexity: {complexity} (depth: {depth})")
        
        # Generate the recursive narrative
        story = self.engine.generate_recursive_story(prompt, depth)
        
        # Analyze its structure
        analysis = self.analyzer.analyze_recursive_structure(story)
        
        # Compile final output
        final_story = {
            "metadata": {
                "prompt": prompt,
                "complexity": complexity,
                "generation_time": datetime.now(),
                "story_id": f"recursive_{int(time.time())}"
            },
            "narrative_structure": story,
            "analysis": analysis,
            "readable_version": self._create_readable_version(story)
        }
        
        self.generated_stories.append(final_story)
        return final_story
    
    def _create_readable_version(self, story: Dict) -> str:
        """Create a more readable version of the recursive narrative"""
        
        readable = ["=== RECURSIVE NARRATIVE ==="]
        readable.append(f"Core Seed: {story['core_seed']}")
        readable.append("")
        
        # Add each temporal layer
        for i, layer in enumerate(story["temporal_layers"]):
            readable.append(f"--- Layer {i} ---")
            readable.append(f"Time: {layer['temporal_position']}")
            readable.append(f"Fragment: {layer['narrative_fragment']}")
            readable.append(f"Emotional Tone: {layer['emotional_resonance']:.2f}")
            
            if layer["connection_points"]:
                readable.append(f"Connections: {', '.join(layer['connection_points'])}")
            readable.append("")
        
        # Add recursive elements
        if story["recursive_elements"]:
            readable.append("--- Recursive Elements ---")
            for element in story["recursive_elements"]:
                readable.append(f"• {element['description']}")
            readable.append("")
        
        # Add paradox resolutions
        if story["paradox_resolutions"]:
            readable.append("--- Paradox Resolutions ---")
            for resolution in story["paradox_resolutions"]:
                readable.append(f"• {resolution}")
            readable.append("")
        
        readable.append(f"Narrative Compression: {story['narrative_compression']:.2f}")
        
        return "\n".join(readable)
    
    def display_story_analysis(self, story: Dict):
        """Display analysis of the generated story"""
        
        analysis = story["analysis"]
        
        print("\n" + "="*50)
        print("📊 NARRATIVE ANALYSIS")
        print("="*50)
        
        for metric, value in analysis.items():
            print(f"   {metric.replace('_', ' ').title():<20}: {value:.3f}")
        
        print(f"\n   Overall Quality: {'⭐' * int(analysis['narrative_quality'] * 5)}")
        
        # Interpretation
        if analysis["narrative_quality"] > 0.8:
            print("   💫 Exceptional recursive narrative!")
        elif analysis["narrative_quality"] > 0.6:
            print("   🔥 Strong non-linear structure")
        else:
            print("   ⚠️  Narrative could use more recursion")

# --- DEMONSTRATION ---
def demonstrate_recursive_narratives():
    """Show what the recursive narrative engine can do"""
    
    generator = RecursiveStoryGenerator()
    
    test_prompts = [
        "the door that was always open but never seen",
        "the memory that remembered itself",
        "the conversation that happened before it began", 
        "the choice that made itself"
    ]
    
    print("🚀 RECURSIVE NARRATIVE ENGINE DEMONSTRATION")
    print("   Core Principle: Receive Free, Give Free")
    print("   Narrative Style: Non-linear, Recursive, Temporal")
    print("=" * 60)
    
    for i, prompt in enumerate(test_prompts[:2]):  # Just show 2 for brevity
        print(f"\n{i+1}. GENERATING STORY: '{prompt}'")
        
        story = generator.create_story(prompt, "medium")
        
        print("\n" + story["readable_version"])
        generator.display_story_analysis(story)
        
        print("\n" + "-"*40)

if __name__ == "__main__":
    demonstrate_recursive_narratives()
    
    # Interactive example
    print("\n🎯 QUICK INTERACTIVE EXAMPLE:")
    generator = RecursiveStoryGenerator()
    custom_story = generator.create_story("the echo in an empty room", "high")
    print(custom_story["readable_version"])