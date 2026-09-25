import json, subprocess

# Get base from 9786b8f
proc = subprocess.run(['git', 'show', '9786b8f:src/data/questionPacks/high_yield_master_clean.json'], capture_output=True, text=True, encoding='utf-8')
data_1665 = json.loads(proc.stdout)

# Add vpa_60
with open('src/data/questionPacks/vpa_60_new.json', 'r', encoding='utf-8') as f:
    vpa_60 = json.load(f)

# Combine
all_1725 = {q['id']: q for q in data_1665}
for q in vpa_60:
    all_1725[q['id']] = q

# Only our own questions (exclude pyq_*)
our_questions = [q for q in all_1725.values() if not q['id'].startswith('pyq_')]

print(f"Total clean our own questions: {len(our_questions)}")

biased = []
for q in our_questions:
    opts = q['options']
    c_idx = q['correctOptionIndex']
    c_opt = opts[c_idx]
    d_opts = [opts[i] for i in range(len(opts)) if i != c_idx]
    c_len = len(c_opt)
    max_d = max(len(d) for d in d_opts)
    avg_d = sum(len(d) for d in d_opts) / len(d_opts)
    
    # Correct option is notably longer than distractors
    # Case 1: Difference > 20 characters
    # Case 2: Ratio > 1.6 and c_len > 25
    if (c_len - max_d > 20) or (c_len > 25 and c_len > 1.6 * max_d):
        biased.append((q['id'], q['subjectId'], c_len, max_d, c_opt, d_opts, q['questionText']))

print(f"Biased clean questions where correct is notably longer: {len(biased)}")

with open('scripts/clean_biased_questions.json', 'w', encoding='utf-8') as f:
    json.dump([{'id': b[0], 'subjectId': b[1], 'c_len': b[2], 'max_d': b[3], 'c_opt': b[4], 'd_opts': b[5], 'qText': b[6]} for b in biased], f, indent=2)

print("Saved to scripts/clean_biased_questions.json")
