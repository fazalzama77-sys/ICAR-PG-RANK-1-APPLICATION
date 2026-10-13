# scripts/micro2_mod6.py
# Module 6: Diagnostic Serology & Molecular Microbiology (40 questions)

TOPIC = "Diagnostic Serology & Molecular Microbiology"

def get_module6_questions():
    return [
        (
            "In the classical Heidelberger-Kendall quantitative precipitin curve, whereas the 'Prozone' phenomenon is caused by antibody excess, the 'Postzone' phenomenon (high-dose hook effect) is a false-negative result caused by:",
            [
                "Extreme ANTIGEN excess, which dissolves cross-linked lattices into small soluble Ag2Ab complexes",
                "Extreme ANTIBODY excess, which coats all antigenic epitopes without cross-linking",
                "High concentrations of complement C1q precipitating heat-denatured IgM",
                "Low ionic strength (0.01% NaCl) preventing hydrophobic interactions"
            ],
            0,
            "In the Heidelberger-Kendall curve, visible precipitation occurs only in the 'Zone of Equivalence' where multivalent antigen and divalent antibody form large cross-linked lattices. In the Prozone (antibody excess), every epitope is saturated by separate antibodies; in the Postzone (antigen excess), every antibody paratope is saturated by separate free antigen molecules (small soluble Ag2Ab complexes).",
            True,
            TOPIC
        ),
        (
            "When comparing the functional efficiency of purified immunoglobulin classes on a molar basis in classical serological assays, how do pentameric IgM and monomeric IgG compare in 'Direct Bacterial Agglutination' versus 'Toxin Neutralization / Precipitation'?",
            [
                "IgG is 500-fold more efficient in direct agglutination; IgM is superior in toxin neutralization",
                "IgM is 100- to 700-fold more efficient in direct agglutination; IgG is superior in precipitation and toxin neutralization",
                "Both IgM and IgG have identical molar efficiency in both agglutination and precipitation",
                "Secretory IgA is the only immunoglobulin capable of mediating tube agglutination"
            ],
            1,
            "Because pentameric IgM has 10 antigen-binding sites (decavalent) and a large molecular span (~30 nm) capable of bridging the negatively charged zeta-potential repulsion between bacteria or RBCs, IgM is 100–700 times more efficient than IgG at direct agglutination. Conversely, divalent IgG forms compact lattices ideal for precipitation and penetrates tissues to neutralize toxins.",
            True,
            TOPIC
        ),
        (
            "In immunochemistry, what is the precise distinction between Antibody 'Affinity' and Antibody 'Avidity'?",
            [
                "Affinity applies only to IgM pentamers; Avidity applies only to monovalent Fab fragments",
                "Affinity is measured by the Coombs test; Avidity is measured by the Weil-Felix test",
                "Affinity is the intrinsic binding strength of a SINGLE paratope for a SINGLE epitope; Avidity is the combined functional strength of multivalent interactions",
                "Affinity measures cross-reactivity with unrelated antigens; Avidity measures complement fixation"
            ],
            2,
            "Affinity (quantified by the association equilibrium constant Ka) is the thermodynamic bond strength between one single antigen-binding site (paratope) and one single antigenic determinant (epitope). Avidity (functional affinity) is the total net stability of a multivalent antibody (e.g., 2 sites on IgG, 4 on sIgA, 10 on IgM) binding a multivalent antigen.",
            True,
            TOPIC
        ),
        (
            "In Mancini's 'Single Radial Immunodiffusion' (SRID) assay—used to quantify serum IgG concentrations in neonatal calves/foals and hemagglutinin content in influenza vaccines—how is the gel prepared and how is the final antigen concentration calculated?",
            [
                "Antigen is mixed into the agar; ring diameter is inversely proportional to antibody titer",
                "Both antigen and antibody are placed in adjacent wells and migrate under an electric field",
                "Complement and sheep RBCs are mixed into the agar; clear lysis zones are measured at 1 hour",
                "Monospecific antibody is uniformly incorporated into the molten agar gel, and test antigen placed in a well diffuses radially until the squared diameter (d^2) of the precipitin ring is directly proportional to antigen concentration"
            ],
            3,
            "In the Mancini Single Radial Immunodiffusion (SRID) test, anti-species antibody (e.g., anti-bovine IgG) is mixed uniformly into the agar before pouring. Antigen (calf serum) pipetted into cylindrical wells diffuses radially outward, forming a halo precipitin ring whose area (or diameter squared, d^2) at equivalence is linearly proportional to the antigen concentration.",
            True,
            TOPIC
        ),
        (
            "In an Ouchterlony Double Immunodiffusion agar gel plate where two adjacent antigen wells diffuse toward a central antibody well, what is indicated when the two precipitin lines meet and fuse completely into a smooth continuous arc WITHOUT any spur?",
            [
                "Reaction of Complete Identity (the two antigens share identical antigenic determinants)",
                "Reaction of Non-Identity (the two antigens are completely unrelated and lines cross as an X)",
                "Reaction of Partial Identity (the antigens share one epitope but one possesses an extra epitope)",
                "Prozone inhibition caused by complement exhaustion in the central well"
            ],
            0,
            "In Ouchterlony double immunodiffusion: (1) Complete fusion into a smooth continuous arc = Reaction of Identity; (2) Complete crossing of the two lines to form an 'X' = Reaction of Non-Identity; and (3) Fusion with a projecting 'spur' pointing toward the deficient antigen well = Reaction of Partial Identity.",
            True,
            TOPIC
        ),
        (
            "How does 'Counter-Immunoelectrophoresis' (CIE / CIEP)—used for rapid diagnosis of Aleutian Mink Disease, PPR, and Contagious Ecthyma—accelerate Ouchterlony double immunodiffusion from 24–48 hours down to 30–60 minutes?",
            [
                "By heating the agar plate to 65°C in a microwave oven during diffusion",
                "In an alkaline agarose gel (pH 8.2–8.6) under an electric field, negatively charged antigens migrate toward the anode (+) while weakly charged IgG antibodies are swept in the opposite direction toward the cathode (-) by electroendosmosis",
                "By digesting antibodies into monovalent Fab fragments with papain prior to loading",
                "By replacing agarose with liquid polyacrylamide containing sodium dodecyl sulfate (SDS)"
            ],
            1,
            "In passive Ouchterlony diffusion, antigens and antibodies diffuse in all directions (wasting >80% of reactants). In Counter-Immunoelectrophoresis (CIE) at pH 8.2–8.6, negatively charged viral/bacterial antigens placed in the cathode well move rapidly toward the anode (+), while antibodies placed in the anode well are carried backward toward the cathode (-) by electroendosmotic flow, colliding head-on in 30–45 minutes.",
            True,
            TOPIC
        ),
        (
            "In the classical 'Complement Fixation Test' (CFT)—the WOAH-prescribed confirmatory test for Glanders, Contagious Bovine Pleuropneumonia, and Brucellosis—what constitutes the 'Indicator System' added in Stage 2, and what visual appearance denotes a POSITIVE test result?",
            [
                "Horse RBCs coated with concanavalin A; complete hemolysis denotes a POSITIVE result",
                "Chicken RBCs coated with Newcastle disease virus; hemagglutination denotes a POSITIVE result",
                "Sheep RBCs sensitized with rabbit anti-sheep hemolysin (amboceptor); ABSENCE of hemolysis (an intact red cell button at the bottom with clear colorless supernatant) denotes a POSITIVE test result",
                "Latex beads coated with Protein A; milky turbidity denotes a POSITIVE result"
            ],
            2,
            "In Stage 1 of the CFT, heat-inactivated test serum (heated at 56°C for 30 min to destroy endogenous complement) is incubated with specific antigen and a measured dose of guinea pig complement. If the patient has specific antibodies, Antigen-Antibody complexes FIX (consume) all the complement. Therefore, when the Stage 2 indicator system (sheep RBCs + rabbit anti-sheep RBC antibody/amboceptor) is added, NO complement remains to lyse the sheep RBCs—so NO hemolysis (a settled RBC button) = POSITIVE test! Complete hemolysis = NEGATIVE test.",
            True,
            TOPIC
        ),
        (
            "Why must test sera from cattle or horses be heated in a water bath at 56°C for 30 minutes ('Inactivation') immediately prior to performing the Complement Fixation Test (CFT) or Virus Neutralization Test (VNT)?",
            [
                "To denature host IgM antibodies so only IgG2 remains active",
                "To release viral nucleic acids from circulating immune complexes",
                "To sterilize bacterial contaminants so the test can be run on an open bench",
                "To destroy heat-labile endogenous host complement proteins (C1, C2, Factor B) while leaving heat-stable immunoglobulins intact, so that only the standardized guinea pig complement controls the assay"
            ],
            3,
            "Complement components (especially C1qrs, C2, and Factor B) are heat-labile and completely inactivated at 56°C for 30 minutes, whereas antibodies (IgG/IgM) are relatively heat-stable at 56°C. Inactivating the patient's variable native complement ensures that only the exact calibrated units (e.g., 5 CH50) of exogenous guinea pig complement operate in the CFT, and prevents non-specific complement cytotoxicity in VNT cell cultures.",
            True,
            TOPIC
        ),
        (
            "In the serodiagnosis of Bovine Brucellosis, adding the reducing agent '2-Mercaptoethanol' (2-ME) or 'Dithiothreitol' (DTT) to the Standard Tube Agglutination Test (STAT) differentiates recent S19 vaccination or early acute exposure from chronic active infection because 2-ME:",
            [
                "Cleaves disulfide bonds of pentameric IgM (abolishing IgM agglutination) while leaving IgG agglutination intact",
                "Selectively destroys monomeric IgG1 and IgG2 while preserving pentameric IgM",
                "Lowers the pH of the serum to 2.0 to dissolve smooth lipopolysaccharide",
                "Converts incomplete non-agglutinating IgA into pentameric agglutinins"
            ],
            0,
            "Pentameric IgM (which predominates early after infection or persists after calfhood S19 vaccination and causes non-specific cross-reactions) depends on inter-subunit disulfide bonds and the J-chain for its decavalent agglutinating activity. Treating serum with 2-mercaptoethanol (2-ME) or DTT reduces these disulfide bonds, splitting IgM into non-agglutinating monomers; any remaining agglutination titer is strictly due to 2-ME-resistant IgG (indicative of active Brucella infection).",
            True,
            TOPIC
        ),
        (
            "The 'Fluorescence Polarization Assay' (FPA) is a WOAH-prescribed confirmatory serological test for Brucellosis (using a fluorescein-labeled 22-kDa O-polysaccharide tracer) that is prized for high-throughput automation because it is a 'homogeneous assay'—meaning it requires NO washing steps—based on which biophysical principle?",
            [
                "Binding of antibody quenches 100% of fluorescence and turns the solution black",
                "Free small fluorescent antigen tracer tumbles rapidly in solution (emitting depolarized light / low mP), whereas tracer bound to a large anti-Brucella antibody molecule tumbles slowly, retaining high fluorescence polarization (high millipolarization, mP)",
                "Antibody binding cleaves fluorescein via beta-lactamase to shift emission from green to red",
                "Agglutinated bacteria settle to the bottom of a capillary tube under a magnetic field"
            ],
            1,
            "In Fluorescence Polarization Assay (FPA), plane-polarized blue light excites a small fluorescein-labeled Brucella O-polysaccharide fragment (~20–30 kDa). If the serum is negative, the small free tracer rotates rapidly during its 4-nanosecond excited lifetime, depolarizing the emitted light (low mP). If anti-Brucella antibodies (~150–900 kDa) bind the tracer, rotational Brownian motion slows dramatically, and emitted light remains highly polarized (high mP).",
            True,
            TOPIC
        ),
        (
            "Why is an 'IgM-Capture ELISA' (MAC-ELISA—where microplate wells are coated first with anti-species mu-chain antibodies to capture patient IgM, followed by addition of viral antigen) strongly preferred over a standard Indirect ELISA for diagnosing acute arboviral infections (such as West Nile Virus, Japanese Encephalitis, or Rift Valley Fever)?",
            [
                "Viral arboviral antigens cannot bind directly to polystyrene microplate wells",
                "IgM antibodies are completely destroyed during standard serum dilution",
                "In a standard Indirect ELISA, high concentrations of patient IgG competitively outcompete IgM for antigen epitopes (causing false-negative IgM results), while Rheumatoid Factor (IgM anti-IgG) bound to IgG causes false-positive results; capturing IgM first eliminates both artifacts",
                "Anti-mu chain antibodies directly neutralize infectious virus without needing a chromogenic substrate"
            ],
            2,
            "In a standard Indirect ELISA (antigen on the plate), if a sample contains high levels of specific IgG, the faster-diffusing, higher-affinity IgG saturates the solid-phase antigen and blocks IgM binding (false negative); conversely, if the patient has IgM Rheumatoid Factor (autoantibody against IgG Fc) plus past IgG, RF binds the attached IgG and triggers the anti-IgM conjugate (false positive). Coating the plate with anti-IgM (MAC-ELISA) captures only IgM first and washes away all IgG.",
            True,
            TOPIC
        ),
        (
            "In Enzyme-Linked Immunosorbent Assays (ELISAs), each reporter enzyme requires a specific chromogenic substrate system. Which pairing of ELISA enzyme and its standard soluble chromogenic substrate(s) is CORRECT?",
            [
                "Horseradish Peroxidase (HRP): p-Nitrophenyl Phosphate (pNPP); Alkaline Phosphatase: TMB",
                "Horseradish Peroxidase (HRP): BCIP/NBT insoluble precipitate; Alkaline Phosphatase: Luminol + H2O2",
                "Beta-Galactosidase: Tetramethylbenzidine (TMB) + H2O2; Urease: Ortho-phenylenediamine (OPD)",
                "Horseradish Peroxidase (HRP): H2O2 + TMB (3,3',5,5'-tetramethylbenzidine), OPD, or ABTS; Alkaline Phosphatase (AP): p-Nitrophenyl Phosphate (pNPP)"
            ],
            3,
            "In ELISA: Horseradish Peroxidase (HRP) reduces hydrogen peroxide (H2O2) while oxidizing chromogenic hydrogen donors—most commonly TMB (turns blue, read at 650 nm, or turns yellow upon acid stop with H2SO4, read at 450 nm), OPD (orange-brown, 492 nm), or ABTS (green, 405 nm). Alkaline Phosphatase (AP) hydrolyzes colorless p-Nitrophenyl Phosphate (pNPP) into yellow p-nitrophenol (read at 405 nm).",
            True,
            TOPIC
        ),
        (
            "In a point-of-care 'Lateral Flow Immunochromatographic Assay' (rapid strip test), what immobilized reagent is printed at the 'Control Line' (C line, located downstream of the Test [T] line) to confirm that capillary migration and gold-nanoparticle conjugate reactivity functioned properly?",
            [
                "Anti-species immunoglobulin antibodies (e.g., goat anti-mouse IgG) that capture excess unbound gold-conjugated detector antibody regardless of whether the sample is positive or negative",
                "High concentrations of live virulent virus that agglutinate red blood cells",
                "A pH-sensitive phenol red dye strip that turns purple upon contact with any liquid",
                "Immobilized Proteinase K that digests the nitrocellulose membrane after 10 minutes"
            ],
            0,
            "In a lateral flow strip, the sample pad contains colloidal gold-conjugated mouse monoclonal detector antibodies against the target pathogen. As liquid wicks past the Test (T) line (coated with anti-pathogen capture antibody), any unbound gold-mouse IgG conjugate continues migrating to the Control (C) line, which is coated with anti-mouse IgG antibodies—guaranteeing a visible red Control band in every valid test.",
            True,
            TOPIC
        ),
        (
            "In 'Flow Cytometry' (and Fluorescence-Activated Cell Sorting, FACS) used to immunophenotype leukocyte subsets (such as CD4+ and CD8+ T-cell counts), what physical properties of each individual cell are measured by 'Forward Scatter' (FSC) versus 'Side Scatter' (SSC) of the laser beam?",
            [
                "Forward Scatter measures nuclear DNA content; Side Scatter measures cell viability",
                "Forward Scatter (FSC) is proportional to 'Cell Size' (cross-sectional surface area/volume); Side Scatter (SSC, at 90°) is proportional to 'Internal Cytoplasmic Granularity' and nuclear complexity",
                "Forward Scatter measures green FITC fluorescence; Side Scatter measures red phycoerythrin fluorescence",
                "Forward Scatter measures surface Zeta potential; Side Scatter measures membrane cholesterol content"
            ],
            1,
            "As hydrodynamically focused single cells pass through the laser beam in a flow cytometer: light diffracted at a narrow angle in the forward direction (Forward Scatter, FSC) measures cell size (small lymphocytes -> intermediate monocytes -> large macrophages), while light refracted and reflected at a 90° angle (Side Scatter, SSC) measures internal granularity (agranular lymphocytes vs highly granular neutrophils/eosinophils).",
            True,
            TOPIC
        ),
        (
            "In molecular biology blotting techniques (Southern, Northern, and Western blotting), which pairing of blot name, target macromolecule separated by gel electrophoresis, and detection probe is CORRECT?",
            [
                "Southern blot: RNA target detected by antibody; Northern blot: DNA target detected by DNA probe",
                "Southern blot: Protein target detected by DNA probe; Northern blot: Lipid target detected by lectin",
                "Southern blot: DNA target detected by labeled nucleic acid probe; Northern blot: RNA target detected by labeled nucleic acid probe; Western blot: Protein target detected by specific antibody",
                "Southern blot: Carbohydrate target; Northern blot: Prion target; Western blot: Plasmid DNA target"
            ],
            2,
            "Developed by Edwin Southern (1975), a Southern blot transfers restriction-digested DNA fragments from agarose gel to a nylon/nitrocellulose membrane for hybridization with a labeled DNA/RNA probe. By whimsical analogy: Northern blotting analyzes RNA (mRNA size and abundance); Western blotting (immunoblotting) analyzes Proteins using antibodies; and Southwestern blotting identifies DNA-binding proteins.",
            True,
            TOPIC
        ),
        (
            "In the Polymerase Chain Reaction (PCR), why is 'Pfu DNA Polymerase' (isolated from the hyperthermophilic archaeon Pyrococcus furiosus) preferred over standard 'Taq DNA Polymerase' (from Thermus aquaticus) when cloning genes for recombinant protein expression or site-directed mutagenesis?",
            [
                "Pfu polymerase is a reverse transcriptase that amplifies RNA directly without cDNA synthesis",
                "Pfu polymerase adds a 100-base poly-A tail to the 3' end of every PCR product",
                "Pfu polymerase operates isothermally at 37°C without requiring a thermal cycler",
                "Pfu polymerase possesses 3'-to-5' exonuclease 'proofreading' activity (excising misincorporated nucleotides for ~6-to-10-fold higher fidelity and generating blunt-ended PCR products), whereas Taq polymerase lacks 3'-to-5' proofreading and adds a single 3'-dA overhang"
            ],
            3,
            "Taq DNA polymerase has 5'->3' polymerase and 5'->3' exonuclease activity (used in TaqMan hydrolysis), adds a template-independent 3'-adenosine overhang (enabling TA cloning), but LACKS 3'->5' proofreading exonuclease activity (error rate ~10^-4 to 10^-5). Pfu (and Phusion/Q5) polymerase possesses a 3'->5' proofreading exonuclease domain that corrects mismatches, yielding blunt-ended amplicons with ultra-high fidelity.",
            True,
            TOPIC
        ),
        (
            "In a standard Polymerase Chain Reaction (PCR) master mix, which divalent cation cofactor is strictly required for the catalytic activity of Taq DNA polymerase (where too little results in no amplification Product, and too much causes non-specific background bands and primer-dimers), and why is EDTA in blood tubes inhibitory if carried over?",
            [
                "Magnesium ions (Mg2+, supplied as MgCl2); EDTA chelates free Mg2+ required by Taq polymerase",
                "Ferric ions (Fe3+, supplied as ferric citrate); EDTA oxidizes Fe3+ to insoluble rust",
                "Calcium ions (Ca2+, supplied as CaCl2); EDTA precipitates dNTPs out of solution",
                "Cupric ions (Cu2+, supplied as CuSO4); EDTA denatures oligonucleotide primers"
            ],
            0,
            "Free divalent Magnesium ions (Mg2+, typically 1.5 to 2.5 mM MgCl2) are the essential catalytic cofactor at the active site of Taq DNA polymerase, coordinating the triphosphate groups of dNTPs for phosphodiester bond formation and stabilizing primer-template duplexes. Carryover of EDTA (or sodium citrate) from anticoagulated blood chelates Mg2+ and inhibits PCR (while heparin directly binds and inhibits Taq polymerase).",
            True,
            TOPIC
        ),
        (
            "When performing Real-Time Quantitative PCR (qPCR) using the intercalating dye 'SYBR Green I' instead of a sequence-specific TaqMan probe, why is it mandatory to run a 'Melting Curve (Dissociation Curve) Analysis' immediately after the final amplification cycle?",
            [
                "To activate the hot-start antibody blocking Taq DNA polymerase",
                "Because SYBR Green I binds non-specifically to ANY double-stranded DNA (including primer-dimers and off-target amplicons); gradually heating the reaction from 60°C to 95°C verifies that fluorescence drops at a single sharp melting temperature (Tm) peak corresponding to the specific target amplicon rather than lower-Tm primer-dimers",
                "To convert double-stranded DNA amplicons into RNA for Sanger sequencing",
                "To regenerate consumed dNTPs so the same plate can be run a second time"
            ],
            1,
            "SYBR Green I emits bright green fluorescence upon binding the minor groove of any dsDNA duplex, so it cannot distinguish between the desired specific amplicon and short primer-dimer artifacts during amplification. A post-PCR Melt Curve slowly ramps temperature from 60°C to 95°C while plotting -d(Fluorescence)/dT: a specific amplicon melts at a single sharp, high Tm peak (e.g., 84°C), whereas primer-dimers melt at a broader, lower Tm peak (e.g., 72–75°C).",
            True,
            TOPIC
        ),
        (
            "In a Real-Time Quantitative PCR (qPCR) assay operating at 100% amplification efficiency (where amplicon copy number doubles every cycle: 2^n), Sample A crosses the fluorescence threshold at a Cycle Threshold (Ct) of 20.0, while Sample B crosses at a Ct of 23.32. How does the initial viral genome load in Sample A compare to Sample B?",
            [
                "Sample A contains 10-fold LESS viral DNA than Sample B",
                "Sample A contains 3.32-fold MORE viral DNA than Sample B",
                "Sample A contains 10-fold MORE viral DNA than Sample B (because a delta-Ct of 3.32 cycles equals one log10 [2^3.32 = 10], and an earlier/lower Ct indicates a higher starting template concentration)",
                "Sample A and Sample B contain the exact same viral load"
            ],
            2,
            "In qPCR, Cycle Threshold (Ct or Cq) is inversely proportional to the log of the initial template copy number. At 100% efficiency, each cycle doubles the DNA (2^1 = 2); therefore, a 10-fold (1 log10) difference in starting template requires log2(10) = 3.322 cycles. Since Sample A reached threshold 3.32 cycles EARLIER (Ct 20.0 vs 23.32), Sample A has 10-fold (10x) MORE starting viral genomes than Sample B.",
            True,
            TOPIC
        ),
        (
            "'Loop-Mediated Isothermal Amplification' (LAMP, developed by Notomi) has revolutionized pen-side and field veterinary molecular diagnostics because it amplifies target DNA at a single constant temperature (60°C–65°C in a simple water bath without a thermal cycler) by utilizing:",
            [
                "Taq DNA polymerase and a single pair of forward and reverse primers cycling between 95°C and 55°C",
                "T4 DNA ligase and restriction endonuclease EcoRI at 37°C",
                "CRISPR-Cas9 and reverse transcriptase at 42°C",
                "Four to six specially designed primers (F3, B3, FIP, BIP, LF, LB) recognizing 6–8 distinct target regions and 'Bst DNA Polymerase' (from Geobacillus stearothermophilus) possessing strong strand-displacement activity, producing visible white Magnesium Pyrophosphate precipitate"
            ],
            3,
            "LAMP operates isothermally at 60–65°C using the large fragment of Bst DNA polymerase (which has high strand-displacement activity without 5'->3' exonuclease activity) and 4–6 primers that form stem-loop 'dumbbell' structures. Massive DNA synthesis releases pyrophosphate ions that react with Mg2+ to form a visible white precipitate of Magnesium Pyrophosphate (Mg2P2O7) (or a color change from violet to sky-blue with Hydroxynaphthol Blue).",
            True,
            TOPIC
        ),
        (
            "In molecular taxonomy and phylogenetic identification of unknown clinical isolates, which conserved ribosomal gene locus serves as the universal 'DNA Barcode' for identifying BACTERIA, and which corresponding ribosomal locus serves as the universal 'DNA Barcode' for identifying FUNGI and YEASTS?",
            [
                "Bacteria: 16S rRNA gene (containing 9 hypervariable regions V1–V9); Fungi: Internal Transcribed Spacer (ITS1–5.8S–ITS2) region of nuclear rDNA",
                "Bacteria: 18S rRNA gene; Fungi: 16S rRNA gene",
                "Bacteria: Mitochondrial Cytochrome c Oxidase subunit I (COI); Fungi: 23S rRNA gene",
                "Bacteria: RecA protein gene; Fungi: Beta-lactamase gene"
            ],
            0,
            "In prokaryotic taxonomy, the ~1,500-bp 16S ribosomal RNA (16S rRNA) gene—comprising 9 hypervariable regions (V1–V9) flanked by conserved universal primer sites—is the universal barcode for Bacteria. In eukaryotic mycology, the nuclear ribosomal Internal Transcribed Spacer (ITS) region (spanning ITS1, the 5.8S rRNA gene, and ITS2 between the 18S and 28S rRNA genes) is the official universal barcode for Fungi.",
            True,
            TOPIC
        ),
        (
            "In Frederick Sanger's classical 'Dideoxy Chain-Termination' DNA sequencing method, why does the incorporation of a 2',3'-dideoxynucleoside triphosphate (ddATP, ddTTP, ddCTP, or ddGTP) immediately halt further elongation of the growing DNA strand by DNA polymerase?",
            [
                "The ddNTP carries a bulky biotin group on its purine ring that blocks the ribosome",
                "The ddNTP lacks the 3'-hydroxyl (-OH) group (having a 3'-H instead) on the deoxyribose sugar required for nucleophilic attack on the alpha-phosphate of the next incoming dNTP to form a phosphodiester bond",
                "The ddNTP lacks the 5'-alpha-phosphate group required to join the preceding nucleotide",
                "The ddNTP permanently denatures the template strand by breaking Watson-Crick hydrogen bonds"
            ],
            1,
            "Normal deoxynucleotides (dNTPs) have a 2'-H and a reactive 3'-OH group on the deoxyribose ring. Dideoxynucleotides (ddNTPs) lack hydroxyl groups at BOTH the 2' and 3' carbons (2',3'-dideoxy). Once incorporated into a growing DNA chain, the absence of a 3'-OH group makes it chemically impossible for DNA polymerase to form the next 3'->5' phosphodiester bond, terminating the chain at that specific base.",
            True,
            TOPIC
        ),
        (
            "Among third-generation 'Next-Generation Sequencing' (NGS) platforms increasingly deployed for rapid field metagenomic sequencing of avian influenza, rabies, and FMD outbreaks, how does 'Oxford Nanopore Sequencing' (e.g., MinION) read the nucleotide sequence of native single-stranded DNA or RNA molecules?",
            [
                "By measuring flashes of chemiluminescent light generated by luciferase when pyrophosphate is released",
                "By imaging fluorescently labeled reversible dye-terminators on glass flow-cell bridge clusters",
                "Byratcheting a single-stranded DNA or RNA molecule via a motor protein through a biological protein nanopore embedded in an electrically resistant membrane and measuring characteristic base-specific disruptions in ionic current (picoamperes) in real time",
                "By cleaving the DNA with four restriction enzymes and weighing fragments in a mass spectrometer"
            ],
            2,
            "Unlike second-generation short-read sequencing-by-synthesis (Illumina, Ion Torrent, Pyrosequencing), third-generation Oxford Nanopore Technology (MinION) requires no PCR amplification or fluorescence imaging: a helicase motor protein feeds a native single-stranded DNA or direct RNA strand through an alpha-hemolysin/CsgG protein nanopore across a voltage-biased membrane, and deep-learning basecallers translate the real-time ionic current squiggle into ultra-long reads (>10–100 kb).",
            True,
            TOPIC
        ),
        (
            "In modern clinical veterinary diagnostic laboratories, 'MALDI-TOF Mass Spectrometry' (Matrix-Assisted Laser Desorption/Ionization Time-of-Flight) identifies a bacterial or yeast colony from an agar plate within 2 minutes primarily by generating a species-specific mass-to-charge (m/z) fingerprint of its:",
            [
                "Extracellular capsular polysaccharides and O-antigen side chains",
                "Whole genomic DNA restriction fragments between 50 kb and 500 kb",
                "Volatile fatty acids and metabolic fermentation gases",
                "Abundant, highly conserved intracellular Ribosomal Proteins (in the 2 to 20 kDa mass range)"
            ],
            3,
            "In MALDI-TOF MS, a tiny smear of a bacterial or yeast colony is overlaid with an energy-absorbing organic acid matrix (e.g., alpha-cyano-4-hydroxycinnamic acid, HCCA) and pulsed with a UV laser in a vacuum flight tube. The soft ionization desorbs abundant, housekeeping ribosomal proteins (2,000–20,000 Da), whose time-of-flight to the detector yields a highly reproducible species-specific proteomic mass spectrum.",
            True,
            TOPIC
        ),
        (
            "In a veterinary microbiology laboratory, how does a 'Class I Biosafety Cabinet' differ fundamentally from a 'Class II Biosafety Cabinet' (such as Class II Type A2) regarding protection of the operator, the environment, and the biological sample/cell culture inside the cabinet?",
            [
                "Class I protects the operator (via inward airflow) and environment (via HEPA exhaust) but draws UNFILTERED room air directly across the work surface (giving ZERO protection to the culture/sample from contamination); Class II provides all three—operator, environment, AND product/sample protection via a vertical laminar curtain of HEPA-filtered supply air",
                "Class I protects only the cell culture sample while blowing unfiltered infectious aerosols into the operator's face",
                "Class I is a totally enclosed gas-tight metal box operated through heavy rubber gloves under positive pressure",
                "Class I and Class II are identical except that Class I uses ultraviolet light instead of HEPA filters"
            ],
            0,
            "A Class I BSC functions like a HEPA-filtered fume hood: room air is drawn inward through the front opening (protecting the operator) and exhausted through a HEPA filter (protecting the environment), but because unsterile room air flows over the work surface, the sample/cell culture is NOT protected from contamination. Class II BSCs (Types A1, A2, B1, B2) add a downward vertical laminar flow of HEPA-filtered supply air over the work surface, protecting the sample, operator, and environment.",
            True,
            TOPIC
        ),
        (
            "Within Class II Biosafety Cabinets, what is the critical engineering difference between a standard 'Class II Type A2' cabinet (the most common tissue culture/microbiology cabinet) and a 'Class II Type B2' ('Total Exhaust') cabinet?",
            [
                "Type A2 recirculates 0% of air; Type B2 recirculates 100% of air back into the room without ducts",
                "Type A2 recirculates ~70% of HEPA-filtered air within the cabinet and exhausts 30%; Type B2 recirculates 0% of air and exhausts 100% of cabinet air through a dedicated hard-ducted external exhaust blower (required when using toxic volatile chemicals/radionuclides)",
                "Type A2 uses 5.0-um fiberglass filters; Type B2 uses activated charcoal without HEPA filters",
                "Type A2 operates under positive pressure; Type B2 operates without an electrical fan"
            ],
            1,
            "In a Class II Type A2 BSC, 70% of the air passing through the work zone is recirculated through the supply HEPA filter back down onto the work surface, while 30% is discharged through the exhaust HEPA filter. In a Class II Type B2 ('Total Exhaust') BSC, 0% of air is recirculated—100% of inflow and downflow air is exhausted through a dedicated hard duct to the outside after HEPA filtration, preventing buildup of toxic chemical vapors.",
            True,
            TOPIC
        ),
        (
            "In epidemiological validation of diagnostic tests for a national disease eradication program (such as Bovine Brucellosis or Tuberculosis), what happens to the 'Positive Predictive Value' (PPV—the probability that an animal with a positive test result is truly infected) as the true prevalence of the disease in the population drops toward zero (e.g., from 20% down to 0.01%), even if test Sensitivity (99%) and Specificity (99%) remain completely unchanged?",
            [
                "The Positive Predictive Value increases to 100% while Negative Predictive Value drops to 0%",
                "The Positive Predictive Value remains constant at 99% because PPV is independent of prevalence",
                "The Positive Predictive Value drops dramatically (because false positives from the 1% specificity error in the vast uninfected population outnumber true positives), requiring 'Serial Testing' with a highly specific confirmatory test",
                "Both Sensitivity and Specificity drop to 50% when prevalence falls below 1%"
            ],
            2,
            "While Diagnostic Sensitivity and Specificity are intrinsic characteristics of a test, Positive Predictive Value (PPV = TP / [TP + FP]) depends heavily on disease prevalence. At 0.01% prevalence in 100,000 cattle, a test with 99% Se and 99% Sp yields ~10 True Positives but ~1,000 False Positives—so PPV falls to ~1%! Hence, late-stage eradication programs use 'Serial Testing' (retesting screen-positives with a high-specificity confirmatory test) to maximize PPV.",
            True,
            TOPIC
        ),
        (
            "When two diagnostic tests (e.g., Rose Bengal Plate Test and Complement Fixation Test) are combined in a herd testing strategy, how does interpreting the two tests in 'Parallel' (an animal is declared positive if EITHER Test A OR Test B is positive) compare with interpreting them in 'Series' (only animals positive on Test A are retested with Test B, and declared positive only if BOTH are positive)?",
            [
                "Parallel testing increases Specificity and decreases Sensitivity; Serial testing increases Sensitivity",
                "Parallel testing and Serial testing yield identical Sensitivity and Specificity",
                "Parallel testing is used only for molecular PCR; Serial testing is used only for bacterial culture",
                "Parallel testing maximizes net Diagnostic Sensitivity (minimizing false negatives for import quarantine or infected herd cleanup); Serial testing maximizes net Diagnostic Specificity and Positive Predictive Value (minimizing false-positive culling of healthy animals)"
            ],
            3,
            "Parallel testing ('OR' rule: positive if Test 1 OR Test 2 is positive) catches infected animals missed by either test alone, thereby increasing net Sensitivity (at the expense of lower Specificity). Serial testing ('AND' rule: positive only if Test 1 AND Test 2 are positive) eliminates false positives from the screening test, thereby maximizing net Specificity and Positive Predictive Value.",
            True,
            TOPIC
        ),
        (
            "In the Indirect Coombs Test (Hajdu's Antiglobulin Test) applied to chronic Bovine Brucellosis serology, why is rabbit anti-bovine immunoglobulin serum added to the washed Brucella antigen-serum suspension after an initial negative or low-titer Standard Tube Agglutination Test (STAT)?",
            [
                "To cross-link 'incomplete' (non-agglutinating / blocking) bovine IgG1, IgG2, and IgA antibodies that are bound to the Brucella cell surface but fail to bridge adjacent bacteria on their own",
                "To lyse the Brucella cell wall and release cytoplasmic ribosomal proteins",
                "To convert rough Brucella abortus RB51 cells into smooth Strain 19 cells",
                "To restore endogenous bovine complement C3 degraded during storage"
            ],
            0,
            "In chronic bovine brucellosis, cattle frequently produce asymmetrically glycosylated or sterically hindered 'incomplete' (blocking) IgG1/IgG2/IgA antibodies that bind firmly to Brucella LPS epitopes (and even block IgM agglutination in low dilutions, causing a prozone/blocking phenomenon) without visibly clumping the bacteria. Washing the bacteria and adding anti-bovine globulin (Coombs reagent) bridges the bound bovine antibodies, producing strong visible agglutination.",
            True,
            TOPIC
        ),
        (
            "How does 'Nested PCR' achieve a 1,000- to 10,000-fold increase in analytical sensitivity and specificity compared to conventional single-round PCR when detecting low-copy latent viruses (such as Malignant Catarrhal Fever virus or Equine Herpesvirus)?",
            [
                "It includes four different thermostable DNA polymerases in a single reaction tube",
                "It performs two sequential rounds of PCR amplification, where the product of the first round (amplified with an 'outer' primer pair) serves as the template for a second round using an internal ('nested') primer pair located inside the first amplicon",
                "It uses reverse transcriptase at 95°C to amplify both DNA and protein simultaneously",
                "It replaces agarose gel electrophoresis with Southern blot hybridization"
            ],
            1,
            "In Nested PCR (and Semi-Nested PCR, which shares one primer), the first PCR round (25–35 cycles) uses an outer pair of primers to amplify a larger target region. A tiny aliquot of the first-round product is then amplified in a second PCR round using an inner ('nested') pair of primers that anneal strictly within the authentic first-round amplicon—ensuring that any non-specific first-round off-target products cannot be amplified in the second round.",
            True,
            TOPIC
        ),
        (
            "What is the diagnostic advantage of 'Multiplex PCR' in veterinary clinical syndromic panels (such as bovine abortion or porcine respiratory panels)?",
            [
                "It amplifies the entire genome of a bacterium without requiring any primers",
                "It operates at room temperature without requiring dNTPs or magnesium chloride",
                "It incorporates multiple distinct pathogen-specific primer pairs into a single PCR reaction tube—designed with compatible annealing temperatures (Ta) to generate amplicons of distinctly different base-pair sizes—allowing simultaneous detection of several pathogens in one reaction",
                "It measures antibody titers and antibiotic susceptibility in the same tube"
            ],
            2,
            "Multiplex PCR combines two or more primer pairs targeting different pathogens (or different virulence genes, such as Clostridium perfringens alpha, beta, epsilon, and iota toxin genes for toxinotyping) inside a single PCR reaction mixture. Each primer pair is engineered to have matched annealing temperatures (~58–60°C) while yielding a uniquely sized amplicon (e.g., 200 bp, 350 bp, 500 bp, 700 bp) resolved on a single gel lane (or via distinct fluorophore channels in multiplex qPCR).",
            True,
            TOPIC
        ),
        (
            "In 'Touchdown PCR', how is the thermal cycler programmed during the initial 10 to 15 cycles to prevent spurious non-specific primer annealing and primer-dimer formation without needing tedious Mg2+ optimization?",
            [
                "The denaturation temperature is started at 50°C and raised by 2°C every cycle up to 95°C",
                "The extension time at 72°C is reduced to 1 millisecond for the first 15 cycles",
                "The reaction tube is physically inverted every 30 seconds during cycling",
                "The annealing temperature (Ta) is initially set 5°C–10°C ABOVE the calculated primer melting temperature (Tm) and then progressively decreased ('touched down') by 0.5°C–1.0°C every cycle until reaching the target Ta for the remaining 20–25 cycles"
            ],
            3,
            "In Touchdown PCR, starting the annealing temperature well above the estimated primer Tm allows primer annealing ONLY to the 100%-complementary specific target sequence during the earliest cycles. As the annealing temperature steps down by 0.5–1°C per cycle to the standard Ta, the specific amplicon has already accumulated a huge exponential head-start that outcompetes any late non-specific binding.",
            True,
            TOPIC
        ),
        (
            "'Nucleic Acid Sequence-Based Amplification' (NASBA) is an isothermal (41°C) molecular diagnostic method uniquely suited for detecting viable/replicating RNA viruses and bacterial mRNA (without interference from background genomic DNA) because it utilizes the concerted action of which three enzymes?",
            [
                "Avian Myeloblastosis Virus Reverse Transcriptase (AMV-RT), RNase H, and T7 DNA-dependent RNA Polymerase",
                "Taq DNA Polymerase, Pfu DNA Polymerase, and Uracil-DNA Glycosylase",
                "Bst DNA Polymerase, T4 Polynucleotide Kinase, and Alkaline Phosphatase",
                "EcoRI Restriction Endonuclease, T4 DNA Ligase, and Topoisomerase I"
            ],
            0,
            "NASBA amplifies single-stranded RNA exponentially at a constant 41°C (a temperature at which genomic dsDNA remains double-stranded and cannot be amplified!). Primer 1 (carrying a 5' T7 promoter overhang) primes AMV Reverse Transcriptase to make an RNA:cDNA hybrid; RNase H digests the RNA strand; AMV-RT synthesizes the second DNA strand with Primer 2; and T7 RNA Polymerase transcribes hundreds of antisense RNA copies from the functional T7 promoter.",
            True,
            TOPIC
        ),
        (
            "Why was 'Pulsed-Field Gel Electrophoresis' (PFGE)—which periodically alternates the orientation of the electric field across an agarose gel (e.g., CHEF system)—developed by Schwartz and Cantor, and what was its historical gold-standard role in veterinary and foodborne epidemiology?",
            [
                "To separate low-molecular-weight oligopeptides (<1 kDa) in less than 30 seconds",
                "Standard constant-field agarose electrophoresis cannot resolve DNA molecules larger than ~20–50 kb (which reptate end-on at the same speed); PFGE periodically switches electric field angles so megabase chromosomal fragments (digested with rare-cutting restriction enzymes like XbaI) reorient at size-dependent rates, serving as the PulseNet gold standard for strain subtyping of Salmonella, Listeria, and E. coli O157:H7",
                "To electrotransfer denatured proteins from polyacrylamide gels onto PVDF membranes",
                "To concentrate dilute viral particles from 10 liters of river water"
            ],
            1,
            "In conventional agarose gel electrophoresis, all DNA fragments >20–40 kb migrate at the same limiting mobility ('reptation'). In PFGE, bacterial cells are embedded in agarose plugs (to prevent mechanical DNA shearing), lysed in situ, digested with a rare-cutting restriction endonuclease (e.g., XbaI, NotI, SmaI), and subjected to periodically alternating electric field vectors (120° angle), resolving fragments up to 5–10 Megabases (Mb) into high-resolution macrorestriction 'barcodes'.",
            True,
            TOPIC
        ),
        (
            "In Immunofluorescence and Immunohistochemistry, the 'Avidin-Biotin Complex' (ABC) or 'Streptavidin-Biotin' system is widely used to amplify weak detection signals because:",
            [
                "Avidin is a radioactive isotope that exposes X-ray film within 5 seconds",
                "Biotin is a thermostable DNA polymerase that replicates the secondary antibody",
                "Tetrameric Avidin (from egg white) or Streptavidin (from Streptomyces avidinii) binds up to FOUR molecules of Biotin (Vitamin B7) with the strongest known non-covalent biological affinity (Kd ~ 10^-15 M), allowing multiple enzyme/fluorophore molecules to dock onto a single biotinylated antibody",
                "Streptavidin enzymatically cleaves cell wall peptidoglycan to unmask hidden nuclear antigens"
            ],
            2,
            "The non-covalent affinity between Avidin (or bacterial Streptavidin, which lacks carbohydrate side chains and has a neutral isoelectric point, reducing non-specific background binding) and the small vitamin Biotin (MW 244 Da) has a dissociation constant Kd of ~10^-15 M (nearly as strong as a covalent bond). Because multiple biotin molecules can be coupled to one antibody and each streptavidin binds four biotins, large macromolecular enzyme complexes form at the antigen site.",
            True,
            TOPIC
        ),
        (
            "In the 'Direct Fluorescent Antibody Test' (dFAT) and 'Indirect Fluorescent Antibody Test' (iFAT), what are the excitation and emission wavelengths/colors of the two classic fluorochromes—Fluorescein Isothiocyanate (FITC) and Tetramethylrhodamine Isothiocyanate (TRITC)?",
            [
                "FITC emits orange-red fluorescence (570 nm); TRITC emits apple-green fluorescence (520 nm)",
                "FITC emits ultraviolet light (260 nm); TRITC emits infrared heat (900 nm)",
                "Both FITC and TRITC emit bright cobalt-blue fluorescence at 405 nm",
                "FITC absorbs blue light (~490–495 nm) and emits bright apple-green fluorescence (~520 nm); TRITC absorbs green light (~540–550 nm) and emits orange-red fluorescence (~570–580 nm)"
            ],
            3,
            "Fluorescein Isothiocyanate (FITC) is the premier fluorochrome in veterinary diagnostic virology/bacteriology: it is excited by blue light (490–495 nm) and emits a characteristic bright apple-green fluorescence (517–520 nm, often contrasted against an Evans Blue counterstain which fluoresces brick-red). Tetramethylrhodamine Isothiocyanate (TRITC) is excited by green light (~550 nm) and emits orange-red light (~575 nm), permitting dual-color immunofluorescence.",
            True,
            TOPIC
        ),
        (
            "In the validation of a new serological ELISA against a gold-standard reference test on the same panel of 500 field sera, what statistical metric—ranging from 0 to 1.0—quantifies the degree of 'Inter-Test Agreement' AFTER correcting for the proportion of agreement expected purely by random chance?",
            [
                "Cohen's Kappa statistic (kappa, where >0.80 indicates almost perfect agreement beyond chance)",
                "Pearson's linear correlation coefficient (r^2)",
                "Student's unpaired t-test p-value",
                "The Reed and Muench 50% endpoint index"
            ],
            0,
            "Raw percent agreement between two diagnostic tests is misleading because two tests will agree on a substantial fraction of samples purely by chance (especially when prevalence is very low or very high). Cohen's Kappa coefficient (k = [Po - Pe] / [1 - Pe], where Po is observed agreement and Pe is chance-expected agreement) measures true concordance beyond chance: k <= 0 is no agreement, 0.41–0.60 is moderate, 0.61–0.80 is substantial, and 0.81–1.00 is almost perfect agreement.",
            True,
            TOPIC
        ),
        (
            "Under the World Health Organization (WHO) and CDC/NIH Biosafety in Microbiological and Biomedical Laboratories (BMBL) standards, what are the mandatory facility engineering controls required for a 'Biosafety Level 3' (BSL-3) containment laboratory (used for culturing Mycobacterium bovis, Brucella melitensis, Bacillus anthracis, and Burkholderia mallei)?",
            [
                "Open benchtops with natural window ventilation and positive room air pressure",
                "Controlled double-door anteroom access, directional inward (negative-pressure) airflow so air flows into the lab from clean corridors, HEPA filtration of exhaust air, and performing all open manipulations inside Biosafety Cabinets",
                "Mandatory full-body positive-pressure air-supplied 'space suits' and chemical dunk tanks for all personnel",
                "Laminar horizontal flow benches that blow air from the culture across the worker's face into the hallway"
            ],
            1,
            "Biosafety Level 3 (BSL-3) is designed for indigenous or exotic agents that may cause serious or potentially lethal disease via inhalation/aerosols (M. bovis, B. abortus/melitensis, Coxiella burnetii, B. anthracis, B. mallei, Rabies, HPAI). Key BSL-3 engineering controls include self-closing interlocking double-door entry, negative room air pressure (directional inward airflow verified by a visual pressure gauge), HEPA-filtered exhaust air without recirculation to other rooms, and hands-free sinks.",
            True,
            TOPIC
        ),
        (
            "When evaluating a diagnostic PCR assay in a reference laboratory, how does 'Analytical Sensitivity' differ from epidemiological 'Diagnostic Sensitivity'?",
            [
                "Analytical sensitivity is the percentage of healthy animals that test negative; Diagnostic sensitivity is the percentage of sick animals that die",
                "Analytical sensitivity and Diagnostic sensitivity are synonymous terms for Positive Predictive Value",
                "Analytical sensitivity (Limit of Detection, LOD) is the smallest physical amount or copy number of target nucleic acid/antigen detectable per reaction in a spiked sample; Diagnostic sensitivity (DSe) is the percentage of truly infected host animals in a population that test positive",
                "Analytical sensitivity depends on herd disease prevalence, whereas Diagnostic sensitivity is measured in picograms per milliliter"
            ],
            2,
            "Analytical Sensitivity (also called the Limit of Detection, LOD) is a laboratory biochemical metric—the minimum concentration or genome copy number (e.g., 10 copies/uL or 5 pg/mL) that the assay can reliably detect. Diagnostic Sensitivity (DSe = TP / [TP + FN]) is a population-level clinical metric—the probability that a truly infected animal (who may be intermittently shedding or latently infected) yields a positive test result.",
            True,
            TOPIC
        ),
        (
            "To prevent 'Carryover Contamination' (false-positive amplification caused by trace aerosolized PCR amplicons from previous runs contaminating new PCR reaction setups), many commercial diagnostic PCR master mixes substitute 'Deoxyuridine Triphosphate' (dUTP) for dTTP during amplification and pre-treat all new reactions for 10 minutes at 37°C–50°C with which enzyme prior to heat denaturation?",
            [
                "Deoxyribonuclease I (DNase I)",
                "Ribonuclease A (RNase A)",
                "Proteinase K",
                "Uracil-DNA Glycosylase (UDG / UNG, which cleaves uracil-containing carryover amplicons from previous PCR runs while sparing native thymine-containing sample genomic DNA)"
            ],
            3,
            "In the dUTP/UDG carryover prevention system: all PCR reactions are run with dUTP instead of dTTP, so every PCR amplicon ever produced in the laboratory contains Uracil (U). When setting up a new PCR run, the master mix is incubated at 37–50°C with heat-labile Uracil-DNA Glycosylase (UDG/UNG), which excises uracil bases and degrades any contaminating carryover amplicons from past runs (while leaving natural T-containing patient DNA untouched), and UDG is then inactivated during the initial 95°C hot-start step.",
            True,
            TOPIC
        )
    ]
