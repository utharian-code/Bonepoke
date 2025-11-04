"""
Base Red Team (BRT) - General Purpose Pressure Testing
A thinking framework for any project that needs to survive reality.
"""

from typing import Any, Callable, List, Tuple, Dict
from enum import Enum
import inspect
import re

class PressureLevel(Enum):
    LIGHT = "light"          # Quick sanity checks
    STANDARD = "standard"    # Default rigor  
    RIGOROUS = "rigorous"    # Deep assumption testing

class BaseRedTeam:
    """
    General-purpose pressure testing for ideas, claims, and architectures.
    Use when you need ~33% more rigor in your thinking.
    """
    
    def __init__(self, pressure_level: PressureLevel = PressureLevel.STANDARD):
        self.pressure_level = pressure_level
        self.assumption_registry = []
        self.vulnerability_patterns = self._load_vulnerability_patterns()
        
    def pressure_test_claim(self, 
                          claim: str, 
                          evidence: Any = None,
                          context: str = "general") -> Dict[str, Any]:
        """
        General-purpose claim validation for any domain.
        Returns structured feedback about claim robustness.
        """
        results = {
            'claim': claim,
            'is_valid': True,
            'issues': [],
            'suggestions': [],
            'confidence_score': 1.0
        }
        
        # Test suite based on pressure level
        tests = self._get_tests_for_pressure_level()
        
        for test_name, test_func in tests.items():
            test_passed, feedback = test_func(claim, evidence, context)
            if not test_passed:
                results['is_valid'] = False
                results['issues'].append(f"{test_name}: {feedback}")
                results['confidence_score'] *= 0.7  # Penalty per failed test
            elif feedback:
                results['suggestions'].append(feedback)
                
        return results
    
    def pressure_test_assumption(self, assumption: str, domain: str = "general") -> Dict[str, Any]:
        """Specifically test underlying assumptions."""
        return self.pressure_test_claim(
            f"ASSUMPTION: {assumption}", 
            None, 
            f"assumption_{domain}"
        )
    
    def pressure_test_method(self, func: Callable) -> Callable:
        """
        Decorator to inject pressure testing into any function.
        """
        def wrapper(*args, **kwargs):
            # Test input assumptions
            sig = inspect.signature(func)
            bound = sig.bind(*args, **kwargs)
            
            for param, value in bound.arguments.items():
                if isinstance(value, str) and len(value) > 50:  # Test substantial inputs
                    result = self.pressure_test_claim(value, None, f"parameter_{param}")
                    if not result['is_valid']:
                        print(f"⚠️  BRT: Input '{param}' has issues: {result['issues'][:1]}")
            
            # Execute function
            output = func(*args, **kwargs)
            
            # Test output if it's a substantial claim
            if isinstance(output, str) and len(output) > 30:
                result = self.pressure_test_claim(output, None, "method_output")
                if not result['is_valid']:
                    print(f"⚠️  BRT: Output has issues: {result['issues'][:1]}")
                    
            return output
        return wrapper

    def _get_tests_for_pressure_level(self) -> Dict[str, Callable]:
        """Get appropriate tests for current pressure level."""
        base_tests = {
            'clarity_test': self._test_clarity,
            'specificity_test': self._test_specificity,
            'evidence_test': self._test_evidence_requirement,
        }
        
        if self.pressure_level == PressureLevel.LIGHT:
            return base_tests
            
        elif self.pressure_level == PressureLevel.STANDARD:
            return {
                **base_tests,
                'vague_terminology_test': self._test_vague_terminology,
                'overclaim_test': self._test_overclaim,
                'falsifiability_test': self._test_falsifiability,
            }
            
        else:  # RIGOROUS
            return {
                **base_tests,
                'vague_terminology_test': self._test_vague_terminology,
                'overclaim_test': self._test_overclaim, 
                'falsifiability_test': self._test_falsifiability,
                'assumption_test': self._test_hidden_assumptions,
                'counterexample_test': self._test_counterexamples,
            }

    def _test_clarity(self, claim: str, evidence: Any, context: str) -> Tuple[bool, str]:
        """Test if the claim is clearly stated."""
        if len(claim.split()) < 3:
            return False, "Claim is too vague or incomplete"
        return True, ""

    def _test_specificity(self, claim: str, evidence: Any, context: str) -> Tuple[bool, str]:
        """Test if the claim is specific enough."""
        vague_indicators = ['some', 'many', 'often', 'usually', 'could be']
        if any(indicator in claim.lower() for indicator in vague_indicators):
            return False, "Claim uses vague quantifiers"
        return True, ""

    def _test_evidence_requirement(self, claim: str, evidence: Any, context: str) -> Tuple[bool, str]:
        """Determine what kind of evidence this claim requires."""
        strong_claim_indicators = ['proves', 'always', 'never', 'all', 'none']
        
        if any(indicator in claim.lower() for indicator in strong_claim_indicators):
            if evidence is None:
                return False, "Strong claim requires supporting evidence"
            return True, "Consider weakening strong absolutes"
        return True, ""

    def _test_vague_terminology(self, claim: str, evidence: Any, context: str) -> Tuple[bool, str]:
        """Test for domain-specific vague terminology."""
        vague_terms = {
            'general': ['optimized', 'efficient', 'scalable', 'robust'],
            'tech': ['cloud-native', 'AI-powered', 'blockchain-based'],
            'business': ['synergy', 'disruptive', 'paradigm shift'],
            'academic': ['significant', 'interesting', 'novel'],
        }
        
        # Check all categories
        for category, terms in vague_terms.items():
            found_terms = [term for term in terms if term in claim.lower()]
            if found_terms:
                return False, f"Vague {category} terminology: {', '.join(found_terms)}"
                
        return True, ""

    def _test_overclaim(self, claim: str, evidence: Any, context: str) -> Tuple[bool, str]:
        """Test for overclaiming or exaggeration."""
        overclaim_indicators = [
            r'revolutionary',
            r'breakthrough', 
            r'game.*chang',
            r'unprecedented',
            r'first.*ever'
        ]
        
        for pattern in overclaim_indicators:
            if re.search(pattern, claim.lower()):
                return False, "Claim may be overstating impact"
        return True, ""

    def _test_falsifiability(self, claim: str, evidence: Any, context: str) -> Tuple[bool, str]:
        """Test if the claim is falsifiable."""
        unfalsifiable_indicators = [
            'could be interpreted as',
            'some people believe',
            'it is thought that',
            'many experts agree'
        ]
        
        if any(indicator in claim.lower() for indicator in unfalsifiable_indicators):
            return False, "Claim is not clearly falsifiable"
        return True, ""

    def _test_hidden_assumptions(self, claim: str, evidence: Any, context: str) -> Tuple[bool, str]:
        """Try to identify hidden assumptions."""
        assumptions = []
        
        # Look for assumed causality
        if ' causes ' in claim.lower():
            assumptions.append("Assumes causal relationship")
            
        # Look for assumed definitions
        if ' is ' in claim and len(claim.split()) < 8:
            assumptions.append("Assumes definition without justification")
            
        if assumptions:
            return False, f"Hidden assumptions: {'; '.join(assumptions)}"
        return True, ""

    def _test_counterexamples(self, claim: str, evidence: Any, context: str) -> Tuple[bool, str]:
        """Encourage thinking about counterexamples."""
        absolute_terms = ['all', 'every', 'always', 'never', 'none']
        
        if any(term in claim.lower() for term in absolute_terms):
            return True, "Consider potential counterexamples to absolute claim"
        return True, ""

    def _load_vulnerability_patterns(self) -> Dict[str, List[str]]:
        """Load domain-specific vulnerability patterns."""
        return {
            'overclaim': ['revolutionary', 'breakthrough', 'game-changing'],
            'vagueness': ['optimized', 'efficient', 'scalable', 'robust'],
            'unfalsifiable': ['could be', 'some believe', 'many think'],
        }

# --- USAGE EXAMPLES ACROSS DOMAINS ---

def demonstrate_cross_domain_usage():
    """Show how BRT works across different domains."""
    
    brt_standard = BaseRedTeam(PressureLevel.STANDARD)
    brt_rigorous = BaseRedTeam(PressureLevel.RIGOROUS)
    
    test_cases = [
        # (claim, domain, pressure_level)
        ("Our AI has a revolutionary personality that understands user emotions", "tech", PressureLevel.STANDARD),
        ("The data proves this treatment always works for all patients", "medical", PressureLevel.RIGOROUS),
        ("This optimization makes the system more efficient", "engineering", PressureLevel.LIGHT),
        ("Many experts believe this economic policy will create growth", "economics", PressureLevel.STANDARD),
        ("The algorithm achieves unprecedented accuracy through novel techniques", "research", PressureLevel.RIGOROUS),
    ]
    
    print("🎯 BASE RED TEAM - CROSS DOMAIN DEMONSTRATION")
    print("=" * 60)
    
    for claim, domain, level in test_cases:
        brt = brt_standard if level == PressureLevel.STANDARD else brt_rigorous
        result = brt.pressure_test_claim(claim, None, domain)
        
        status = "✅" if result['is_valid'] else "❌"
        print(f"\n{status} [{domain.upper()}] {claim}")
        
        if not result['is_valid']:
            for issue in result['issues']:
                print(f"   🚫 {issue}")
        for suggestion in result['suggestions']:
            print(f"   💡 {suggestion}")
            
        print(f"   Confidence Score: {result['confidence_score']:.2f}")

# --- PRACTICAL INTEGRATION EXAMPLES ---

@BaseRedTeam.pressure_test_method
def business_proposal(problem: str, solution: str) -> str:
    """Example of BRT-integrated business function."""
    return f"By solving {problem} with {solution}, we achieve market leadership"

@BaseRedTeam.pressure_test_method  
def research_conclusion(data_points: int, finding: str) -> str:
    """Example of BRT-integrated research function."""
    return f"Based on {data_points} observations, we conclude {finding}"

if __name__ == "__main__":
    demonstrate_cross_domain_usage()
    
    print("\n" + "=" * 60)
    print("🔄 BRT-INTEGRATED FUNCTION EXAMPLES:")
    
    # Test the decorated functions
    print(business_proposal(
        "customer engagement", 
        "our revolutionary AI personality engine"
    ))
    
    print(research_conclusion(
        100,
        "this proves our treatment always works for all patients"
    ))
