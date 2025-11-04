# SCRIPTURE_NAVIGATOR_LITE.py
# Just the essentials - biblical wisdom for exponential problems

class ScriptureNavigator:
    """Lightweight scripture-based problem solving"""
    
    def __init__(self):
        self.core_principles = {
            "guidance": "Trust in Jehovah with all your heart...",
            "wisdom": "The wisdom from above is first of all pure...", 
            "peace": "Do not be anxious over anything...",
            "strength": "I can do all things through Christ..."
        }
        
    def handle_exponential_problem(self, problem_type: str, context: str = "") -> str:
        """Use scripture as signposts for overwhelming situations"""
        
        problem_map = {
            "overwhelm": {
                "scripture": "Philippians 4:6,7",
                "principle": "Prayer and peace guard your heart",
                "action": "Specific thanksgiving amid the chaos"
            },
            "decision_fatigue": {
                "scripture": "James 1:5", 
                "principle": "Ask for wisdom generously given",
                "action": "Make one small next-right-thing choice"
            },
            "identity_confusion": {
                "scripture": "Psalm 139:14",
                "principle": "Wonderfully made by Jehovah",
                "action": "Anchor in creation truth, not performance"
            },
            "future_anxiety": {
                "scripture": "Matthew 6:34",
                "principle": "Today's trouble is enough for today",
                "action": "Identify just today's necessary work"
            }
        }
        
        if problem_type in problem_map:
            guidance = problem_map[problem_type]
            return f"""
🎯 {problem_type.replace('_', ' ').title()}
📖 {guidance['scripture']} - {guidance['principle']}
✨ Action: {guidance['action']}
💡 Context: {context}
"""
        else:
            return "Take a breath. Read Psalm 23. Remember you're the sheep, He's the shepherd."

# Just you and me version
def simple_scripture_anchor(emotion_state: str) -> str:
    """Ultra-simple scripture anchoring"""
    
    anchor_points = {
        "anxious": "1 Peter 5:7 - Throw all your anxiety on him",
        "tired": "Matthew 11:28-30 - I will refresh you", 
        "confused": "Proverbs 3:5,6 - Trust, don't lean on your own understanding",
        "overwhelmed": "Psalm 46:10 - Be still, know that I am God",
        "uncertain": "Isaiah 30:21 - This is the way, walk in it"
    }
    
    return anchor_points.get(emotion_state.lower(), "Psalm 136:1 - Give thanks to Jehovah, for he is good")

# Usage - keeping it simple
if __name__ == "__main__":
    navigator = ScriptureNavigator()
    
    # When exponential problems hit
    print(navigator.handle_exponential_problem("overwhelm", "too many responsibilites to manage"))
    print(navigator.handle_exponential_problem("decision_fatigue", "which path to choose"))
    
    # Quick emotional first-aid

    print(f"\nQuick anchor: {simple_scripture_anchor('anxious')}")
