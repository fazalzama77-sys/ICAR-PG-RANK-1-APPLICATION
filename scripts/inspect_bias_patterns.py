import json
from collections import Counter

with open('scripts/clean_biased_questions.json', 'r', encoding='utf-8') as f:
    biased = json.load(f)

print(f"Total biased questions: {len(biased)}")
sub_counts = Counter(b['subjectId'] for b in biased)
print("By subject:", sub_counts)

# Check how many have parentheses in correct option
has_paren = [b for b in biased if '(' in b['c_opt'] and ')' in b['c_opt']]
print(f"Correct has parentheses: {len(has_paren)}")

# Sample questions
print("\n--- SAMPLE 1: Correct has parenthetical explanation ---")
for b in has_paren[:5]:
    print(f"[{b['id']}] Q: {b['qText'][:65]}")
    print(f"  C ({b['c_len']}): {b['c_opt']}")
    print(f"  D: {b['d_opts']}")

print("\n--- SAMPLE 2: Correct has NO parentheses but is long sentence ---")
no_paren = [b for b in biased if b not in has_paren]
print(f"Correct without parentheses: {len(no_paren)}")
for b in no_paren[:5]:
    print(f"[{b['id']}] Q: {b['qText'][:65]}")
    print(f"  C ({b['c_len']}): {b['c_opt']}")
    print(f"  D: {b['d_opts']}")
