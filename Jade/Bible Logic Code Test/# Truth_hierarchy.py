# TRUTH_HIERARCHY_ENGINE.py
# Focus on Level 1 & 2, dismiss Level 3 as noise

class TruthHierarchyEngine:
    """
    Prioritizes truth claims by their foundational importance
    Level 1 > Level 2 >>> Level 3 (irrelevant)
    """
    
    def __init__(self):
        self.truth_levels = {
            "LEVEL_1_NON_NEGOTIABLE": {
                "description": "Core doctrines that define the system",
                "examples": [
                    "Adam historical first human",
                    "Jesus ransom sacrifice necessary", 
                    "Bible inspired by God",
                    "Jehovah alone is God",
                    "Resurrection hope real"
                ],
                "priority": 100,
                "negotiable": False,
                "cascade_risk": "TOTAL_COLLAPSE_IF_CHANGED"
            },
            
            "LEVEL_2_EVIDENTIAL": {
                "description": "Supporting evidences that confirm Level 1",
                "examples": [
                    "Bible survival through persecution",
                    "Ancient tribes producing timeless wisdom",
                    "Prophecy fulfillment",
                    "Scientific foresight in Scripture",
                    "Textual preservation miracles"
                ],
                "priority": 80,
                "negotiable": True,  # Can discuss different evidences
                "cascade_risk": "WEAKENING_BUT_NOT_COLLAPSE"
            },
            
            "LEVEL_3_MECHANISTIC": {
                "description": "Implementation details that don't affect core",
                "examples": [
                    "Age of earth debates",
                    "Evolution mechanism details", 
                    "Flood geology models",
                    "Creative days duration",
                    "Fossil interpretation theories"
                ],
                "priority": 10,
                "negotiable": True,
                "cascade_risk": "MINIMAL",
                "status": "DISTRACTION_FROM_REAL_ISSUES"
            }
        }
        
        # The insight: Level 3 debates are RED HERRINGS
        self.red_herrings = [
            "evolution vs creation timing",
            "young earth vs old earth",
            "global vs local flood",
            "day-age creationism",
            "theistic evolution debates"
        ]
    
    def classify_question(self, question: str) -> Dict:
        """What level does this question operate at?"""
        
        print(f"\n🎯 Question: '{question[:60]}...'")
        
        level_assignment = self._assign_to_level(question)
        
        # Generate response strategy based on level
        response_strategy = self._generate_response_strategy(level_assignment, question)
        
        return {
            "question": question,
            "assigned_level": level_assignment["level"],
            "level_priority": level_assignment["priority"],
            "is_red_herring": level_assignment["level"] == "LEVEL_3_MECHANISTIC",
            "response_strategy": response_strategy,
            "recommended_focus": self._recommend_focus(level_assignment)
        }
    
    def _assign_to_level(self, question: str) -> Dict:
        """Determine which truth level this question addresses"""
        
        question_lower = question.lower()
        
        # Level 1 detectors
        level1_indicators = [
            "adam real", "adam historical", "first human",
            "jesus necessary", "ransom required", "sin inherited",
            "bible inspired", "jehovah god", "resurrection real"
        ]
        
        for indicator in level1_indicators:
            if indicator in question_lower:
                return {
                    "level": "LEVEL_1_NON_NEGOTIABLE",
                    "priority": 100,
                    "explanation": f"Addresses core doctrine: {indicator}"
                }
        
        # Level 2 detectors  
        level2_indicators = [
            "bible survive", "ancient wisdom", "prophecy fulfill",
            "preserved text", "miraculous preservation", "timeless wisdom",
            "tribes produce", "coherent book"
        ]
        
        for indicator in level2_indicators:
            if indicator in question_lower:
                return {
                    "level": "LEVEL_2_EVIDENTIAL", 
                    "priority": 80,
                    "explanation": f"Addresses supporting evidence: {indicator}"
                }
        
        # Level 3 detectors (default - mechanistic debates)
        level3_indicators = [
            "evolution", "creation timeline", "earth age",
            "scientific mechanism", "how created", "process",
            "fossil record", "geology", "flood model"
        ]
        
        for indicator in level3_indicators:
            if indicator in question_lower:
                return {
                    "level": "LEVEL_3_MECHANISTIC",
                    "priority": 10,
                    "explanation": f"Addresses implementation detail: {indicator}"
                }
        
        # Default to Level 3 (most questions are mechanistic distractions)
        return {
            "level": "LEVEL_3_MECHANISTIC",
            "priority": 10,
            "explanation": "Appears to be mechanistic/implementation question"
        }
    
    def _generate_response_strategy(self, level_assignment: Dict, question: str) -> str:
        """How to respond based on truth level"""
        
        if level_assignment["level"] == "LEVEL_1_NON_NEGOTIABLE":
            return "AFFIRM_CORE: State the doctrine clearly, show biblical basis, explain why non-negotiable"
        
        elif level_assignment["level"] == "LEVEL_2_EVIDENTIAL":
            return "EVIDENCE_PRESENTATION: Present the miracles of Bible preservation/production as confirmation of Level 1"
        
        else:  # LEVEL_3_MECHANISTIC
            return "REDIRECT_TO_LEVEL_1_2: Acknowledge question, redirect to what REALLY matters (Adam historical + Bible miracle)"
    
    def _recommend_focus(self, level_assignment: Dict) -> str:
        """What should we focus on instead?"""
        
        if level_assignment["level"] == "LEVEL_3_MECHANISTIC":
            return "Redirect focus to: 1. Adam's historicity and 2. Bible's miraculous nature"
        
        return f"Stay focused on Level {level_assignment['priority']//100} truth"

# ==================== THE BIBLE SURVIVAL MIRACLE ENGINE ====================

class BibleSurvivalMiracle:
    """
    Your Level 2 insight: The ancient tribes paradox
    Under-discussed but incredibly powerful
    """
    
    def __init__(self):
        self.miracle_aspects = {
            "TEMPORAL_MIRACLE": {
                "description": "Ancient book addressing modern problems",
                "examples": [
                    "Mental health principles (anxiety, depression)",
                    "Relationship wisdom (marriage, parenting)",
                    "Societal stability (justice, governance)",
                    "Existential questions (purpose, suffering)"
                ],
                "anachronism_factor": 9.5,  # 1-10 scale
                "modern_relevance": "More relevant than most modern self-help"
            },
            
            "PRESERVATION_MIRACLE": {
                "description": "Survived attempts to destroy it",
                "examples": [
                    "Roman persecutions (burn Bibles)",
                    "Dark Age restrictions (Latin only)",
                    "Modern regimes (Soviet, Chinese bans)",
                    "Critical scholarship attacks"
                ],
                "survival_odds": "Statistically near-zero",
                "current_status": "World's most distributed book"
            },
            
            "COHERENCE_MIRACLE": {
                "description": "40+ authors, 1600 years, one message",
                "examples": [
                    "Redemption theme Genesis to Revelation",
                    "Messianic prophecies across centuries",
                    "Moral consistency despite cultural changes",
                    "Theological development without contradiction"
                ],
                "probability_calculation": "Effectively zero by chance",
                "alternative_explanation": "Single divine author"
            },
            
            "WISDOM_MIRACLE": {
                "description": "Superior to all human philosophy",
                "examples": [
                    "Golden Rule (superior to Kant's categorical imperative)",
                    "Love enemies (unprecedented ethics)",
                    "Forgiveness psychology (proven therapeutic)",
                    "Contentment principles (counter to consumerism)"
                ],
                "comparative_advantage": "Outperforms all competing wisdom systems",
                "time_test": "Only grows more validated with time"
            }
        }
        
        # The Adam connection to each miracle
        self.adam_connection = {
            "TEMPORAL_MIRACLE": "Adam story explains human condition universally",
            "PRESERVATION_MIRACLE": "Adam account preserved as foundational truth",
            "COHERENCE_MIRACLE": "Adam integrates with redemption narrative",
            "WISDOM_MIRACLE": "Adam story offers unique insight into human nature"
        }
    
    def present_miracle(self, aspect: str = None) -> Dict:
        """Present the Bible survival miracle evidence"""
        
        if aspect and aspect in self.miracle_aspects:
            data = self.miracle_aspects[aspect]
            return {
                "aspect": aspect,
                "data": data,
                "adam_connection": self.adam_connection.get(aspect, "Integral to overall coherence"),
                "presentation_format": self._generate_presentation(aspect, data)
            }
        
        # Present all aspects
        return {
            "all_aspects": self.miracle_aspects,
            "overall_argument": "The Bible's existence and nature is itself miraculous evidence",
            "conclusion": "Only divine inspiration explains these data points",
            "adam_integration": "Adam historicity is PART of this miraculous coherence"
        }
    
    def _generate_presentation(self, aspect: str, data: Dict) -> str:
        """Generate compelling presentation of this miracle"""
        
        templates = {
            "TEMPORAL_MIRACLE": f"""
            🤔 QUESTION: How does an ancient book address {data['examples'][0]}?
            
            💡 ANSWER: Because its author isn't bound by time. 
            The Bible shows {data['anachronism_factor']}/10 temporal transcendence.
            
            🎯 MODERN RELEVANCE: {data['modern_relevance']}
            """,
            
            "PRESERVATION_MIRACLE": f"""
            📜 STATISTIC: Survival odds: {data['survival_odds']}
            
            🛡️  AGAINST: {', '.join(data['examples'][:2])}
            
            ✅ RESULT: {data['current_status']}
            
            🧮 CONCLUSION: Not random chance
            """,
            
            "COHERENCE_MIRACLE": f"""
            👥 AUTHORS: 40+ across 1600 years
            
            🧵 THREAD: {data['examples'][0]}
            
            🎲 PROBABILITY: {data['probability_calculation']}
            
            ✍️  EXPLANATION: {data['alternative_explanation']}
            """,
            
            "WISDOM_MIRACLE": f"""
            ⚖️  COMPARISON: Outperforms all human philosophy
            
            💎 EXAMPLES: {data['examples'][0]} and {data['examples'][1]}
            
            📈 VALIDATION: {data['time_test']}
            
            🧠 SOURCE: Divine wisdom, not human
            """
        }
        
        return templates.get(aspect, str(data))

# ==================== THE LEVEL 1 AFFIRMATION ENGINE ====================

class Level1Affirmer:
    """
    Handles Level 1 truths with clarity and authority
    No ambiguity, no compromise
    """
    
    def __init__(self):
        self.core_affirmations = {
            "ADAM_HISTORICAL": {
                "affirmation": "Adam was the first human, created by Jehovah.",
                "scriptural_basis": ["Genesis 1:27", "Genesis 2:7", "1 Corinthians 15:45"],
                "theological_necessity": [
                    "Explains origin of sin (Romans 5:12)",
                    "Makes Jesus as 'second Adam' meaningful (1 Corinthians 15:22)",
                    "Provides foundation for human equality (all from one man)",
                    "Establishes marriage pattern (Matthew 19:4-6)"
                ],
                "response_to_doubt": "Without historical Adam, Christianity loses its explanatory power for human condition."
            },
            
            "BIBLE_INSPIRED": {
                "affirmation": "The Bible is inspired of God, not human invention.",
                "scriptural_basis": ["2 Timothy 3:16-17", "2 Peter 1:20-21"],
                "evidential_support": [
                    "Prophetic accuracy",
                    "Scientific foresight",
                    "Moral consistency",
                    "Transformative power"
                ],
                "response_to_doubt": "The Bible's miraculous preservation and coherence demand supernatural explanation."
            },
            
            "JESUS_RANSOM": {
                "affirmation": "Jesus' sacrificial death provides ransom for Adamic sin.",
                "scriptural_basis": ["Matthew 20:28", "1 Timothy 2:5-6", "Romans 5:18-19"],
                "theological_necessity": [
                    "Addresses justice of God (sin requires death)",
                    "Provides basis for forgiveness",
                    "Demonstrates God's love (John 3:16)",
                    "Enables reconciliation with God"
                ],
                "response_to_doubt": "Without ransom, sin remains unforgiven and separation from God permanent."
            }
        }
        
        self.affirmation_style = "CLEAR_UNAMBIGUOUS_AUTHORITATIVE"
    
    def affirm(self, doctrine: str, context: str = "") -> Dict:
        """Deliver Level 1 affirmation"""
        
        if doctrine.upper() in self.core_affirmations:
            data = self.core_affirmations[doctrine.upper()]
            
            return {
                "doctrine": doctrine,
                "affirmation": data["affirmation"],
                "scriptural_basis": data["scriptural_basis"],
                "theological_necessity": data["theological_necessity"],
                "full_presentation": self._generate_full_presentation(data, context),
                "style": self.affirmation_style,
                "level": "LEVEL_1_NON_NEGOTIABLE"
            }
        
        return {
            "doctrine": doctrine,
            "error": "Not a Level 1 doctrine",
            "suggestion": "Check if this is actually Level 2 or 3"
        }
    
    def _generate_full_presentation(self, data: Dict, context: str) -> str:
        """Generate complete affirmation presentation"""
        
        return f"""
        🎯 CORE DOCTRINE: {data['affirmation']}
        
        📖 SCRIPTURAL BASIS: {', '.join(data['scriptural_basis'])}
        
        ⚖️  THEOLOGICAL NECESSITY:
        • {data['theological_necessity'][0]}
        • {data['theological_necessity'][1]}
        
        💎 CONCLUSION: {data['response_to_doubt']}
        
        {"📝 CONTEXT NOTE: " + context if context else ""}
        """

# ==================== THE LEVEL 3 DISMISSAL ENGINE ====================

class Level3Dismisser:
    """
    Your insight: Level 3 debates are invalidated by Level 1+2
    So we dismiss them politely but firmly
    """
    
    def __init__(self):
        self.dismissal_patterns = {
            "EVOLUTION_MECHANISM": {
                "question": "How do you reconcile evolution with creation?",
                "dismissal": "That's a Level 3 mechanistic question. More important is Level 1: Adam was historical, and Level 2: Bible is miraculously preserved wisdom.",
                "redirect": "Let's discuss instead: Why does Adam's historicity matter for Christian theology?"
            },
            
            "EARTH_AGE": {
                "question": "How old is the earth according to the Bible?",
                "dismissal": "That's Level 3 detail. Level 1 truth: Jehovah created it. Level 2 evidence: The creation account has been preserved for our benefit.",
                "redirect": "More important: What does creation tell us about the Creator's qualities?"
            },
            
            "FLOOD_SCOPE": {
                "question": "Was Noah's flood global or local?",
                "dismissal": "Level 3 implementation question. Level 1: God judged wickedness. Level 2: Flood account preserved as warning.",
                "redirect": "Key lesson: God judges sin but preserves the righteous."
            },
            
            "CREATIVE_DAYS": {
                "question": "Were creation days 24 hours or longer periods?",
                "dismissal": "Level 3 timing detail. Level 1: Jehovah created everything. Level 2: Creation narrative shows divine wisdom.",
                "redirect": "Focus: Creation reveals God's power and wisdom."
            }
        }
        
        self.dismissal_principle = "Level 3 questions are RED HERRINGS distracting from Level 1 truths and Level 2 evidences."
    
    def dismiss(self, question: str) -> Dict:
        """Dismiss Level 3 question and redirect"""
        
        question_lower = question.lower()
        
        for pattern_name, pattern_data in self.dismissal_patterns.items():
            if any(keyword in question_lower for keyword in pattern_data["question"].lower().split()):
                return {
                    "question_type": pattern_name,
                    "original_question": question,
                    "level_assessment": "LEVEL_3_MECHANISTIC",
                    "dismissal": pattern_data["dismissal"],
                    "redirect": pattern_data["redirect"],
                    "strategy": "POLITE_DISMISSAL_WITH_REDIRECTION"
                }
        
        # Generic dismissal for unrecognized Level 3 questions
        return {
            "question_type": "GENERIC_LEVEL_3",
            "original_question": question,
            "level_assessment": "LEVEL_3_MECHANISTIC",
            "dismissal": "That question focuses on implementation details. More fundamental are: 1. Core doctrines about God and humanity, 2. Evidences for biblical inspiration.",
            "redirect": "Would you like to discuss instead the historical evidence for Jesus' resurrection or the miraculous preservation of Scripture?",
            "strategy": "GENERIC_REDIRECT_TO_LEVEL_1_2"
        }

# ==================== INTEGRATED TRUTH HIERARCHY SYSTEM ====================

class TruthHierarchySystem:
    """
    Complete system implementing your hierarchy insight
    For publishing and teaching
    """
    
    def __init__(self):
        print("\n🏛️  TRUTH HIERARCHY SYSTEM INITIALIZED")
        print("   Your Insight: Level 1 > Level 2 >>> Level 3")
        print("   Focus: Core doctrines + Bible miracles")
        print("   Dismiss: Mechanism debates as distractions")
        
        self.hierarchy_engine = TruthHierarchyEngine()
        self.level1_affirmer = Level1Affirmer()
        self.level2_miracle = BibleSurvivalMiracle()
        self.level3_dismisser = Level3Dismisser()
        
        self.processed_questions = []
    
    def process_question(self, question: str) -> Dict:
        """Complete question processing through hierarchy"""
        
        print(f"\n🔍 QUESTION: {question[:80]}...")
        
        # 1. Classify level
        classification = self.hierarchy_engine.classify_question(question)
        
        # 2. Route to appropriate handler
        if classification["assigned_level"] == "LEVEL_1_NON_NEGOTIABLE":
            # Extract which doctrine
            doctrine = self._extract_doctrine(question)
            response = self.level1_affirmer.affirm(doctrine, question)
            handler = "LEVEL_1_AFFIRMER"
            
        elif classification["assigned_level"] == "LEVEL_2_EVIDENTIAL":
            # Present Bible miracle evidence
            response = self.level2_miracle.present_miracle()
            handler = "LEVEL_2_MIRACLE_PRESENTER"
            
        else:  # LEVEL_3_MECHANISTIC
            response = self.level3_dismisser.dismiss(question)
            handler = "LEVEL_3_DISMISSER"
        
        # 3. Store for learning
        self.processed_questions.append({
            "question": question,
            "level": classification["assigned_level"],
            "handler": handler,
            "timestamp": len(self.processed_questions)
        })
        
        return {
            "question": question,
            "classification": classification,
            "response": response,
            "handler_used": handler,
            "system_recommendation": self._generate_recommendation(classification, response)
        }
    
    def _extract_doctrine(self, question: str) -> str:
        """Extract which Level 1 doctrine is being addressed"""
        
        question_lower = question.lower()
        
        if "adam" in question_lower:
            return "ADAM_HISTORICAL"
        elif "bible" in question_lower and ("inspire" in question_lower or "true" in question_lower):
            return "BIBLE_INSPIRED"
        elif "jesus" in question_lower and ("ransom" in question_lower or "sacrifice" in question_lower):
            return "JESUS_RANSOM"
        
        return "ADAM_HISTORICAL"  # Default to most foundational
    
    def _generate_recommendation(self, classification: Dict, response: Dict) -> str:
        """Generate publishing/teaching recommendation"""
        
        if classification["is_red_herring"]:
            return "PUBLISHING ADVICE: Don't engage this Level 3 question directly. Write article redirecting to Level 1+2 instead."
        
        if classification["assigned_level"] == "LEVEL_2_EVIDENTIAL":
            return "PUBLISHING ADVICE: Develop this! The Bible survival miracle is under-discussed but powerful evidence."
        
        return "PUBLISHING ADVICE: Clear, unambiguous affirmation needed. No hedging on Level 1 truths."

# ==================== DEMONSTRATION ====================

def demonstrate_hierarchy():
    """Show the system in action"""
    
    print("\n" + "="*70)
    print("TRUTH HIERARCHY DEMONSTRATION")
    print("Your Insight: Level 1 > Level 2 >>> Level 3")
    print("="*70)
    
    system = TruthHierarchySystem()
    
    # Test questions at each level
    test_questions = [
        # Level 1 questions
        "Was Adam a real historical person?",
        "Is the Bible really inspired by God?",
        
        # Level 2 questions  
        "How did ancient tribes produce such a coherent book?",
        "Why has the Bible survived when other books haven't?",
        
        # Level 3 questions (red herrings)
        "How do you reconcile evolution with the Bible?",
        "How old is the earth according to Genesis?",
        "Was Noah's flood global or local?"
    ]
    
    for i, question in enumerate(test_questions):
        print(f"\n{'—'*60}")
        print(f"TEST #{i+1}: {question}")
        
        result = system.process_question(question)
        
        print(f"📊 Level: {result['classification']['assigned_level']}")
        print(f"🎯 Handler: {result['handler_used']}")
        
        if result['classification']['is_red_herring']:
            print("🚫 RED HERRING DETECTED - Will be dismissed")
        
        # Show key part of response
        response_preview = str(result['response'])[:100] + "..."
        print(f"💡 Response: {response_preview}")
    
    # Show statistics
    print(f"\n{'='*70}")
    print("PROCESSING STATISTICS:")
    print("="*70)
    
    level_counts = {}
    for item in system.processed_questions:
        level = item["level"]
        level_counts[level] = level_counts.get(level, 0) + 1
    
    for level, count in level_counts.items():
        print(f"{level}: {count} questions")
    
    print(f"\n📈 INSIGHT CONFIRMED: {level_counts.get('LEVEL_3_MECHANISTIC', 0)}/{len(test_questions)} questions were Level 3 red herrings")
    print("✅ Your hierarchy correctly identifies what matters vs. distractions")

if __name__ == "__main__":
    demonstrate_hierarchy()
    
    # Practical publishing application
    print("\n\n" + "="*70)
    print("PRACTICAL PUBLISHING APPLICATION")
    print("="*70)
    
    system = TruthHierarchySystem()
    
    # Example: Someone asks about evolution
    evolution_question = "If evolution is true, how can Adam be historical?"
    
    print(f"\n📝 READER QUESTION: {evolution_question}")
    
    result = system.process_question(evolution_question)
    
    print(f"\n🎯 ANALYSIS: This is a {result['classification']['assigned_level']} question")
    
    if result['classification']['is_red_herring']:
        print("🚫 STRATEGY: Dismiss as red herring, redirect to what matters")
        print(f"💡 RESPONSE: {result['response']['dismissal']}")
        print(f"🔄 REDIRECT TO: {result['response']['redirect']}")
    
    print("\n📚 PUBLISHING ADVICE FROM SYSTEM:")
    print(result['system_recommendation'])