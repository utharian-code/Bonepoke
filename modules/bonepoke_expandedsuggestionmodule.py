class ExpandedSuggestionModule:
    def __init__(self, fragment):
        self.fragment = fragment
        self.suggestions = []

    def generate(self):
        self.suggestions = []

        if "water" in self.fragment:
            self.suggestions.append({
                "prompt": "Let the water remember you before you taste it.",
                "drift": "Curiosity ? Nostalgia",
                "anchor": "Memory",
                "rupture": "Experience-as-linear"
            })

        if "store" in self.fragment or "district" in self.fragment:
            self.suggestions.append({
                "prompt": "Let the store bloom from your forgotten moment.",
                "drift": "Silence ? Product",
                "anchor": "Surprise",
                "rupture": "Cause-before-effect"
            })

        if "hangover" in self.fragment:
            self.suggestions.append({
                "prompt": "Let the reverse hangover become a ritual of emotional sequencing.",
                "drift": "Pain ? Buzz",
                "anchor": "Resolution",
                "rupture": "Pleasure-as-goal"
            })

        if not self.suggestions:
            self.suggestions.append({
                "prompt": "Let the fragment compost into myth before it answers.",
                "drift": "Silence ? Shadow",
                "anchor": "Grief",
                "rupture": "Linear causality"
            })

        return self.suggestions

