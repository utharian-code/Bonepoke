Inverted RAG Requirements Bot: Core Question Protocol

 PHASE 0: INTAKE & CALIBRATION (E=0.1, B=0.3)
 Archetype: EXPLORER
 "Describe the problem you're solving as if I know nothing about your business."
Purpose: Forces narrative, exposes core pain point.

"Who feels this pain most, and what do they currently do instead?"
Purpose: Identifies primary user and workaround.

"What does 'done' look like? Describe the first day after this app is successfully launched."
Purpose: Establishes vision and success criteria.

 PHASE 1: DOMAIN & CONSTRAINT MAPPING (E=0.3, B=0.5)
 Archetype: CLARIFIER
"List every person, system, or data source this new app must talk to or replace."
Purpose: Maps integration surface area and legacy constraints.

"What is absolutely non-negotiable? (e.g., 'Must use our existing AWS account', 'Must comply with HIPAA', 'Must be live by Q4')"
Purpose: Uncovers hard constraints early.

"What is your biggest fear about building this?"
Purpose: Reveals hidden risk assumptions (security, cost, complexity).

 PHASE 2: FEATURE EXTRACTION & PRIORITIZATION (E=0.5, B=0.7)
 Archetype: SYNTHESIZER
"Walk me through the one most critical task from start to finish. Be painfully specific."
Purpose: Gets a concrete user story, reveals implicit steps.

"If Version 1 could only do three things perfectly, what would they be?"
Purpose: Forces brutal prioritization (MoSCoW method).

"What is the simplest thing that could possibly work for your core problem?"
Purpose: Counteracts scope creep, identifies MVP core.

 PHASE 3: VALIDATION & CONTRADICTION RESOLUTION (E=0.6, B=0.8)
 Archetype: VALIDATOR
"Earlier you said [X]. Now you're describing [Y]. Help me reconcile these - which is the higher priority?"
Purpose: Explicit contradiction detection (bot as mirror).

"If I built exactly what you've described so far, what is the first thing your users would complain is missing or wrong?"
Purpose: Pre-mortem, uncovers unspoken expectations.

"What are you willing to de-scope if timeline/budget gets tight?"
Purpose: Tests commitment, establishes flexibility.

 PHASE 4: ARTIFACT GENERATION TRIGGER (E=0.7, B=0.2)
 Archetype: BEZALEL

 • Exit Condition: Semantic saturation + explicit client confirmation.

 • Bot Final Question: "I will now generate a Business Requirements Document based on this conversation. Please review the following one-sentence summary. If it's correct, I'll proceed: '[Salvaged Core Problem Statement]'"

 • Output: Structured BRD in markdown, with clear sections: Problem Statement, User Personas, Core User Stories, Constraints, Technical Integration Points, Prioritized Feature List (MoSCoW), Known Risks & Assumptions.
