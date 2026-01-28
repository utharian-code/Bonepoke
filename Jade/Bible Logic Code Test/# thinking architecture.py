# THINKING_ARCHITECTURE.py
# 150 lines - The cognitive pattern without the scaffolding

class ThinkingCore:
    """
    Your brain export: Essential patterns only
    No verbose outputs, just thinking architecture
    """
    
    def __init__(self):
        # 1. TRUTH HIERARCHY (Your Level 1>2>>>3 insight)
        self.truth_layers = {
            'CORE': ['adam_historical', 'bible_inspired', 'jesus_ransom'],
            'EVIDENCE': ['bible_survival', 'ancient_wisdom', 'prophecy'],
            'DETAIL': ['creation_timing', 'flood_scope', 'earth_age']
        }
        
        # 2. LEXICAL ARCHAEOLOGY METHOD
        self.semantic_excavations = {
            'day': {'range': ['period', 'era', 'age'], 'key': 'flexibility'},
            'flood': {'range': ['judgment', 'salvation', 'covenant'], 'key': 'theology_over_hydrology'},
            'adam': {'range': ['historical', 'archetype', 'narrative'], 'key': 'both_and'}
        }
        
        # 3. CASCADE AWARENESS
        self.dependency_chains = {
            'adam_historical': ['original_sin', 'ransom', 'second_adam'],
            'bible_inspired': ['prophecy_valid', 'moral_authority', 'divine_guidance']
        }
        
        # 4. REORIENTATION PATTERN (not dismissal)
        self.redirection_patterns = {
            'from_timing': 'to_purpose',
            'from_mechanism': 'to_meaning',
            'from_literal': 'to_semantic_range'
        }
        
        # Audit trail
        self.thinking_log = []
    
    def process(self, input_text, context=None):
        """Lean thinking process - returns thinking state, not verbose output"""
        
        # Log entry
        log_id = len(self.thinking_log)
        
        # 1. Classify by truth layer
        layer = self._classify_layer(input_text)
        
        # 2. Apply appropriate thinking
        if layer == 'CORE':
            thinking_pattern = 'AFFIRM_WITH_BASIS'
            content = self._handle_core(input_text)
            
        elif layer == 'EVIDENCE':
            thinking_pattern = 'PRESENT_MIRACLE'
            content = self._handle_evidence(input_text)
            
        else:  # DETAIL layer
            thinking_pattern = 'REORIENT_THROUGH_ARCHAEOLOGY'
            content = self._handle_detail(input_text)
        
        # 3. Check cascade implications
        cascade_check = self._check_cascade(input_text)
        
        # 4. Store thinking process (audit trail)
        self.thinking_log.append({
            'id': log_id,
            'input': input_text[:50],
            'layer': layer,
            'pattern': thinking_pattern,
            'cascade': cascade_check,
            'timestamp': log_id
        })
        
        # Return thinking state, not verbose explanation
        return {
            'thinking_state': {
                'active_layer': layer,
                'applied_pattern': thinking_pattern,
                'cascade_risk': cascade_check.get('risk', 'none'),
                'semantic_excavation_applied': content.get('excavation', False)
            },
            'content': content,
            'audit_id': log_id  # For looking up full thinking process
        }
    
    def _classify_layer(self, text):
        """Your hierarchy in action"""
        text_lower = text.lower()
        
        # Core layer detectors
        if any(term in text_lower for term in ['adam historical', 'bible inspired', 'jesus ransom']):
            return 'CORE'
        
        # Evidence layer detectors
        if any(term in text_lower for term in ['bible survive', 'ancient wisdom', 'prophecy']):
            return 'EVIDENCE'
        
        # Default to detail (most questions are detail-level)
        return 'DETAIL'
    
    def _handle_detail(self, text):
        """Your reorientation method"""
        # Check which excavation applies
        excavation = None
        if 'day' in text.lower():
            excavation = self.semantic_excavations['day']
        elif 'flood' in text.lower():
            excavation = self.semantic_excavations['flood']
        elif 'adam' in text.lower():
            excavation = self.semantic_excavations['adam']
        
        # Generate reoriented content
        if excavation:
            reorientation = f"Reoriented from {text.split()[0]} to {excavation['key']}"
        else:
            reorientation = "Reoriented from mechanism to meaning"
        
        return {
            'excavation': excavation,
            'reorientation': reorientation,
            'new_focus': 'theological meaning over scientific detail'
        }
    
    def _check_cascade(self, text):
        """Your cascade awareness"""
        risks = []
        for core_term, dependents in self.dependency_chains.items():
            if core_term in text.lower():
                risks.append(f"Affects {len(dependents)} dependent beliefs")
        
        return {
            'has_cascade': len(risks) > 0,
            'risks': risks,
            'risk_level': 'high' if 'adam' in text.lower() else 'medium' if 'bible' in text.lower() else 'low'
        }

# AUDIT INTERFACE (Your request)
class ThinkingAuditor:
    """
    Access the thinking process without verbose real-time output
    """
    
    def __init__(self, thinking_core):
        self.core = thinking_core
    
    def get_audit_trail(self, last_n=10):
        """See how the system has been thinking"""
        return self.core.thinking_log[-last_n:] if self.core.thinking_log else []
    
    def explain_decision(self, audit_id):
        """Reconstruct thinking for a specific decision"""
        if 0 <= audit_id < len(self.core.thinking_log):
            entry = self.core.thinking_log[audit_id]
            
            # Reconstruct thinking process
            reconstruction = {
                'input': entry['input'],
                'layer_assignment_reasoning': self._explain_layer(entry['layer'], entry['input']),
                'pattern_selection_logic': self._explain_pattern(entry['pattern'], entry['input']),
                'cascade_assessment': entry['cascade'],
                'semantic_excavations_applied': self._find_excavations(entry['input'])
            }
            
            return reconstruction
        
        return {'error': 'Audit ID not found'}
    
    def _explain_layer(self, layer, input_text):
        """Explain why input was assigned to this layer"""
        explanations = {
            'CORE': 'Input addressed foundational non-negotiable doctrine',
            'EVIDENCE': 'Input addressed supporting miraculous evidence',
            'DETAIL': 'Input addressed implementation details (often distractions)'
        }
        return explanations.get(layer, 'Unknown layer')

# LEAN OPERATION DEMO
def demo_lean_thinking():
    """Show the architecture thinking without verbose output"""
    
    print("🧠 LEAN THINKING ARCHITECTURE")
    print("Your patterns, minimal output")
    print("="*50)
    
    thinker = ThinkingCore()
    auditor = ThinkingAuditor(thinker)
    
    # Process some inputs quietly
    inputs = [
        "Was Adam a real historical person?",
        "How do you reconcile 24-hour creation days with science?",
        "The Bible's survival through persecution is miraculous"
    ]
    
    for i, input_text in enumerate(inputs):
        print(f"\n[{i+1}] Input: {input_text}")
        
        # Process (quietly - just returns state)
        result = thinker.process(input_text)
        
        # Show only essential output
        state = result['thinking_state']
        print(f"   State: Layer={state['active_layer']}, Pattern={state['applied_pattern']}")
        print(f"   Cascade risk: {state['cascade_risk']}")
        
        # Content is minimal
        if 'reorientation' in result['content']:
            print(f"   Reorientation: {result['content']['reorientation'][:40]}...")
    
    print("\n" + "="*50)
    print("AUDIT TRAIL (accessible on demand):")
    print("="*50)
    
    # Show audit trail
    audit = auditor.get_audit_trail(3)
    for entry in audit:
        print(f"ID {entry['id']}: {entry['input']} → {entry['layer']} ({entry['pattern']})")
    
    # Demonstrate audit reconstruction
    print("\n" + "="*50)
    print("THINKING RECONSTRUCTION (for any decision):")
    print("="*50)
    
    if audit:
        explanation = auditor.explain_decision(audit[0]['id'])
        print(f"For input: {explanation['input']}")
        print(f"Layer assignment: {explanation['layer_assignment_reasoning']}")
        print(f"Pattern selection: {explanation['pattern_selection_logic']}")

# OPEN-ENDED ARCHITECTURE VERSION
class OpenEndedThinker:
    """
    Even leaner: Just the thinking architecture, 
    outputs are whatever you want them to be
    """
    
    def __init__(self):
        # Your core thinking patterns as pure functions
        self.patterns = {
            'truth_hierarchy': self._apply_hierarchy,
            'lexical_archaeology': self._apply_archaeology,
            'cascade_check': self._check_cascade,
            'reorientation': self._reorient_question
        }
        
        # State only
        self.state = {
            'active_patterns': [],
            'recent_inputs': [],
            'cascade_warnings': []
        }
    
    def think_about(self, input_text):
        """Apply thinking patterns, return thinking state only"""
        
        # Apply all relevant patterns
        applied = []
        for pattern_name, pattern_func in self.patterns.items():
            if self._pattern_applies(pattern_name, input_text):
                result = pattern_func(input_text)
                applied.append((pattern_name, result))
        
        # Update state
        self.state['active_patterns'] = [p[0] for p in applied]
        self.state['recent_inputs'].append(input_text[:30])
        if len(self.state['recent_inputs']) > 5:
            self.state['recent_inputs'].pop(0)
        
        # Return minimal state
        return {
            'patterns_applied': [p[0] for p in applied],
            'pattern_results': {p[0]: p[1] for p in applied},
            'thinking_summary': self._generate_summary(applied)
        }
    
    def _apply_hierarchy(self, text):
        """Your Level 1>2>>>3 thinking"""
        if 'adam' in text.lower() and 'historical' in text.lower():
            return {'layer': 'CORE', 'priority': 100}
        elif 'bible' in text.lower() and ('survive' in text.lower() or 'miraculous' in text.lower()):
            return {'layer': 'EVIDENCE', 'priority': 80}
        else:
            return {'layer': 'DETAIL', 'priority': 10}
    
    def _apply_archaeology(self, text):
        """Your lexical archaeology"""
        excavations = []
        if 'day' in text.lower():
            excavations.append({'term': 'day', 'insight': 'semantic_range_includes_eras'})
        if 'flood' in text.lower():
            excavations.append({'term': 'flood', 'insight': 'theology_over_hydrology'})
        return {'excavations': excavations}
    
    def _reorient_question(self, text):
        """Your reorientation pattern"""
        if '24' in text and 'hour' in text:
            return {'from': 'literal_timing', 'to': 'divine_perspective_on_time'}
        return {'from': 'mechanism', 'to': 'meaning'}

# ULTIMATE MINIMAL VERSION
class ThinkingArchitecture:
    """
    50 lines - Just the architectural essence
    Your brain export at maximum compression
    """
    
    def __init__(self):
        # Your three core insights
        self.hierarchy = lambda t: 'CORE' if 'adam historical' in t else 'DETAIL'
        self.archaeology = lambda t: 'day→era' if 'day' in t else 'flood→judgment' if 'flood' in t else None
        self.cascade = lambda t: ['sin','ransom'] if 'adam' in t else []
        
        # Audit
        self.log = []
    
    def process(self, text):
        # Apply your thinking
        layer = self.hierarchy(text.lower())
        excavation = self.archaeology(text.lower())
        cascade = self.cascade(text.lower())
        
        # Log for audit
        self.log.append({
            't': text[:20], 'l': layer, 'e': excavation, 'c': len(cascade)
        })
        
        # Return only architecture state
        return {
            'layer': layer,
            'excavation': excavation,
            'cascade_effects': cascade,
            'thinking_style': 'reorientation' if layer == 'DETAIL' else 'affirmation'
        }
    
    def audit(self):
        return self.log[-10:] if self.log else []

# DEMONSTRATE MINIMAL ARCHITECTURE
print("\n" + "="*60)
print("MINIMAL THINKING ARCHITECTURE (50 lines)")
print("Your brain export, maximum compression")
print("="*60)

thinker = ThinkingArchitecture()

test_inputs = [
    "Adam was the first human created by God",
    "Creation days were 24 hours each", 
    "Noah's flood covered the whole earth"
]

for inp in test_inputs:
    result = thinker.process(inp)
    print(f"\n📥: {inp}")
    print(f"   Layer: {result['layer']}")
    print(f"   Excavation: {result['excavation']}")
    print(f"   Thinking: {result['thinking_style']}")

print("\n📊 Audit trail available:")
for entry in thinker.audit():
    print(f"  {entry['t']}... → {entry['l']} (cascade: {entry['c']})")