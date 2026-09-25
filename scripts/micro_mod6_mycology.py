# scripts/micro_mod6_mycology.py
# Module 6: Veterinary Mycology & Mycotoxicoses (15 Questions)
# Aligned with ICAR AIEEA (PG) M.V.Sc. Syllabus Code 13 Unit II

def get_module6_questions():
    qs = [
        # 1-15: Dermatophytes, systemic mycoses, mycotoxins
        ("Microsporum canis, the primary cause of ringworm (dermatophytosis) in dogs and cats, is identified on direct microscopic examination of hair plucks by producing:",
         ["Ectothrix arthrospores forming a dense mosaic sheath around the exterior of the hair shaft, and fluorescing bright apple-green under Wood's lamp (365 nm)", "Endothrix large spores packed solely inside the hair shaft", "Intracellular yeasts inside RBCs", "No fluorescence under any lamp"],
         0, "Microsporum canis produces ectothrix invasion where arthroconidia cluster on the exterior surface of the hair cuticle; pteridine metabolites produced by the fungus emit diagnostic bright apple-green fluorescence under Wood's ultraviolet light (365 nm).",
         True, "Veterinary Mycology (ICAR PG PYQ)"),

        ("Trichophyton verrucosum, the etiological agent of 'Cattle Ringworm' producing thick, hard, asbestos-like, grayish-white crusts around the eyes and neck, is culturally fastidious and strictly requires which two nutritional vitamins for in vitro growth?",
         ["Thiamine and Inositol", "Riboflavin and Niacin", "Ascorbic acid and Biotin", "Vitamin B12 and Folic acid"],
         0, "Unlike most dermatophytes that grow readily on plain Sabouraud dextrose agar, Trichophyton verrucosum requires enrichment with thiamine (and often inositol) and optimal incubation at 37°C for colonial development.",
         True, "Veterinary Mycology (ICAR PG PYQ)"),

        ("Microsporum canis is microscopically distinguished from Trichophyton species in culture by its characteristic macroconidia, which are:",
         ["Abundant, large, thick-walled, spindle-shaped (fusiform) with an asymmetrical curved terminal beak, containing 6 or more internal transverse septa", "Pencil-shaped, smooth, and thin-walled", "Spherical, single-celled chlamydospores", "Completely absent in culture"],
         0, "M. canis produces prominent, rough-walled, echinulate, spindle-shaped macroconidia with a hooked apex and >= 6 internal transverse cells, whereas Trichophyton produces rare, thin-walled, cigar-shaped/pencil-shaped macroconidia and abundant microconidia.",
         True, "Veterinary Mycology (ICAR PG PYQ)"),

        ("Aspergillus fumigatus, causing 'Brooder Pneumonia' in chicks and mycotic abortion in cattle, is identified microscopically in tissue sections by forming:",
         ["Uniform, septate hyphae (3 to 5 um wide) exhibiting characteristic progressive dichotomous branching at an acute 45-degree angle", "Broad, non-septate, ribbon-like hyphae branching at right angles (90 degrees)", "Budding yeast cells with broad bases", "Pseudohyphae with terminal chlamydospores"],
         0, "Aspergillus hyphae are uniformly narrow, regularly septate, and branch dichotomously (dividing into two equal branches) at an acute angle of approximately 45 degrees, which distinguishes them from Zygomycetes (Mucor/Rhizopus: non-septate, 90-degree branching).",
         True, "Veterinary Mycology (ICAR PG PYQ)"),

        ("Candida albicans is rapidly differentiated from all other non-albicans Candida species in the diagnostic mycology laboratory by the positive:",
         ["Germ Tube Test (formation of true germ tubes extending without constriction from yeast cells incubated in horse or fetal calf serum at 37°C within 2 to 3 hours)", "Urease test", "Catalase test", "Bile-esculin hydrolysis"],
         0, "When Candida albicans blastospores are incubated in mammalian serum at 37°C for 2-3 hours, >95% of cells form elongated, cylindrical parallel-walled filamentous outgrowths (germ tubes) with no constriction at their junction with the parent yeast.",
         True, "Veterinary Mycology (ICAR PG PYQ)"),

        ("Cryptococcus neoformans is an environmental encapsulated yeast associated with dried pigeon droppings, recognized under negative staining with India ink by its:",
         ["Massive, mucopolysaccharide (glucuronoxylomannan) capsule that repels colloidal carbon particles, appearing as a wide clear halo around the yeast cell", "Dense, non-encapsulated oval cells forming pseudohyphae", "Internal spore-bearing asci", "Acid-fast staining with Ziehl-Neelsen"],
         0, "Cryptococcus neoformans produces a thick, gelatinous, immunomodulatory capsule composed of glucuronoxylomannan (GXM); India ink cannot penetrate the capsule, highlighting the round, budding yeast cells inside prominent translucent halos.",
         True, "Veterinary Mycology (ICAR PG PYQ)"),

        ("Rhinosporidium seeberi, causing chronic polypoid granulomatous masses in the nasal passages of cattle, dogs, and horses, is microscopically characterized in biopsy sections by containing:",
         ["Enormous, thick-walled spherical sporangia (100 to 350 um in diameter) containing thousands of mature spherical endospores", "Septate hyphae with conidiophores", "Tiny intracellular yeasts inside Kupffer cells", "Acantholytic keratinocytes"],
         0, "Rhinosporidiosis (now classified among the Mesomycetozoea / Ichthyosporea) forms conspicuous giant sporangia (up to 300-350 um) filled with hundreds of 5-7 um endospores that release through a distinct apical pore to form new polyps.",
         True, "Veterinary Mycology (ICAR PG PYQ)"),

        ("Blastomyces dermatitidis, causing canine blastomycosis (pulmonary and cutaneous pyogranulomatous disease), appears in infected host tissues as a:",
         ["Large (8 to 15 um), thick, refractile 'double-contoured' wall yeast cell that buds singly with a characteristic broad base of attachment to the daughter cell", "Tiny (2 to 4 um) intracellular yeast packed in macrophages", "Giant spherule with endospores", "Narrow-based budding yeast"],
         0, "In tissue at 37°C, B. dermatitidis is a dimorphic fungus forming thick-walled, refractile, unencapsulated spherical yeasts; the daughter bud connects to the parent cell via a broad, wide neck/base before detaching.",
         True, "Veterinary Mycology (ICAR PG PYQ)"),

        ("Histoplasma capsulatum is an endemic thermal dimorphic fungus that in animal tissues lives and multiplies obligately as:",
         ["Tiny (2 to 4 um) oval yeast cells located intracellularly within the cytoplasm of monocytes and tissue macrophages", "Large extracellular branching mycelia", "Encapsulated yeasts with broad bases", "Sporangia containing zoospores"],
         0, "At mammalian body temperature (37°C), microconidia convert into small, oval, single-budding yeasts that are phagocytosed by macrophages; they survive inside phagolysosomes, packing the cytoplasm of reticuloendothelial cells in bone marrow, liver, and spleen.",
         True, "Veterinary Mycology (ICAR PG PYQ)"),

        ("Aflatoxin B1, produced primarily by Aspergillus flavus and Aspergillus parasiticus on stored cereal grains and oilseeds, exerts its potent hepatotoxic and carcinogenic effects following bioactivation by hepatic CYP450 enzymes into:",
         ["Aflatoxin B1-8,9-epoxide, which covalently binds to the N7 position of guanine residues in genomic DNA", "Free benzoic acid", "Gluconic acid", "Ascorbic acid"],
         0, "Hepatic cytochrome P450 oxidizes Aflatoxin B1 into a highly reactive, electrophilic exo-8,9-epoxide intermediate, which intercalates into DNA and forms covalent trans-8,9-dihydro-8-(N7-guanyl)-9-hydroxy-AFB1 adducts, inducing G->T transversion mutations in p53.",
         True, "Mycotoxicoses (ICAR PG PYQ)"),

        ("When lactating dairy cows consume feed contaminated with Aflatoxin B1, the toxin is metabolized in the liver and excreted in commercial milk as the hydroxylated derivative known as:",
         ["Aflatoxin M1 (AFM1)", "Aflatoxin G1", "Aflatoxin B2", "Aflatoxicol"],
         0, "Hepatocytes hydroxylate Aflatoxin B1 at carbon 4 to form Aflatoxin M1 (M = milk); AFM1 is excreted in milk within 12-24 hours of ingestion, representing a major public health residue regulated by strict legal limits (e.g. 0.5 ug/kg).",
         True, "Mycotoxicoses (ICAR PG PYQ)"),

        ("Ochratoxin A, synthesized by Aspergillus ochraceus and Penicillium verrucosum, is of major clinical significance in swine and poultry because it is primarily a potent:",
         ["Nephrotoxin, causing porcine nephropathy characterized by proximal renal tubular degeneration, interstitial fibrosis, and pale swollen kidneys", "Hepatocarcinogen only", "Neurotoxin causing flaccid paralysis", "Cardiac glycoside"],
         0, "Ochratoxin A competitively inhibits phenylalanyl-tRNA synthetase and disrupts renal mitochondrial respiration, accumulating selectively in renal proximal convoluted tubules and causing endemic porcine nephropathy.",
         True, "Mycotoxicoses (ICAR PG PYQ)"),

        ("Zearalenone (F-2 toxin), produced by Fusarium graminearum and Fusarium culmorum in moldy maize, is notorious in swine production because it binds host estrogen receptors, causing:",
         ["Hyperestrogenism in prepubertal gilts (swollen hyperemic vulva / 'vulvovaginitis', mammary enlargement, and rectal prolapse)", "Acute pulmonary edema and hydrothorax", "Severe bone marrow aplasia", "Dry gangrene of the tail"],
         0, "Zearalenone is a resorcylic acid lactone that structurally mimics 17-beta-estradiol, binding high-affinity estrogen receptors in target reproductive tissues; in prepubertal gilts, it induces marked vulvar swelling, vaginal prolapse, and nymphomania.",
         True, "Mycotoxicoses (ICAR PG PYQ)"),

        ("Fumonisin B1 (FB1), produced by Fusarium verticillioides in moldy corn, inhibits ceramide synthase (sphingosine N-acyltransferase), leading to accumulation of toxic sphinganine and causing which two species-specific fatal diseases?",
         ["Equine Leukoencephalomalacia (ELEM / 'Moldy Corn Disease' in horses) and Porcine Pulmonary Edema (PPE in swine)", "Canine hepatitis and feline lymphoma", "Bovine mastitis and ovine enterotoxemia", "Avian gout and Newcastle disease"],
         0, "Fumonisin B1 disrupts sphingolipid metabolism; in equines, it causes liquefactive necrosis of cerebral white matter (ELEM); in pigs, it alters pulmonary capillary hemodynamics, producing fatal acute pulmonary edema (PPE).",
         True, "Mycotoxicoses (ICAR PG PYQ)"),

        ("The 'Satratoxins' and 'T-2 Toxin' are trichothecene mycotoxins produced by Stachybotrys chartarum and Fusarium species that produce radiomimetic tissue damage by directly inhibiting:",
         ["Eukaryotic protein synthesis by binding to the 60S ribosomal subunit and inhibiting peptidyl transferase activity", "Bacterial cell wall cross-linking", "RNA reverse transcriptase", "ATP synthase in the cell membrane"],
         0, "Trichothecenes (T-2 toxin, vomitoxin/DON, satratoxins) possess a core 12,13-epoxytrichothecene skeleton that binds with high affinity to the 28S rRNA peptidyl transferase active center on the eukaryotic 60S ribosome, irreversibly halting translation.",
         True, "Mycotoxicoses (ICAR PG PYQ)")
    ]
    return qs

if __name__ == '__main__':
    qs = get_module6_questions()
    print(f"Microbiology Module 6 loaded: {len(qs)} questions")
