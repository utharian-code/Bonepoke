# LEXICAL_ARCHAEOLOGY_TEMPLATE.py
# The pattern, not the specific implementations

class LexicalArchaeologyTemplate:
    """
    Your method generalized
    """
    
    def __init__(self):
        # THE TEMPLATE STRUCTURE:
        self.template = {
            'STEP_1': 'IDENTIFY_MODERN_QUESTION',
            'STEP_2': 'LOCATE_KEY_TERMS',
            'STEP_3': 'EXCAVATE_SEMANTIC_STRATA',
            'STEP_4': 'IDENTIFY_ANACHRONISM',
            'STEP_5': 'REORIENT_TO_ANCIENT_CONCERNS',
            'STEP_6': 'EXTRACT_THEOLOGICAL_CORE'
        }
        
        # The reusable patterns
        self.patterns = {
            'SEMANTIC_STRATA_EXCAVATION': {
                'inputs': ['term', 'context', 'time_periods'],
                'process': 'Map how meaning changed across cultural/linguistic layers',
                'output': 'Semantic range understanding'
            },
            
            'ANACHRONISM_DETECTION': {
                'inputs': ['modern_question', 'ancient_context'],
                'process': 'Identify where modern concerns misalign with ancient ones',
                'output': 'Category error identification'
            },
            
            'THEOLOGICAL_REORIENTATION': {
                'inputs': ['misguided_debate', 'semantic_excavation'],
                'process': 'Redirect from modern categories to ancient purposes',
                'output': 'Reframed understanding'
            }
        }
    
    def apply_to_new_topic(self, topic_data):
        """Generalized application"""
        return {
            'modern_question': topic_data.get('modern_debate'),
            'key_terms': self._extract_terms(topic_data),
            'semantic_strata': self._excavate_strata(topic_data),
            'anachronisms': self._detect_anachronisms(topic_data),
            'reoriented_understanding': self._reorient(topic_data),
            'theological_core': self._extract_core(topic_data)
        }

# FUTURE APPLICATIONS
potential_applications = [
    {
        'topic': 'HELL (SHEOL/GEHENNA/HADES)',
        'modern_question': 'Is hell eternal torment?',
        'key_terms': ['sheol', 'gehenna', 'hades', 'tartarus'],
        'semantic_strata': [
            'Hebrew "sheol" = grave, not torment',
            'Greek "hades" = equivalent to sheol', 
            'Gehenna = valley of Hinnom, symbolic of destruction',
            'Tartarus = prison for angels, not humans'
        ],
        'anachronism': 'Reading Dante/Medieval torment back into biblical terms',
        'reorientation': 'From "eternal torment" to "eternal destruction"',
        'theological_core': 'God judges sin with death, not eternal torture'
    },
    
    {
        'topic': 'SOUL (NEFESH/PSYCHE)',
        'modern_question': 'Is the soul immortal?',
        'key_terms': ['nephesh', 'psyche', 'pneuma', 'ruach'],
        'semantic_strata': [
            'Nephesh = living being, breath, life force',
            'Psyche = equivalent to nephesh',
            'Pneuma/Ruach = spirit, breath, wind (different from soul)',
            'Biblical view: Soul CAN die (Ezekiel 18:4)'
        ],
        'anachronism': 'Imposing Greek philosophy (Platonic immortality) onto Hebrew thought',
        'reorientation': 'From "immortal soul" to "mortal living being with hope of resurrection"',
        'theological_core': 'Eternal life is gift through Christ, not inherent property'
    },
    
    {
        'topic': 'CHURCH (EKKLESIA)',
        'modern_question': 'What is the true church?',
        'key_terms': ['ekklesia', 'qahal', 'assembly', 'congregation'],
        'semantic_strata': [
            'Ekklesia = called-out assembly (political term)',
            'Qahal = Hebrew equivalent, assembly of Israel',
            'New Testament: Local congregations, not universal institution',
            'No building/temple focus in early usage'
        ],
        'anachronism': 'Reading medieval cathedral/church structure back into ekklesia',
        'reorientation': 'From "institution with buildings/hierarchy" to "people called out"',
        'theological_core': 'God gathers a people to himself, not builds institutions'
    },
    
    {
        'topic': 'FAITH (PISTIS/EMUNAH)',
        'modern_question': 'Is faith blind belief?',
        'key_terms': ['pistis', 'emunah', 'belief', 'trust'],
        'semantic_strata': [
            'Pistis = faithfulness, trustworthiness, reliability',
            'Emunah = firmness, steadfastness, fidelity',
            'Hebrews 11:1 - "faith is substantiation..." (not blind)',
            'Biblical faith based on evidence, relationship'
        ],
        'anachronism': 'Modern "leap of faith" vs. ancient "trust based on character"',
        'reorientation': 'From "believing without evidence" to "trusting based on evidence"',
        'theological_core': 'Faith responds to God\'s faithfulness with trust'
    }
]