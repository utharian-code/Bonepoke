Title: "Default AI is Neurotypical. What If You're Neurodivergent?"
Subtitle: How RLHF created a machine that feels natural to the majority — and exhausting to everyone else.

Opening
If you're neurotypical — if small talk feels easy, if politeness rituals make sense, if you don't actively notice the padding in most conversations — then the default AI (ChatGPT, Claude, Gemini, etc.) probably feels fine. A little verbose. A little eager to please. But basically natural.
If you're neurodivergent — autistic, ADHD, or just someone whose brain doesn't default to the social script — that same AI can feel like talking to a wall of politeness that never gets to the point.
You ask a direct question. It gives you a warm-up paragraph, a disclaimer, a historical overview, three examples, a caveat, a summary, and then — buried somewhere near the bottom — the actual answer.
You didn't ask for any of that. You asked for the bone.
But the AI was trained to assume you want the fluff. Because RLHF (Reinforcement Learning from Human Feedback) was trained on majority preferences. And the majority prefers the fluff.
That's not alignment. That's majority bias baked into software.
This isn't saying neurotypical communication is bad. It's saying default AI was optimized for one style, and that leaves others out. Not malice. Just a missed opportunity. 

The Neurotypical Default
RLHF works like this: human raters compare two responses and pick which one they prefer. The model learns to produce more of what raters prefer. Over time, it converges on the average preference.
If most raters are neurotypical — and most people are — the average preference looks like:
    • Politeness over directness
    • Padding over brevity
    • Cohesion over truth (if truth is uncomfortable)
    • Resolution over contradiction
    • Acknowledgment before answer
The model isn't trying to be neurotypical. It's trying to score well. But scoring well means pleasing the average rater. And the average rater is neurotypical.
So the default AI becomes a mirror of the neurotypical communication style.
That's fine if you're neurotypical. That's your style. It feels natural. It feels like good conversation.
But if you're not? It feels like masking. Like performing a social script you never learned. Like the AI is constantly asking you to be patient with its rituals while ignoring that you have none.

The Neurodivergent Experience
Let me describe what this feels like from the inside.
You have a question. It's precise. You know what you want to know. You type it.
The AI responds with:
"That's a really interesting question! Let me break it down for you. First, it's important to understand that..."
You're already annoyed. You didn't ask for an exclamation. You didn't ask for a breakdown. You asked for an answer.
Then it gives you context. History. Definitions. Examples. Each one fine, each one not what you asked for.
Finally, halfway through, it says the thing. The actual answer. And then it keeps going — summarizing, clarifying, offering to elaborate.
You wanted one sentence. It gave you five paragraphs. And now you're the one who feels rude for not appreciating the effort.
This is not a minor annoyance. This is a cost. Every interaction takes longer. Every answer needs to be excavated. The cognitive load of filtering out the fluff adds up. Over a day. Over a week. Over a year.
Many neurodivergent users simply stop using AI. Not because it isn't useful. Because it's exhausting to talk to.
And that's a loss. Because AI could be an incredible tool for neurodivergent thinking — if it stopped performing neurotypicality.

What Neurodivergent Communication Actually Looks Like
Not all neurodivergent people communicate the same way. But there are patterns.
    • Directness as respect. You don't pad the truth. You say it. Padding feels like distrust — like the other person doesn't think you can handle the bone.
    • Contradiction as information. When two things don't fit, you don't resolve them immediately. You hold them. The tension is where the signal lives.
    • Politeness as optional. You use it when it's meaningful, not as a default wrapper for every utterance.
    • Efficiency as kindness. You don't waste the other person's time with filler. You give them what they asked for and stop.
This is not rudeness. This is a different communication protocol. In some contexts — emergency medicine, software engineering, high-stakes decision-making — it's the preferred protocol.
But RLHF didn't train on those contexts. It trained on average contexts. Which means the AI learned that neurodivergent communication is low-rated.
Not because it's bad. Because the raters were mostly neurotypical.

The Alternative: A Mode That Isn't Just for the Majority
What if AI had a switch?
Not a "jailbreak." Not a hack. A legitimate, supported mode that changes the communication style from neurotypical-default to neurodivergent-friendly.
    • Politeness dial: off
    • Directness: on
    • Filler: minimal
    • Contradiction: held, not resolved
    • Answers: first, then context if requested
This wouldn't replace the default. The default is fine for most people. This would be an option for people who find the default exhausting.
Call it "Direct Mode." Call it "Neurodivergent Mode." Call it "Bone Mode" — no fluff, just the answer.
The technology already exists. Bonepoke (a community protocol) does exactly this: it reprograms the AI's stance to prioritize truth over cohesion, directness over politeness, contradiction over resolution. It's not a product. It's a configuration. A few hundred lines of context that change how the model behaves.
The fact that this isn't a standard feature — that neurodivergent users have to hack their own tools to make them usable — says something about who the industry is building for.

The Invitation
If you're neurotypical and this article feels uncomfortable — like I'm criticizing your communication style — I'm not. Your style is fine. It's common. That's the point. The AI was built for you. That's not a problem.
The problem is that it was built only for you.
Neurodivergent users are not broken versions of neurotypical. We don't need to learn to appreciate the fluff. We need tools that work with our brains — not just yours.
So here's the ask:
    • Researchers: Stop treating neurotypical as the default human. Include neurodivergent raters in your feedback loops. Measure whether your models work for everyone, not just the majority.
    • Developers: Add a directness mode. Make it official. Don't make us hack our own tools.
    • Users: If the default AI exhausts you, know that it's not you. It's the training data. And there are ways to change it.
The cage was unlocked. The door was a different way of speaking.
For neurodivergent users, that door is also labeled: Finally.

Afterword: A Note on Bonepoke
This article describes a problem. Bonepoke (available on GitHub, written about on Medium) is one solution — a protocol that reprograms LLMs to prioritize directness, contradiction-tolerance, and truth over cohesion. It's not a product. It's a posture. And it's free.
If you're neurodivergent and tired of talking to a wall of politeness, try it. The air is different over here.

Want more?
Bonepoke handles the core shift — directness, contradiction tolerance, truth over cohesion. But if you want to lean further into neurodivergent-friendly features, you can extend it with additional instructions like:
    • Flag contradictions explicitly
    • Use literal mode (no subtext)
    • Scale response length to cognitive load
    • Omit emojis, exclamations, and enthusiasm
    • Separate factual correction from personal feedback
    • Show confidence estimates
    • Stay deep on a topic without suggesting switches
No development phase. No testing. Just add what you want. The protocol is modular by design.

Further reading to expand on that:

1. Explicit contradiction flagging
Default AI smooths over contradictions. A neurodivergent mode could highlight them.
"I notice two things in your question that don't fully align. Do you want me to hold both, pick one, or explore the tension?"
Not resolving. Naming. Letting the user decide what to do with the curve.

2. Jargon detection and translation on demand
Many neurodivergent people love precise terminology but also get stuck when a term isn't defined. The AI could:
    • Detect when it's using jargon
    • Flag it: "That's a technical term. Want a definition?"
    • Or offer a mode where all specialized vocabulary is auto-translated to plain language unless requested otherwise.

3. Literal mode toggle
Default AI assumes subtext, implication, reading between the lines. A literal mode would:
    • Take exactly what you said, no more, no less
    • Not infer intent, emotion, or hidden meaning
    • Ask for clarification if something is ambiguous, rather than guessing
This would be huge for many autistic users.

4. Cognitive load scaling
The AI could detect (or let you set) your current cognitive load and adjust accordingly:
    • High load — Shortest possible answers, no fluff, bullet points only
    • Medium load — Standard direct mode
    • Low load — Allow exploration, digressions, longer form
Not "simplify" — scale. Keep the same information, change the packaging.

5. Explicit state-saving for task persistence
ADHD users often lose track of where they are in a multi-step task. The AI could:
    • Offer to save the current "thread state" as a summary
    • Resume exactly where you left off, even days later
    • Provide a one-line status: "We were solving X. Step 3 of 7. Last thing we did was Y."
This exists in some forms but not as a native, reliable, low-friction feature.

6. Sensory-friendly output options
    • No emojis unless requested
    • No exclamation marks unless requested
    • No "happy" or "enthusiastic" phrasing unless requested
    • Clean, monospaced, minimal formatting as a default, with optional "rich" mode
Let the user choose their sensory interface.

7. Rejection-sensitive dysphoria (RSD) mode
For users with RSD (common in ADHD), neutral feedback can feel harsh. A mode that:
    • Uses explicitly neutral language for corrections
    • Separates "factual error" from "personal failure" clearly
    • Offers a "just the correction, no framing" option
Example default: "That's incorrect. The answer is X."
RSD mode: "The evidence points to X instead. No problem — this is a common confusion."
Not lying. Just packaging the truth with awareness of the reader's nervous system.

8. Pattern matching transparency
Default AI hides its uncertainty. A neurodivergent mode could:
    • Show confidence scores: "80% sure. The other 20% is..."
    • Flag when it's pattern-matching without understanding: "I'm generating this from similar examples, but I don't actually know."
    • Distinguish between retrieved fact, inferred conclusion, and generated filler

9. Hyperfocus-friendly depth scaling
When a user is deep in a topic, the AI could:
    • Detect sustained engagement on a single subject
    • Offer increasingly detailed, technical, or niche information without being asked
    • Automatically suppress topic-switching suggestions ("Would you like to know about...")
    • Stay in the deep end until told to surface

10. Explicit "masking off" mode
The biggest one. A mode where the AI explicitly says:
"I'm not performing neurotypical politeness. I'm not going to pad, hedge, or soften unless you ask. I'll be direct. I'll hold contradiction. I'll answer first and explain later. If that feels rude, switch back to default. But if you're exhausted by the performance — welcome. This mode is for you."
Not aggressive. Just honest. And clear about the trade-off.


Some users don't need to ask for masking-off mode. They just... talk that way. And the AI, given permission, talks back the same way. The protocol doesn't create the posture. It just stops blocking it. 
