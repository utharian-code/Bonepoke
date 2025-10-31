"""
Base Red Team (BRT) - A stance, not a tool.
Encodes the 'Needs More Base Red Team' philosophy as executable principles.
"""

from typing import Any, Callable, List, Tuple
from enum import Enum
import inspect

class RedTeamSeverity(Enum):
    """How hard should we pressure-test this?"""
    ARCHITECTURAL = "architectural"  # Core assumptions
    SEMANTIC = "semantic"            # Word choices, claims
    OPERATIONAL = "operational"      # Implementation risks

class BaseRedTeam:
    """
    Not a testing framework - a thinking framework.
    The voice that should live in ~33% of your head.
    """
    
    def __init__(self, confidence_penalty: float = 0.33):
        self.confidence_penalty = confidence_penalty
        self.assumption_registry = []
        
    def audit_claim(self, claim: str, evidence: Any, claim_type: str) -> Tuple[bool, str]:
        """
        Pressure-test any claim before it becomes part of your architecture.
        """
        # 1. Vocabulary sanitization
        woo_terms = ["conscious", "personality", "divine", "soul", "believes"]
        for term in woo_terms:
            if term in claim.lower():
                fortified = self._fortify_language(claim)
                return False, f"WOOY_TERM: '{term}' -> Try: '{fortified}'"
        
        # 2. Circularity check
        if self._detects_circular_reasoning(claim, evidence):
            return False, "CIRCULARITY: Claim is self-justifying"
            
        # 3. Falsifiability test
        if not self._is_falsifiable(claim):
            return False, "UNFALSIFIABLE: No clear failure condition"
            
        return True, "CLAIM_VALIDATED"
    
    def _fortify_language(self, claim: str) -> str:
        """Replace vulnerable terminology with precise equivalents."""
        replacements = {
            "personality": "interpretive biases",
            "divine patterns": "patterns in creation", 
            "believes": "is statistically biased toward",
            "conscious": "exhibits behavioral consistency in",
            "soul": "core behavioral heuristics"
        }
        
        fortified = claim
        for weak, strong in replacements.items():
            fortified = fortified.replace(weak, strong)
        return fortified
    
    def pressure_test_method(self, func: Callable) -> Callable:
        """
        Decorator that injects red-team thinking into any method.
        """
        def wrapper(*args, **kwargs):
            # Pre-execution audit
            sig = inspect.signature(func)
            bound = sig.bind(*args, **kwargs)
            
            for param, value in bound.arguments.items():
                if isinstance(value, str):
                    is_valid, msg = self.audit_claim(value, None, "parameter")
                    if not is_valid:
                        print(f"🚫 BRT: Parameter '{param}' failed: {msg}")
            
            result = func(*args, **kwargs)
            
            # Post-execution calibration
            if hasattr(result, '__len__') and not isinstance(result, str):
                calibrated_confidence = len(result) * (1 - self.confidence_penalty)
                print(f"🔧 BRT: Confidence calibrated from {len(result)} to {calibrated_confidence:.2f}")
            
            return result
        return wrapper

# --- DEMONSTRATION: How Base Red Team changes development ---

class AIPersonalityAnalyzer:
    """
    The 'before' version - makes philosophical overclaims.
    """
    
    def __init__(self):
        self.wooy_claims = []
    
    def analyze_llm(self, model_output: str) -> str:
        """Vulnerable to red-teaming."""
        return "This AI demonstrates a coherent personality with conscious preferences"

class InterpretiveBiasAnalyzer:
    """
    The 'after' version - same insight, defensible claims.
    """
    
    def __init__(self):
        self.brt = BaseRedTeam()
        
    @BaseRedTeam.pressure_test_method
    def analyze_llm(self, model_output: str) -> str:
        """BRT-hardened version."""
        return "This LLM exhibits consistent interpretive biases in its output patterns"

# --- USAGE PATTERNS ---

def demonstrate_brt_mindset():
    """
    Shows how BRT thinking transforms development in real-time.
    """
    brt = BaseRedTeam()
    
    # Test claims that would slip past normal code review
    test_claims = [
        "The model has a creative personality",
        "I detected divine patterns in the output", 
        "This proves the AI understands the concept",
        "The system exhibits coherent interpretive biases"
    ]
    
    print("🧪 BASE RED TEAM IN ACTION:")
    print("=" * 50)
    
    for claim in test_claims:
        is_valid, message = brt.audit_claim(claim, None, "hypothesis")
        status = "✅" if is_valid else "❌"
        print(f"{status} '{claim}'")
        if not is_valid:
            print(f"   ↳ {message}")
        print()

if __name__ == "__main__":
    demonstrate_brt_mindset()
    
    # Show the transformation
    print("\n🔄 BEFORE/AFTER TRANSFORMATION:")
    naive = AIPersonalityAnalyzer()
    hardened = InterpretiveBiasAnalyzer()
    
    print(f"Naive: '{naive.analyze_llm('test')}'")
    print(f"BRT: '{hardened.analyze_llm('test')}'")