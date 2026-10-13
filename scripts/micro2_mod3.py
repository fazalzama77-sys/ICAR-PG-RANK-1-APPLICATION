# scripts/micro2_mod3.py
# Module 3: Veterinary Mycology & Mycotoxicoses (45 questions)

TOPIC = "Veterinary Mycology & Mycotoxicoses"

def get_module3_questions():
    return [
        (
            "The rigid cell wall of true pathogenic fungi (Eumycota) is structurally composed of chitin and beta-glucans, while their plasma membrane contains which principal sterol in place of mammalian cholesterol?",
            [
                "Ergosterol (targeted by polyenes and azoles)",
                "Stigmasterol (targeted by echinocandins)",
                "Hopanoids (targeted by polymyxin E)",
                "Lanosterol (targeted by griseofulvin)"
            ],
            0,
            "True fungi contain chitin (beta-1,4-linked N-acetylglucosamine) and beta-1,3/1,6-D-glucans in their cell wall, and utilize Ergosterol as the primary sterol maintaining plasma membrane fluidity and integrity.",
            True,
            TOPIC
        ),
        (
            "Polyene macrolide antifungal drugs (such as Amphotericin B, Nystatin, and Natamycin) exert their rapid fungicidal action by:",
            [
                "Inhibiting cytochrome P450 14-alpha-sterol demethylase in the endoplasmic reticulum",
                "Binding directly to membrane ergosterol to form transmembrane ion-leaking pores",
                "Non-competitively inhibiting beta-1,3-D-glucan synthase in the fungal cell wall",
                "Disrupting mitotic spindle microtubules by binding polymerized fungal tubulin"
            ],
            1,
            "Polyene antifungals (Amphotericin B, Nystatin, Natamycin) are amphipathic molecules that bind directly to ergosterol in the fungal plasma membrane, assembling into transmembrane hydrophilic pores that cause lethal leakage of intracellular K+ and Mg2+.",
            True,
            TOPIC
        ),
        (
            "Azole antifungal agents (such as Itraconazole, Fluconazole, Ketoconazole, and Enilconazole) inhibit fungal growth by blocking the conversion of lanosterol to ergosterol via inhibition of which enzyme?",
            [
                "Squalene epoxidase (encoded by ERG1)",
                "Beta-1,3-D-glucan synthase (encoded by FKS1)",
                "Cytochrome P450-dependent 14-alpha-sterol demethylase (ERG11 / CYP51)",
                "Thymidylate synthase and cytosine deaminase"
            ],
            2,
            "Imidazoles (ketoconazole, enilconazole, miconazole) and triazoles (itraconazole, fluconazole, voriconazole) bind the heme iron of fungal cytochrome P450 14-alpha-sterol demethylase (CYP51), depleting ergosterol and accumulating toxic 14-alpha-methyl sterols.",
            True,
            TOPIC
        ),
        (
            "The allylamine antifungal drug Terbinafine, widely used for treating dermatophytosis, is fungicidal against dermatophytes because it selectively inhibits which early enzyme in sterol biosynthesis, causing toxic intracellular accumulation of squalene?",
            [
                "14-alpha-sterol demethylase (CYP51A1)",
                "Chitin synthase-3 (CHS3)",
                "HMG-CoA reductase",
                "Squalene epoxidase (ERG1)"
            ],
            3,
            "Allylamines (terbinafine, naftifine) non-competitively inhibit fungal squalene epoxidase (squalene monooxygenase), blocking the conversion of squalene to squalene-2,3-epoxide; the resulting intracellular accumulation of squalene is directly fungicidal.",
            True,
            TOPIC
        ),
        (
            "Echinocandin antifungals (such as Caspofungin and Micafungin) are referred to as 'fungal penicillins' because they inhibit the synthesis of which essential fungal cell wall component?",
            [
                "Beta-(1,3)-D-glucan (by inhibiting beta-1,3-D-glucan synthase)",
                "Chitin polymers (by inhibiting UDP-N-acetylglucosamine transferase)",
                "Ergosterol (by inhibiting delta-14-sterol reductase)",
                "Mannoproteins (by inhibiting dolichol phosphate mannosyltransferase)"
            ],
            0,
            "Echinocandins (caspofungin, micafungin, anidulafungin) are cyclic lipopeptides that non-competitively inhibit the catalytic subunit Fks1p of beta-(1,3)-D-glucan synthase, causing osmotic lysis of Candida and hyphal tip lysis of Aspergillus.",
            True,
            TOPIC
        ),
        (
            "Griseofulvin, an oral fungistatic antibiotic derived from Penicillium griseofulvum used solely for systemic treatment of dermatophytosis, acts intracellularly by:",
            [
                "Forming hydrophilic pores across the nuclear envelope of arthrospores",
                "Binding to polymerized tubulin to disrupt the fungal mitotic spindle",
                "Inhibiting fungal dihydrofolate reductase and purine biosynthesis",
                "Chelation of ferric iron required by fungal catalase and peroxidase"
            ],
            1,
            "Griseofulvin is absorbed better with a fatty meal, deposits in newly forming keratin precursor cells of skin, hair, and claws, and binds fungal microtubule proteins (tubulin) to arrest fungal mitosis in metaphase. Because it disrupts microtubules, it is teratogenic in pregnant queens (causing cleft palate and cyclopia).",
            True,
            TOPIC
        ),
        (
            "Flucytosine (5-Fluorocytosine, 5-FC) exhibits selective toxicity against pathogenic yeasts (Candida and Cryptococcus) while sparing mammalian host cells because mammalian cells lack which enzyme that converts 5-FC into 5-fluorouracil?",
            [
                "Dihydroorotate dehydrogenase",
                "Xanthine oxidase",
                "Cytosine deaminase",
                "Hypoxanthine-guanine phosphoribosyltransferase"
            ],
            2,
            "Flucytosine enters fungal cells via cytosine permease and is deaminated by fungal cytosine deaminase (an enzyme absent in mammalian cells) into 5-fluorouracil (5-FU), which is converted into 5-FdUMP (inhibiting thymidylate synthase/DNA synthesis) and 5-FUTP (disrupting RNA processing).",
            False,
            TOPIC
        ),
        (
            "Sabouraud Dextrose Agar (SDA), the universal primary culture medium for veterinary fungi, suppresses competing bacterial growth primarily by utilizing:",
            [
                "7.5% sodium chloride and 0.5% bile salts at an alkaline pH of 8.5",
                "Crystal violet, potassium tellurite, and thallous acetate at pH 7.4",
                "Malachite green and egg albumin inspissated at 85°C",
                "High dextrose concentration (4%) and an acidic pH of 5.6"
            ],
            3,
            "Formulated by Raymond Sabouraud in 1892, standard Sabouraud Dextrose Agar contains 4% dextrose (glucose) and 1% peptone adjusted to an acidic pH of 5.6, which inhibits most bacteria; for contaminated clinical skins/hairs, chloramphenicol (or gentamicin) and cycloheximide (actidione) are added.",
            True,
            TOPIC
        ),
        (
            "On Dermatophyte Test Medium (DTM)—which contains cycloheximide, gentamicin, chlortetracycline, and Phenol Red indicator—pathogenic dermatophytes (Microsporum and Trichophyton) are presumptively identified within 7–14 days because they:",
            [
                "Preferentially catabolize peptone proteins first, releasing alkaline metabolites that turn the medium from yellow to bright red",
                "Rapidly ferment glucose into lactic acid, turning the medium from bright red to lemon yellow",
                "Reduce sodium thiosulfate to hydrogen sulfide, turning the agar base jet-black",
                "Synthesize melanin from caffeic acid, turning the fungal colony dark brown"
            ],
            0,
            "On DTM, pathogenic dermatophytes preferentially utilize nitrogenous peptones before carbohydrates, producing alkaline ammonium metabolites that raise the pH and turn the phenol red indicator from yellow (acidic) to bright red simultaneously with white/buff fluffy colony growth.",
            True,
            TOPIC
        ),
        (
            "In the standard 'Lactophenol Cotton Blue' (LPCB) mounting fluid used for microscopic identification of fungal mycelia and conidia, what are the specific functions of Lactic acid, Phenol, and Cotton blue (Aniline blue)?",
            [
                "Lactic acid kills the fungus; Phenol stains ergosterol; Cotton blue prevents drying",
                "Lactic acid preserves fungal structures; Phenol kills the fungus; Cotton blue stains chitin in the fungal cell wall",
                "Lactic acid dissolves chitin; Phenol induces sporulation; Cotton blue stains lipid granules",
                "Lactic acid fixes nuclear chromatin; Phenol buffers pH to 8.0; Cotton blue quenches fluorescence"
            ],
            1,
            "In LPCB: Lactic acid acts as a clearing and preserving agent that maintains intact fungal morphology; Phenol acts as a fungicide to kill live infectious spores; Glycerol prevents desiccation; and Cotton Blue (methyl blue/aniline blue) stains the chitinous cell wall deep blue.",
            True,
            TOPIC
        ),
        (
            "Which two specialized histopathological stains are routinely employed to visualize fungal hyphae and yeasts in formalin-fixed tissue sections, staining fungal cell walls bright magenta-red and brown-black, respectively?",
            [
                "Ziehl-Neelsen stain and Albert's toluidine blue stain",
                "Masson's trichrome stain and Prussian blue stain",
                "Periodic Acid-Schiff (PAS) stain and Gomori Methenamine Silver (GMS) stain",
                "Congo red amyloid stain and Sudan Black B lipid stain"
            ],
            2,
            "Periodic acid oxidizes 1,2-glycol groups in fungal cell wall polysaccharides (glucans/mannans) into aldehydes that react with Schiff's leucofuchsin to stain fungi bright magenta (PAS), while chromic acid oxidation and methenamine-silver nitrate reduction (GMS) stain fungal walls sharp black.",
            True,
            TOPIC
        ),
        (
            "When canine or feline ringworm lesions caused by Microsporum canis are examined in a darkened room under a Wood's Lamp (filtered ultraviolet light at 365 nm), infected hairs emit a bright apple-green fluorescence due to:",
            [
                "Ergosterol peroxides accumulated within the fungal plasma membrane",
                "Calcium dipicolinate chelated inside thick-walled macroconidia",
                "Melanin and aflatoxin B1 synthesized by saprophytic mycelia",
                "A water-soluble pteridine pigment metabolite produced in actively growing invaded hair shafts"
            ],
            3,
            "Wood's lamp (UV-A light at 365 nm filtered through cobalt/nickel glass) excites a tryptophan-derived pteridine metabolite produced ONLY when Microsporum canis actively invades growing hair shafts in vivo; in vitro colonies on agar do not fluoresce similarly.",
            True,
            TOPIC
        ),
        (
            "Which geophilic (soil-inhabiting) dermatophyte frequently causes focal crusty ringworm lesions on the muzzle and legs of dogs and horses, does NOT fluoresce under Wood's lamp, and forms cinnamon-buff powdery colonies with thin-walled, rough, 4-to-6-celled ellipsoidal macroconidia?",
            [
                "Microsporum gypseum (reclassified as Nannizzia gypsea)",
                "Microsporum canis (zoophilic spindle-shaped 6-to-15-celled macroconidia)",
                "Trichophyton verrucosum (zoophilic cattle dermatophyte)",
                "Epidermophyton floccosum (anthropophilic club-shaped macroconidia)"
            ],
            0,
            "Microsporum gypseum (Nannizzia gypsea) is the classic geophilic dermatophyte acquired by dogs rooting/digging in soil; its colonies grow rapidly as flat cinnamon-tan suede-like powders producing abundant thin-walled, echinulate, boat/ellipsoid macroconidia with 4–6 cells and rounded ends.",
            True,
            TOPIC
        ),
        (
            "What is the primary host-adapted dermatophyte responsible for porcine ringworm (characterized by centrifugally expanding, brown crusted skin lesions behind the ears and on the flanks of adult pigs) that produces distinctive small, pear-shaped 2-celled macroconidia?",
            [
                "Trichophyton equinum",
                "Microsporum nanum (Nannizzia nana)",
                "Trichophyton gallinae",
                "Microsporum audouinii"
            ],
            1,
            "Microsporum nanum is the specific dermatophyte of swine worldwide; microscopically on LPCB mounts, it is uniquely identified by numerous small, ovoid-to-pear-shaped (pyriform), thin-walled macroconidia divided into only two (occasionally three) cells.",
            True,
            TOPIC
        ),
        (
            "Most classical strains of Trichophyton equinum, the premier cause of equine dermatophytosis ('Girth Itch' in horses), are nutritionally distinguished in Trichophyton Agar #1–#7 testing by their strict requirement for which vitamin?",
            [
                "Thiamine and Inositol (Trichophyton Agar #3)",
                "Para-aminobenzoic acid (PABA)",
                "Nicotinic acid / Niacin (Trichophyton Agar #5)",
                "L-Histidine (Trichophyton Agar #6)"
            ],
            2,
            "Whereas Trichophyton verrucosum of cattle requires thiamine and inositol (T-agar #3 and #4) and grows better at 37°C, classical Trichophyton equinum var. equinum of horses has an absolute nutritional requirement for nicotinic acid (niacin, T-agar #5).",
            True,
            TOPIC
        ),
        (
            "'Avian Favus' ('White Comb'), a chronic dermatophytosis of chickens and turkeys characterized by chalky white, flour-like crusts on the comb and wattles that may spread to feathered skin, is caused by:",
            [
                "Aspergillus flavus",
                "Candida albicans",
                "Macrorhabdus ornithogaster",
                "Trichophyton gallinae (Microsporum gallinae / Lophophyton gallinae)"
            ],
            3,
            "Trichophyton gallinae (Lophophyton gallinae) is the zoophilic dermatophyte of poultry that causes Avian Favus ('White Comb') and produces a characteristic strawberry-red diffusible pigment on the reverse side of Sabouraud dextrose agar.",
            True,
            TOPIC
        ),
        (
            "When Candida albicans is inoculated onto nutritionally poor Cornmeal Tween-80 Agar at 25°C (Dalmau plate technique under a coverslip), it is definitively identified by forming pseudohyphae bearing:",
            [
                "Large, round, thick-walled terminal Chlamydoconidia (chlamydospores)",
                "Spindle-shaped, rough-walled, 12-celled macroconidia with terminal knobs",
                "Dichotomously branching septate hyphae with conidial heads and phialides",
                "Barrel-shaped arthroconidia alternating with empty disjunctor cells"
            ],
            0,
            "In addition to forming true germ tubes without constriction in serum at 37°C within 2 hours (Reynolds-Braude phenomenon), Candida albicans (and C. dubliniensis) forms characteristic large, refractile, thick-walled spherical chlamydoconidia (chlamydospores) on Cornmeal Tween-80 agar.",
            True,
            TOPIC
        ),
        (
            "On Niger Seed Agar (Guizotia abyssinica / Staib's birdseed agar) containing caffeic acid, Cryptococcus neoformans forms diagnostic dark brown-to-black colonies due to the activity of which virulence enzyme?",
            [
                "Extracellular phospholipase B",
                "Phenol oxidase (laccase), which synthesizes melanin from diphenolic substrates",
                "Cytoplasmic urease, which hydrolyzes urea into ammonium carbonate",
                "Keratinolytic serine protease, which digests stratum corneum proteins"
            ],
            1,
            "Cryptococcus neoformans and C. gattii are the only pathogenic yeasts that possess copper-dependent phenol oxidase (laccase), which converts diphenolic compounds (such as caffeic acid in birdseed/Niger seed agar or L-DOPA in brain tissue) into dark brown-black melanin pigment that protects the yeast from oxidative killing.",
            True,
            TOPIC
        ),
        (
            "How does Malassezia pachydermatis—the peanut-shaped unipolar budding yeast causing canine otitis externa and seborrheic dermatitis—differ nutritionally from all other species in the genus Malassezia (such as M. furfur and M. globosa)?",
            [
                "It is an obligate anaerobe that requires 10% hydrogen gas and cysteine",
                "It requires thiamine, inositol, and nicotinic acid for budding",
                "It is the only non-lipid-dependent species capable of growing on standard Sabouraud dextrose agar without olive oil",
                "It grows only at 42°C on media supplemented with pigeon droppings"
            ],
            2,
            "All human-associated Malassezia species (M. furfur, M. sympodialis, M. globosa) are obligately lipid-dependent (requiring long-chain C12–C24 fatty acids / olive oil overlay on Dixon's agar because they lack fatty acid synthase). Malassezia pachydermatis is uniquely non-lipid-dependent and grows readily on plain Sabouraud dextrose agar.",
            True,
            TOPIC
        ),
        (
            "Sporothrix schenckii (and Sporothrix brasiliensis in cats) causes lymphocutaneous 'Rose Gardener's Disease' in horses, cats, and dogs. In histopathological sections and pus smears, its pleomorphic 'cigar-shaped' yeast cells are characteristically surrounded by:",
            [
                "A wide, unstained mucopolysaccharide capsule demonstrated by India ink",
                "Double-contoured refractile walls with broad-based unipolar buds",
                "A thick-walled spherule membrane enclosing hundreds of endospores",
                "Star-like eosinophilic radiate Splendore-Hoeppli projections termed 'Asteroid Bodies'"
            ],
            3,
            "Sporothrix schenckii is a thermally dimorphic fungus (delicate 'daisy-head' conidiophores at 25°C; pleomorphic elongated 'cigar-shaped' yeasts at 37°C). In host tissues, yeast cells are frequently encased in a stellate, brightly eosinophilic antigen-antibody complex halo (Splendore-Hoeppli phenomenon) called an Asteroid Body.",
            True,
            TOPIC
        ),
        (
            "In its saprophytic mycelial phase grown on Sabouraud dextrose agar at 25°C, Histoplasma capsulatum produces which pathognomonic diagnostic conidial structure?",
            [
                "Large, spherical, thick-walled 'tuberculate macroconidia' covered with finger-like echinulate projections",
                "Alternating barrel-shaped arthroconidia separated by empty disjunctor cells",
                "Multiseptate spindle-shaped macroconidia with a curved apical beak",
                "Uncoiled helical sporangiophores terminating in a dark columella and sporangium"
            ],
            0,
            "While Histoplasma capsulatum exists in host tissues at 37°C as small (2–4 um) intracellular budding yeasts inside macrophages, its mold phase at 25°C produces diagnostic large (8–14 um), round, thick-walled 'tuberculate macroconidia' bearing spiky tuberculate projections.",
            True,
            TOPIC
        ),
        (
            "'Epizootic Lymphangitis' ('Pseudoglanders')—a chronic, contagious, ulcerating pyogranulomatous lymphangitis of the limbs, neck, and nostrils of horses, mules, and donkeys—is caused by:",
            [
                "Burkholderia mallei",
                "Histoplasma capsulatum var. farciminosum",
                "Corynebacterium pseudotuberculosis biovar equi",
                "Coccidioides immitis"
            ],
            1,
            "Histoplasma capsulatum var. farciminosum (formerly Cryptococcus farciminosus) causes Epizootic Lymphangitis in equids, clinically mimicking cutaneous glanders ('farcy'). Giemsa or Gram-stained smears of pus reveal numerous oval, lemon-shaped, double-contoured yeast cells (2.5–4 um) both inside macrophages and extracellularly.",
            True,
            TOPIC
        ),
        (
            "Coccidioides immitis and Coccidioides posadasii (causative agents of 'Valley Fever' in dogs, horses, and camelids in arid regions) are dimorphic fungi that replicate inside host tissues at 37°C not by yeast budding, but by forming:",
            [
                "Narrow intracellular yeasts inside reticuloendothelial macrophages",
                "Broad-based budding yeast cells with thick double-refractile walls",
                "Large, thick-walled 'Spherules' (20–80 um) that cleave internally into hundreds of 'Endospores'",
                "Elongated cigar-shaped blastoconidia surrounded by eosinophilic asteroid bodies"
            ],
            2,
            "In desert soil (25°C), Coccidioides forms infectious barrel-shaped arthroconidia. Once inhaled into the lungs of dogs or horses (37°C), each arthroconidium rounds up into a giant multinucleated 'spherule' (20–80 um) whose cytoplasm undergoes progressive cleavage to release hundreds of endospores.",
            True,
            TOPIC
        ),
        (
            "In histopathological tissue sections of cattle with mycotic rumenitis or placentitis, how are Zygomycetes of the order Mucorales (Mucor, Rhizopus, Lichtheimia/Absidia) morphologically differentiated from Aspergillus fumigatus?",
            [
                "Mucorales form narrow (2–3 um) regularly septate hyphae with acute 45° dichotomous branching",
                "Mucorales form pigmented brown septate hyphae and sclerotic Medlar bodies",
                "Mucorales form exclusively budding yeasts and pseudohyphae without true mycelia",
                "Mucorales form broad (10–20 um), ribbon-like, pauciseptate (aseptate) hyphae with wide right-angle (90°) branching"
            ],
            3,
            "Aspergillus species produce narrow (3–6 um), uniform, parallel-walled, regularly septate hyphae that branch dichotomously at acute 45° angles. In contrast, Mucorales (Mucor, Rhizopus, Lichtheimia) produce wide (10–25 um), irregular, collapsible ribbon-like, non-septate (pauciseptate) hyphae that branch erratically at 90° right angles and aggressively invade blood vessels.",
            True,
            TOPIC
        ),
        (
            "In horses, 'Guttural Pouch Mycosis'—a life-threatening infection in which a fungal diphtheritic plaque grows on the roof of the medial compartment of the guttural pouch—frequently causes sudden death by eroding the wall of the:",
            [
                "Internal carotid artery (causing fatal spontaneous epistaxis) and cranial nerves IX and X (causing dysphagia)",
                "Tracheal bifurcation and cranial vena cava (causing hemothorax)",
                "Ethmoid turbinates and optic chiasm (causing acute blindness)",
                "Nasolacrimal duct and facial artery (causing submandibular hematoma)"
            ],
            0,
            "Equine guttural pouch mycosis (caused primarily by Aspergillus fumigatus and A. nidulans) forms a necrohemorrhagic mycotic plaque directly over the internal carotid artery (or external carotid/maxillary artery) and glossopharyngeal/vagus nerves (CN IX, X), leading to fatal arterial rupture (epistaxis), pharyngeal paralysis (dysphagia), and Horner's syndrome.",
            True,
            TOPIC
        ),
        (
            "Pythium insidiosum—the etiological agent of 'Equine and Canine Pythiosis' ('Swamp Cancer', 'Leeches', or 'Bursattee') characterized by pruritic granulomatous cutaneous masses containing coral-like 'kunkers'—is resistant to standard azole and polyene antifungals because it is:",
            [
                "An acid-fast actinomycete whose cell wall is composed of mycolic acids and peptidoglycan",
                "An aquatic Oomycete (kingdom Stramenopila) whose cell wall contains cellulose and beta-glucans and whose membrane lacks ergosterol",
                "An obligate intracellular microsporidian parasite that lacks mitochondria and peroxisomes",
                "A cyanobacterium that synthesizes microcystin and saxitoxin in stagnant ponds"
            ],
            1,
            "Pythium insidiosum is not a true fungus (Eumycota), but a fungus-like aquatic Oomycete (water mold). Because its cell wall contains beta-glucans and cellulose (not chitin) and its plasma membrane lacks ergosterol, ergosterol-targeting drugs (amphotericin B, itraconazole) are generally ineffective.",
            True,
            TOPIC
        ),
        (
            "Prototheca zopfii (cause of incurable chronic granulomatous bovine mastitis) and Prototheca wickerhamii (cause of canine cutaneous and ocular protothecosis) are taxonomically classified as:",
            [
                "Dimorphic basidiomycetous yeasts related to Cryptococcus",
                "Thermophilic actinomycetes related to Dermatophilus",
                "Achlorophyllous (colorless) unicellular green algae (related to Chlorella) that reproduce by endosporulation",
                "Aquatic chytridiomycetes that infect amphibians and waterfowl"
            ],
            2,
            "Prototheca species are colorless (achlorophyllous) saprophytic mutant green microalgae (family Chlorellaceae) that lost their chloroplasts. In tissues and milk, they form oval-to-spherical sporangia (theca) that cleave internally into 2 to 16 daughter endospores (autospores) arranged in a 'morula' or 'Mercedes-Benz star' pattern.",
            True,
            TOPIC
        ),
        (
            "Pneumocystis carinii (and Pneumocystis canis)—which causes fatal diffuse interstitial pneumonia with foamy eosinophilic alveolar casts in Arabian foals with SCID and immunodeficient dogs—is an atypical fungus that does NOT respond to amphotericin B or azoles and is instead treated with:",
            [
                "Griseofulvin combined with oral potassium iodide",
                "Ivermectin combined with praziquantel",
                "Penicillin G combined with streptomycin",
                "Trimethoprim-Sulfamethoxazole (Co-trimoxazole)"
            ],
            3,
            "Although ribosomal RNA phylogeny established that Pneumocystis is an atypical ascomycetous fungus, its plasma membrane contains cholesterol (scavenged from the host) rather than ergosterol, making polyenes and azoles useless. It is treated and prevented with Trimethoprim-Sulfamethoxazole (or pentamidine/atovaquone).",
            True,
            TOPIC
        ),
        (
            "Encephalitozoon cuniculi, an obligate intracellular spore-forming microsporidian parasite closely related to fungi, infects rabbits via urinary spore ingestion and causes which classic clinical triad of lesions?",
            [
                "Granulomatous meningoencephalitis (vestibular head tilt), chronic interstitial nephritis, and phacoclastic uveitis (lens rupture/cataract)",
                "Caseous bronchopneumonia, ulcerative typhlitis, and degenerative polymyositis",
                "Hemorrhagic tracheitis, fibrinous pericarditis, and hepatic coccidiosis",
                "Hyperplastic biliary cirrhosis, cutaneous myxomatosis, and splenic infarction"
            ],
            0,
            "Encephalitozoon cuniculi extrudes a coiled polar tubule to inject its sporoplasm into host cells, showing a strong tropism for the brain (vestibular torticollis/wry neck), kidneys (pitted cortical scars), and the developing lens of the eye (anterior lens capsule rupture and phacoclastic uveitis).",
            True,
            TOPIC
        ),
        (
            "Macrorhabdus ornithogaster (formerly known as 'Megabacteria' and now recognized as 'Avian Gastric Yeast') is a very large, Gram-positive, PAS-positive rod-shaped ascomycetous yeast that colonizes which specific anatomical site in budgerigars, canaries, and finches, causing 'Going Light Syndrome'?",
            [
                "The mucosal epithelium of the crop and cervical esophagus",
                "The narrow isthmus (intermediate zone) between the proventriculus and the ventriculus (gizzard)",
                "The cecal tonsils and cloacal bursa of Fabricius",
                "The parabronchi and abdominal air sacs"
            ],
            1,
            "Macrorhabdus ornithogaster is an elongated (20–90 um long) filamentous yeast that forms a dense palisading mat specifically in the koilin/mucus layer at the isthmus connecting the glandular proventriculus and muscular ventriculus, causing proventricular dilatation, regurgitation of undigested seeds, and chronic emaciation ('going light').",
            True,
            TOPIC
        ),
        (
            "The four major naturally occurring Aflatoxins (B1, B2, G1, and G2) were named based on their thin-layer chromatography (TLC) mobility and the characteristic color of their fluorescence under long-wave ultraviolet light (365 nm):",
            [
                "Aflatoxins B1/B2 fluoresce Blood-red, while Aflatoxins G1/G2 fluoresce Golden-orange",
                "Aflatoxins B1/B2 are produced by Bacillus, while Aflatoxins G1/G2 are produced by Geotrichum",
                "Aflatoxins B1/B2 fluoresce Blue, while Aflatoxins G1/G2 fluoresce Green",
                "Aflatoxins B1/B2 bind Bile acids, while Aflatoxins G1/G2 bind Glomerular capillaries"
            ],
            2,
            "Aflatoxins B1 and B2 (cyclopentenone ring fused to the coumarin lactone) emit a bright Blue fluorescence under UV light (365 nm), whereas Aflatoxins G1 and G2 (six-membered lactone ring) emit a yellow-Green fluorescence. Aflatoxin M1 (hydroxylated metabolite of B1) was named because it was isolated from Milk.",
            True,
            TOPIC
        ),
        (
            "In hepatocarcinogenesis induced by Aflatoxin B1, hepatic cytochrome P450 enzymes convert AFB1 into the reactive AFB1-8,9-exo-epoxide, which covalently binds the N7 position of guanine in DNA and characteristically induces which signature mutation in the p53 tumor suppressor gene?",
            [
                "An A-to-G transition at codon 12 of the ras proto-oncogene",
                "A frameshift deletion of 3 base pairs at codon 508",
                "Chromosomal translocation t(8;14) activating c-myc",
                "A G-to-T transversion at the third base of codon 249 of p53 (AGG -> AGT, Arg -> Ser)"
            ],
            3,
            "The AFB1-8,9-epoxide forms a bulky AFB1-N7-guanine DNA adduct that undergoes depurination or ring opening to form a stable formamidopyrimidine (AFB1-FAPY) lesion, driving a signature G:C to T:A transversion specifically at codon 249 of the p53 tumor suppressor gene.",
            True,
            TOPIC
        ),
        (
            "Which feed additive class is most widely and effectively incorporated into poultry and livestock diets to selectively adsorb Aflatoxins via their planar beta-dicarbonyl ring system in the gastrointestinal tract and prevent systemic bioavailability?",
            [
                "Hydrated Sodium Calcium Aluminosilicate (HSCAS / bentonite and montmorillonite smectite clays)",
                "Ethoxyquin and butylated hydroxytoluene (BHT) synthetic lipid antioxidants",
                "Propionic acid and calcium propionate mold inhibitors",
                "Zinc bacitracin and monensin sodium ionophore coccidiostats"
            ],
            0,
            "Phyllosilicate clays—specifically Hydrated Sodium Calcium Aluminosilicate (HSCAS), bentonites, and montmorillonite smectites—intercalate and chelate the planar beta-dicarbonyl moiety of Aflatoxin B1 with high affinity in the gut lumen, reducing hepatic uptake and milk Aflatoxin M1 excretion.",
            True,
            TOPIC
        ),
        (
            "Classic 'Ergotism' in cattle and swine results from ingestion of cereal grains (especially rye, triticale, and barley) whose ovaries have been replaced by hard, dark purple-black banana-shaped fungal sclerotia of:",
            [
                "Fusarium graminearum (Gibberella zeae)",
                "Claviceps purpurea",
                "Aspergillus parasiticus",
                "Penicillium verrucosum"
            ],
            1,
            "Claviceps purpurea infects the florets of rye and other small grains, replacing the developing seed kernel with a dense, dark purple-black overwintering mycelial mass called a sclerotium ('ergot' / 'cock's spur') rich in ergopeptine alkaloids (ergotamine, ergocristine, ergometrine).",
            True,
            TOPIC
        ),
        (
            "Ergopeptine alkaloids (such as ergotamine from Claviceps purpurea and ergovaline from tall fescue endophytes) produce two major pharmacological syndromes in livestock: dry gangrene of the extremities (hooves, tail, ears) and agalactia in sows and mares. Through which two receptor mechanisms do these occur?",
            [
                "Muscarinic M3 receptor agonism (gangrene) and beta-2 adrenergic blockade (agalactia)",
                "Histamine H1 receptor activation (gangrene) and oxytocin receptor antagonism (agalactia)",
                "Alpha-adrenergic / 5-HT2 receptor vasoconstriction (gangrene) and Dopamine D2 receptor agonism inhibiting pituitary prolactin (agalactia)",
                "Nicotinic acetylcholine receptor blockade (gangrene) and GABA-A chloride channel opening (agalactia)"
            ],
            2,
            "Ergot alkaloids contain a tetracyclic ergoline ring structurally homologous to norepinephrine, serotonin, and dopamine. Agonism at vascular alpha-adrenergic and 5-HT2A receptors causes intense arteriolar vasoconstriction and ischemic dry gangrene, while agonism at lactotroph Dopamine D2 receptors suppresses prolactin secretion, causing agalactia.",
            True,
            TOPIC
        ),
        (
            "'Fescue Foot', 'Summer Slump', and prolonged gestation/agalactia with thickened 'red bag' placentas in broodmares are caused by grazing Tall Fescue (Festuca arundinacea) infected with which mutualistic seed-borne endophytic fungus?",
            [
                "Pithomyces chartarum",
                "Rhizoctonia leguminicola",
                "Stachybotrys chartarum",
                "Epichloë coenophiala (formerly Neotyphodium / Acremonium coenophialum)"
            ],
            3,
            "Epichloë coenophiala (formerly Neotyphodium coenophialum / Acremonium coenophialum) grows intercellularly inside tall fescue grass and is transmitted vertically through seeds, synthesizing the vasoconstrictive and dopaminergic ergopeptine alkaloid ergovaline.",
            True,
            TOPIC
        ),
        (
            "What is the specific pharmacological antidote administered orally to late-pregnant broodmares grazing endophyte-infected tall fescue to block Dopamine D2 receptors on pituitary lactotrophs, restore prolactin secretion, and prevent agalactia without crossing the blood-brain barrier?",
            [
                "Domperidone (or Sulpiride)",
                "Atropine sulfate",
                "Bromocriptine mesylate",
                "Yohimbine hydrochloride"
            ],
            0,
            "Domperidone is a peripheral selective Dopamine D2 receptor antagonist that competitively blocks ergovaline at the anterior pituitary lactotrophs, restoring normal periparturient prolactin surges, mammary development, and normal gestation length in mares.",
            True,
            TOPIC
        ),
        (
            "'Facial Eczema' (Pithomycotoxicosis) in grazing sheep, goats, and dairy cattle in New Zealand, Australia, and South Africa is a severe secondary (hepatogenous) photosensitization caused by ingestion of pasture litter containing spores of Pithomyces chartarum, which produce the hepatotoxin:",
            [
                "Fumonisin B1",
                "Sporidesmin",
                "Phomopsin A",
                "Penitrem A"
            ],
            1,
            "Pithomyces chartarum spores contain the epipolythiodioxopiperazine mycotoxin Sporidesmin, which undergoes redox cycling in bile canaliculi to generate superoxide radicals, causing necrotizing obliterative cholangiohepatitis. The damaged liver cannot excrete phylloerythrin (the photodynamic breakdown product of chlorophyll), leading to severe facial and ear photosensitization.",
            True,
            TOPIC
        ),
        (
            "In hepatogenous photosensitization caused by Sporidesmin ('Facial Eczema') or Lantana camara toxicity in ruminants, what is the exact photodynamic pigment derived from ruminal microbial degradation of dietary chlorophyll that accumulates in systemic blood and skin when biliary excretion is obstructed?",
            [
                "Hypericin (primary photosensitizing naphthodianthrone pigment)",
                "Uroporphyrin I (congenital erythropoietic porphyria pigment)",
                "Phylloerythrin (chlorophyll porphyrin metabolite normally excreted in bile)",
                "Conjugated bilirubin diglucuronide"
            ],
            2,
            "In the rumen, anaerobic bacteria convert dietary chlorophyll into the fluorescent porphyrin derivative Phylloerythrin. A healthy liver extracts phylloerythrin from portal blood and excretes it harmlessly into bile; when sporidesmin damages bile ducts, phylloerythrin enters peripheral skin capillaries and absorbs UV light, generating singlet oxygen.",
            True,
            TOPIC
        ),
        (
            "'Slobbers Syndrome'—characterized by profuse ptyalism (salivation), lacrimation, diarrhea, and bloat in horses and cattle consuming red clover (Trifolium pratense) hay infected with the black-patch fungus Rhizoctonia leguminicola—is caused by which parasympathomimetic mycotoxin?",
            [
                "Swainsonine (locoweed alpha-mannosidase inhibitor)",
                "Satratoxin H (macrocyclic trichothecene)",
                "Lolitrem B (indole-diterpene tremorgen)",
                "Slaframine (indolizidine alkaloid bioactivated to a muscarinic M3 agonist)"
            ],
            3,
            "Rhizoctonia leguminicola (Slafractonia leguminicola, causing 'black patch disease' on red clover) synthesizes the indolizidine alkaloid Slaframine, which is oxidized by hepatic microsomal flavoprotein monooxygenases into a ketoimine that directly stimulates muscarinic acetylcholine (M3) receptors on salivary glands and pancreas (treatable with atropine).",
            True,
            TOPIC
        ),
        (
            "Cattle fed moldy, damaged sweet potatoes (Ipomoea batatas) colonized by the fungus Fusarium solani develop acute, fatal 'Atypical Interstitial Pneumonia' (pulmonary edema and emphysema) because the fungus metabolizes sweet potato phytoalexins into which pneumotoxic furanoterpenoid?",
            [
                "4-Ipomeanol (bioactivated by pulmonary Clara/club cell CYP450 enzymes)",
                "3-Methylindole (produced from L-tryptophan by ruminal Lactobacillus)",
                "Fumonisin B1 (inhibitor of sphinganine N-acyltransferase)",
                "Dicoumarol (vitamin K epoxide reductase antagonist from moldy sweet clover)"
            ],
            0,
            "When sweet potatoes are injured and infected by Fusarium solani, stress metabolites are converted into 4-Ipomeanol. After ingestion by cattle, 4-ipomeanol is selectively bioactivated by cytochrome P450 (CYP4B1) inside non-ciliated bronchiolar epithelial (Clara/club) cells into a reactive dialdehyde that destroys Type I pneumocytes.",
            True,
            TOPIC
        ),
        (
            "'Lupinosis' in sheep and cattle grazing lupin stubbles colonized by the fungus Diaporthe toxica (formerly Phomopsis leptostromiformis) is a severe mycotoxic hepatosis characterized histologically by arrest of hepatocytes in mitotic metaphase due to which mycotoxins?",
            [
                "Aflatoxins B1 and G1 (which alkylate guanine bases in DNA)",
                "Phomopsins (hexapeptide mycotoxins that bind beta-tubulin and depolymerize microtubules)",
                "Rubratoxins A and B (which inhibit protein phosphatase 2A)",
                "Oosporein and Citrinin (which uncouple renal mitochondrial oxidative phosphorylation)"
            ],
            1,
            "Diaporthe toxica (Phomopsis leptostromiformis) growing on lupin stalks produces cyclic hexapeptide mycotoxins called Phomopsins (Phomopsin A). Phomopsins bind tightly to tubulin, preventing microtubule polymerization and arresting dividing hepatocytes in abnormal C-mitosis (metaphase arrest), leading to fatty liver, icterus, andlupinosis.",
            True,
            TOPIC
        ),
        (
            "'Perennial Ryegrass Staggers' in sheep, cattle, horses, and alpacas—characterized by fine head tremors, head nodding, stiff-legged hopping ataxia, and collapse when excited—is caused by grazing Lolium perenne infected with the endophyte Epichloë festucae var. lolii, which synthesizes:",
            [
                "Ergovaline (a vasoconstrictive ergopeptine alkaloid)",
                "Corynetoxins (tunicamycin-like glycolipid inhibitors from Rathayibacter toxicus)",
                "Lolitrem B (a potent indole-diterpene tremorgenic neurotoxin)",
                "Swainsonine (an indolizidine alkaloid inhibiting lysosomal alpha-mannosidase)"
            ],
            2,
            "While the tall fescue endophyte (Epichloë coenophiala) produces ergovaline (fescue foot), the perennial ryegrass endophyte (Epichloë festucae var. lolii) produces the indole-diterpene neurotoxin Lolitrem B, which blocks large-conductance calcium-activated potassium (BK) channels in the cerebellum and spinal cord, causing reversible intention tremors ('ryegrass staggers').",
            True,
            TOPIC
        ),
        (
            "Deoxynivalenol (DON)—a Type B trichothecene mycotoxin produced by Fusarium graminearum (Gibberella zeae) in scabby wheat, barley, and corn—is colloquially known as 'Vomitoxin' because it induces acute feed refusal and emesis, with which domestic species being the most sensitive?",
            [
                "Adult beef cattle and water buffaloes",
                "Laying hens and broiler chickens",
                "Adult Merino sheep and cashmere goats",
                "Swine (growing and finishing pigs)"
            ],
            3,
            "Swine are by far the most sensitive domestic species to Deoxynivalenol (DON / vomitoxin), showing reduced feed intake at >=1 ppm and complete feed refusal and central serotonin (5-HT3)/peptide YY-mediated emesis at 10–20 ppm, whereas ruminants and poultry degrade DON extensively in the rumen/gut.",
            True,
            TOPIC
        ),
        (
            "Which nephrotoxic mycotoxin produced by Penicillium citrinum, Penicillium verrucosum, and Aspergillus terreus often co-contaminates stored cereal grains alongside Ochratoxin A, acting synergistically to damage the renal proximal convoluted tubules in pigs and poultry?",
            [
                "Citrinin",
                "Zearalenone",
                "Diacetoxyscirpenol (DAS)",
                "Cyclopiazonic acid"
            ],
            0,
            "Citrinin is a polyketide nephrotoxin produced by Penicillium and Aspergillus species that frequently co-occurs with Ochratoxin A in temperate cereal grains (barley, oats, corn), causing synergistic degeneration of renal proximal tubules, polydipsia, polyuria, and visceral gout/nephrosis in swine and poultry.",
            True,
            TOPIC
        ),
        (
            "In diagnostic mycology, the in vitro 'Hair Perforation Test' (Ajello and Georg method) is used to differentiate Trichophyton mentagrophytes from Trichophyton rubrum based on the ability of T. mentagrophytes to:",
            [
                "Emit bright orange fluorescence when growing on autoclaved equine tail hairs",
                "Produce specialized perforating organs that cut wedge-shaped perpendicular pits into sterile hair shafts",
                "Dissolve the entire keratin shaft into a clear liquid within 24 hours via alkaline keratinase",
                "Form dark black endothrix chains strictly inside the medulla without penetrating the cuticle"
            ],
            1,
            "When incubated with sterile prepubertal human or blond equine hair fragments in water + yeast extract at 25°C, Trichophyton mentagrophytes (and Microsporum canis) forms specialized 'perforating organs' that bore radial, wedge-shaped perpendicular cones into the hair shaft, whereas T. rubrum (and M. equinum) only erodes the surface.",
            True,
            TOPIC
        ),
        (
            "Cryptococcus gattii (which causes nasal, pulmonary, and CNS cryptococcosis in immunocompetent cats, dogs, and koalas) differs ecologically and biochemically from Cryptococcus neoformans because C. gattii is:",
            [
                "Associated with pigeon droppings and fails to produce urease or capsule",
                "Associated with bat guano in caves and grows as a filamentous mold at 37°C",
                "Associated with Eucalyptus trees and turns Canavanine-Glycine-Bromothymol Blue (CGB) agar cobalt blue",
                "Associated with stagnant swamp water and lacks melanin synthesis on birdseed agar"
            ],
            2,
            "Whereas Cryptococcus neoformans (Serotypes A and D) is associated globally with weathered pigeon guano and leaves CGB agar yellow-green, Cryptococcus gattii (Serotypes B and C) is ecologically associated with decaying hollows of Eucalyptus (red gum) and Douglas fir trees, is resistant to L-canavanine, assimilates glycine, and turns CGB agar deep cobalt blue.",
            True,
            TOPIC
        ),
        (
            "Dogs that scavenge moldy walnuts, moldy cheese, or spoiled garbage colonized by Penicillium crustosum develop acute, severe whole-body muscle tremors, hyperesthesia, and seizures (often misdiagnosed as strychnine or metaldehyde poisoning) due to which tremorgenic mycotoxin?",
            [
                "Zearalenone (resorcylic acid lactone)",
                "Aflatoxin B1 (difuranocoumarin epoxide)",
                "Fumonisin B1 (sphinganine analog)",
                "Penitrem A (often co-occurring with Roquefortine C)"
            ],
            3,
            "Penicillium crustosum growing on fallen walnuts, dairy products, and household compost produces the potent indole-diterpene tremorgenic neurotoxin Penitrem A (alongside the diketopiperazine alkaloid Roquefortine C, which serves as a diagnostic biomarker in stomach contents), inhibiting central inhibitory glycine/GABA interneurons in dogs.",
            True,
            TOPIC
        ),
        (
            "Which nephrotoxic bibenzoquinone mycotoxin produced by Chaetomium trilaterale and Phomopsis species in contaminated poultry feed causes acute proximal tubular necrosis, severe hyperuricemia, and fatal visceral and articular gout in broiler chicks and turkey poults?",
            [
                "Oosporein",
                "Slaframine",
                "Sporidesmin",
                "Ergovaline"
            ],
            0,
            "Oosporein is a red-crystalline bibenzoquinone mycotoxin produced by Chaetomium and Aureobasidium species in maize and poultry rations. In chickens and turkeys, it is a potent specific nephrotoxin that blocks uric acid secretion by proximal renal tubules, producing widespread chalky white urate deposits on the pericardium, liver capsule, and joints (visceral and articular gout).",
            False,
            TOPIC
        )
    ]

