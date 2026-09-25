import json

with open('src/data/questionPacks/high_yield_1080.json', 'r', encoding='utf-8') as f:
    base_json = json.load(f)

with open('src/data/questionPacks/pyqs_300.json', 'r', encoding='utf-8') as f:
    pyqs_json = json.load(f)

with open('src/data/questionPacks/vpp_300_new.json', 'r', encoding='utf-8') as f:
    vpp_exp_json = json.load(f)

with open('src/data/questionPacks/vmc_300_new.json', 'r', encoding='utf-8') as f:
    vmc_exp_json = json.load(f)

print(f"Base JSON: {len(base_json)} questions")
print(f"PYQs 300 JSON: {len(pyqs_json)} questions")
print(f"VPP Exp JSON: {len(vpp_exp_json)} questions")
print(f"VMC Exp JSON: {len(vmc_exp_json)} questions")
total = len(base_json) + len(pyqs_json) + len(vpp_exp_json) + len(vmc_exp_json)
print(f"Total across the 4 packs: {total}")

# Verify IDs across all 4 are unique
all_ids = [q['id'] for q in base_json + pyqs_json + vpp_exp_json + vmc_exp_json]
print(f"Total IDs: {len(all_ids)}, Unique IDs: {len(set(all_ids))}")
assert len(all_ids) == len(set(all_ids)), "Duplicate IDs found!"

from collections import Counter
pyq_subj_counts = Counter(q['subjectId'] for q in pyqs_json)
print("PYQs 300 by subject:", pyq_subj_counts)
base_subj_counts = Counter(q['subjectId'] for q in base_json)
print("Base by subject:", base_subj_counts)
vpp_exp_subj_counts = Counter(q['subjectId'] for q in vpp_exp_json)
print("VPP Exp by subject:", vpp_exp_subj_counts)
vmc_exp_subj_counts = Counter(q['subjectId'] for q in vmc_exp_json)
print("VMC Exp by subject:", vmc_exp_subj_counts)

all_combined = base_json + pyqs_json + vpp_exp_json + vmc_exp_json
import hashlib
import random

# Group questions by subject
subjects = sorted(list(set(q['subjectId'] for q in all_combined)))
shuffled_by_id = {}

for s in subjects:
    subj_qs = [q for q in all_combined if q['subjectId'] == s]
    # Sort deterministically by id
    subj_qs.sort(key=lambda x: x['id'])
    n = len(subj_qs)
    
    # Generate balanced target indices: repeat [0, 1, 2, 3]
    # To avoid repeating pattern [0,1,2,3], permute each block of 4 with a deterministic seed
    blocks = []
    rng_subj = random.Random(f"subject_balance_{s}")
    for i in range(0, n, 4):
        block = [0, 1, 2, 3]
        rng_subj.shuffle(block)
        blocks.extend(block)
    target_indices = blocks[:n]
    
    subj_counter = Counter(target_indices)
    print(f"Subject {s} ({n} Qs) target distribution: {dict(subj_counter)}")
    
    for q, target_idx in zip(subj_qs, target_indices):
        old_idx = q['correctOptionIndex']
        correct_text = q['options'][old_idx]
        distractors = [opt for i, opt in enumerate(q['options']) if i != old_idx]
        
        # Shuffle distractors with question-specific seed
        rng_q = random.Random(f"q_distractor_{q['id']}")
        rng_q.shuffle(distractors)
        
        new_opts = [None] * 4
        new_opts[target_idx] = correct_text
        d_idx = 0
        for i in range(4):
            if i != target_idx:
                new_opts[i] = distractors[d_idx]
                d_idx += 1
                
        # Verification check
        assert new_opts[target_idx] == correct_text
        assert sorted(new_opts) == sorted(q['options'])
        
        shuffled_by_id[q['id']] = {
            'options': new_opts,
            'correctOptionIndex': target_idx
        }

total_counts = Counter(v['correctOptionIndex'] for v in shuffled_by_id.values())
print("\nOVERALL BALANCED DISTRIBUTION across all 1515 questions:")
print(dict(total_counts))
print("Percentages:", {k: f"{v / len(shuffled_by_id) * 100:.1f}%" for k, v in sorted(total_counts.items())})


