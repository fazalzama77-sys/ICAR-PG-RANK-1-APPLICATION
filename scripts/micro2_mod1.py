# scripts/micro2_mod1.py
# Module 1: General Bacteriology & Bacterial Genetics (65 questions)

TOPIC = "General Bacteriology & Bacterial Genetics"

def get_module1_questions():
    return [
        (
            "In typical Gram-negative bacterial peptidoglycan (such as Escherichia coli), peptide cross-linking occurs via a direct covalent bond between:",
            [
                "Meso-diaminopimelic acid (m-DAP) at position 3 and D-alanine at position 4",
                "A pentaglycine (Gly5) interbridge connecting L-lysine at position 3 and D-alanine at position 4",
                "Two N-acetylmuramic acid (NAM) sugar residues linked via a beta-1,4-glycosidic oxygen bridge",
                "L-alanine at position 1 and D-glutamic acid at position 2 of adjacent tetrapeptide stems"
            ],
            0,
            "In Gram-negative bacteria (and Bacillus species), the third amino acid of the stem tetrapeptide is meso-diaminopimelic acid (m-DAP), which forms a direct peptide bond with the D-alanine at position 4 of an adjacent peptide chain, whereas Staphylococcus aureus uses a pentaglycine (Gly5) interbridge.",
            True,
            TOPIC
        ),
        (
            "The bacteriocin enzyme 'Lysostaphin', produced by Staphylococcus simulans, selectively lyses Staphylococcus aureus by cleaving:",
            [
                "The beta-1,4-glycosidic linkage between alternating NAM and NAG sugar units",
                "Glycyl-glycine peptide bonds within the pentaglycine cross-bridge",
                "The amide bond connecting N-acetylmuramic acid to the L-alanine stem",
                "Phosphodiester bonds linking wall teichoic acids to peptidoglycan"
            ],
            1,
            "Lysostaphin is a zinc metalloprotease (glycylglycine endopeptidase) that specifically cleaves the pentaglycine (Gly5) cross-bridges unique to Staphylococcus aureus peptidoglycan, making S. aureus highly susceptible while sparing most other bacteria.",
            True,
            TOPIC
        ),
        (
            "Which antibiotic inhibits the very first committed cytoplasmic step of bacterial peptidoglycan synthesis by irreversibly inhibiting MurA (enolpyruvyl transferase)?",
            [
                "D-Cycloserine (structural analog of D-alanine)",
                "Bacitracin (cyclic polypeptide from Bacillus licheniformis)",
                "Fosfomycin (phosphoenolpyruvate analog)",
                "Vancomycin (high-molecular-weight glycopeptide)"
            ],
            2,
            "Fosfomycin is a phosphoenolpyruvate (PEP) analog that irreversibly alkylates the active-site cysteine residue of MurA, preventing the conversion of UDP-NAG to UDP-NAM in the bacterial cytoplasm.",
            True,
            TOPIC
        ),
        (
            "In bacterial cell wall biosynthesis, D-cycloserine exerts its antimicrobial effect by competitively inhibiting which pair of cytoplasmic enzymes?",
            [
                "Transpeptidase (PBP) and D,D-carboxypeptidase in the periplasmic space",
                "Transglycosylase and undecaprenyl pyrophosphate phosphatase in the membrane",
                "MurA enolpyruvyl transferase and MurB reductase in the cytosol",
                "Alanine racemase and D-alanyl-D-alanine synthetase (ligase)"
            ],
            3,
            "D-cycloserine is a structural analog of D-alanine that competitively inhibits both alanine racemase (which converts L-Ala to D-Ala) and D-alanyl-D-alanine ligase, blocking synthesis of the terminal D-Ala-D-Ala dipeptide.",
            True,
            TOPIC
        ),
        (
            "Bacitracin inhibits bacterial cell wall synthesis by binding to undecaprenyl pyrophosphate (bactoprenol-PP, C55-PP) and preventing its:",
            [
                "Dephosphorylation to active bactoprenol monophosphate carrier",
                "Cross-linking to nascent peptidoglycan strands by transpeptidases",
                "Enzymatic condensation with UDP-N-acetylglucosamine in the cytosol",
                "Passive diffusion through trimeric outer membrane porin channels"
            ],
            0,
            "Bactoprenol (undecaprenyl phosphate) is the lipid carrier that translocates NAM-NAG-pentapeptide units across the cytoplasmic membrane. After releasing its cargo, bactoprenol pyrophosphate must be dephosphorylated to bactoprenol monophosphate; bacitracin blocks this step.",
            False,
            TOPIC
        ),
        (
            "In Gram-positive bacteria, Lipoteichoic Acid (LTA) differs structurally from Wall Teichoic Acid (WTA) in that LTA is:",
            [
                "Covalently attached to the C-6 hydroxyl group of N-acetylmuramic acid in peptidoglycan",
                "Anchored via a glycolipid moiety into the outer leaflet of the cytoplasmic membrane",
                "Composed exclusively of poly-gamma-D-glutamic acid capsular polypeptide chains",
                "Restricted solely to acid-fast bacteria of the genera Mycobacterium and Nocardia"
            ],
            1,
            "Wall teichoic acids (WTA) are covalently linked to the peptidoglycan (NAM C-6 hydroxyl), whereas lipoteichoic acids (LTA) are amphiphilic polymers of glycerol phosphate anchored via a glycolipid into the cytoplasmic membrane.",
            False,
            TOPIC
        ),
        (
            "In the cell envelope of Escherichia coli, Braun's lipoprotein (murein lipoprotein, Lpp) serves which critical structural function?",
            [
                "It forms trimeric water-filled channels (porins) for passive diffusion of hydrophilic solutes",
                "It acts as the outer membrane secretin ring for the Type III secretion injectisome",
                "It covalently tethers the outer membrane to the underlying peptidoglycan layer",
                "It polymerizes the O-antigen polysaccharide repeats of lipopolysaccharide"
            ],
            2,
            "Braun's lipoprotein is the most abundant protein in E. coli; its N-terminal lipid moiety inserts into the inner leaflet of the outer membrane, while its C-terminal lysine residue is covalently linked to meso-DAP in the peptidoglycan layer.",
            True,
            TOPIC
        ),
        (
            "Which unique 8-carbon sugar acid directly links the Lipid A moiety to the inner core polysaccharide in the lipopolysaccharide (LPS) of Gram-negative bacteria?",
            [
                "N-Acetylmuramic acid (NAM)",
                "D-Arabinofuranose-5-phosphate",
                "N-Acetylneuraminic acid (sialic acid)",
                "2-Keto-3-deoxyoctulosonic acid (KDO)"
            ],
            3,
            "2-Keto-3-deoxyoctulosonic acid (KDO) and L-glycero-D-manno-heptose are invariant signature sugars of the inner core oligosaccharide of Gram-negative LPS, connecting the phosphorylated glucosamine disaccharide of Lipid A to the outer core.",
            True,
            TOPIC
        ),
        (
            "The transition of Gram-negative bacterial colonies from 'Smooth' (S) to 'Rough' (R) morphology upon serial subculture is caused by:",
            [
                "Loss of the terminal O-specific polysaccharide side chains of LPS",
                "Complete deletion of the endotoxic Lipid A moiety from the outer membrane",
                "Phase variation between H1 and H2 flagellin structural genes",
                "Spontaneous loss of the periplasmic peptidoglycan sacculus"
            ],
            0,
            "Smooth (S) strains possess complete LPS including the hydrophilic, repetitive O-antigen polysaccharide side chain. Mutations blocking O-antigen synthesis expose the core glycolipid, resulting in hydrophobic Rough (R) colonies that autoagglutinate in saline.",
            True,
            TOPIC
        ),
        (
            "The Limulus Amebocyte Lysate (LAL) assay is an ultrasensitive biological test used in pharmaceutical quality control to detect picogram levels of:",
            [
                "Gram-positive bacterial peptidoglycan and wall teichoic acids",
                "Gram-negative bacterial endotoxin (Lipid A / lipopolysaccharide)",
                "Heat-stable staphylococcal enterotoxins in dairy products",
                "Preformed clostridial neurotoxins in contaminated silage"
            ],
            1,
            "Aqueous extracts of blood amebocytes from the Atlantic horseshoe crab (Limulus polyphemus) contain Factor C, a serine protease zymogen activated specifically by Gram-negative LPS (endotoxin), triggering gelation of coagulogen.",
            True,
            TOPIC
        ),
        (
            "When Gram-negative bacteria are treated with lysozyme and EDTA in an osmotically protected medium, the resulting fragile structures retaining outer membrane patches are termed:",
            [
                "Protoplasts (completely devoid of all cell envelope layers outside the plasma membrane)",
                "Bacteroids (nitrogen-fixing differentiated forms inside root nodules)",
                "Spheroplasts (osmotically fragile cells retaining outer membrane remnants)",
                "Elementary bodies (metabolically dormant extracellular infectious units)"
            ],
            2,
            "Unlike Gram-positive protoplasts (which lose their entire cell wall leaving only the cytoplasmic membrane), Gram-negative bacteria treated with EDTA and lysozyme retain residual outer membrane patches and are called spheroplasts.",
            True,
            TOPIC
        ),
        (
            "Cell-wall-deficient variants of walled bacteria that arise after exposure to penicillin and replicate into 'fried-egg'-like colonies on hypertonic media are known as:",
            [
                "Mycoplasmas (permanently wall-less Mollicutes containing sterols)",
                "Minicells (achromosomal spherical buds formed by polar septation)",
                "Rickettsiae (obligate intracellular alphaproteobacteria)",
                "L-forms (Lister Institute reversible wall-deficient variants)"
            ],
            3,
            "First discovered by Emmy Klieneberger-Nobel at the Lister Institute in Streptobacillus moniliformis, L-forms are cell-wall-deficient variants of walled bacteria that can divide in osmotically stabilized media and revert when penicillin is removed.",
            True,
            TOPIC
        ),
        (
            "In the flagellar basal body ultrastructure, Gram-negative bacteria possess four rings (L, P, MS, and C), whereas Gram-positive bacteria possess only:",
            [
                "Two inner rings (the MS ring and C ring)",
                "Two outer rings (the L ring and P ring)",
                "A single periplasmic P ring anchored to teichoic acid",
                "Three outer rings (L, P, and MS) without a cytoplasmic C ring"
            ],
            0,
            "Because Gram-positive bacteria lack an outer membrane and a distinct periplasmic space, their flagellar basal body contains only the inner pair of rings—the MS ring (in the cytoplasmic membrane) and the cytoplasmic C (rotor/switch) ring.",
            True,
            TOPIC
        ),
        (
            "The characteristic corkscrew flexing and rotational motility of pathogenic spirochetes (Leptospira, Borrelia, and Brachyspira) is driven by:",
            [
                "External peritrichous flagella distributed uniformly over the outer membrane",
                "Periplasmic endoflagella (axial filaments) located beneath the outer sheath",
                "Ratchet-like gliding adhesin complexes moving along sulfated slime tracks",
                "ATP-powered extension and retraction of polar Type IV fimbriae"
            ],
            1,
            "Spirochetes possess endoflagella (axial filaments or periplasmic flagella) anchored at each pole that wrap around the helical protoplasmic cylinder inside the periplasmic space beneath the outer sheath.",
            True,
            TOPIC
        ),
        (
            "During chemotaxis in peritrichously flagellated bacteria like Escherichia coli, a smooth forward swimming 'run' is produced when the flagella rotate:",
            [
                "Clockwise (CW), causing the flagellar bundle to fly apart and tumble randomly",
                "Alternately clockwise and counter-clockwise every millisecond via ATP hydrolysis",
                "Counter-clockwise (CCW), coalescing into a single coordinated propulsive bundle",
                "Stationary while cytoplasmic contractile microtubules flex the cell body"
            ],
            2,
            "When flagella rotate counter-clockwise (CCW), their left-handed helices form a cohesive bundle that pushes the bacterium forward in a straight 'run'. When phosphorylated CheY-P binds the motor switch, rotation reverses to clockwise (CW), causing a 'tumble'.",
            False,
            TOPIC
        ),
        (
            "Which specialized bacterial surface appendages mediate 'twitching motility' across moist solid surfaces (as in Moraxella bovis and Dichelobacter nodosus) via PilT ATPase-powered retraction?",
            [
                "Type 1 mannose-sensitive fimbriae (FimH adhesin)",
                "Extracellular curli amyloid fibers",
                "Conjugative F-pili encoded by tra genes",
                "Polar Type IV pili"
            ],
            3,
            "Type IV pili are polar polymeric filaments of pilin that undergo rapid assembly (PilB ATPase) and disassembly/retraction (PilT ATPase), pulling the bacterial cell forward in jerky 'twitching' movements.",
            True,
            TOPIC
        ),
        (
            "Common Type 1 fimbriae (bearing the FimH adhesin at their tip) expressed by Enterobacteriaceae are diagnostically characterized by mediating hemagglutination that is:",
            [
                "Inhibited by the addition of D-mannose (Mannose-Sensitive, MSHA)",
                "Resistant to D-mannose but inhibited by P-blood group galabiose disaccharide",
                "Active only at 4°C and completely eluted from erythrocytes at 37°C",
                "Strictly dependent on exogenous neuraminidase cleavage of sialic acid"
            ],
            0,
            "Type 1 fimbriae bind specifically to alpha-D-mannosylated glycoproteins on host epithelial cells and erythrocytes; adding free D-mannose competitively blocks this binding, defining Mannose-Sensitive Hemagglutination (MSHA).",
            False,
            TOPIC
        ),
        (
            "The 'Type III Secretion System' (T3SS) found in Gram-negative veterinary pathogens such as Salmonella, Yersinia, and Enteropathogenic E. coli functions as a:",
            [
                "Conjugative relaxosome pore that transfers single-stranded plasmid DNA between bacteria",
                "Molecular syringe (injectisome) that translocates effectors directly into host cell cytosol",
                "Tripartite RND efflux pump that exports beta-lactam antibiotics across the outer membrane",
                "Chaperone-usher pathway that assembles adhesive fimbriae on the bacterial surface"
            ],
            1,
            "Evolved from the flagellar basal body, the T3SS injectisome spans both the inner and outer bacterial membranes and inserts a translocation pore into the eukaryotic plasma membrane, injecting virulence effectors directly into the host cell.",
            True,
            TOPIC
        ),
        (
            "In bacterial biofilm formation and density-dependent gene regulation ('Quorum Sensing'), Gram-negative bacteria predominantly use which signaling molecules as autoinducers?",
            [
                "Cyclic thiolactone autoinducing oligopeptides (AIPs of the agr system)",
                "Furanosyl borate diester and phosphorylated teichoic acid dimers",
                "N-Acyl homoserine lactones (AHLs of the LuxI/LuxR system)",
                "Calcium dipicolinate chelates released during stationary phase lysis"
            ],
            2,
            "Gram-negative bacteria use the LuxI/LuxR-type quorum sensing system mediated by freely diffusible N-acyl homoserine lactones (AHLs, Autoinducer-1), whereas Gram-positive bacteria (such as S. aureus) use processed oligopeptides (AIPs).",
            True,
            TOPIC
        ),
        (
            "The metachromatic granules (Babes-Ernst or Volutin granules) observed inside Corynebacterium species when stained with Albert's or Neisser's stain are chemically composed of:",
            [
                "Poly-beta-hydroxybutyrate (PHB) neutral lipid storage polymers",
                "Branched alpha-1,4-glucan glycogen and starch reserves",
                "Intracellular elemental sulfur globules oxidized from H2S",
                "Inorganic polymetaphosphate (polyphosphate) energy reserves"
            ],
            3,
            "Volutin (Babes-Ernst) granules are cytoplasmic linear polymers of orthophosphate (polymetaphosphate). Due to their high negative charge density, they polymerize basic dyes like toluidine blue, shifting the absorption spectrum to stain reddish-purple.",
            True,
            TOPIC
        ),
        (
            "Intracellular lipid inclusion granules composed of Poly-beta-hydroxybutyrate (PHB) found in Bacillus and Burkholderia species are specifically demonstrated microscopically using:",
            [
                "Sudan Black B (or Nile Blue A fat stain)",
                "Albert's stain (Toluidine blue and Malachite green)",
                "Lugol's iodine-potassium iodide solution",
                "Alcian blue and Congo red acidic mucin stain"
            ],
            0,
            "Poly-beta-hydroxybutyrate (PHB) is a neutral carbon-and-energy storage polyester accumulated by Bacillus and Burkholderia species; its lipophilic nature allows specific staining with fat-soluble dyes such as Sudan Black B.",
            True,
            TOPIC
        ),
        (
            "In the Schaeffer-Fulton method for staining bacterial endospores, steaming is applied to drive which primary stain into the spore before counterstaining with Safranin?",
            [
                "Strong Carbol Fuchsin with 5% phenol",
                "5% Aqueous Malachite Green",
                "1% Alkaline Crystal Violet with ammonium oxalate",
                "Polychrome Loeffler's Methylene Blue"
            ],
            1,
            "In the Schaeffer-Fulton endospore stain, 5% aqueous malachite green is forced through the impermeable spore coat by steaming for 5 minutes; water washes malachite green out of the vegetative cytoplasm (stained red by safranin), leaving endospores green.",
            True,
            TOPIC
        ),
        (
            "How does the 'Kinyoun Acid-Fast Stain' (cold method) achieve staining of mycolic acid-rich mycobacterial cell walls without applying heat?",
            [
                "By pre-treating the smear with 10% potassium hydroxide and ethylenediaminetetraacetic acid",
                "By substituting crystal violet and dimethyl sulfoxide (DMSO) for basic fuchsin",
                "By increasing the concentrations of basic fuchsin and phenol in the primary stain",
                "By fixing the slide in alkaline 2% glutaraldehyde vapor for 60 minutes prior to staining"
            ],
            2,
            "Kinyoun's cold acid-fast method increases the concentration of basic fuchsin and lipid-soluble phenol (often with a wetting detergent like Tergitol), enabling penetration of the waxy mycolic acid barrier at room temperature.",
            True,
            TOPIC
        ),
        (
            "In Stamp's modification of the Ziehl-Neelsen stain, weakly acid-fast intracellular pathogens (Brucella, Chlamydia, and Coxiella in placental smears) are differentiated by decolorizing with:",
            [
                "3% hydrochloric acid in 95% ethanol (standard acid-alcohol) for 3 minutes",
                "20% aqueous sulfuric acid combined with absolute acetone for 2 minutes",
                "95% ethanol saturated with picric acid and Lugol's iodine for 5 minutes",
                "0.5% dilute acetic acid (or 0.5–1% sulfuric acid) for 10 to 15 seconds"
            ],
            3,
            "Stamp's modified Ziehl-Neelsen stain uses 0.4–0.5% acetic acid as a gentle decolorizer, followed by methylene blue or malachite green counterstain, allowing weakly acid-fast organisms (Brucella, Coxiella, Chlamydia) to retain red carbol fuchsin.",
            True,
            TOPIC
        ),
        (
            "In 'Ryu's 3% KOH String Test' used to rapidly corroborate the Gram reaction, emulsifying a bacterial colony in a drop of 3% KOH forms a viscous mucoid string within 60 seconds if the organism is:",
            [
                "Gram-negative (alkali lyses the thin wall and releases viscous DNA)",
                "Gram-positive (alkali cross-links thick peptidoglycan and teichoic acids)",
                "Acid-fast (alkali saponifies mycolic acids into viscous soaps)",
                "Endospore-forming (alkali solubilizes cortical calcium dipicolinate)"
            ],
            0,
            "In 3% KOH, the thin peptidoglycan and outer membrane of Gram-negative bacteria rapidly rupture, liberating high-molecular-weight chromosomal DNA that turns the suspension viscous and forms a string when the loop is lifted; Gram-positive walls resist lysis.",
            True,
            TOPIC
        ),
        (
            "For fluorescence microscopy screening of Mycobacterium bovis in smears (Truant's method), which fluorochrome dye pair stains acid-fast bacilli bright yellow-orange against a potassium permanganate-quenched background?",
            [
                "Fluorescein isothiocyanate (FITC) and Tetramethylrhodamine (TRITC)",
                "Auramine O and Rhodamine B",
                "Acridine Orange and Ethidium Bromide",
                "Calcofluor White and Evans Blue"
            ],
            1,
            "Auramine-Rhodamine staining binds to mycolic acids in the mycobacterial cell wall; potassium permanganate is used as a quenching counterstain to eliminate non-specific background fluorescence, allowing rapid scanning at lower magnification.",
            False,
            TOPIC
        ),
        (
            "Which biological indicator organism is internationally recommended for validating the sterilization efficacy of Dry Heat (Hot Air Oven) and Ethylene Oxide gas sterilization?",
            [
                "Geobacillus stearothermophilus spores",
                "Clostridium sporogenes spores",
                "Bacillus atrophaeus (B. subtilis var. niger) spores",
                "Bacillus pumilus radiation-resistant spores"
            ],
            2,
            "While Geobacillus stearothermophilus is the biological indicator for steam autoclaving and hydrogen peroxide plasma, spores of Bacillus atrophaeus (ATCC 9372) are the standard biological indicator for dry heat (160°C) and ethylene oxide gas.",
            True,
            TOPIC
        ),
        (
            "The physical process of 'Inspissation', used to solidify protein-rich media such as Lowenstein-Jensen egg medium or Loeffler's serum slopes without causing steam bubbles, involves heating at:",
            [
                "121°C for 15 minutes at 15 psi in a jacketed steam autoclave",
                "160°C for 120 minutes in a fan-assisted hot air oven",
                "56°C for 30 minutes on three consecutive days in a water bath",
                "80°C to 85°C for 30 to 60 minutes in an inspissator"
            ],
            3,
            "Inspissation coagulates egg and serum proteins smoothly at 80–85°C (below the boiling point of water) so that the agar-free medium solidifies into a smooth slant without foaming or disrupting heat-labile nutrients.",
            True,
            TOPIC
        ),
        (
            "Commercial milk pasteurization temperatures (63°C for 30 min in Holder method, or 72°C for 15 sec in HTST method) were specifically raised and set to ensure complete destruction of which most heat-resistant non-sporing milk-borne pathogen?",
            [
                "Coxiella burnetii (causative agent of Q fever)",
                "Mycobacterium bovis (causative agent of bovine tuberculosis)",
                "Brucella abortus (causative agent of contagious abortion)",
                "Listeria monocytogenes (causative agent of circling disease)"
            ],
            0,
            "Pasteurization temperatures were originally set to kill Mycobacterium bovis, but were later raised slightly (from 61.1°C to 62.8°C/63°C for 30 min) because Coxiella burnetii is the most heat-resistant non-spore-forming pathogen found in raw milk.",
            True,
            TOPIC
        ),
        (
            "Complete inactivation of transmissible spongiform encephalopathy (Prion / PrPSc) infectivity on surgical instruments requires which stringent decontamination regimen?",
            [
                "Immersion in 70% ethyl alcohol or 2% alkaline glutaraldehyde for 60 minutes at room temperature",
                "Immersion in 1N–2N NaOH (or 20,000 ppm bleach) followed by autoclaving at 134°C for 18–60 minutes",
                "Boiling in 1% benzalkonium chloride detergent solution at 100°C for 30 minutes",
                "Exposure to germicidal ultraviolet (UV-C, 254 nm) radiation and ethylene oxide gas for 2 hours"
            ],
            1,
            "Prions are extraordinarily resistant to proteases, UV/ionizing radiation, alcohol, and aldehyde fixatives (like formalin and glutaraldehyde, which stabilize prions). Effective destruction requires strong alkali (1N–2N NaOH) or concentrated bleach plus autoclaving at 134°C.",
            True,
            TOPIC
        ),
        (
            "Before 2% aqueous Glutaraldehyde ('Cidex') can be used as a high-level cold liquid sporicidal sterilant for veterinary endoscopes, it must be 'activated' by adding sodium bicarbonate buffer to:",
            [
                "Acidify the solution to pH 2.5 to liberate nascent chlorine and hydroxyl radicals",
                "Chelate divalent calcium and magnesium ions present in hard tap water",
                "Adjust the pH to alkaline (pH 7.5–8.5), converting it into the active cross-linking form",
                "Stabilize the dialdehyde polymers to extend shelf-life from 14 days to 3 years"
            ],
            2,
            "Acidic aqueous glutaraldehyde is stable in storage but poorly sporicidal. Adding an alkaline buffer raises the pH to 7.5–8.5, activating the dialdehyde groups to alkylate amino and sulfhydryl groups of microbial proteins and nucleic acids.",
            False,
            TOPIC
        ),
        (
            "How does the 'Chick-Martin test' improve upon the classic 'Rideal-Walker test' when determining the Phenol Coefficient of a veterinary disinfectant?",
            [
                "It replaces Salmonella Typhi with Geobacillus stearothermophilus endospores as the test organism",
                "It measures zones of inhibition on Mueller-Hinton agar plates rather than broth tubes",
                "It evaluates virucidal potency against enveloped RNA viruses in cell culture",
                "It incorporates organic matter (3% dried feces or killed yeast suspension) into the test mixture"
            ],
            3,
            "The Rideal-Walker test evaluates disinfectants in pure distilled water, which unrealistically overestimates the potency of halogens and QACs. The Chick-Martin test adds 3% organic matter (dried feces or yeast suspension) to mimic real-world organic load.",
            True,
            TOPIC
        ),
        (
            "Strict obligate anaerobes (such as Clostridium chauvoei, Fusobacterium necrophorum, and Bacteroides fragilis) are killed by atmospheric oxygen primarily because they lack which protective enzymes?",
            [
                "Superoxide dismutase (SOD) and Catalase",
                "Cytochrome c oxidase and Nitrate reductase",
                "DNA gyrase and Topoisomerase IV",
                "Pyruvate:ferredoxin oxidoreductase and Hydrogenase"
            ],
            0,
            "In the presence of oxygen, flavoproteins generate toxic superoxide radicals (O2.-) and hydrogen peroxide (H2O2). Aerobes and facultative anaerobes neutralize these via Superoxide Dismutase and Catalase; strict anaerobes lack one or both enzymes.",
            True,
            TOPIC
        ),
        (
            "In a McIntosh and Fildes or GasPak anaerobic jar, what is the chemical role of the cold palladium-coated alumina pellets placed inside the lid?",
            [
                "They absorb excess carbon dioxide to prevent acidification of the culture media",
                "They catalyze the reaction of evolved hydrogen gas (H2) with atmospheric oxygen (O2) to form water",
                "They serve as a redox indicator that turns from colorless to blue if oxygen leaks in",
                "They generate hydrogen sulfide gas to lower the oxidation-reduction potential (Eh) below -200 mV"
            ],
            1,
            "In anaerobic jars, hydrogen and CO2 are generated from a GasPak envelope. Cold palladium catalyst pellets catalyze the combination of 2H2 + O2 -> 2H2O, removing free oxygen while methylene blue or resazurin serves as the redox indicator.",
            False,
            TOPIC
        ),
        (
            "If a batch culture of bacteria begins with an initial inoculum of 1,000 cells/mL (10^3) and reaches 32,000 cells/mL (3.2 x 10^4) after 100 minutes of exponential growth, what is its generation time (doubling time)?",
            [
                "10 minutes per generation",
                "15 minutes per generation",
                "20 minutes per generation",
                "32 minutes per generation"
            ],
            2,
            "Since 1,000 -> 2,000 (1) -> 4,000 (2) -> 8,000 (3) -> 16,000 (4) -> 32,000 (5), the population doubled exactly n = 5 times in t = 100 minutes. Generation time g = t / n = 100 / 5 = 20 minutes.",
            True,
            TOPIC
        ),
        (
            "When Escherichia coli is grown in a minimal medium containing limiting glucose and excess lactose, it displays a 'Diauxic Growth Curve' (two exponential phases separated by a lag phase) because:",
            [
                "Lactose is utilized first because beta-galactosidase is constitutively expressed at high levels",
                "Half of the bacterial population undergoes spontaneous frame-shift mutation during mid-log phase",
                "Dissolved oxygen is exhausted midway, forcing a metabolic switch from respiration to fermentation",
                "Glucose causes catabolite repression (low cAMP) and inducer exclusion until all glucose is consumed"
            ],
            3,
            "Discovered by Jacques Monod, diauxic growth occurs because glucose inhibits adenylate cyclase (lowering cAMP) and blocks lactose permease (inducer exclusion). Only after glucose is depleted does cAMP rise to activate CAP-cAMP transcription of the lac operon.",
            True,
            TOPIC
        ),
        (
            "A continuous culture apparatus that maintains bacteria in perpetual exponential (log) phase at constant biomass by continuously adding fresh medium with a limiting nutrient while removing spent culture is a:",
            [
                "Chemostat (continuous-flow bioreactor)",
                "Coulter impedance particle counter",
                "McFarland barium sulfate nephelometer",
                "Manometric Warburg respirometer"
            ],
            0,
            "In a chemostat, the specific growth rate (mu) of the bacteria is controlled by the dilution rate (flow rate divided by culture volume), while the steady-state cell density is controlled by the concentration of the limiting nutrient.",
            False,
            TOPIC
        ),
        (
            "Strictly aerobic Gram-negative bacteria such as Pseudomonas aeruginosa that lack phosphofructokinase-1 (PFK-1) catabolize glucose to pyruvate primarily via which alternative pathway?",
            [
                "Embden-Meyerhof-Parnas (EMP) glycolytic pathway",
                "Entner-Doudoroff (ED) pathway (via KDPG intermediate)",
                "Bifidobacterium fructose-6-phosphate phosphoketolase shunt",
                "Stickland coupled amino acid oxidation-reduction pathway"
            ],
            1,
            "The Entner-Doudoroff pathway converts glucose-6-phosphate to 6-phosphogluconate and dehydrates it to the unique intermediate 2-keto-3-deoxy-6-phosphogluconate (KDPG), which is cleaved by KDPG aldolase into pyruvate and glyceraldehyde-3-phosphate.",
            True,
            TOPIC
        ),
        (
            "In the IMViC biochemical series, the Voges-Proskauer (VP) test (using alpha-naphthol and 40% KOH) detects which neutral metabolic intermediate of the 2,3-butanediol fermentation pathway?",
            [
                "Indole ring cleaved from tryptophan by tryptophanase",
                "Mixed organic acids (formic, acetic, lactic, and succinic acids)",
                "Acetoin (acetylmethylcarbinol) oxidized to diacetyl",
                "Alpha-ketoglutarate and phenylpyruvic acid"
            ],
            2,
            "In the presence of atmospheric oxygen, 40% KOH, and alpha-naphthol (Barritt's reagent), acetoin (acetylmethylcarbinol)—an intermediate in 2,3-butanediol fermentation characteristic of Klebsiella and Enterobacter—is oxidized to diacetyl, forming a red complex.",
            True,
            TOPIC
        ),
        (
            "To overcome host 'nutritional immunity' (where free serum Fe3+ is sequestered by transferrin and lactoferrin), pathogenic bacteria secrete low-molecular-weight, high-affinity ferric iron chelators known as:",
            [
                "Bacteriocins (such as colicins, pyocins, and sakacins)",
                "Outer membrane porins (such as OmpF, OmpC, and PhoE)",
                "Heat-shock chaperonins (such as GroEL and DnaK)",
                "Siderophores (such as enterobactin, aerobactin, and mycobactin)"
            ],
            3,
            "Siderophores (e.g., catecholate enterobactin in E. coli, hydroxamate aerobactin, and salicylate mycobactin in Mycobacterium) bind Fe3+ with extremely high affinity and are actively imported via TonB-dependent outer membrane receptors.",
            True,
            TOPIC
        ),
        (
            "In 1944, Avery, MacLeod, and McCarty conclusively proved that DNA—and not protein or RNA—was the 'transforming principle' in Griffith's Streptococcus pneumoniae system by showing that:",
            [
                "Transformation of rough (R) cells into smooth (S) cells was abolished only by DNase",
                "Radioactive 32P entered the bacterial cytoplasm while 35S remained in phage ghosts",
                "Transformation was blocked when cells were separated by a sintered glass filter in a U-tube",
                "Trypsin, chymotrypsin, and RNase completely destroyed the transforming activity of S extracts"
            ],
            0,
            "Avery, MacLeod, and McCarty purified the active transforming extract from heat-killed Type III S pneumococci and showed that trypsin, chymotrypsin, and RNase had no effect, whereas deoxyribonuclease (DNase) completely destroyed transforming activity.",
            True,
            TOPIC
        ),
        (
            "In the classic 1946 Bernard Davis U-tube experiment, separating two auxotrophic strains of Escherichia coli with a sintered glass filter (pore size < 0.2 um) prevented prototrophic recombinants, proving that:",
            [
                "Generalized transduction is mediated by filterable lytic bacteriophages",
                "Bacterial conjugation requires direct cell-to-cell contact between donor and recipient",
                "Natural competence requires secreted competence-stimulating pheromones",
                "Spontaneous antibiotic resistance mutations occur prior to selection"
            ],
            1,
            "In the Davis U-tube, media and any soluble DNA could be flushed back and forth through the fine sintered glass filter, but bacterial cells could not cross. The absence of recombinants proved that E. coli conjugation requires direct physical contact.",
            True,
            TOPIC
        ),
        (
            "During bacterial conjugation between an F+ donor and an F- recipient, why does the F- recipient become F+ while the donor ALSO remains F+?",
            [
                "The donor cell divides by binary fission immediately before transferring both plasmid copies",
                "The F plasmid integrates into the chromosome and excises two copies via reverse transcriptase",
                "The F plasmid undergoes Rolling Circle replication at oriT, transferring one strand while replacing it",
                "Only mRNA transcripts of the F plasmid are transferred through the sex pilus and reverse-transcribed"
            ],
            2,
            "At the origin of transfer (oriT), TraI relaxase nicks one strand of the F plasmid and pilots its 5' end into the F- recipient. Rolling-circle DNA synthesis simultaneously replaces the transferred strand in the donor and synthesizes the complementary strand in the recipient.",
            True,
            TOPIC
        ),
        (
            "When an Hfr (High Frequency of Recombination) donor conjugates with an F- recipient, the recipient acquires donor chromosomal genes at high frequency but almost NEVER becomes F+ or Hfr because:",
            [
                "The integrated F factor is immediately degraded by restriction endonucleases in the recipient",
                "Hfr strains lack sex pili and transfer chromosomal fragments exclusively via phage heads",
                "The recipient cell lacks RecA protein required for homologous chromosomal recombination",
                "The trailing end of the integrated F factor enters last (after 100 min) and mating breaks early"
            ],
            3,
            "In an Hfr cell, the F plasmid is integrated into the 4.6-Mb E. coli chromosome. Nicking at oriT transfers the leading end of F followed by chromosomal genes, taking ~100 minutes to transfer the entire chromosome and the trailing end of F; mating bridges break much earlier.",
            True,
            TOPIC
        ),
        (
            "The transfer of chromosomal genes carried on an autonomous F' (F-prime) episome into a recipient cell that already possesses its own chromosomal alleles for those genes creates a partially diploid bacterium called a:",
            [
                "Merozygote (partial diploid formed by sexduction)",
                "Heterokaryon (dikaryotic fungal anastomosis cell)",
                "Protoplast (osmotically fragile wall-less cell)",
                "Lysogen (bacterium carrying a repressed prophage)"
            ],
            0,
            "Because an F' plasmid is an autonomous, self-replicating episome carrying excised bacterial chromosomal genes (e.g., F' lac+), its transfer into an F- recipient creates a stable partial diploid (merozygote) for those specific chromosomal loci—a process called sexduction.",
            True,
            TOPIC
        ),
        (
            "Norton Zinder and Joshua Lederberg (1952) discovered bacterial 'Transduction' while studying genetic recombination in which bacterium-bacteriophage system?",
            [
                "Escherichia coli K-12 and temperate bacteriophage Lambda",
                "Salmonella enterica serovar Typhimurium and temperate phage P22",
                "Corynebacterium diphtheriae and toxigenic Corynephage Beta",
                "Bacillus subtilis and generalized transducing phage PBS1"
            ],
            1,
            "Zinder and Lederberg placed two auxotrophic strains of Salmonella Typhimurium (LT2 and LT22) in opposite arms of a Davis U-tube separated by a glass filter and still obtained prototrophs; the filterable DNase-resistant agent was identified as temperate phage P22.",
            True,
            TOPIC
        ),
        (
            "In Specialized Transduction mediated by temperate bacteriophage Lambda in Escherichia coli, why are only the 'gal' (galactose) and 'bio' (biotin) genes transduced?",
            [
                "Phage Lambda head capsids can package only DNA sequences rich in galactose-binding motifs",
                "All other chromosomal genes are degraded by Lambda exonuclease during the lytic cycle",
                "Phage Lambda integrates site-specifically at attB located precisely between gal and bio",
                "The gal and bio operons are located on an autonomous conjugative plasmid co-packaged by Lambda"
            ],
            2,
            "Unlike generalized transducing phages (P1, P22) that randomly package any chromosomal fragment, phage Lambda integrates via Campbell-type site-specific recombination at attB (between gal and bio). Rare imprecise excision generates defective lambda-dgal or lambda-dbio particles.",
            True,
            TOPIC
        ),
        (
            "Which group of bacterial exotoxins is a classic example of 'Lysogenic Conversion' (Phage Conversion), where a temperate prophage integrated into the bacterial chromosome directly encodes the toxin structural gene?",
            [
                "Protective Antigen, Edema Factor, and Lethal Factor of Bacillus anthracis (pXO1)",
                "Alpha-toxin (phospholipase C) and Theta-toxin of Clostridium perfringens",
                "Heat-stable (STa) and Heat-labile (LT) enterotoxins of Enterotoxigenic E. coli",
                "Shiga toxins (Stx1/Stx2) of E. coli O157:H7 and Botulinum neurotoxins C1 and D"
            ],
            3,
            "Lysogenic (phage) conversion occurs when a temperate prophage encodes a virulence trait. Classic examples include Diphtheria toxin (beta-phage), Botulinum toxins C1 and D (c and d phages), Shiga toxins Stx1/Stx2 (lambdoid phages), Cholera toxin (CTXphi), and S. pyogenes erythrogenic toxin SpeA.",
            True,
            TOPIC
        ),
        (
            "The prokaryotic adaptive immune system known as 'CRISPR-Cas' protects bacteria against invading bacteriophages and conjugative plasmids by:",
            [
                "Using spacer-derived crRNAs to guide Cas endonucleases to cleave invading DNA next to a PAM motif",
                "Methylating cytosine and adenine bases at palindromic restriction sites across the host genome",
                "Secreting soluble immunoglobulin-like proteins into the periplasm to neutralize phage tails",
                "Downregulating outer membrane porins and sex pili upon sensing N-acyl homoserine lactones"
            ],
            0,
            "CRISPR arrays capture short 'spacer' fragments from invading phage/plasmid DNA. Upon re-infection, transcribed crRNAs guide Cas nucleases (such as Cas9) to cleave matching target DNA sequences adjacent to a short Protospacer Adjacent Motif (PAM).",
            True,
            TOPIC
        ),
        (
            "In the regulation of the repressible Tryptophan (trp) operon of Escherichia coli, high intracellular levels of tryptophan arrest transcription through which two cooperative mechanisms?",
            [
                "Cleavage of the TrpR repressor by activated RecA protease AND cAMP-CAP dissociation",
                "Binding of tryptophan as corepressor to TrpR AND ribosome-mediated leader peptide attenuation",
                "Phosphorylation of the RNA polymerase sigma-70 subunit AND methylation of the promoter TATA box",
                "Antisense RNA degradation by RNase III AND Rho-dependent premature termination in trpA"
            ],
            1,
            "Tryptophan acts as a corepressor that binds the inactive TrpR aporepressor, enabling it to bind the operator. Additionally, when Trp-tRNA is abundant, rapid translation across tandem Trp codons in the leader peptide (trpL) causes mRNA regions 3 and 4 to form a transcription-terminating hairpin (attenuation).",
            False,
            TOPIC
        ),
        (
            "The classic 'Fluctuation Test' (Luria and Delbrück, 1943) and 'Replica Plating Experiment' (Joshua and Esther Lederberg, 1952) established which fundamental principle of bacterial genetics?",
            [
                "Antibiotics directly induce adaptive directed mutations in the target genes of exposed bacteria",
                "Resistance genes are acquired exclusively through horizontal plasmid transfer from soil actinomycetes",
                "Mutations conferring phage or antibiotic resistance arise spontaneously BEFORE selective exposure",
                "All bacterial point mutations revert to wild-type when incubated below 22°C in minimal medium"
            ],
            2,
            "Luria & Delbrück's high variance across independent parallel cultures and the Lederbergs' indirect velvet-pad replica plating (isolating antibiotic-resistant colonies that had never touched the antibiotic) proved that bacterial mutations are pre-adaptive, random, and spontaneous.",
            True,
            TOPIC
        ),
        (
            "Two different plasmids belonging to the same 'Plasmid Incompatibility (Inc) Group' cannot be stably maintained together in the same bacterial cell line because they:",
            [
                "Encode mutually destructive Type II restriction-modification endonucleases",
                "Synthesize incompatible sex pili that trigger lethal outer membrane rupture",
                "Integrate into the exact same tRNA gene locus on the host chromosome",
                "Share identical replication control (ori) or partitioning (par) systems"
            ],
            3,
            "Plasmids are classified into Inc groups based on their ability to coexist in the same cell. Two plasmids of the same Inc group compete for the same negative-feedback replication initiator or partitioning machinery, causing segregation loss during division.",
            False,
            TOPIC
        ),
        (
            "In laboratory genetics, 'Plasmid Curing' (the artificial elimination of plasmids from host bacteria without killing the cell) is routinely accomplished by growing bacteria in sub-inhibitory concentrations of:",
            [
                "Intercalating dyes such as Acridine Orange or Ethidium Bromide",
                "Cell-wall active beta-lactam antibiotics such as Penicillin G",
                "Lysozyme and EDTA in hypertonic 20% sucrose buffer",
                "Alkylating cold sterilants such as 2% alkaline Glutaraldehyde"
            ],
            0,
            "Intercalating agents like acridine orange and ethidium bromide (as well as SDS or growth at 42–43°C) preferentially inhibit supercoiled plasmid DNA replication without halting chromosomal replication, yielding plasmid-free ('cured') daughter cells.",
            True,
            TOPIC
        ),
        (
            "Methicillin-Resistant Staphylococcus aureus (MRSA) and Methicillin-Resistant Staphylococcus pseudintermedius (MRSP) exhibit broad resistance to beta-lactams due to the mobile SCCmec element carrying:",
            [
                "The blaZ gene encoding an inducible narrow-spectrum extracellular penicillinase",
                "The mecA (or mecC) gene encoding low-affinity Penicillin-Binding Protein 2a (PBP2a)",
                "The vanA gene cluster encoding D-Ala-D-Lac depsipeptide synthetase",
                "The ermB gene encoding a 23S rRNA adenine N6-methyltransferase"
            ],
            1,
            "The mecA gene located on the mobile Staphylococcal Cassette Chromosome mec (SCCmec) encodes PBP2a (PBP2'), a transpeptidase whose active site has extremely low affinity for beta-lactam rings, allowing cell wall synthesis to continue in the presence of beta-lactams.",
            True,
            TOPIC
        ),
        (
            "High-level Vancomycin resistance in Enterococci (VRE) and Staphylococcus aureus (VRSA) mediated by the vanA gene cluster (carried on transposon Tn1546) operates through:",
            [
                "Production of an extracellular periplasmic glycopeptide-hydrolyzing esterase",
                "Overexpression of the tripartite AcrAB-TolC multidrug efflux pump",
                "Replacement of the terminal D-Ala-D-Ala peptidoglycan target with D-Ala-D-Lac",
                "Dimethylation of the 16S rRNA decoding site on the 30S ribosomal subunit"
            ],
            2,
            "Vancomycin binds via five hydrogen bonds to the terminal D-Ala-D-Ala motif of nascent peptidoglycan pentapeptides. The vanA operon synthesizes the depsipeptide D-Alanyl-D-Lactate (D-Ala-D-Lac), eliminating a critical hydrogen bond and reducing vancomycin affinity by ~1,000-fold.",
            True,
            TOPIC
        ),
        (
            "New Delhi Metallo-beta-lactamase-1 (blaNDM-1), which confers carbapenem resistance in Enterobacteriaceae, belongs to Ambler Class B and is uniquely characterized by:",
            [
                "Using a catalytic active-site serine residue that is strongly inhibited by clavulanic acid",
                "Hydrolyzing only narrow-spectrum penicillins while sparing oxyimino-cephalosporins",
                "Being chromosomally restricted to obligate anaerobic Gram-positive spore-formers",
                "Requiring active-site Zinc ions (Zn2+) and being inhibited by EDTA but NOT by clavulanate"
            ],
            3,
            "Ambler Class B enzymes (NDM-1, IMP, VIM) are metallo-beta-lactamases requiring one or two Zn2+ ions at their active site. They hydrolyze penicillins, cephalosporins, and carbapenems, are resistant to serine beta-lactamase inhibitors (clavulanate, tazobactam), and are inhibited by EDTA.",
            True,
            TOPIC
        ),
        (
            "Classical Extended-Spectrum Beta-Lactamases (ESBLs, such as CTX-M, TEM, and SHV variants) in Escherichia coli and Klebsiella pneumoniae are phenotypically confirmed in diagnostic laboratories by demonstrating that:",
            [
                "Cefotaxime/ceftazidime resistance is reversed in the presence of Clavulanic acid",
                "The isolate is resistant to imipenem and meropenem but susceptible to ampicillin",
                "Resistance is inducible by cefoxitin and completely unaffected by clavulanic acid",
                "Beta-lactamase activity is abolished by adding 0.5 M EDTA to the disc"
            ],
            0,
            "Classical Ambler Class A ESBLs hydrolyze penicillins, 3rd/4th-generation oxyimino-cephalosporins (cefotaxime, ceftazidime), and aztreonam, but remain susceptible to cephamycins (cefoxitin) and carbapenems, and are strongly inhibited by clavulanic acid (increasing zone diameter by >= 5 mm).",
            True,
            TOPIC
        ),
        (
            "Plasmid-mediated resistance to Colistin (Polymyxin E) in Gram-negative bacteria is conferred by the globally disseminated 'mcr-1' gene, which encodes a:",
            [
                "Metallo-protease that cleaves the cyclic heptapeptide ring of polymyxin E",
                "Phosphoethanolamine transferase that modifies Lipid A to reduce its negative charge",
                "Ribosomal protection protein that displaces colistin from the 50S subunit",
                "Porin channel repressor that blocks diffusion of colistin into the periplasm"
            ],
            1,
            "Polymyxins (Polymyxin B and Colistin) are cationic lipopeptides that electrostatically bind negatively charged phosphate groups of Lipid A. The mcr-1 gene encodes a phosphoethanolamine transferase that adds positively charged phosphoethanolamine to Lipid A, repelling colistin.",
            True,
            TOPIC
        ),
        (
            "Cross-resistance to Macrolides (tylosin), Lincosamides (lincomycin), and Streptogramin B antibiotics—the 'MLSB phenotype'—is mediated by erm genes through:",
            [
                "Acetylation of the 16S rRNA decoding region on the 30S ribosomal subunit",
                "Enzymatic hydrolysis of the macrolide lactone ring by erythromycin esterase",
                "Dimethylation of adenine-2058 in the 23S rRNA of the 50S ribosomal subunit",
                "Point mutation in the beta-subunit of DNA-dependent RNA polymerase (rpoB)"
            ],
            2,
            "Although chemically distinct, Macrolides, Lincosamides, and Streptogramin B all bind overlapping sites in the peptidyl transferase center (23S rRNA) of the 50S ribosomal subunit. Methylation of A2058 by Erm methyltransferases blocks binding of all three classes.",
            True,
            TOPIC
        ),
        (
            "Which pair of veterinary antibiotic classes inhibits bacterial protein synthesis specifically by binding to the 30S ribosomal subunit?",
            [
                "Macrolides (tylosin, tilmicosin) and Phenicols (florfenicol, chloramphenicol)",
                "Lincosamides (lincomycin, clindamycin) and Pleuromutilins (tiamulin)",
                "Oxazolidinones (linezolid) and Streptogramins (virginiamycin)",
                "Aminoglycosides (gentamicin, streptomycin) and Tetracyclines (oxytetracycline)"
            ],
            3,
            "Both Aminoglycosides (which bind 16S rRNA in the 30S subunit, causing mRNA misreading and initiation freeze) and Tetracyclines (which bind the 30S subunit to block aminoacyl-tRNA attachment to the A-site) target the 30S subunit, whereas macrolides, phenicols, lincosamides, and pleuromutilins target the 50S subunit.",
            True,
            TOPIC
        ),
        (
            "Why are obligate anaerobic bacteria (such as Clostridium and Bacteroides) intrinsically resistant to all Aminoglycoside antibiotics (gentamicin, amikacin, streptomycin)?",
            [
                "Uptake of polar aminoglycosides across the inner membrane requires an O2-dependent electron transport chain",
                "Obligate anaerobes possess 80S eukaryotic-type ribosomes instead of 70S prokaryotic ribosomes",
                "Anaerobes constitutively secrete extracellular aminoglycoside-modifying acetyltransferases",
                "Aminoglycosides are chemically reduced and precipitated by hydrogen sulfide gas in anaerobic tissues"
            ],
            0,
            "Penetration of polycationic aminoglycosides across the inner cytoplasmic membrane (Energy-Dependent Phase I) is strictly driven by the transmembrane electrical potential generated by oxidative phosphorylation (respiratory quinones/cytochromes), which obligate anaerobes lack.",
            True,
            TOPIC
        ),
        (
            "Fluoroquinolone antibiotics (such as enrofloxacin, marbofloxacin, and ciprofloxacin) exert rapid bactericidal activity by trapping covalent enzyme-DNA cleavage complexes of:",
            [
                "Topoisomerase I (Topo I) and the replicative DnaB helicase hexamer",
                "DNA Gyrase (GyrA/GyrB) and Topoisomerase IV (ParC/ParE)",
                "DNA Polymerase III holoenzyme and NAD-dependent DNA Ligase",
                "RNA Polymerase sigma-70 factor and the LexA SOS repressor"
            ],
            1,
            "Fluoroquinolones target bacterial Type II topoisomerases: DNA gyrase (which introduces negative supercoils ahead of the replication fork; primary target in Gram-negatives) and Topoisomerase IV (which decatenates daughter chromosomes; primary target in many Gram-positives).",
            True,
            TOPIC
        ),
        (
            "The bactericidal synergy achieved by combining a Sulfonamide with Trimethoprim ('potentiated sulfonamides' / co-trimazine) results from sequential blockade of which two enzymes in the bacterial folate pathway?",
            [
                "Para-aminobenzoic acid (PABA) synthase and Thymidylate synthase",
                "Alanine racemase and D-alanyl-D-alanine synthetase",
                "Dihydropteroate synthase (DHPS) and Dihydrofolate reductase (DHFR)",
                "Enolpyruvyl transferase (MurA) and Dihydroorotate dehydrogenase"
            ],
            2,
            "Bacteria must synthesize tetrahydrofolate de novo from PABA. Sulfonamides (structural analogs of PABA) competitively inhibit dihydropteroate synthase (DHPS), while diaminopyrimidines (trimethoprim, ormetoprim) inhibit dihydrofolate reductase (DHFR).",
            True,
            TOPIC
        ),
        (
            "Rifampicin (Rifampin), a cornerstone drug in the treatment of Rhodococcus equi pneumonia in foals and mycobacterial infections, acts by binding directly to the:",
            [
                "50S ribosomal subunit 23S rRNA peptidyl transferase center",
                "Arabinogalactan mycolyltransferase enzyme (EmbB) in the acid-fast cell wall",
                "Alpha-subunit of bacterial DNA gyrase (encoded by gyrA)",
                "Beta-subunit of bacterial DNA-dependent RNA polymerase (encoded by rpoB)"
            ],
            3,
            "Rifampicin binds with high affinity to the beta-subunit of bacterial DNA-dependent RNA polymerase (encoded by rpoB), sterically blocking elongation of the nascent RNA chain. Single-step point mutations in rpoB confer high-level resistance.",
            True,
            TOPIC
        ),
        (
            "In molecular genetics, a 'Nonsense Mutation' designated historically as an 'Amber Mutation' refers specifically to a base substitution that generates which mRNA premature stop codon?",
            [
                "5'-UAG-3' (whereas 5'-UAA-3' is Ochre and 5'-UGA-3' is Opal)",
                "5'-UAA-3' (whereas 5'-UAG-3' is Opal and 5'-UGA-3' is Amber)",
                "5'-UGA-3' (whereas 5'-UAG-3' is Ochre and 5'-UAA-3' is Amber)",
                "5'-AUG-3' (whereas 5'-GUG-3' is Ochre and 5'-UUG-3' is Opal)"
            ],
            0,
            "The three nonsense (stop) codons in bacterial genetics are designated by trivial names: Amber (UAG, named after Harris Bernstein, whose German surname means amber), Ochre (UAA), and Opal/Umber (UGA).",
            False,
            TOPIC
        ),
        (
            "In the Hershey-Chase 'Waring Blender Experiment' (1952) using T2 bacteriophage infecting Escherichia coli, which radioactive isotope selectively labeled the phage DNA that entered the bacterial host cell?",
            [
                "Radioactive Sulfur-35 (35S) incorporated into cysteine and methionine",
                "Radioactive Phosphorus-32 (32P) incorporated into the sugar-phosphate backbone",
                "Radioactive Carbon-14 (14C) incorporated into outer capsid lipoproteins",
                "Radioactive Iodine-125 (125I) conjugated to phage tail fibers"
            ],
            1,
            "Alfred Hershey and Martha Chase labeled T2 phage protein coats with 35S (since DNA contains no sulfur) and phage DNA with 32P (since proteins contain virtually no phosphorus). After shearing phage ghosts off cells in a blender, 32P remained inside the bacteria and appeared in progeny phage.",
            True,
            TOPIC
        ),
        (
            "During bacterial DNA replication in Escherichia coli, which enzyme uses ATP energy to introduce negative supercoils into circular chromosomal DNA and relax positive supercoils accumulating ahead of the DnaB replication fork?",
            [
                "DNA Topoisomerase I (omega protein, which relaxes negative supercoils without ATP)",
                "Single-stranded DNA-binding protein (SSB, which stabilizes unwound templates)",
                "DNA Gyrase (a bacterial Type II topoisomerase tetramer of GyrA2GyrB2)",
                "DNA Polymerase I (Kornberg enzyme possessing 5' to 3' exonuclease activity)"
            ],
            2,
            "DNA gyrase is a unique bacterial Type II topoisomerase (composed of two GyrA and two GyrB subunits) that hydrolyzes ATP via GyrB to pass a double-stranded DNA segment through a transient double-strand break created by GyrA, introducing negative supercoils.",
            False,
            TOPIC
        ),
        (
            "On the lagging strand of replicating bacterial DNA, who synthesizes the short RNA primers (10–12 nucleotides) required to initiate each Okazaki fragment, and which enzyme subsequently removes those RNA primers?",
            [
                "RNA Polymerase holoenzyme synthesizes primers; RNase H removes them",
                "DNA Polymerase III synthesizes primers; DNA Ligase removes them",
                "Helicase DnaB synthesizes primers; Topoisomerase IV removes them",
                "Primase (DnaG) synthesizes primers; DNA Polymerase I (5'->3' exonuclease) removes them"
            ],
            3,
            "In bacteria, DnaG primase synthesizes the short RNA primers for Okazaki fragments, DNA Polymerase III extends them, DNA Polymerase I removes the RNA primers via its 5'->3' exonuclease domain while filling the gap via its polymerase domain, and DNA ligase seals the nick.",
            True,
            TOPIC
        ),
        (
            "Unlike eukaryotic mRNAs (which bind the 40S ribosome via a 5' 7-methylguanosine cap), prokaryotic mRNAs initiate translation by base-pairing a purine-rich ribosome-binding site (5'-AGGAGG-3') located 5–10 bases upstream of the AUG start codon with:",
            [
                "The 3' end of the 16S rRNA within the 30S ribosomal subunit (Shine-Dalgarno interaction)",
                "The 5' end of the 23S rRNA within the 50S ribosomal subunit (Peptidyl transferase center)",
                "The anticodon loop of initiator N-formylmethionyl-tRNA (fMet-tRNAfMet)",
                "The Rho (p) hexameric transcription termination helicase factor"
            ],
            0,
            "The Shine-Dalgarno sequence (consensus 5'-AGGAGGU-3') on prokaryotic polycistronic mRNA base-pairs directly with the complementary anti-Shine-Dalgarno pyrimidine tract at the 3' end of 16S rRNA in the 30S ribosomal subunit, aligning the AUG start codon in the P-site.",
            True,
            TOPIC
        ),
        (
            "In prokaryotic translation initiation, the very first amino acid incorporated at the N-terminus of every nascent bacterial polypeptide chain (encoded by the start codon 5'-AUG-3' or 5'-GUG-3') is:",
            [
                "Unmodified L-Methionine carried by eukaryotic-type Met-tRNAi",
                "N-Formylmethionine (fMet) carried by initiator fMet-tRNAfMet",
                "D-Alanine synthesized by cytoplasmic alanine racemase",
                "N-Acetylglutamate activated by initiation factor IF-2"
            ],
            1,
            "Bacteria initiate protein synthesis with N-formylmethionine (fMet), which is later removed from most mature proteins by peptide deformylase and methionine aminopeptidase; eukaryotic cytosolic ribosomes use unmodified methionine.",
            True,
            TOPIC
        ),
        (
            "How does 'Intrinsic (Rho-independent) Transcription Termination' occur at the 3' end of bacterial genes?",
            [
                "The hexameric ATP-dependent helicase Rho translocates along mRNA and unwinds the RNA-DNA hybrid",
                "Cleavage of the nascent transcript by endoribonuclease E followed by polyadenylation",
                "Formation of a GC-rich self-complementary mRNA stem-loop hairpin followed by a run of 6–8 Uracils (poly-U)",
                "Binding of the sigma-70 initiation factor to the C-terminal domain of RNA polymerase"
            ],
            2,
            "Intrinsic (Rho-independent) terminators consist of a GC-rich inverted repeat that folds into a stable stem-loop hairpin in the nascent RNA (stalling RNA polymerase), immediately followed by a stretch of 6–8 U residues whose weak rU-dA base-pairing allows the transcript to dissociate.",
            False,
            TOPIC
        ),
        (
            "When bacteria are exposed to ultraviolet (UV) light at 254–260 nm, the primary lethal DNA lesion formed is:",
            [
                "Interstrand cross-linking between opposing guanine and cytosine bases",
                "Depurination of adenine residues and oxidation of deoxyribose rings",
                "Single-stranded nicks at methylated GATC Dam recognition sequences",
                "Intrastrand cyclobutane pyrimidine dimers (thymine-thymine dimers)"
            ],
            3,
            "UV-C radiation (peaking near the 260 nm absorption maximum of DNA) induces covalent cyclobutane rings between adjacent pyrimidine bases (primarily thymine-thymine dimers) on the same DNA strand, distorting the helix and blocking replication.",
            True,
            TOPIC
        ),
        (
            "In bacterial DNA repair of UV-induced thymine dimers, 'Photoreactivation' (light repair) directly monomerizes the cyclobutane ring in the presence of visible blue light (300–500 nm) using which enzyme?",
            [
                "DNA Photolyase (encoded by phr, utilizing FADH- and folate chromophores)",
                "UvrABC excinuclease complex (nucleotide excision repair endonuclease)",
                "MutS-MutL-MutH methyl-directed mismatch repair complex",
                "Error-prone DNA Polymerase V (UmuD'2C translesion polymerase)"
            ],
            0,
            "DNA photolyase binds specifically to cyclobutane pyrimidine dimers in the dark and, upon absorbing a photon of visible blue/near-UV light (350–450 nm), transfers an electron from FADH- to split the dimer directly back into two normal thymine bases without excising nucleotides.",
            False,
            TOPIC
        ),
        (
            "In the 'Dark Repair' (Nucleotide Excision Repair) of bulky DNA lesions and thymine dimers in Escherichia coli, which endonuclease complex makes dual incisions flanking the damaged nucleotides so UvrD helicase can release the 12-mer oligomer?",
            [
                "The MutS, MutL, and MutH hemimethylated GATC repair complex",
                "The UvrABC excinuclease complex (UvrA, UvrB, and UvrC proteins)",
                "The RecBCD exonuclease V and Chi-site recombinase complex",
                "Uracil-DNA glycosylase and Apurinic/Apyrimidinic (AP) endonuclease"
            ],
            1,
            "In Nucleotide Excision Repair (dark repair), the UvrA2B complex scans DNA for helical distortions (such as thymine dimers), UvrB melts the DNA and recruits UvrC endonuclease to cleave 8 nucleotides 5' and 4–5 nucleotides 3' to the lesion, and DNA Pol I + ligase fill the gap.",
            True,
            TOPIC
        ),
        (
            "What is the primary antiseptic mechanism and distinctive clinical advantage of 2% Chlorhexidine gluconate in veterinary surgical scrubs and teat dips?",
            [
                "It alkylates spore DNA at 121°C and completely inactivates prion proteins within 30 seconds",
                "It oxidizes bacterial sulfhydryl groups by liberating nascent oxygen gas upon contact with catalase",
                "It is a cationic bisbiguanide that disrupts membranes and binds skin proteins for residual activity",
                "It is an anionic phenolic coal-tar derivative that selectively dissolves acid-fast mycolic acid waxes"
            ],
            2,
            "Chlorhexidine is a cationic bisbiguanide antiseptic that disrupts cytoplasmic membranes of Gram-positive and Gram-negative bacteria (though non-sporicidal) and binds strongly to negatively charged proteins in skin and mucous membranes ('substantivity'), providing persistent residual antimicrobial activity.",
            True,
            TOPIC
        ),
        (
            "In Methyl-Directed Mismatch Repair (MMR) of newly replicated Escherichia coli DNA, how does the MutS-MutL-MutH enzyme system distinguish the newly synthesized daughter strand (containing the replication error) from the parental template strand?",
            [
                "The parental strand carries full N6-adenine methylation at 5'-GATC-3' sequences (by Dam methylase), whereas the nascent daughter strand is transiently unmethylated",
                "The nascent daughter strand contains thymine dimers, whereas the parental strand contains only uracil bases",
                "The parental strand is covalently bound to histone H1 proteins, whereas the daughter strand is naked",
                "The nascent daughter strand is synthesized entirely of ribonucleotides before RNase H conversion"
            ],
            0,
            "Dam (DNA adenine methylase) methylates the adenine in palindromic 5'-GATC-3' sequences. Immediately after passage of the replication fork, the newly synthesized daughter strand is transiently unmethylated (hemimethylated duplex), directing MutH endonuclease to nick only the unmethylated daughter strand.",
            False,
            TOPIC
        ),
        (
            "Which mobile genetic element is the simplest autonomous transposable element in bacteria, encoding ONLY the transposase enzyme required for its own movement flanked by short inverted repeats (IRs), without carrying any antibiotic resistance or virulence genes?",
            [
                "Composite Transposon (such as Tn5, Tn9, or Tn10)",
                "Insertion Sequence (IS element, such as IS1 or IS3)",
                "Conjugative Resistance Plasmid (R-factor)",
                "Class 1 Resistance Integron (intI1 cassette array)"
            ],
            1,
            "An Insertion Sequence (IS element, ~750–1,500 bp) is the simplest transposable element, consisting solely of a single open reading frame encoding transposase flanked by short terminal inverted repeats (15–40 bp), without accessory resistance or toxin genes.",
            True,
            TOPIC
        ),
        (
            "During preparation of Loeffler's Alkaline Methylene Blue stain for demonstrating metachromatic granules, a dilute alkali (0.01% potassium hydroxide) is added specifically to:",
            [
                "Precipitate crystal violet-iodine complexes inside the periplasmic space",
                "Dissolve the waxy mycolic acid layer of acid-fast mycobacteria at room temperature",
                "Enhance dye penetration and promote oxidative 'ripening' into polychrome azure dyes",
                "Decolorize non-sporing vegetative cells during endospore counterstaining"
            ],
            2,
            "Loeffler's methylene blue contains 0.01% KOH, which increases the basophilia of bacterial chromatin/volutin granules and accelerates oxidative demethylation ('polychroming' or aging) of methylene blue into azure A, azure B, and methylene violet.",
            False,
            TOPIC
        ),
        (
            "In the 'Kelsey-Sykes Capacity Test' for evaluating veterinary disinfectants, what specific parameter is measured that is not assessed by the Rideal-Walker test?",
            [
                "The vapor-phase sporicidal penetration of formaldehyde gas through porous cotton fabrics",
                "The minimum inhibitory concentration (MIC) of systemic antibiotics in Mueller-Hinton broth",
                "The ability of a membrane filter to retain Serratia marcescens under positive pressure",
                "The capacity of a disinfectant to retain bactericidal activity after successive additions of bacteria under clean and dirty conditions"
            ],
            3,
            "The Kelsey-Sykes test is a triple-challenge 'capacity test' in which bacterial suspensions (in clean broth or dirty yeast/serum suspension) are added in three successive increments at 0, 10, and 20 minutes to determine the safe use-dilution that retains killing power under repeated organic loading.",
            False,
            TOPIC
        )
    ]

