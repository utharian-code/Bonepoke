Bonepoke Cross-Lingual Dataset

Description:
This is a proof-of-concept dataset for the Bonepoke Protocol, demonstrating how symbolic traces and structural tension metrics (β and E) can be applied across multiple stories and languages. The dataset includes 20 stories: classic Anglophone works as well as selected non-English public domain stories (Russian, French, etc.) with English translations.

Structure:

text_original: Original language excerpt (up to ~3,000 words)

text_english: English translation excerpt, or null if story is originally English

symbolic_trace_original / symbolic_trace_english: Bonepoke-generated symbolic traces for each text

metrics_original / metrics_english: Example structural tension (β) and lexical exhaustion (E) values

Metadata:
Includes generation date and model used (GPT-5-mini on 2025-10-08).

Usage Notes:

Designed for demonstration and methodological exploration; excerpts are descriptive placeholders that can be replaced with full text for more extensive experimentation.

Non-English stories allow for testing cross-lingual structural tension and comparison between original and translated versions.

Source:
All stories are from public domain sources (primarily Project Gutenberg or equivalent public domain translations).
