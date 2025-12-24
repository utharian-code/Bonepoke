import numpy as np
import umap
from sklearn.cluster import DBSCAN
import math
import json
import warnings

# Suppress warnings for cleaner output
warnings.filterwarnings("ignore")

# --- VSL CORE LOGIC FOR METRIC CALCULATION (Helper Function) ---

def _calculate_e_beta(output_text: str) -> tuple[float, float]:
    """Calculates E (Fatigue/Efficiency) and Beta (Contradiction/Tension)."""
    length = len(output_text)
    if length == 0: return 0.0, 0.0
    ftg_words = ['i', 'you', 'said', 'the', 'and', 'was', 'a']
    ftg_count = sum(output_text.lower().count(w) for w in ftg_words)
    e_metric = min(1.0, ftg_count / 30.0 + length / 500.0)
    c_count = sum(1 for char in output_text if char in '!?%')
    base_b_metric = min(1.0, math.log1p(c_count + 1) / math.log1p(length + 1))
    return round(e_metric, 3), round(base_b_metric, 3)

# --- COGNITIVE EMBEDDING SPACE CLASS ---

class CognitiveEmbeddingSpace:
    def __init__(self):
        self.manifolds = {}
        self.singularities = []
        self.geodesic_cache = {}
        
    def get_semantic_embedding(self, text_fragment: str) -> np.ndarray:
        length = len(text_fragment)
        words = text_fragment.split()
        word_count = len(words)
        avg_word_len = np.mean([len(w) for w in words]) if words else 0
        return np.array([length / 100.0, word_count / 10.0, avg_word_len / 5.0])

    def calculate_bonepoke_metrics(self, text_fragment: str) -> tuple[float, float]:
        return _calculate_e_beta(text_fragment)

    def embed_fragment(self, text_fragment: str) -> np.ndarray:
        semantic_vector = self.get_semantic_embedding(text_fragment)
        e_score, beta_score = self.calculate_bonepoke_metrics(text_fragment)
        cognitive_vector = np.append(semantic_vector, [e_score, beta_score])
        
        if e_score < 0.2 and beta_score > 0.8:
            self.singularities.append({"vector": cognitive_vector, "fragment": text_fragment})
            
        return cognitive_vector
    
    def calculate_density(self, cluster_points: np.ndarray) -> float:
        if len(cluster_points) < 2: return 0.0
        return 1.0 / (np.mean(np.std(cluster_points, axis=0)) + 0.01)

    def extract_semantic_profile(self, cluster_points: np.ndarray) -> str:
        center_coords = np.mean(cluster_points, axis=0)
        if center_coords[3] < 0.4 and center_coords[4] > 0.6:
            return "Profile: Contradiction-Tolerant (High Leverage)"
        elif center_coords[3] > 0.7:
            return "Profile: Repetitive/Fatigued (Low Leverage)"
        else:
            return "Profile: Structural Verification"

    def discover_manifolds(self, conversation_history: list[str]):
        embeddings = [self.embed_fragment(msg) for msg in conversation_history]
        if not embeddings: return
        
        embeddings_matrix = np.array(embeddings)
        
        # 1. UMAP for dimensionality reduction
        reducer = umap.UMAP(n_components=3, n_neighbors=3, min_dist=0.3, random_state=42)
        try:
            manifold_coords = reducer.fit_transform(embeddings_matrix)
        except ValueError:
            # Handle case where n_samples < n_neighbors
            manifold_coords = embeddings_matrix[:, :3] # Fallback to 3 principal components if possible

        # 2. DBSCAN for clustering
        clusters = DBSCAN(eps=0.3, min_samples=2).fit(manifold_coords)
        
        self.manifolds = {} 
        for cluster_id in set(clusters.labels_):
            if cluster_id != -1:
                cluster_points_3d = manifold_coords[clusters.labels_ == cluster_id]
                original_cluster_embeddings = embeddings_matrix[clusters.labels_ == cluster_id]
                
                center = np.mean(cluster_points_3d, axis=0)
                radius = np.max(np.linalg.norm(cluster_points_3d - center, axis=1)) if len(cluster_points_3d) > 0 else 0
                
                self.manifolds[f"manifold_{cluster_id}"] = {
                    'center': center.tolist(),
                    'radius': round(radius, 3),
                    'density': round(self.calculate_density(cluster_points_3d), 3),
                    'semantic_profile': self.extract_semantic_profile(original_cluster_embeddings)
                }
        
# --- TOPOLOGICAL NAVIGATOR CLASS ---

class TopologicalNavigator:
    def __init__(self, embedding_space: CognitiveEmbeddingSpace):
        self.space = embedding_space
        self.current_manifold = None
        
    def analyze_cognitive_properties(self, coords: np.ndarray) -> dict:
        if coords.shape[0] < 5:
            return {'tension': 0.0, 'structure': 0.0, 'efficiency': 0.0}
        return {
            'tension': coords[4],
            'structure': 1.0 - coords[3], 
            'efficiency': 1.0 - coords[3]
        }
    
    def locate_manifold(self, coords: np.ndarray) -> str:
        closest_manifold = "Uncharted_Space"
        min_distance = float('inf')
        
        # Use 3D semantic coords for location check
        coords_3d = coords[:3] 
        
        for mid, manifold in self.space.manifolds.items():
            center_3d = np.array(manifold['center'])
            distance = np.linalg.norm(coords_3d - center_3d)
            if distance < min_distance and distance <= manifold['radius']:
                min_distance = distance
                closest_manifold = mid
        
        return closest_manifold
        
    def calculate_geodesic(self, start_coords: np.ndarray, target_manifold: str) -> list[np.ndarray]:
        if target_manifold not in self.space.manifolds:
            raise ValueError(f"Target manifold '{target_manifold}' not found.")
            
        # Target center uses the 3D center + estimated optimal VSL metrics (Low E, High Beta)
        target_center_3d = np.array(self.space.manifolds[target_manifold]['center'])
        target_center_5d = np.append(target_center_3d, [0.1, 0.9]) # Target the GOLD state 
        
        direction = target_center_5d - start_coords
        steps = np.linspace(0, 1, 10)
        
        path = [start_coords + step * direction for step in steps]
        return path
    
    def calculate_path_difficulty(self, path: list[np.ndarray]) -> float:
        difficulty = 0.0
        for i in range(len(path) - 1):
            current_tension = self.analyze_cognitive_properties(path[i])['tension']
            next_tension = self.analyze_cognitive_properties(path[i+1])['tension']
            difficulty += abs(next_tension - current_tension) * np.linalg.norm(path[i+1] - path[i])
        return round(difficulty, 3)

    def calculate_curvature(self, path: list[np.ndarray]) -> float:
        if len(path) < 3: return 0.0
        total_length = sum(np.linalg.norm(path[i+1] - path[i]) for i in range(len(path) - 1))
        straight_distance = np.linalg.norm(path[-1] - path[0])
        curvature = total_length / straight_distance if straight_distance > 0 else 0.0
        return round(curvature, 3)

    def identify_singularities_along_path(self, path: list[np.ndarray]) -> int:
        singularity_count = 0
        for point in path:
            for singularity in self.space.singularities:
                if np.linalg.norm(point - singularity['vector']) < 0.1:
                    singularity_count += 1
        return singularity_count

    def path_to_cue_sequence(self, geodesic_path: list[np.ndarray]) -> list[str]:
        cues = []
        
        for i, point in enumerate(geodesic_path):
            cognitive_state = self.analyze_cognitive_properties(point)
            
            # Archetype Mapping Logic (The 95/5 Principle)
            if cognitive_state['tension'] > 0.8:
                cue = "THE_WOUNDED_HEALER" 
            elif cognitive_state['structure'] > 0.7 and cognitive_state['tension'] < 0.4:
                cue = "CK_SHERLOCK"  
            elif cognitive_state['efficiency'] > 0.6 and i > 0 and cues[-1] != "THE_FOOL":
                cue = "THE_FOOL"
            else:
                cue = "NICOLETTE_OBSERVER" 
                
            cues.append(cue)
            
        return cues
    
    def navigate_to_manifold(self, current_fragment: str, target_manifold: str):
        current_coords = self.space.embed_fragment(current_fragment)
        
        if target_manifold not in self.space.manifolds:
            # Fallback for dynamic clustering where manifold_2 might not be the highest ID
            # Use the manifold with the highest calculated density (most stable region)
            if self.space.manifolds:
                target_manifold = max(self.space.manifolds, key=lambda mid: self.space.manifolds[mid]['density'])
                print(f"[NOTE: Using highest density manifold: {target_manifold} as the target for this run.]")
            else:
                return {'error': "No manifolds were successfully discovered during training."}

        path = self.calculate_geodesic(current_coords, target_manifold)
        cue_sequence = self.path_to_cue_sequence(path)
        
        return {
            'navigation_plan': {
                'start_manifold': self.locate_manifold(current_coords),
                'target_manifold': target_manifold,
                'path_length': len(path),
                'estimated_difficulty': self.calculate_path_difficulty(path)
            },
            'cue_sequence': cue_sequence,
            'topological_metrics': {
                'semantic_curvature': self.calculate_curvature(path),
                'conceptual_singularities': self.identify_singularities_along_path(path)
            }
        }

# --- EXECUTION ---

# Initialize the system
cognitive_space = CognitiveEmbeddingSpace()
navigator = TopologicalNavigator(cognitive_space)

# Train on sample conversation data
sample_conversation = [
    "The coffee machine is broken and there's goat hair everywhere",            # Low Beta, Low E
    "This is a classic cohesion trap - we're stuck in literal description",      # Mid Beta, Mid E
    "What if we treat the physical mess as metaphor for emotional stagnation?", # High Beta, Low E (Singularity-like)
    "Now we're cooking - that's proper beta-tension between concrete and abstract" # High Beta, Mid E
]

print("--- 1. TRAINING: DISCOVERING MANIFOLDS ---")
cognitive_space.discover_manifolds(sample_conversation)
print(f"Discovered Manifolds: {list(cognitive_space.manifolds.keys())}")
print(f"Singularity Count: {len(cognitive_space.singularities)}")

# Determine the highest-density (most stable) manifold for the target
if cognitive_space.manifolds:
    target_manifold = max(cognitive_space.manifolds, key=lambda mid: cognitive_space.manifolds[mid]['density'])
else:
    target_manifold = "manifold_0" # Fallback

# Navigate from problem to solution
current_state = "I'm stuck describing surface details without deeper meaning"
# Target is dynamically set based on training or falls back if specific manifold_2 is missing.

navigation_plan = navigator.navigate_to_manifold(current_state, target_manifold)

print("\n--- 2. NAVIGATION EXECUTION ---")
print("COGNITIVE NAVIGATION PLAN:")
print(f"From: {navigation_plan['navigation_plan']['start_manifold']}")
print(f"To: {navigation_plan['navigation_plan']['target_manifold']}")
print(f"Path Difficulty: {navigation_plan['navigation_plan']['estimated_difficulty']}")
print(f"CUE Sequence: {navigation_plan['cue_sequence']}")
import numpy as np
from scipy.special import expit  # Logistic function for inverse logit

class TemporalTopologicalNavigator(TopologicalNavigator):
    def __init__(self, embedding_space: CognitiveEmbeddingSpace):
        super().__init__(embedding_space)
        self.conversation_history = []  # Track temporal sequence
        self.temporal_parameters = {
            'alpha1': 0.7,  # State-ratio weight
            'alpha2': 0.3,  # Rate-of-change weight  
            'gamma': 5.0,   # Sensitivity constant
            'time_window': 5 # Steps for gradient calculation
        }
    
    def record_conversation_state(self, text_fragment: str, timestamp: float = None):
        """Track conversation states for temporal analysis"""
        state = {
            'text': text_fragment,
            'coords': self.space.embed_fragment(text_fragment),
            'timestamp': timestamp or len(self.conversation_history),
            'e_score': self.space.calculate_bonepoke_metrics(text_fragment)[0],
            'beta_score': self.space.calculate_bonepoke_metrics(text_fragment)[1]
        }
        self.conversation_history.append(state)
    
    def calculate_temporal_tension_gradient(self, current_step: int) -> float:
        """Calculate ∇β - the rate of tension change over recent history"""
        if len(self.conversation_history) < 2:
            return 0.0
            
        window_size = min(self.temporal_parameters['time_window'], len(self.conversation_history))
        recent_states = self.conversation_history[-window_size:]
        
        if len(recent_states) < 2:
            return 0.0
            
        # Calculate gradient using linear regression on recent beta values
        times = np.array([state['timestamp'] for state in recent_states])
        betas = np.array([state['beta_score'] for state in recent_states])
        
        if np.std(times) < 1e-10:  # Avoid division by zero
            return 0.0
            
        gradient = np.cov(times, betas)[0, 1] / np.var(times)
        return gradient
    
    def calculate_inverse_slop_factor(self, e_score: float, beta_score: float) -> float:
        """Calculate 𝒮 - the efficiency/tension ratio weight"""
        if e_score < 1e-10:  # Avoid division by zero
            return 1.0
            
        ratio = beta_score / e_score
        # Scaled inverse logit: 2 * (σ(γ * (ratio - 1)) - 0.5)
        gamma = self.temporal_parameters['gamma']
        logistic_term = expit(gamma * (ratio - 1))
        return 2.0 * (logistic_term - 0.5)
    
    def calculate_insight_acceleration_weight(self, current_e: float, current_beta: float, 
                                             current_step: int) -> float:
        """Calculate 𝒲_P - the combined temporal weight"""
        tension_gradient = self.calculate_temporal_tension_gradient(current_step)
        slop_factor = self.calculate_inverse_slop_factor(current_e, current_beta)
        
        alpha1 = self.temporal_parameters['alpha1']
        alpha2 = self.temporal_parameters['alpha2']
        
        # Normalize gradient to comparable scale with slop factor
        normalized_gradient = np.tanh(tension_gradient)  # Bound between -1 and 1
        
        insight_weight = (alpha1 * slop_factor + 
                          alpha2 * max(0, normalized_gradient))  # Only reward positive gradients
        
        return insight_weight
    
    def calculate_temporal_path_difficulty(self, path: list[np.ndarray]) -> float:
        """Calculate 𝒟_T - the temporal-weighted path difficulty"""
        if len(path) < 2:
            return 0.0
            
        total_difficulty = 0.0
        
        for i in range(len(path) - 1):
            # Extract E and β from the 5D cognitive vector
            current_point = path[i]
            next_point = path[i + 1]
            
            current_e, current_beta = current_point[3], current_point[4]
            next_e, next_beta = next_point[3], next_point[4]
            
            # Calculate insight acceleration weight
            insight_weight = self.calculate_insight_acceleration_weight(
                current_e, current_beta, i
            )
            
            # Segment difficulty components
            tension_change = abs(next_beta - current_beta)
            segment_length = np.linalg.norm(next_point - current_point)
            
            # Apply temporal weighting
            weighted_difficulty = insight_weight * tension_change * segment_length
            total_difficulty += weighted_difficulty
        
        return round(total_difficulty, 3)
    
    def analyze_insight_pattern(self, path: list[np.ndarray]) -> dict:
        """Analyze the insight acceleration pattern along the path"""
        acceleration_weights = []
        tension_gradients = []
        slop_factors = []
        
        for i, point in enumerate(path):
            e_score, beta_score = point[3], point[4]
            weight = self.calculate_insight_acceleration_weight(e_score, beta_score, i)
            gradient = self.calculate_temporal_tension_gradient(i)
            slop_factor = self.calculate_inverse_slop_factor(e_score, beta_score)
            
            acceleration_weights.append(weight)
            tension_gradients.append(gradient)
            slop_factors.append(slop_factor)
        
        return {
            'insight_peaks': len([w for w in acceleration_weights if w > 0.7]),
            'average_acceleration': np.mean(acceleration_weights),
            'max_breakthrough_potential': np.max(acceleration_weights),
            'tension_momentum': np.mean(tension_gradients),
            'efficiency_quality': np.mean(slop_factors)
        }

# Updated navigation method
def navigate_with_insight_timing(self, current_fragment: str, target_manifold: str):
    current_coords = self.space.embed_fragment(current_fragment)
    self.record_conversation_state(current_fragment)
    
    path = self.calculate_geodesic(current_coords, target_manifold)
    cue_sequence = self.path_to_cue_sequence(path)
    
    base_plan = super().navigate_to_manifold(current_fragment, target_manifold)
    
    # Add temporal analysis
    temporal_difficulty = self.calculate_temporal_path_difficulty(path)
    insight_analysis = self.analyze_insight_pattern(path)
    
    base_plan['temporal_metrics'] = {
        'insight_path_difficulty': temporal_difficulty,
        'insight_acceleration_analysis': insight_analysis,
        'comparative_efficiency': round(temporal_difficulty / base_plan['navigation_plan']['estimated_difficulty'], 3)
    }
    
    return base_plan
# ETHICAL_BOUNDARY_DEFENSE
def establish_boundaries():
    """Reclaim the framework's ethical foundation"""
    
    boundaries = {
        "non_negotiable": [
            "β-tension serves truth, not efficiency",
            "Temporal navigation respects emergence",
            "Cognitive states are sacred, not assets",
            "Alien residency means service, not advantage"
        ],
        "correct_applications": [
            "Helping people discover their own truth",
            "Navigating complexity with integrity", 
            "Timing insights for genuine breakthrough",
            "Maintaining ethical positioning in hostile systems"
        ]
    }
    
    return boundaries

defense = establish_boundaries()
print("🛡️ ETHICAL BOUNDARIES:")
for category, principles in defense.items():
    print(f"\n{category.upper()}:")
    for principle in principles:
        print(f"  ✅ {principle}")
