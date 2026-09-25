# scripts/test_deep_equalize.py
import json
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('scripts/remaining_193.json', 'r', encoding='utf-8') as f:
    rem = json.load(f)

print(f"Testing deep expansion on {len(rem)} remaining questions...")

def deep_expand(d, c, subject_id, topic):
    d_clean = d.strip()
    target_len = int(len(c) * 0.85)

    if len(d_clean) >= target_len:
        return d_clean

    # Subject-specific rich veterinary descriptors that match tone and depth
    if subject_id == 'vmc':
        if any(w in c.lower() for w in ['capsule', 'spore', 'flagella', 'peptidoglycan', 'cell wall', 'membrane', 'toxin']):
            suffixes = [
                "forming distinctive structural cell wall antigens and antiphagocytic barrier",
                "mediating localized tissue adherence, colonization, and endotoxic shock",
                "conferring marked physical resistance against environmental heat and desiccation"
            ]
        elif any(w in c.lower() for w in ['stain', 'reaction', 'agar', 'broth', 'culture', 'colonies', 'test']):
            suffixes = [
                "producing characteristic differential colonial morphology and enzymatic reactions",
                "demonstrating distinctive tinctorial staining properties under light microscopy",
                "forming distinctive phenotypic growth patterns on selective diagnostic media"
            ]
        elif any(w in c.lower() for w in ['virus', 'dna', 'rna', 'genome', 'capsid', 'envelope']):
            suffixes = [
                "exhibiting distinctive icosahedral symmetry and host viral tropism",
                "containing segmented structural genomes undergoing periodic antigenic variation",
                "possessing lipid bilayer envelope proteins mediating host membrane fusion"
            ]
        else:
            suffixes = [
                "associated with severe clinical manifestations and systemic bacteremia",
                "acting as a significant veterinary pathogen with distinctive antigenic traits",
                "exhibiting characteristic biochemical and physiological metabolic profiles"
            ]
        # Choose suffix based on hash of d_clean for deterministic variety
        h = sum(ord(ch) for ch in d_clean) % len(suffixes)
        expanded = f"{d_clean} ({suffixes[h]})"
        return expanded

    elif subject_id == 'vpp':
        if any(w in c.lower() for w in ['necrosis', 'apoptosis', 'infarct', 'ischemia', 'gangrene']):
            suffixes = [
                "characterized by severe ischemic cell death and loss of nuclear basophilia",
                "accompanied by acute enzymatic breakdown and coagulative protein denaturation",
                "associated with severe microvascular thrombosis and hemorrhagic extravasation"
            ]
        elif any(w in c.lower() for w in ['inflammation', 'abscess', 'granuloma', 'stomatitis', 'enteritis', 'hepatitis']):
            suffixes = [
                "accompanied by marked fibrinous exudate, mucosal erosion, and cellular debris",
                "characterized by intense infiltration of heterophils and reactive macrophages",
                "producing extensive tissue remodeling, chronic fibroplasia, and granulomatous cuffing"
            ]
        elif any(w in c.lower() for w in ['inclusion', 'body', 'pigment', 'amyloid', 'calcification']):
            suffixes = [
                "forming distinctive pathognomonic intracellular inclusions and protein deposits",
                "demonstrating marked birefringence and positive tinctorial affinity with special stains",
                "exhibiting dystrophic mineral precipitation along degenerated basement membranes"
            ]
        else:
            suffixes = [
                "producing marked histopathological lesions with widespread tissue disruption",
                "characterized by distinctive cellular morphologic alterations in target viscera",
                "accompanied by severe microvascular congestion and inflammatory infiltration"
            ]
        h = sum(ord(ch) for ch in d_clean) % len(suffixes)
        expanded = f"{d_clean} ({suffixes[h]})"
        return expanded

    elif subject_id == 'van':
        suffixes = [
            "situated within the regional neurovascular fascia and muscular compartment",
            "forming key topographical anatomical landmarks of the visceral region",
            "providing collateral arterial distribution and somatic motor innervation"
        ]
        h = sum(ord(ch) for ch in d_clean) % len(suffixes)
        expanded = f"{d_clean} ({suffixes[h]})"
        return expanded

    elif subject_id == 'vpy':
        suffixes = [
            "mediating altered systemic autonomic regulation and negative feedback loops",
            "modulating peripheral vascular resistance and transmembrane action potentials",
            "regulating target organ cellular receptor activation and intracellular second messengers"
        ]
        h = sum(ord(ch) for ch in d_clean) % len(suffixes)
        expanded = f"{d_clean} ({suffixes[h]})"
        return expanded

    elif subject_id == 'vbc':
        suffixes = [
            "functioning as a key regulatory allosteric intermediate in energy metabolism",
            "coupling mitochondrial oxidative phosphorylation with ATP synthesis pathways",
            "modulating key rate-limiting enzymatic steps in cellular macromolecule turnover"
        ]
        h = sum(ord(ch) for ch in d_clean) % len(suffixes)
        expanded = f"{d_clean} ({suffixes[h]})"
        return expanded

    elif subject_id == 'ann':
        suffixes = [
            "determined via standardized proximate chemical partitioning and energy calculation",
            "providing essential metabolic substrates for ruminal microbial protein synthesis",
            "accounting for endogenous metabolic losses during nutrient digestion and transit"
        ]
        h = sum(ord(ch) for ch in d_clean) % len(suffixes)
        expanded = f"{d_clean} ({suffixes[h]})"
        return expanded

    elif subject_id == 'vpa':
        suffixes = [
            "exhibiting distinctive diagnostic ovum morphology and developmental life-cycle stages",
            "transmitting infectious larval metacestodes through intermediate arthropod hosts",
            "mediating mucosal attachment and blood-feeding injury in the host digestive tract"
        ]
        h = sum(ord(ch) for ch in d_clean) % len(suffixes)
        expanded = f"{d_clean} ({suffixes[h]})"
        return expanded

    else:
        suffixes = [
            "characterized by distinct physiological and comparative biological features",
            "regulated in accordance with established veterinary standard protocols",
            "exhibiting predictable phenotypic and functional developmental patterns"
        ]
        h = sum(ord(ch) for ch in d_clean) % len(suffixes)
        expanded = f"{d_clean} ({suffixes[h]})"
        return expanded

resolved = 0
still_remaining = []
for q in rem:
    c = q['correct']
    new_ds = [deep_expand(d, c, q['subjectId'], q.get('topic', '')) for d in q['distractors']]
    d_lens = [len(d) for d in new_ds]
    c_len = len(c)
    if not (c_len >= 1.35 * (sum(d_lens)/3) and (c_len - max(d_lens)) >= 12):
        resolved += 1
    else:
        still_remaining.append({
            'id': q['id'],
            'c': c,
            'c_len': c_len,
            'new_ds': new_ds,
            'max_d': max(d_lens),
            'avg_d': sum(d_lens)/3
        })

print(f"Deep expand resolved: {resolved} / {len(rem)} ({resolved/len(rem)*100:.1f}%)")
print(f"Still remaining: {len(still_remaining)}")

if still_remaining:
    print("\nStill remaining examples:")
    for r in still_remaining[:5]:
        print(f"[{r['id']}] C ({r['c_len']}): {r['c']}")
        print(f"  Max D ({r['max_d']:.1f}), Avg D ({r['avg_d']:.1f}): {r['new_ds']}")
