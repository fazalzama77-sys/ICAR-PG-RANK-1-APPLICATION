# scripts/micro2_mod5.py
# Module 5: Veterinary Immunology & Vaccinology (50 questions)

TOPIC = "Veterinary Immunology & Vaccinology"

def get_module5_questions():
    return [
        (
            "In calves, lambs, and piglets, the continuous 'Ileal Peyer's Patch' (unlike the discrete jejunal Peyer's patches) functions during fetal and early neonatal life as a:",
            [
                "Primary lymphoid organ for antigen-independent B-cell repertoire diversification prior to involution",
                "Secondary lymphoid organ dedicated exclusively to CD8+ cytotoxic T-cell memory maintenance",
                "Purely endocrine organ secreting thymosin and erythropoietin into portal blood",
                "Filtration bed for senescent erythrocytes and intravascular hemosiderin storage"
            ],
            0,
            "In ruminants, swine, and dogs (the 'GALT species'), the large continuous Ileal Peyer's Patch develops prenatally without exogenous antigen, mediates primary B-cell diversification (via somatic hypermutation/gene conversion), and involutes by sexual maturity—functioning as a primary lymphoid organ analogous to the avian Bursa of Fabricius.",
            True,
            TOPIC
        ),
        (
            "In comparative veterinary anatomy and immunology, lymph nodes of SWINE (as well as hippopotamuses and dolphins) are structurally unique among domestic mammals because they are:",
            [
                "Completely absent and replaced by nucleated thrombocytes in the spleen",
                "Anatomically 'inverted' (cortical lymphoid follicles are central and medulla is peripheral, with lymphocytes exiting directly into venules)",
                "Filled with circulating red blood cells instead of lymph fluid ('hemal nodes')",
                "Located exclusively inside the lumen of the appendix and cecal tonsils"
            ],
            1,
            "Porcine lymph nodes have an 'inverted' microarchitecture: afferent lymphatics enter at the hilus-like capsule to deliver antigen to centrally located cortical B-cell follicles, while the medulla is on the outer periphery. Furthermore, recirculating porcine lymphocytes exit the lymph node directly into post-capillary High Endothelial Venules (HEVs) into the blood rather than via efferent lymphatics.",
            True,
            TOPIC
        ),
        (
            "In poultry immunology, which paraocular secondary lymphoid gland—located behind the third eyelid within the orbit and densely populated with IgA- and IgG (IgY)-secreting plasma cells—is the primary site of local mucosal immunity following eye-drop vaccination against Newcastle Disease or Infectious Bronchitis?",
            [
                "The Cloacal Bursa of Fabricius",
                "Meckel's diverticulum of the jejunum",
                "The Harderian gland (Gland of Harder)",
                "The Pineal gland of the epithalamus"
            ],
            2,
            "The Harderian gland is the dominant paraocular lymphoid organ in birds, located ventromedial to the eyeball. It contains massive accumulations of B-lineage plasma cells and T cells that mount rapid local secretory IgA and IgY responses across the conjunctiva and upper respiratory tract after eye-drop or spray vaccination.",
            True,
            TOPIC
        ),
        (
            "In avian B-lymphocyte development inside the Bursa of Fabricius, unlike humans and mice (which generate antibody diversity primarily through combinatorial V-D-J joining of hundreds of V segments), chickens possess only a single functional V and J segment and generate their entire primary antibody repertoire via:",
            [
                "Alternative mRNA splicing of twenty constant-region exons",
                "Horizontal transfer of maternal immunoglobulin mRNA from egg albumen",
                "Cytoplasmic reverse transcription of endogenous retroviral LTRs",
                "Somatic 'Gene Conversion' (unidirectional transfer of sequence blocks from upstream V-pseudogenes into the single rearranged V-J gene)"
            ],
            3,
            "Chickens (as well as rabbits and cattle to a degree) rearrange only a single functional VH1 and VL1 gene segment; inside the Bursa of Fabricius, Activation-Induced Cytidine Deaminase (AID) drives somatic Gene Conversion, copying hypervariable stretches from an upstream array of non-functional V-pseudogenes into the rearranged V gene.",
            True,
            TOPIC
        ),
        (
            "In the innate immune system, Pattern Recognition Receptors (PRRs) of the Toll-Like Receptor (TLR) family recognize conserved microbial PAMPs. Which pairing of Toll-Like Receptor and its specific microbial ligand is CORRECT?",
            [
                "TLR4: Gram-negative LPS; TLR5: Flagellin; TLR3: viral dsRNA; TLR9: unmethylated CpG DNA",
                "TLR4: viral dsRNA; TLR5: CpG DNA; TLR3: bacterial Flagellin; TLR9: Gram-negative LPS",
                "TLR2: viral ssRNA; TLR3: Lipoteichoic acid; TLR4: Flagellin; TLR5: Peptidoglycan",
                "TLR1: Chitin; TLR4: Mycolic acid; TLR7: Dipicolinic acid; TLR9: Ergosterol"
            ],
            0,
            "Canonical TLR specificity: TLR4 (with MD-2 and CD14) senses Gram-negative Lipopolysaccharide (Lipid A); TLR5 senses bacterial Flagellin; TLR2 (heterodimerized with TLR1 or TLR6) senses lipopeptides, peptidoglycan, and lipoteichoic acid; endosomal TLR3 senses viral dsRNA; TLR7/8 sense viral ssRNA; and endosomal TLR9 senses unmethylated CpG DNA.",
            True,
            TOPIC
        ),
        (
            "While Toll-Like Receptors scan the cell surface and endosomes, which cytosolic Nucleotide-binding Oligomerization Domain (NOD)-like receptor specifically senses 'Muramyl Dipeptide' (MDP)—the minimal bioactive peptidoglycan motif found in both Gram-positive and Gram-negative bacteria and Freund's Complete Adjuvant?",
            [
                "RIG-I (Retinoic acid-inducible gene I)",
                "NOD2 (Caspase recruitment domain-containing protein 15)",
                "cGAS (Cyclic GMP-AMP synthase)",
                "MDA5 (Melanoma differentiation-associated protein 5)"
            ],
            1,
            "NOD1 senses gamma-D-glutamyl-meso-diaminopimelic acid (iE-DAP, specific to Gram-negative peptidoglycan), whereas NOD2 is a general cytosolic sensor of Muramyl Dipeptide (MurNAc-L-Ala-D-isoGln, MDP), conserved in all bacterial peptidoglycans and the active immunostimulatory motif of mycobacteria in FCA.",
            True,
            TOPIC
        ),
        (
            "During the oxygen-dependent 'Respiratory Burst' inside the phagolysosome of activated neutrophils, which enzyme complex first reduces molecular oxygen (O2) to superoxide anion (O2.-), and which granule enzyme then uses hydrogen peroxide (H2O2) and chloride ions (Cl-) to generate potent bactericidal Hypochlorous Acid (HOCl)?",
            [
                "Catalase generates superoxide; Lysozyme generates hypochlorous acid",
                "Cytochrome c oxidase generates superoxide; Inducible nitric oxide synthase (iNOS) generates HOCl",
                "NADPH oxidase (Phox) generates superoxide; Myeloperoxidase (MPO) generates hypochlorous acid",
                "Xanthine oxidase generates superoxide; Lactoferrin generates hypochlorous acid"
            ],
            2,
            "Upon phagocytosis, the membrane-bound NADPH oxidase complex (gp91phox/p22phox + p47/p67/Rac) transfers electrons from NADPH to O2, forming superoxide (O2.-), which dismutates to H2O2. Azurophilic granule Myeloperoxidase (MPO) then catalyzes H2O2 + Cl- + H+ -> HOCl (hypochlorous acid/bleach) + H2O.",
            True,
            TOPIC
        ),
        (
            "According to Klas Kärre's 'Missing-Self Hypothesis', how do Natural Killer (NK) cells selectively spare healthy host cells while lysing virus-infected cells (such as herpesvirus-infected cells) and tumor cells?",
            [
                "NK cells require prior immunization and recognize viral peptides bound to MHC Class II",
                "NK cells express rearranged T-cell receptor alpha-beta chains that bind free viral capsids",
                "NK cells phagocytose only bacteria coated with IgE and eosinophil major basic protein",
                "NK cells express inhibitory receptors that engage self MHC Class I on normal cells; when viruses or tumors downregulate MHC Class I ('missing self'), inhibition is lost and activating receptors trigger Perforin/Granzyme lysis"
            ],
            3,
            "NK cells integrate signals from activating receptors (recognizing stress ligands like MICA/ULBPs or IgG Fc via CD16) and dominant inhibitory receptors (KIRs, Ly49, CD94/NKG2A) that bind normal self MHC Class I. When viruses evade CD8+ T cells by downregulating MHC Class I, they remove the inhibitory brake on NK cells, triggering exocytosis of Perforin and Granzyme B.",
            True,
            TOPIC
        ),
        (
            "Differentiation of naive CD4+ T-helper lymphocytes into specialized effector lineages (Th1, Th2, Th17, and regulatory Treg cells) is governed by lineage-defining 'Master Transcription Factors'. Which pairing of T-helper subset and its master transcription factor is CORRECT?",
            [
                "Th1: T-bet; Th2: GATA-3; Th17: ROR-gamma-t (RORgt); Treg: FoxP3",
                "Th1: GATA-3; Th2: T-bet; Th17: FoxP3; Treg: ROR-gamma-t",
                "Th1: FoxP3; Th2: ROR-gamma-t; Th17: STAT1; Treg: GATA-3",
                "Th1: Bcl-6; Th2: NFAT; Th17: c-Myc; Treg: p53"
            ],
            0,
            "Lineage-defining master transcription factors of CD4+ T cells: Th1 (induced by IL-12/IFN-gamma) expresses T-bet; Th2 (induced by IL-4) expresses GATA-3; Th17 (induced by TGF-beta + IL-6/IL-23) expresses RORgt; Follicular helper Tfh expresses Bcl-6; and Regulatory T cells (Treg, CD4+CD25+) express FoxP3.",
            True,
            TOPIC
        ),
        (
            "In mucosal immunology and helminth infections, which cytokine—secreted by Th2 lymphocytes and Group 2 Innate Lymphoid Cells (ILC2s)—serves as the principal hematopoietin driving bone marrow differentiation, activation, and survival of Eosinophils, and which cytokine drives B-cell class switching to mucosal IgA?",
            [
                "Interleukin-2 drives eosinophils; Interferon-gamma drives IgA class switching",
                "Interleukin-5 (IL-5) drives eosinophil production/activation; Transforming Growth Factor-beta (TGF-beta, assisted by IL-5) drives IgA class switching",
                "Interleukin-12 drives eosinophils; Tumor Necrosis Factor-alpha drives IgA class switching",
                "Interleukin-17 drives eosinophils; Interleukin-1 beta drives IgA class switching"
            ],
            1,
            "Interleukin-5 (IL-5) is the master eosinophilopoietin responsible for peripheral blood and tissue eosinophilia in parasitic infections and allergies. In Peyer's patches and mucosal lymphoid tissues, Transforming Growth Factor-beta (TGF-beta) induces B-cell heavy-chain class switching to IgA, while IL-5 and IL-6 promote terminal differentiation into IgA-secreting plasma cells.",
            True,
            TOPIC
        ),
        (
            "In the endogenous MHC Class I antigen presentation pathway, after cytosolic viral proteins are degraded into 8-to-10-amino-acid peptides by the immunoproteasome, how are these peptides translocated across the membrane of the Rough Endoplasmic Reticulum (RER) to load onto MHC Class I molecules?",
            [
                "Via passive diffusion through outer membrane OmpF porin channels",
                "By binding to the Invariant chain (CD74) and endosomal sorting via clathrin pits",
                "By active ATP-dependent transport through the heterodimeric TAP (Transporter Associated with Antigen Processing: TAP1/TAP2) complex",
                "By exocytosis into the extracellular fluid followed by pinocytosis into the Golgi apparatus"
            ],
            2,
            "Peptides generated in the cytosol by the 26S immunoproteasome (LMP2/LMP7) are actively pumped into the lumen of the Rough Endoplasmic Reticulum by the ATP-binding cassette (ABC) heterodimer TAP (TAP1 + TAP2), where tapasin, calreticulin, and ERp57 load them into the MHC Class I alpha-chain + beta-2-microglobulin groove.",
            True,
            TOPIC
        ),
        (
            "In the exogenous MHC Class II antigen presentation pathway, why do newly synthesized MHC Class II alpha-beta heterodimers inside the Rough Endoplasmic Reticulum NOT accidentally bind endogenous cytosolic peptides present in the ER?",
            [
                "MHC Class II molecules are synthesized exclusively inside lysosomes rather than the ER",
                "Endogenous peptides carry a positive charge that is repelled by MHC Class II",
                "MHC Class II molecules remain unfolded until secreted outside the plasma membrane",
                "The peptide-binding groove of MHC Class II in the ER is sterically blocked by the Invariant Chain (Ii / CD74), whose CLIP fragment is later removed in endolysosomes by HLA-DM (BoLA-DM)"
            ],
            3,
            "Inside the ER, trimers of the Invariant Chain (Ii / CD74) associate with nascent MHC Class II alpha-beta dimers, inserting the CLIP (Class II-associated Invariant chain Peptide) region directly into the peptide-binding groove to block endogenous peptide binding and guide the complex to acidified MIIC endolysosomes, where cathepsins cleave Ii and DM catalyzes exchange of CLIP for exogenous peptide.",
            True,
            TOPIC
        ),
        (
            "Which non-classical MHC Class I-like family of antigen-presenting molecules (associated with beta-2-microglobulin) possesses a deep hydrophobic binding groove specialized for presenting microbial LIPID and GLYCOLIPID antigens (such as mycobacterial mycolic acids and lipoarabinomannan) to T cells and iNKT cells?",
            [
                "CD1 molecules (CD1a, CD1b, CD1c, CD1d)",
                "CD28 costimulatory homodimers",
                "FcRn (Neonatal Fc receptors)",
                "TAP1/TAP2 peptide transporters"
            ],
            0,
            "Whereas classical MHC Class I and Class II molecules present linear peptide antigens, the non-polymorphic CD1 family of glycoproteins features a deep, non-polar hydrophobic pocket that binds the fatty acyl chains of mycobacterial lipids (mycolic acids, glucose monomycolate, lipoarabinomannan), presenting their hydrophilic headgroups to T cells and invariant NKT (iNKT) cells.",
            True,
            TOPIC
        ),
        (
            "In comparative veterinary immunology, young ruminants (calves, lambs, kids) and young pigs are classified as 'Gamma-Delta (gd) T-cell High' species (in contrast to 'gd-Low' humans, mice, and dogs) because in young calves and piglets:",
            [
                "Alpha-beta T cells are completely absent due to physiological thymic aplasia",
                "Gamma-delta (gd) T lymphocytes (expressing the scavenger receptor WC1) constitute 30% to 60% of circulating peripheral blood T cells",
                "Gamma-delta T cells secrete all circulating serum IgG1 and IgM antibodies",
                "Gamma-delta T cells are restricted exclusively to the brain and never enter blood"
            ],
            1,
            "In humans, mice, and dogs, gamma-delta (gd) T cells account for <5% of peripheral blood lymphocytes. In contrast, ruminants (cattle, sheep, goats), pigs, and chickens are 'gd-high' species where gd T cells (many expressing the Workshop Cluster 1 [WC1] transmembrane scavenger receptor) comprise 30–60% of circulating T cells in young animals, acting as rapid MHC-unrestricted sentinels at mucosae.",
            True,
            TOPIC
        ),
        (
            "According to the Two-Signal Model of naive T-lymphocyte activation, what happens if a naive T cell receives Signal 1 (TCR-CD3 binding to peptide-MHC on an APC) in the COMPLETE ABSENCE of Signal 2 (costimulatory binding of T-cell CD28 to CD80/CD86 [B7-1/B7-2] on the APC)?",
            [
                "The T cell immediately differentiates into a long-lived memory plasma cell",
                "The T cell undergoes rapid polyclonal proliferation and secretes massive amounts of IL-2",
                "The T cell enters a state of prolonged antigen-specific functional unresponsiveness termed 'Clonal Anergy' (or undergoes apoptosis)",
                "The T cell switches its TCR from alpha-beta to gamma-delta and lyses the APC"
            ],
            2,
            "Signal 1 (TCR-CD3 + CD4/CD8 engaging peptide-MHC) provides antigen specificity, while Signal 2 (CD28 engaging B7.1 [CD80] / B7.2 [CD86] induced on PRR-activated professional APCs) is mandatory to stabilize IL-2 mRNA and drive proliferation. Receiving Signal 1 alone without Signal 2 induces peripheral tolerance via Clonal Anergy.",
            True,
            TOPIC
        ),
        (
            "Bacterial 'Superantigens' (such as Staphylococcus aureus Enterotoxins A–E, Toxic Shock Syndrome Toxin-1 [TSST-1], and Streptococcus pyogenes SpeA) trigger a massive, life-threatening cytokine storm (TNF-alpha, IL-1, IL-2, IFN-gamma) by:",
            [
                "Being endocytosed, cleaved into 9-mer peptides, and presented by MHC Class I to 0.001% of CD8+ T cells",
                "Binding directly to Toll-like receptor 4 and CD14 on polymorphonuclear neutrophils",
                "Cleaving the Fc region of secretory IgA and activating the alternative complement pathway",
                "Binding intact (without intracellular processing) outside the peptide-binding groove to cross-link the conserved V-beta (Vb) domain of the TCR to the alpha-chain of MHC Class II, polyclonally activating up to 20% of all T cells"
            ],
            3,
            "Conventional peptide antigens sit inside the MHC groove and activate only ~0.0001–0.001% of T cells bearing a matching CDR3. Superantigens are intact proteins that clamp onto the outside lateral surfaces of MHC Class II and specific V-beta families of the TCR, non-specifically activating 5–20% of the entire T-cell repertoire simultaneously.",
            True,
            TOPIC
        ),
        (
            "In classical immunochemistry implemented by Rodney Porter and Alfred Nisonoff, how does proteolytic digestion of an intact IgG molecule with 'Papain' differ from digestion with 'Pepsin'?",
            [
                "Papain cleaves above the hinge disulfide bonds to yield two monovalent Fab fragments and one intact Fc fragment; Pepsin cleaves below the hinge disulfide bonds to yield one divalent F(ab')2 fragment and degraded Fc peptides",
                "Papain yields a single divalent F(ab')2 fragment; Pepsin yields two monovalent Fab fragments and an intact Fc",
                "Papain cleaves only the interchain disulfide bonds to separate intact heavy chains from light chains",
                "Pepsin leaves the Fc complement-binding domain completely intact while destroying both antigen-binding sites"
            ],
            0,
            "Papain cleaves the IgG heavy chain on the N-terminal side (above) of the hinge inter-heavy-chain disulfide bridge, producing two separate monovalent Fab fragments (which bind antigen but cannot precipitate/agglutinate) and one crystalline Fc fragment. Pepsin cleaves on the C-terminal side (below) of the hinge disulfide bonds, keeping the two Fab arms linked as a divalent F(ab')2 fragment (used in commercial equine tetanus/snake antivenoms to neutralize toxin without causing Fc-mediated serum sickness).",
            True,
            TOPIC
        ),
        (
            "In immunoglobulin genetics and serology, what is the precise distinction between an 'Isotype', an 'Allotype', and an 'Idiotype'?",
            [
                "Isotype is an individual's unique paratope; Allotype is the heavy chain class; Idiotype is an allelic polymorphism",
                "Isotypes are constant-region classes/subclasses shared by all members of a species; Allotypes are intraspecies allelic variations in constant regions; Idiotypes are unique variable-region (VH/VL CDR) antigenic determinants of a specific antibody clone",
                "Isotypes occur only in IgM; Allotypes occur only in IgA; Idiotypes occur only in IgE",
                "Isotypes are encoded by RAG-1; Allotypes are generated by somatic hypermutation; Idiotypes are located on the Fc tail"
            ],
            1,
            "Isotypes (e.g., IgG1, IgG2, IgM, IgA, IgE) are defined by constant-region genes present in the genome of every normal member of a species. Allotypes are minor amino acid differences in constant regions encoded by different alleles among individuals of the same species. Idiotypes are the unique antigenic determinants (idiotopes) formed by the hypervariable complementarity-determining regions (CDRs) of a single B-cell clone's V domains.",
            True,
            TOPIC
        ),
        (
            "Avian 'Immunoglobulin Y' (IgY)—the major systemic and egg-yolk antibody of chickens, ducks, and reptiles—differs structurally from mammalian IgG in that avian IgY:",
            [
                "Is a pentamer of five four-chain units joined by a J-chain and restricted to bile",
                "Contains only heavy chains without any light chains and has a molecular weight of 45 kDa",
                "Possesses four heavy-chain constant domains (Cupsilon1–4), lacks a flexible genetic hinge region, and does NOT bind Staphylococcal Protein A or mammalian Fc receptors",
                "Consists of two heavy chains and four kappa light chains linked by secretory component"
            ],
            2,
            "Avian IgY (~180 kDa, compared to ~150 kDa for mammalian IgG) has a longer heavy chain containing four constant domains (Cv1–Cv4, evolutionary ancestor of both mammalian IgG and IgE) instead of three, lacks a flexible hinge region, is selectively pumped into egg yolk, and does NOT bind Staphylococcal Protein A, Streptococcal Protein G, or mammalian rheumatoid factor/Fc receptors.",
            True,
            TOPIC
        ),
        (
            "Camelids (dromedary and Bactrian camels, llamas, alpacas) and cartilaginous sharks naturally synthesize unique functional IgG subclasses (IgG2 and IgG3 in camelids) that are prized in biotechnology for generating 'Nanobodies' (VHH) because these antibodies:",
            [
                "Contain four light chains and no heavy chains",
                "Are composed entirely of alpha-helical mucopolysaccharides rather than polypeptides",
                "Can replicate autonomously inside bacterial cells like plasmids",
                "Are 'Heavy-Chain-Only Antibodies' (HcAbs) completely devoid of light chains and lacking the CH1 domain, binding antigen via a single compact 15-kDa VHH variable domain"
            ],
            3,
            "In camelids, up to 50–75% of serum IgG consists of homodimeric Heavy-Chain-Only Antibodies (HcAbs, IgG2 and IgG3) that lack light chains and splice out the CH1 domain. Their single-domain variable head (VHH or 'Nanobody', ~12–15 kDa) is extraordinarily heat- and acid-stable and projects a long finger-like CDR3 loop capable of reaching cryptic catalytic clefts of viral enzymes and toxins.",
            True,
            TOPIC
        ),
        (
            "In equine immunology, horses hyperimmunized to produce commercial Tetanus Antitoxin or snake antivenom synthesize large quantities of a specialized, heavily glycosylated IgG subclass historically designated 'IgG(T)' (modern IgG3 and IgG5), which is notable because it:",
            [
                "Strongly flocculates and neutralizes soluble toxins, but fails to fix complement by the classical pathway (and competitively inhibits complement fixation by IgG1/IgG4)",
                "Crosses the equine epitheliochorial placenta in utero during the first trimester",
                "Binds exclusively to mast cells to cause immediate anaphylactic shock",
                "Exists as a decamer in nasal secretions and cannot enter the bloodstream"
            ],
            0,
            "Equine IgG(T) (comprising IgG3 and IgG5 among the 7 equine IgG subclasses encoded on chromosome 24) is the predominant antibody formed in horses hyperimmunized with protein toxoids. It forms characteristic sharp flocculation zones with toxin (Ramon flocculation) and neutralizes tetanus/diphtheria toxins with high avidity, but does not activate classical complement (explaining negative CFT results in hyperimmunized horses).",
            True,
            TOPIC
        ),
        (
            "How does the anatomical structure of the placenta in dogs and cats ('Endotheliochorial' placenta, 4 tissue layers) compare with that of horses, pigs, and ruminants ('Epitheliochorial / Synepitheliochorial' placenta, 6 tissue layers) regarding transplacental transfer of maternal IgG in utero?",
            [
                "Dogs and cats transfer 100% of maternal IgG in utero and require no colostrum, whereas calves and foals transfer 50% in utero",
                "Dogs and cats transfer ~5% to 10% of maternal IgG transplacentally in utero (with 90% via colostrum), whereas foals, piglets, calves, and lambs receive 0% in utero (100% dependent on colostrum)",
                "Both dogs/cats and horses/cattle have hemochorial placentas that transfer 100% of IgM in utero",
                "Foals and piglets receive 80% of maternal IgA in utero, whereas puppies receive only IgE"
            ],
            1,
            "Primates and rodents have a 3-layer Hemochorial placenta (~100% in utero IgG transfer via FcRn). Dogs and cats have a 4-layer Endotheliochorial placenta allowing limited (5–10%) in utero IgG transfer, with 90–95% acquired via colostrum. Horses and pigs (Epitheliochorial, 6 layers) and ruminants (Synepitheliochorial) transfer ZERO (0%) immunoglobulins in utero, making neonates agammaglobulinemic at birth until they ingest colostrum.",
            True,
            TOPIC
        ),
        (
            "In a 24-to-48-hour-old neonatal thoroughbred foal or dairy calf, which rapid stall-side / farm-side blood tests are routinely used to screen for 'Failure of Passive Transfer' (FPT), and what serum IgG threshold defines adequate passive transfer in foals?",
            [
                "Rose Bengal Plate Test and Coombs Test; >50 mg/dL IgG is adequate in foals",
                "Coggins AGID Test and Mallein Test; >100 mg/dL IgG is adequate in foals",
                "Zinc Sulfate Turbidity, Sodium Sulfite Precipitation, Glutaraldehyde Coagulation, Refractometry, and SNAP Foal IgG ELISA; >800 mg/dL IgG is adequate in foals (<400 mg/dL is severe FPT)",
                "Weil-Felix Test and Nagler Reaction; >5,000 mg/dL IgG is required in foals"
            ],
            2,
            "In neonatal foals at 18–24 hours of age, serum IgG > 800 mg/dL (8 g/L) indicates adequate passive transfer, 400–800 mg/dL indicates partial FPT, and < 400 mg/dL indicates complete/severe FPT (in calves, serum IgG >= 1,000 mg/dL or serum total protein >= 5.2–5.5 g/dL by refractometer indicates adequacy). Field screening uses Zinc Sulfate turbidity, Sodium Sulfite precipitation, Glutaraldehyde coagulation, or SNAP Foal IgG.",
            True,
            TOPIC
        ),
        (
            "How is the 'Lectin Pathway' of the complement cascade initiated on the surface of invading bacteria and fungi in the absence of specific antibodies?",
            [
                "Binding of C1q to the Fc CH2 domain of aggregated IgG1 molecules",
                "Spontaneous tick-over hydrolysis of C3 into C3(H2O) and binding of Factor B and Properdin",
                "Direct cleavage of C5 by bacterial coagulase and plasminogen",
                "Binding of serum Mannose-Binding Lectin (MBL) or ficolins to microbial surface mannose/N-acetylglucosamine carbohydrates, activating MASP-1 and MASP-2 to cleave C4 and C2"
            ],
            3,
            "The Lectin pathway is an antibody-independent innate cascade initiated when plasma Mannose-Binding Lectin (MBL, an acute-phase collectin structurally homologous to C1q) or ficolins bind terminal mannose, fucose, or GlcNAc residues on microbial surfaces. Associated serine proteases MASP-1 and MASP-2 (homologs of C1r and C1s) then cleave C4 and C2 to assemble the C4b2a C3 convertase.",
            True,
            TOPIC
        ),
        (
            "Which GPI-anchored host cell membrane complement regulatory protein ('Protectin') protects normal autologous erythrocytes and endothelial cells from accidental bystander osmotic lysis by binding to C5b-8 and blocking the polymerization of C9 into the Membrane Attack Complex (MAC)?",
            [
                "CD59 (Protectin / Membrane Inhibitor of Reactive Lysis, MIRL), alongside CD55 (Decay-Accelerating Factor, DAF)",
                "CD4 (T-helper MHC Class II co-receptor)",
                "CD14 (GPI-anchored lipopolysaccharide co-receptor)",
                "CD79a (B-cell receptor ITAM signaling subunit)"
            ],
            0,
            "Host cells shield themselves from homologous complement attack using membrane-bound regulators: CD55 (Decay-Accelerating Factor, DAF) accelerates the dissociation of C3 convertases (C4b2a and C3bBb), while CD59 (Protectin) binds C8 in the C5b-8 complex and physically prevents the insertion and unfolding of multiple C9 molecules to form the lytic MAC pore.",
            False,
            TOPIC
        ),
        (
            "'Bovine Leukocyte Adhesion Deficiency' (BLAD) is a lethal autosomal recessive primary immunodeficiency of Holstein-Friesian calves characterized by recurrent mucosal bacterial infections, ulcerative stomatitis/gingivitis, delayed wound healing with COMPLETE ABSENCE of extravascular pus, and extreme persistent blood neutrophilia (>40,000–100,000/uL). It is caused by a point mutation (D128G) in the gene encoding:",
            [
                "The DNA-dependent protein kinase catalytic subunit (DNA-PKcs) required for V(D)J recombination",
                "The CD18 (beta-2 integrin) subunit of LFA-1 and Mac-1 on leukocytes, preventing firm adhesion to endothelial ICAM-1 and transendothelial migration (diapedesis)",
                "The NADPH oxidase gp91phox subunit required for the respiratory burst",
                "The neonatal Fc receptor (FcRn) in mammary alveolar epithelium"
            ],
            1,
            "BLAD in Holstein cattle (and Canine Leukocyte Adhesion Deficiency [CLAD] in Irish Setters) is caused by a deficiency of the beta-2 integrin subunit CD18 (ITGB2). Without functional beta-2 integrins (LFA-1 [CD11a/CD18] and Mac-1 [CD11b/CD18]), rolling blood neutrophils cannot arrest firmly on vascular endothelial ICAM-1 or extravasate into infected tissues, remaining trapped in the bloodstream (massive neutrophilia with no tissue pus).",
            True,
            TOPIC
        ),
        (
            "'Chédiak-Higashi Syndrome'—an autosomal recessive disorder documented in Aleutian-coat mink, Blue Smoke Persian cats, Hereford/Brangus cattle, and killer whales—is caused by a mutation in the LYST (lysosomal trafficking regulator) gene and is clinically recognized by which diagnostic triad?",
            [
                "Complete absence of T and B lymphocytes, thymic aplasia, and agammaglobulinemia",
                "Hyper-IgE eczema, eosinophilia, and asthma",
                "Partial oculocutaneous albinism (diluted coat color and pale irides from giant melanosomes), increased susceptibility to pyogenic infections (giant fused neutrophil azurophilic granules with defective chemotaxis/killing), and a platelet storage-pool bleeding tendency",
                "Autoimmune hemolytic anemia, thrombocytopenia, and systemic lupus nephritis"
            ],
            2,
            "In Chédiak-Higashi Syndrome, defective regulation of lysosomal membrane fusion (LYST protein) causes melanosomes to fuse into giant macromelanosomes (diluting coat pigment to 'Aleutian blue' in mink or 'smoke blue' in Persian cats), neutrophil granules to fuse into giant Dohle-like peroxidase-positive inclusions on blood smears (impairing phagolysosome function), and platelet dense granules to fail (prolonged bleeding time).",
            True,
            TOPIC
        ),
        (
            "'Lethal Acrodermatitis' in Bull Terrier dogs and 'Trait A46' (Hereditary Parakeratosis / Adema Disease) in Black Pied Friesian calves are autosomal recessive primary T-cell immunodeficiencies (characterized by severe thymic hypoplasia, parakeratotic crusting of the muzzle/footpads, and fatal bronchopneumonia) associated with defective metabolism/absorption of which essential trace mineral?",
            [
                "Selenium",
                "Cobalt",
                "Molybdenum",
                "Zinc (required as an essential cofactor for the thymic hormone Thymulin)"
            ],
            3,
            "Trait A46 in Friesian cattle (caused by a mutation in the intestinal zinc transporter ZIP4 / SLC39A4, completely reversible by high-dose oral zinc supplementation) and Lethal Acrodermatitis in Bull Terriers (MKL1 mutation) demonstrate the critical dependence of T-cell maturation and the nonapeptide thymic hormone Thymulin (formerly Facteur Thymique Sérique, FTS) on Zinc.",
            True,
            TOPIC
        ),
        (
            "In horses stabled indoors and fed poorly cured, dusty hay, 'Recurrent Airway Obstruction' (RAO / 'Heaves' / Severe Equine Asthma) is triggered by inhalation of spores from thermophilic actinomycetes (Saccharopolyspora rectivirgula) and Aspergillus fumigatus, representing a pulmonary hypersensitivity driven by:",
            [
                "Combined Type I (IgE-mediated bronchospasm) and Type III / Th17-mediated immune-complex neutrophilic bronchiolitis (occurring 4–8 hours post-exposure)",
                "Purely Type II cytotoxic autoantibodies directed against alveolar Type IV collagen (Goodpasture syndrome)",
                "Purely CD8+ cytotoxic T-lymphocyte lysis of tracheal cartilage rings",
                "Immediate complement-mediated intravascular hemolysis in pulmonary arteries"
            ],
            0,
            "Equine 'Heaves' (Recurrent Airway Obstruction / Barn-Associated Equine Asthma) is an environmental hypersensitivity to inhaled mold spores (Aspergillus fumigatus, Saccharopolyspora [Faenia] rectivirgula, Thermoactinomyces vulgaris) combining immediate Type I mast-cell bronchoconstriction with a dominant Type III (Arthus-like immune complex) and Th17/IL-8-driven influx of neutrophils into small bronchioles 4–8 hours after feeding dusty hay.",
            True,
            TOPIC
        ),
        (
            "'Queensland Itch' ('Sweet Itch' / Equine Insect Bite Hypersensitivity)—a recurrent seasonal pruritic dermatitis affecting the mane, withers, and tail base of horses during warm months—is mediated primarily by:",
            [
                "IgM cold agglutinins precipitating in cutaneous capillaries",
                "Type I (IgE-mediated mast cell/eosinophil activation) and Type IV (delayed cell-mediated) hypersensitivity to salivary antigens of Culicoides biting midges",
                "Type III immune-complex deposition induced by Onchocerca cervicalis microfilariae alone",
                "Autoantibodies against epidermal hemidesmosomes triggered by ultraviolet sunlight"
            ],
            1,
            "Equine Insect Bite Hypersensitivity ('Sweet Itch' / 'Queensland Itch' / 'Kasen') is the most common allergic skin disease of horses worldwide, caused by a combined Type I (immediate IgE/histamine/IL-5 eosinophilic) and Type IV (late-phase Th2/cell-mediated) hypersensitivity to salivary gland proteins injected by biting midges of the genus Culicoides.",
            True,
            TOPIC
        ),
        (
            "In veterinary immunodermatology, how does 'Pemphigus Foliaceus' (the most common autoimmune skin disease of dogs, cats, and horses, characterized by superficial pustules, crusts, and rounded 'acantholytic keratinocytes' on cytology) differ in its target autoantigen from 'Bullous Pemphigoid'?",
            [
                "Pemphigus foliaceus targets nuclear double-stranded DNA; Bullous pemphigoid targets cytoplasmic ribosomes",
                "Pemphigus foliaceus targets vascular endothelial cadherin; Bullous pemphigoid targets hair follicle melanin",
                "Pemphigus foliaceus autoantibodies target 'Desmosomes' (Desmoglein-1 / Desmocollin-1) between keratinocytes causing intraepidermal acantholysis; Bullous pemphigoid autoantibodies target 'Hemidesmosomes' (Collagen XVII / BP180) at the dermo-epidermal basement membrane",
                "Pemphigus foliaceus is a Type IV T-cell reaction; Bullous pemphigoid is a Type I IgE reaction"
            ],
            2,
            "Both are Type II antibody-mediated autoimmune dermatoses, but Pemphigus foliaceus (and Pemphigus vulgaris) targets intercellular desmosomal cadherins (Desmoglein-1 in P. foliaceus; Desmoglein-3 in P. vulgaris), breaking keratinocyte-to-keratinocyte adhesion (acantholysis) and releasing rounded 'acantholytic cells'. Bullous pemphigoid targets hemidesmosomal Type XVII collagen (BP180) anchoring basal keratinocytes to the basement membrane, causing subepidermal clefting without acantholysis.",
            True,
            TOPIC
        ),
        (
            "'Masticatory Muscle Myositis' (MMM) is an inflammatory autoimmune myopathy in dogs characterized by painful swelling followed by severe atrophy of the temporalis, masseter, and pterygoid muscles (causing 'trismus' / inability to open the jaw) while completely sparing the limb muscles. Why are ONLY the jaw muscles attacked?",
            [
                "The jaw muscles are uniquely innervated by sympathetic fibers expressing rabies receptors",
                "Limb muscles lack MHC Class I molecules and cannot be recognized by the immune system",
                "The autoimmune response is triggered by local tooth root abscesses that never enter systemic blood",
                "Canine masticatory muscles (derived from the first pharyngeal arch) uniquely express 'Type 2M Myosin Heavy Chain' fibers, and diagnostic autoantibodies specifically target only Type 2M fibers ( absent in limb muscles)"
            ],
            3,
            "Unlike limb and trunk skeletal muscles (which contain Type 1 and Type 2A/2X myosin fibers), carnivore muscles of mastication (masseter, temporalis, pterygoids, tensor tympani) uniquely contain 'Type 2M' myosin heavy chain isoforms and masticatory myosin binding protein-C. The definitive 2M-antibody ELISA detects circulating autoantibodies specific for Type 2M fibers.",
            True,
            TOPIC
        ),
        (
            "Saponin adjuvants—such as 'Quil-A' and its purified fraction 'QS-21', which also assemble with cholesterol and phospholipids into cage-like 40-nm 'Immune Stimulating Complexes' (ISCOMs)—are extracted from the bark of which tree and possess what key immunological advantage over alum adjuvants?",
            [
                "Extracted from the South American soapbark tree (Quillaja saponaria); they stimulate strong Th1 cell-mediated immunity and CD8+ cytotoxic T-lymphocyte (CTL) responses via antigen cross-presentation in addition to high antibody titers",
                "Extracted from the neem tree (Azadirachta indica); they induce exclusively mucosal IgE without any IgG response",
                "Extracted from Mycobacterium bovis cell walls; they cause permanent tuberculin skin test conversion",
                "Extracted from the rubber tree (Hevea brasiliensis); they act solely by forming a non-biodegradable mineral depot"
            ],
            0,
            "Quil-A and QS-21 are triterpenoid saponin glycosides purified from the bark of Quillaja saponaria. Whereas aluminum salts (alum) induce primarily a Th2/humoral antibody response and poor CD8+ CTL immunity, saponins and ISCOMs destabilize endosomal membranes in dendritic cells, routing exogenous vaccine antigens into the cytosolic MHC Class I cross-presentation pathway to prime potent CD8+ CTLs and Th1 (IFN-gamma/IgG2a) immunity.",
            True,
            TOPIC
        ),
        (
            "Commercial inactivated Foot and Mouth Disease (FMD) and Hemorrhagic Septicemia (HS) vaccines frequently utilize 'Montanide ISA 206', which is formulated as a 'Water-in-Oil-in-Water' (W/O/W) double emulsion. What is the practical and immunological rationale for using a W/O/W double emulsion over a classical Freund-type Water-in-Oil (W/O) single emulsion?",
            [
                "It eliminates all oil from the vaccine so it can be administered via drinking water",
                "Because the continuous external phase is aqueous (water), it has low viscosity (easy syringeability and minimal local injection-site granulomas) while still providing biphasic rapid priming (outer water phase) and prolonged slow-release depot immunity (inner oil droplets)",
                "It allows live bacterial spores to germinate inside the syringe prior to injection",
                "It selectively destroys non-structural 3ABC proteins during storage at room temperature"
            ],
            1,
            "Classical Water-in-Oil (W/O) emulsions have oil as the continuous external phase, making them extremely viscous, difficult to inject in cold weather, and prone to causing sterile abscesses/granulomas at the injection site. In a Water-in-Oil-in-Water (W/O/W) emulsion like Montanide ISA 206, aqueous antigen droplets are trapped inside oil globules that are themselves suspended in an outer aqueous phase—yielding fluid, low-viscosity injectability plus both fast (outer phase) and slow-depot (inner phase) immune stimulation.",
            True,
            TOPIC
        ),
        (
            "What is the immunological principle behind 'Polysaccharide-Protein Conjugate Vaccines' (where a bacterial capsular polysaccharide is covalently linked to an immunogenic carrier protein such as tetanus toxoid or CRM197)?",
            [
                "The carrier protein acts as a protease that digests the bacterial capsule inside the bloodstream",
                "The polysaccharide converts the protein from a T-dependent antigen into a T-independent mitogen",
                "It converts a T-independent Type 2 (TI-2) polysaccharide antigen into a T-dependent antigen via 'linked recognition' (B cells specific for the polysaccharide internalize the conjugate and present carrier protein peptides on MHC Class II to CD4+ Tfh cells), inducing IgG class-switching, affinity maturation, and memory in young animals",
                "It allows the polysaccharide to be presented directly on MHC Class I molecules to CD8+ cytotoxic T cells"
            ],
            2,
            "Pure bacterial capsular polysaccharides are T-independent Type 2 (TI-2) antigens: they cross-link surface IgM on B cells without T-cell help, eliciting only low-affinity IgM, no germinal center memory, and poor responses in neonates. Covalently linking the polysaccharide (hapten-like) to a carrier protein allows polysaccharide-specific B cells to endocytose the complex and present carrier-derived peptides on MHC Class II to helper T cells ('hapten-carrier linked recognition').",
            True,
            TOPIC
        ),
        (
            "Recombinant 'Canarypox Virus' (ALVAC vector) is widely used in commercial veterinary vaccines for dogs, cats, and horses (e.g., against Canine Distemper, Rabies, Feline Leukemia, Equine Influenza, and West Nile Virus). How does a Canarypox-vectored vaccine safely immunize mammals without the risk of vector shedding or reversion to virulence?",
            [
                "Canarypox virus is heat-killed with formalin before being mixed with aluminum hydroxide",
                "Canarypox virus integrates permanently into the mammalian host chromosome like a lentivirus",
                "Canarypox virus replicates lytically to high titers in mammalian lungs and is shed in aerosols",
                "Avipoxviruses (Canarypox and Fowlpox) are host-restricted to birds and undergo 'abortive replication' in mammalian cells—entering the cytoplasm and expressing early recombinant vaccine antigens (inducing both MHC-I CTL and antibody responses) without assembling infectious progeny virions"
            ],
            3,
            "Avipoxviruses (Canarypox [ALVAC] and Fowlpox [TROVAC]) are genetically restricted to avian cells for productive replication. When injected into a dog, cat, or horse, the canarypox vector enters mammalian cells and expresses early/immediate-early promoters driving synthesis of the inserted foreign glycoprotein (presenting it on both MHC Class I and II), but replication is blocked before viral DNA synthesis/morphogenesis—guaranteeing 100% safety with zero viral shedding.",
            True,
            TOPIC
        ),
        (
            "In commercial broiler hatcheries, automated 'In Ovo Vaccination' delivers Marek's disease (HVT/SB-1/CVI988) or infectious bursal disease immune-complex vaccines into the amniotic fluid (or embryo body) at which precise stage of chicken egg incubation (during transfer from the setter incubator to the hatcher)?",
            [
                "At Day 18 (17.5 to 19 days) of incubation",
                "At Day 1 (immediately prior to setting the fertile egg)",
                "At Day 9 (via the chorioallantoic membrane)",
                "At Day 5 (via the yolk sac route)"
            ],
            0,
            "In ovo vaccination is performed at Day 18 (between 17.5 and 19.2 days) of the 21-day chicken incubation period when eggs are transferred from setter trays to hatcher baskets. At Day 18, the embryo is physiologically mature enough to mount an immune response and swallows the amniotic fluid, ensuring uniform mass immunization 3 days before hatch.",
            True,
            TOPIC
        ),
        (
            "Wildlife rabies eradication campaigns in Europe and North America utilize air-dropped oral vaccine baits containing recombinant Vaccinia-Rabies Glycoprotein (V-RG) or attenuated rabies strains (SAG2). Why is the antibiotic 'Tetracycline' routinely incorporated into the outer fat/fishmeal bait matrix?",
            [
                "To cure foxes and raccoons of concurrent bacterial pneumonia so they survive to seroconvert",
                "To prevent bacterial spoilage of the liquid viral sachet during summer heat",
                "Tetracycline chelates calcium in growing teeth and bones, forming a permanent yellow fluorescent ring under UV microscopy of premolar tooth sections during post-campaign trapping surveys to verify bait consumption",
                "Tetracycline acts as a chemical mucosal adjuvant that opens tight junctions in the tonsils"
            ],
            2,
            "Tetracycline binds avidly to calcium ions being deposited in the dentin/cementum of teeth and cortical bone. When wildlife authorities trap or collect jaws from foxes/raccoons after an aerial baiting campaign, examining unstained ground sections of a premolar/canine tooth under UV fluorescence microscopy reveals a bright yellow tetracycline line, proving whether the animal ate the bait.",
            True,
            TOPIC
        ),
        (
            "Hepatocytes synthesize 'Acute Phase Proteins' (APPs) in response to IL-6, IL-1beta, and TNF-alpha during acute inflammation or infection, but the dominant major positive APP varies markedly across domestic animal species. Which pairing of animal species and its premier major positive Acute Phase Protein (increasing 10- to 1000-fold) is CORRECT?",
            [
                "Cattle & Sheep: Haptoglobin and Serum Amyloid A (SAA); Dogs: C-Reactive Protein (CRP); Horses: Serum Amyloid A (SAA); Cats: Serum Amyloid A and alpha-1-acid glycoprotein (AGP)",
                "Cattle & Sheep: C-Reactive Protein (CRP) only; Dogs: Albumin; Horses: Transferrin",
                "All domestic mammals use exclusively C-Reactive Protein (CRP) and Albumin as positive APPs",
                "Cattle: Pig-MAP; Dogs: Haptoglobin only; Horses: C-Reactive Protein only"
            ],
            0,
            "Major positive Acute Phase Proteins are highly species-specific in veterinary clinical pathology: in Cattle and Small Ruminants, Haptoglobin (Hp) and Serum Amyloid A (SAA) are the major APPs (CRP is NOT an acute phase reactant in cattle!); in Dogs, C-Reactive Protein (CRP) and SAA are major; in Horses, SAA is the premier rapid marker; in Cats, SAA and alpha-1-acid glycoprotein (AGP, especially in FIP) dominate; and in Pigs, Pig-MAP, Haptoglobin, and CRP dominate. (Albumin and Transferrin are NEGATIVE APPs that decrease during inflammation).",
            True,
            TOPIC
        ),
        (
            "In immunological memory to rapidly mutating viruses (such as Influenza A virus or Foot and Mouth Disease virus), what is the phenomenon of 'Original Antigenic Sin' (the Hoskins Effect / Immune Imprinting)?",
            [
                "Complete deletion of all T and B cells following transplacental infection in the first trimester",
                "Memory B cells primed by the FIRST historical viral strain dominate responses to subsequent mutated variants",
                "Spontaneous production of natural IgM isoantibodies against A and B blood group antigens without prior transfusion",
                "Inability of a newborn animal to respond to a vaccine in the presence of maternal colostral IgG"
            ],
            1,
            "First described by Thomas Francis Jr. (1960), 'Original Antigenic Sin' occurs because memory B cells have a much lower activation threshold and higher frequency than naive B cells. When infected or vaccinated with a drifted antigenic variant, pre-existing memory B cells against the first historical strain encountered in life are preferentially recalled.",
            True,
            TOPIC
        ),
        (
            "In sheep, goats, and cattle, 'Hemal Nodes' are small, dark-red to brown encapsulated lymphoid organs located along the abdominal aorta and mesenteric blood vessels that differ from standard lymph nodes because their sinuses:",
            [
                "Contain only chylomicrons and lack all B and T lymphocytes",
                "Communicate directly with the lumen of the rumen and abomasum",
                "Are filled with circulating blood and erythrocytes rather than lymph (lacking afferent and efferent lymphatics and filtering blood like miniature spleens)",
                "Produce exclusively eosinophils and basophils during fetal life"
            ],
            2,
            "Hemal nodes are specialized secondary lymphoid organs peculiar to ruminants. They lack afferent and efferent lymphatic vessels; instead, their subcapsular and deep sinuses receive blood directly from arterioles and are packed with erythrocytes and macrophages, functioning like accessory miniature spleens to trap blood-borne pathogens.",
            True,
            TOPIC
        ),
        (
            "When a DNA virus (such as African Swine Fever virus or a Herpesvirus) or an intracellular bacterium releases double-stranded DNA into the host cell cytosol, which cytosolic DNA sensor synthesizes the cyclic dinucleotide second messenger 2'3'-cGAMP to activate the endoplasmic reticulum adaptor STING and induce Type I interferons?",
            [
                "TLR9 (Endosomal CpG DNA receptor)",
                "NOD2 (Muramyl dipeptide sensor)",
                "RIG-I (5'-triphosphate RNA helicase sensor)",
                "cGAS (Cyclic GMP-AMP Synthase)"
            ],
            3,
            "The cGAS-STING pathway is the principal cytosolic DNA-sensing innate immune pathway: Cyclic GMP-AMP Synthase (cGAS) binds sequence-independently to cytosolic dsDNA and catalyzes synthesis of 2'3'-cyclic GMP-AMP (cGAMP) from ATP and GTP, which binds STING on the ER to activate TBK1 and IRF3 for IFN-alpha/beta transcription.",
            True,
            TOPIC
        ),
        (
            "Which potent anti-inflammatory cytokine—secreted primarily by CD4+FoxP3+ Regulatory T cells (Tregs), Th2 cells, and M2 macrophages—functions as the 'Cytokine Synthesis Inhibitory Factor' by downregulating MHC Class II and B7 costimulators on macrophages and suppressing IL-12 and IFN-gamma production?",
            [
                "Interleukin-10 (IL-10, alongside Transforming Growth Factor-beta, TGF-beta)",
                "Interleukin-12 (IL-12p70 heterodimer)",
                "Interleukin-17A (IL-17A)",
                "Tumor Necrosis Factor-alpha (TNF-alpha)"
            ],
            0,
            "Interleukin-10 (IL-10) is the chief immunosuppressive feedback cytokine that prevents immunopathology during infections by inhibiting macrophage activation, blocking NF-kappaB signaling, downregulating MHC Class II and CD80/CD86 expression on APCs, and suppressing Th1 cytokine (IL-12, IFN-gamma, TNF-alpha) synthesis.",
            True,
            TOPIC
        ),
        (
            "In vaccinology and viral immunology, 'Cross-Presentation' refers to the specialized ability of Classical Type 1 Dendritic Cells (cDC1) to:",
            [
                "Transfer intact maternal IgG across intestinal enterocytes into the neonatal bloodstream",
                "Internalize EXOGENOUS antigens (from virus-infected apoptotic cells or subunit vaccines) and route them onto MHC Class I molecules to prime naive CD8+ cytotoxic T lymphocytes",
                "Present endogenous cytosolic viral peptides on MHC Class II molecules to B-lymphocytes",
                "Secrete antibodies that simultaneously neutralize two unrelated viral families"
            ],
            1,
            "Normally, exogenous endocytosed antigens are presented exclusively on MHC Class II to CD4+ T cells. However, specialized dendritic cells (cDC1) can export exogenous phagocytosed antigens from endosomes into the cytosol/proteasome/TAP pathway to load onto MHC Class I molecules ('cross-presentation'), enabling activation of naive CD8+ CTLs against viruses that do not directly infect dendritic cells and against killed/saponin-adjuvanted vaccines.",
            True,
            TOPIC
        ),
        (
            "Because membrane-bound Immunoglobulin (mIgM / mIgD) on the surface of a naive B-lymphocyte possesses an extremely short cytoplasmic tail (only 3 amino acids: Lys-Val-Lys), how does the B-Cell Receptor (BCR) transduce intracellular activation signals upon antigen binding?",
            [
                "By directly phosphorylating nuclear STAT3 via its extracellular Fab hinge domain",
                "By associating non-covalently with the T-cell CD3-zeta and CD28 signaling complex",
                "Via the disulfide-linked heterodimer Ig-alpha / Ig-beta (CD79a / CD79b), whose cytoplasmic tails contain Immunoreceptor Tyrosine-based Activation Motifs (ITAMs)",
                "By opening voltage-gated sodium channels in the outer mitochondrial membrane"
            ],
            2,
            "Just as the T-cell receptor (TCR alpha/beta) relies on the CD3 complex and zeta-chains for signaling, the B-cell receptor's membrane immunoglobulin (mIg) is non-covalently complexed with the disulfide-linked heterodimer Ig-alpha/Ig-beta (CD79a/CD79b). Cross-linking mIg brings the cytoplasmic ITAMs of Ig-alpha/Ig-beta together for phosphorylation by Src-family kinase Lyn and recruitment of Syk.",
            True,
            TOPIC
        ),
        (
            "Inside the germinal centers of secondary lymphoid follicles, both 'Somatic Hypermutation' (which drives antibody affinity maturation in the variable region) and 'Class Switch Recombination' (which switches heavy-chain isotype from IgM to IgG, IgA, or IgE) are initiated by which single B-cell-specific enzyme?",
            [
                "Terminal deoxynucleotidyl transferase (TdT)",
                "Recombination-Activating Gene 1 and 2 endonucleases (RAG-1 / RAG-2)",
                "DNA Polymerase III exonuclease",
                "Activation-Induced Cytidine Deaminase (AID, which deaminates deoxycytidine to deoxyuridine in single-stranded DNA)"
            ],
            3,
            "Whereas RAG-1/RAG-2 and TdT mediate antigen-independent V(D)J recombination in primary lymphoid organs (bone marrow/thymus), antigen-driven Somatic Hypermutation (SHM) and Class Switch Recombination (CSR) in germinal center centroblasts both strictly require Activation-Induced Cytidine Deaminase (AID), which converts cytosine (C) to uracil (U) in transcribed V genes and switch (S) regions.",
            True,
            TOPIC
        ),
        (
            "X-Linked Severe Combined Immunodeficiency (X-SCID) documented in Basset Hound and Cardigan Welsh Corgi dogs—characterized by stunted growth, absent tonsils/thymic hypoplasia, complete absence of functional T cells, and agammaglobulinemia despite normal numbers of circulating B cells—is caused by a mutation in the gene encoding:",
            [
                "The Common Gamma Chain (gamma-c / CD132) shared by the receptors for IL-2, IL-4, IL-7, IL-9, IL-15, and IL-21",
                "The DNA-dependent protein kinase catalytic subunit (DNA-PKcs, which causes autosomal recessive SCID in Arabian foals and Jack Russell Terriers)",
                "The beta-2 integrin subunit CD18 (which causes BLAD in Holstein cattle and CLAD in Irish Setters)",
                "The lysosomal trafficking regulator LYST (which causes Chédiak-Higashi syndrome)"
            ],
            0,
            "Canine X-SCID (in Basset Hounds and Cardigan Welsh Corgis, homologous to human X-SCID) is caused by a frameshift mutation in the IL2RG gene on the X chromosome encoding the Common Gamma Chain (gamma-c / CD132). Without functional IL-7R (for T-cell development), IL-15R (for NK cells), and IL-2R/IL-4R/IL-21R (for B-cell activation/class switching), affected male pups have a T-negative, NK-negative, B-positive SCID phenotype.",
            True,
            TOPIC
        ),
        (
            "In modern vaccine development, what is 'Reverse Vaccinology' (pioneered by Rino Rappuoli)?",
            [
                "Attenuating a virulent virus by serial passage in an unnatural host at 25°C",
                "In silico bioinformatic analysis of a pathogen's whole sequenced genome to predict novel surface-exposed or secreted protein antigens for recombinant subunit expression, without needing to culture the pathogen",
                "Injecting preformed hyperimmune serum before administering a live virulent field strain",
                "Converting a DNA vaccine back into an RNA virus using reverse transcriptase"
            ],
            1,
            "Conventional vaccinology (Pasteur's paradigm) starts by growing the microorganism in vitro and biochemically purifying its components. Reverse Vaccinology starts instead from the pathogen's genomic DNA sequence, using computer algorithms to screen all open reading frames (ORFs) for signal peptides, outer-membrane domains, and T/B-cell epitopes—identifying novel protective antigens even for uncultivable pathogens.",
            True,
            TOPIC
        ),
        (
            "How do commercial 'Immune-Complex Vaccines' (Virus-Antibody Complex vaccines) used for in ovo or day-1 immunization of broiler chicks against Infectious Bursal Disease Virus (IBDV) overcome variable levels of Maternal Derived Antibodies (MDA) within a flock?",
            [
                "They contain a virulent bacterial protease that digests all maternal IgY in the chick's bloodstream",
                "They use a chimeric turkey herpesvirus vector that integrates into the chick's feather follicles",
                "Live intermediate-plus IBDV vaccine virus is pre-coated in vitro with specific anti-IBDV hyperimmune chicken IgY, which shields the vaccine virus from neutralization by MDA and retains it on follicular dendritic cells until MDA declines to a permissive level in each individual chick",
                "They consist of naked double-stranded RNA encapsulated in aluminum hydroxide gel"
            ],
            2,
            "In a broiler flock, individual chicks hatch with widely varying titers of maternal anti-IBDV IgY, making it impossible to pick a single drinking-water vaccination day that fits all birds. An Immune-Complex (Icx) vaccine complexes live IBDV with specific anti-IBDV IgY antibodies; the complex is trapped on Follicular Dendritic Cells (FDCs) in the spleen/bursa and releases live vaccine virus to replicate only when that specific chick's maternal antibody titer drops below the neutralization threshold.",
            True,
            TOPIC
        ),
        (
            "During Gram-negative bacterial sepsis and endotoxic shock, what is the exact sequence of host serum and macrophage receptor interactions that enables picogram concentrations of Lipopolysaccharide (LPS / Lipid A) to trigger NF-kappaB activation and massive TNF-alpha / IL-1beta release?",
            [
                "LPS binds directly to MHC Class II and TCR V-beta without any accessory proteins",
                "LPS binds C1q in serum and enters macrophages via the neonatal Fc receptor (FcRn)",
                "LPS binds IgE on mast cells and activates the cytoplasmic RIG-I helicase",
                "Plasma LPS-Binding Protein (LBP) extracts LPS monomers and transfers them to GPI-anchored CD14, which delivers Lipid A to the TLR4 / MD-2 receptor complex on macrophages"
            ],
            3,
            "In the bloodstream, acute-phase LPS-Binding Protein (LBP) binds LPS micelles and transfers monomeric LPS to membrane-bound or soluble CD14. Because CD14 is a GPI-anchored protein lacking a transmembrane signaling domain, CD14 transfers the Lipid A moiety to the transmembrane Toll-Like Receptor 4 (TLR4) complexed with its essential accessory protein MD-2, triggering MyD88/TRIF and NF-kappaB cytokine storm.",
            True,
            TOPIC
        ),
        (
            "In transplantation immunology and blood transfusion medicine, 'Hyperacute Rejection'—which occurs within minutes to hours of connecting a vascularized organ xenograft or mismatched allograft, turning the organ cyanotic and mottled—is mediated by:",
            [
                "Pre-existing recipient antibodies (such as natural xenoreactive anti-Gal-alpha-1,3-Gal antibodies or alloantibodies) binding donor vascular endothelial antigens and activating the Classical Complement cascade, triggering instantaneous endothelial damage and intravascular thrombosis",
                "Slow differentiation of naive CD8+ cytotoxic T cells over 14 to 21 days",
                "Delayed-type hypersensitivity mediated by Th1 macrophages and giant cells after 6 months",
                "Infiltration of eosinophils induced by Interleukin-5"
            ],
            0,
            "Hyperacute rejection occurs within minutes of revascularization because the recipient ALREADY possesses circulating preformed antibodies against donor vascular endothelial surface antigens (e.g., ABO/DEA blood group antigens, prior sensitization MHC alloantibodies, or anti-Gal-alpha-1,3-Gal xenoreactive antibodies). Immediate classical complement activation and von Willebrand factor release cause fulminant microvascular thrombosis and ischemic necrosis.",
            True,
            TOPIC
        ),
        (
            "How do naive T and B lymphocytes circulating in the arterial bloodstream selectively recognize and extravasate into peripheral lymph nodes to scan for foreign antigens?",
            [
                "They enter exclusively through afferent lymphatic capillaries draining the skin",
                "Lymphocyte L-selectin (CD62L) binds addressins (PNAd) on cuboidal High Endothelial Venules (HEVs)",
                "They phagocytose vascular endothelial cells to bore holes through the lymph node capsule",
                "They bind IgE on perivascular mast cells to trigger histamine-induced vascular rupture"
            ],
            1,
            "Whereas effector leukocytes enter inflamed tissues across flat post-capillary venules, naive T and B lymphocytes (~90%) enter lymph nodes directly from the blood across specialized plump, cuboidal post-capillary venules called High Endothelial Venules (HEVs) located in the paracortex.",
            True,
            TOPIC
        ),
        (
            "Following T-cell activation, how does the induced co-inhibitory checkpoint receptor 'CTLA-4' (CD152) act as a physiological brake to prevent runaway lymphoproliferation and autoimmunity?",
            [
                "CTLA-4 cleaves Interleukin-2 in the extracellular space via a serine protease domain",
                "CTLA-4 ubiquitinates MHC Class I molecules inside the endoplasmic reticulum",
                "CTLA-4 binds CD80/CD86 (B7) on APCs with 20-fold higher affinity than CD28, delivering an ITIM-like inhibitory signal",
                "CTLA-4 polymerizes Perforin pores in the plasma membrane of neighboring B-lymphocytes"
            ],
            2,
            "Once a T cell is activated via CD28-B7 costimulation, it upregulates surface CTLA-4 (CD152, also constitutively expressed on FoxP3+ Tregs). CTLA-4 binds CD80/CD86 (B7-1/B7-2) with ~20-fold higher affinity than CD28, competitively stripping B7 from APCs and recruiting phosphatases (SHP-2/PP2A) to terminate T-cell proliferation.",
            True,
            TOPIC
        )
    ]


