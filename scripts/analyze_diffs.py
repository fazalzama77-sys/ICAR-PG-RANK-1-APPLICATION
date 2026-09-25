import json, re

with open('scripts/clean_biased_questions.json', 'r', encoding='utf-8') as f:
    biased = json.load(f)

print(f"Total: {len(biased)}")

# Let's inspect the distribution of length differences
diffs = [b['c_len'] - b['max_d'] for b in biased]
print(f"Min diff: {min(diffs)}, Max diff: {max(diffs)}, Avg diff: {sum(diffs)/len(diffs):.1f}")

# Check questions where c_len - max_d > 40
very_biased = [b for b in biased if b['c_len'] - b['max_d'] > 40]
print(f"Very biased (diff > 40): {len(very_biased)}")
