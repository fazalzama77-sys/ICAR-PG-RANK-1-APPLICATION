import json, re

with open('scripts/clean_biased_questions.json', 'r', encoding='utf-8') as f:
    biased = json.load(f)

# Let's inspect the types of terms in biased questions
print(f"Loaded {len(biased)} biased questions.")
