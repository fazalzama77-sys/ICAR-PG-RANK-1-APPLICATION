# scripts/apply_equalization_to_all_packs.py
import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')
scripts_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(scripts_dir)

from equalize_engine import process_question

def main():
    packs_dir = os.path.join(scripts_dir, '..', 'src', 'data', 'questionPacks')
    pack_files = [
        'high_yield_clean_base.json',
        'pyqs_300.json',
        'vpp_300_new.json',
        'vmc_300_new.json',
        'van_150_new.json',
        'vpa_60_new.json'
    ]

    total_processed = 0
    for filename in pack_files:
        path = os.path.join(packs_dir, filename)
        if not os.path.exists(path):
            print(f"Skipping {filename} (not found)")
            continue

        with open(path, 'r', encoding='utf-8') as f:
            questions = json.load(f)

        updated_questions = []
        for q in questions:
            orig_c = q['options'][q['correctOptionIndex']]
            q_proc = process_question(q)
            new_c = q_proc['options'][q_proc['correctOptionIndex']]
            assert orig_c == new_c, f"Correct answer mismatch in {q['id']}!"
            updated_questions.append(q_proc)

        with open(path, 'w', encoding='utf-8') as f:
            json.dump(updated_questions, f, indent=2, ensure_ascii=False)

        total_processed += len(updated_questions)
        print(f"Equalized and updated {len(updated_questions)} questions in {filename}")

    print(f"\nTotal equalized questions across all 5 packs: {total_processed}")

    print("\nNow running apply_balanced_options.py to balance options across A, B, C, D and compile TS/JSON master...")
    from apply_balanced_options import apply_balance
    apply_balance()
    print("Compilation and balancing complete!")

if __name__ == '__main__':
    main()
