# scripts/micro_mod3_genbact.py
# Module 3: General Bacteriology, Genetics & Physiology (45 Questions)
# Aligned with ICAR AIEEA (PG) M.V.Sc. Syllabus Code 13 Unit II

def get_module3_questions():
    qs = [
        # 1-10: Bacterial structure, cell wall, peptidoglycan, LPS
        ("The primary structural component providing mechanical rigidity and osmotic shape protection to the eubacterial cell wall is:",
         ["Peptidoglycan (Murein / Mucopeptide)", "Phospholipid bilayer", "Cellulose", "Chitin"],
         0, "Peptidoglycan is a giant bag-shaped cross-linked heteropolymer composed of alternating beta-(1,4)-linked N-acetylglucosamine (NAG) and N-acetylmuramic acid (NAM) residues cross-linked by short oligopeptide chains.",
         True, "General Bacteriology (ICAR PG PYQ)"),

        ("Gram-positive bacterial cell walls differ from Gram-negative bacterial cell walls by having a:",
         ["Thick (20-80 nm) multilayered peptidoglycan meshwork containing Teichoic and Lipoteichoic acids, and lacking an outer membrane", "Thin peptidoglycan layer enclosed by an outer membrane", "Lipopolysaccharide layer with lipid A", "Periplasmic space occupying 40% of the volume"],
         0, "Gram-positive walls have thick, multi-layered peptidoglycan (up to 40 layers, 20-80 nm) decorated with polyol phosphate polymers (wall teichoic acid and lipoteichoic acid), lacking the outer membrane found in Gram-negative bacteria.",
         True, "General Bacteriology (ICAR PG PYQ)"),

        ("In the Gram-negative bacterial outer membrane, the toxic, bioactive moiety responsible for endotoxic shock, pyrogenicity, and macrophage activation is:",
         ["Lipid A of the Lipopolysaccharide (LPS)", "Core polysaccharide", "O-specific polysaccharide antigen side chain", "Braun's lipoprotein"],
         0, "LPS (endotoxin) consists of three domains: Lipid A (a phosphorylated glucosamine disaccharide with multiple fatty acid chains anchor), core oligosaccharide, and O-antigen. Lipid A is the toxic component that binds TLR-4.",
         True, "General Bacteriology (ICAR PG PYQ)"),

        ("The natural enzyme Lysozyme (present in tears, saliva, and egg white) cleaves which specific chemical bond in bacterial peptidoglycan?",
         ["Beta-(1,4)-glycosidic bond between N-acetylmuramic acid (NAM) and N-acetylglucosamine (NAG)", "Peptide bond linking L-alanine to D-glutamic acid", "Disulfide bonds", "Phosphodiester bonds"],
         0, "Lysozyme is an endo-N-acetylmuramidase that selectively hydrolyzes the beta-(1,4) glycosidic linkage between C-1 of NAM and C-4 of NAG in peptidoglycan, causing cell lysis in hypotonic media.",
         True, "General Bacteriology (ICAR PG PYQ)"),

        ("Gram-positive bacteria whose cell walls have been completely removed by lysozyme digestion in an isotonic sucrose medium are termed:",
         ["Protoplasts", "Spheroplasts", "L-forms", "Mycoplasmas"],
         0, "Enzymatic removal of the entire peptidoglycan wall from a Gram-positive bacterium produces an osmotically fragile, spherical, bounded body termed a 'protoplast', whereas Gram-negative bacteria retaining remnants of outer membrane are called 'spheroplasts'.",
         True, "General Bacteriology (ICAR PG PYQ)"),

        ("Beta-lactam antibiotics (such as Penicillins and Cephalosporins) exert their bactericidal action by inhibiting which bacterial enzyme during cell wall synthesis?",
         ["Transpeptidase (Penicillin-Binding Proteins / PBPs) that catalyze peptide cross-linking", "DNA gyrase (Topoisomerase II)", "RNA polymerase", "Peptidyl transferase"],
         0, "Penicillins mimic the D-Ala-D-Ala terminus of peptidoglycan peptide chains, irreversibly binding and acylating the active-site serine of transpeptidase enzymes (PBPs), preventing cross-linking of adjacent glycan strands.",
         True, "General Bacteriology (ICAR PG PYQ)"),

        ("Bacterial endospores formed by Bacillus and Clostridium species possess extreme thermal resistance primarily due to the dehydration of the spore core and the presence of high concentrations of:",
         ["Calcium dipicolinate (dipicolinic acid chelated with Ca2+ ions)", "Trehalose and glycerol", "Poly-beta-hydroxybutyrate", "Magnesium sulfate"],
         0, "Dipicolinic acid (pyridine-2,6-dicarboxylic acid) constitutes up to 10-15% of the dry weight of bacterial endospores; it chelates calcium ions to form calcium dipicolinate, which intercalates into DNA and stabilizes proteins during heat exposure.",
         True, "General Bacteriology (ICAR PG PYQ)"),

        ("Small Acid-Soluble Spore Proteins (SASPs) present in the spore core contribute to endospore resistance by:",
         ["Binding to spore DNA, converting it from B-DNA to the more compact A-DNA conformation that resists UV irradiation and heat damage", "Enzymatically hydrolyzing incoming antibiotics", "Pumping water out of the core", "Forming the thick keratin coat"],
         0, "Alpha/beta-type SASPs saturate spore chromosomal DNA, changing its geometry from B-DNA to A-DNA, which prevents the formation of cyclobutane pyrimidine dimers upon UV irradiation, generating spore photoproducts that are rapidly repaired upon germination.",
         False, "General Bacteriology"),

        ("The official biological indicator organism used to validate the efficacy of moist heat sterilization in an Autoclave (121°C for 15 minutes) is:",
         ["Geobacillus stearothermophilus (spores)", "Bacillus atrophaeus", "Clostridium sporogenes", "Escherichia coli"],
         0, "Spores of the thermophilic bacterium Geobacillus stearothermophilus have a high thermal death time (D121°C >= 1.5-2.0 mins); survival strips or ampoules are placed inside autoclaves to physically verify sterilization.",
         True, "Diagnostic Microbiology (ICAR PG PYQ)"),

        ("Bacterial flagella are composed of polymer subunits of the protein Flagellin, which rotate driven by energy derived from:",
         ["Proton Motive Force (PMF / H+ ion gradient across the cytoplasmic membrane)", "Direct ATP hydrolysis by myosin", "GTP hydrolysis", "Glycolytic phosphorylation"],
         0, "The bacterial flagellar basal motor (MotA/MotB stator complex) acts as a proton turbine, using the electrochemical gradient of protons (or sodium ions) across the cell membrane (Proton Motive Force) to generate rotational torque without ATP consumption.",
         True, "General Bacteriology (ICAR PG PYQ)"),

        # 11-20: Flagella, capsules, staining, growth curve
        ("A bacterium possessing a tuft of multiple flagella at one pole or both poles of the cell is termed:",
         ["Lophotrichous", "Monotrichous", "Amphitrichous", "Peritrichous"],
         0, "Flagellar arrangements are: Monotrichous (single polar flagellum, e.g. Pseudomonas), Lophotrichous (a tuft/cluster of flagella at one or both ends, e.g. Spirillum), Amphitrichous (single flagellum at both poles), and Peritrichous (flagella distributed all over the cell, e.g. E. coli, Proteus).",
         True, "General Bacteriology (ICAR PG PYQ)"),

        ("In the Gram staining procedure developed by Christian Gram, the chemical role of Gram's Iodine is to act as a:",
         ["Mordant, forming an insoluble Crystal Violet-Iodine (CV-I) complex inside the cell wall", "Primary basic stain", "Decolorizing agent", "Counterstain"],
         0, "Gram's iodine (iodine and potassium iodide in water) acts as a chemical mordant; iodine penetrates into the cytoplasm and forms a large, water-insoluble crystal violet-iodine (CV-I) precipitate that cannot readily escape thick peptidoglycan.",
         True, "General Bacteriology (ICAR PG PYQ)"),

        ("In the Ziehl-Neelsen (Acid-Fast) staining protocol, the primary dye Carbol Fuchsin must be heated during application in order to:",
         ["Melt and soften the waxy mycolic acid barriers of the cell wall, allowing the dye to penetrate", "Inactivate bacterial catalase", "Denature bacterial DNA", "Prevent precipitation of methylene blue"],
         0, "Mycolic acids render the cell wall hydrophobic and impermeable at room temperature; heating the phenolic carbol fuchsin stain until steam rises softens and liquefies the lipids, driving carbol fuchsin into the bacterial cytoplasm.",
         True, "General Bacteriology (ICAR PG PYQ)"),

        ("Negative staining (using India ink or 10% Nigrosin) is specifically utilized in veterinary microbiology to demonstrate bacterial and fungal:",
         ["Capsules (which remain clear and unstained against a dark carbon background)", "Flagella", "Ribosomes", "Cell walls directly"],
         0, "Because capsules are uncharged, non-ionic gelatinous polysaccharides, they do not bind basic or acidic stains; colloidal India ink particles cannot penetrate the dense capsule, leaving clear halos around cells against an opaque black field.",
         True, "General Bacteriology (ICAR PG PYQ)"),

        ("In the standard four-phase closed-system bacterial growth curve, the phase during which cells are synthesizing enzymes, increasing in volume, but not dividing is the:",
         ["Lag phase", "Log (Exponential) phase", "Stationary phase", "Decline (Death) phase"],
         0, "In the lag phase, bacteria adapt to the new medium, synthesizing transport proteins, metabolic enzymes, and RNA; cell mass and size increase significantly, but cell number remains constant (growth rate = 0).",
         True, "General Bacteriology (ICAR PG PYQ)"),

        ("Bacteria exhibit the highest susceptibility to cell-wall active antibiotics (such as Penicillins and Ampicillin) during which growth phase?",
         ["Log (Exponential) phase", "Lag phase", "Stationary phase", "Decline phase"],
         0, "Beta-lactam antibiotics require active cell division and active peptidoglycan transpeptidation to exert their bactericidal action; during the exponential phase, virtually 100% of cells are synthesizing new cell walls.",
         True, "General Bacteriology (ICAR PG PYQ)"),

        ("The generation time (doubling time) of rapidly growing Escherichia coli in rich nutrient broth under optimal aeration at 37°C is approximately:",
         ["20 minutes", "2 hours", "12 hours", "24 hours"],
         0, "Under optimal physiological conditions (aerated, rich broth at 37°C), the generation time (time required for the bacterial population to double) of E. coli is approximately 20 minutes.",
         True, "General Bacteriology (ICAR PG PYQ)"),

        ("In the stationary phase of a batch culture, the cessation of net population growth is caused by:",
         ["Exhaustion of essential nutrients and accumulation of toxic metabolic byproducts, so that cell division equals cell death", "Complete loss of bacterial ribosomes", "Degradation of all DNA polymerases", "Rapid consumption of all oxygen in 1 minute"],
         0, "Stationary phase occurs when growth rate slows until the number of new cells produced equals the number of dying cells (cryptic growth), driven by depletion of limiting nutrients and acidification/toxin buildup.",
         True, "General Bacteriology (ICAR PG PYQ)"),

        ("Secondary metabolites (including most clinically useful antibiotics such as Penicillin, Streptomycin, and Tetracyclines) are synthesized by microorganisms primarily during which physiological phase?",
         ["Stationary phase (Idiophase)", "Early lag phase", "Early log phase (Trophophase)", "Decline phase"],
         0, "Industrial microbiology divides growth into the trophophase (exponential growth, primary metabolites) and idiophase (stationary phase), during which nutrient stress triggers the expression of secondary metabolic pathways producing antibiotics.",
         False, "General Bacteriology"),

        ("Chemoorganotrophic veterinary pathogenic bacteria obtain both their energy and carbon from:",
         ["Preformed organic chemical compounds (such as carbohydrates and amino acids)", "Inorganic carbon dioxide and sunlight", "Inorganic oxidation of sulfur compounds", "Atmospheric nitrogen gas"],
         0, "Almost all medically and veterinarily significant bacteria are chemoorganoheterotrophs: they oxidize preformed organic substrates (glucose, amino acids) to generate ATP (chemo-) and use organic carbon for cellular biosynthesis (-heterotroph).",
         False, "General Bacteriology"),

        # 21-30: Bacterial genetics: Conjugation, Transduction, Transformation, Plasmids
        ("The classical discovery of genetic 'Transformation' by Frederick Griffith (1928) utilized which veterinary/medical pathogen?",
         ["Streptococcus pneumoniae (demonstrating transfer of capsule virulence from heat-killed smooth to live rough strains)", "Escherichia coli", "Bacillus anthracis", "Salmonella Typhimurium"],
         0, "Griffith showed that heat-killed virulent capsulated (S) S. pneumoniae cells transformed live, avirulent non-capsulated (R) cells into lethal capsulated bacteria in mice; Avery, MacLeod, and McCarty (1944) proved the 'transforming principle' was DNA.",
         True, "Bacterial Genetics (ICAR PG PYQ)"),

        ("In bacterial genetics, 'Natural Competence' refers to the physiological state that allows a bacterium to:",
         ["Directly bind and take up naked, exogenous fragments of extracellular DNA from the environment", "Survive boiling at 100°C", "Form sex pili", "Survive phagocytosis"],
         0, "Competence is a genetically regulated transient physiological state (e.g. in Streptococcus, Bacillus, and Neisseria) where cell surface DNA-binding complexes and translocases actively import extracellular DNA across the membrane.",
         True, "Bacterial Genetics (ICAR PG PYQ)"),

        ("The transfer of genetic material between two viable bacterial cells mediated by a bacteriophage (bacterial virus) is termed:",
         ["Transduction", "Transformation", "Conjugation", "Transposition"],
         0, "Transduction (discovered by Zinder and Lederberg in 1952 in Salmonella) is the accidental packaging of bacterial chromosome fragments into viral capsids during bacteriophage assembly, transferring host genes to recipient cells upon infection.",
         True, "Bacterial Genetics (ICAR PG PYQ)"),

        ("Generalized transduction differs from Specialized transduction in that Generalized transduction:",
         ["Can transfer virtually any random segment of the bacterial chromosome, mediated by lytic virulent bacteriophages", "Transfers only specific chromosomal genes immediately adjacent to the prophage integration site", "Requires direct cell-to-cell contact via an F-pilus", "Requires competent cells"],
         0, "Generalized transduction occurs when a lytic phage accidentally degrades host DNA into fragments and packages any random chromosomal segment into a phage head; specialized transduction occurs during imprecise excision of a lysogenic prophage.",
         True, "Bacterial Genetics (ICAR PG PYQ)"),

        ("Bacterial 'Conjugation' is the direct transfer of DNA from a donor cell to a recipient cell mediated by a specialized hollow protein tube called the:",
         ["Sex pilus (F pilus / Conjugative pilus)", "Flagellum", "Common fimbria", "Porin channel"],
         0, "Conjugation is encoded by conjugative plasmids (e.g. F plasmid); the donor cell produces a specialized F pilus that binds the recipient cell, retracts to establish cell-to-cell contact, and initiates rolling-circle single-stranded DNA transfer.",
         True, "Bacterial Genetics (ICAR PG PYQ)"),

        ("An 'Hfr' (High Frequency of Recombination) bacterial strain is generated when the conjugative Fertility (F) plasmid:",
         ["Integrates into the circular bacterial host chromosome via homologous recombination at insertion sequences", "Is permanently lost from the cell", "Replicates autonomously in the cytoplasm as 50 copies", "Mutates into a virulent phage"],
         0, "When an episomal F plasmid integrates into the main circular bacterial chromosome, the cell becomes an Hfr strain; during mating, it attempts to transfer the entire bacterial chromosome, yielding extraordinarily high recombination frequencies.",
         True, "Bacterial Genetics (ICAR PG PYQ)"),

        ("An 'F-prime' (F') plasmid is created when an integrated F factor in an Hfr strain undergoes:",
         ["Imprecise, faulty excision from the chromosome, carrying adjacent host bacterial genes with it into the autonomous plasmid", "Complete chromosomal deletion", "Inversion of the entire genome", "Duplication of all transposons"],
         0, "When an F factor excises abnormally from an Hfr chromosome, it takes flanking chromosomal genes (e.g. lac operon) along into a free circular episome, known as an F' plasmid, which transfers those specific host genes at 100% frequency to F- recipients.",
         True, "Bacterial Genetics (ICAR PG PYQ)"),

        ("R-Plasmids (Resistance Plasmids) of multi-drug resistant Enterobacteriaceae consist structurally of two distinct functional components:",
         ["Resistance Transfer Factor (RTF, encoding conjugative transfer) and the r-determinant (carrying multiple antibiotic resistance genes)", "Promoter and Operator only", "Leader sequence and Attenuator", "Inverted terminal repeats only"],
         0, "R-plasmids possess: (1) The Resistance Transfer Factor (RTF), an ~80-kb region encoding the sex pilus and transfer operon, and (2) The r-determinant, which carries transposons encoding resistance enzymes (e.g. beta-lactamases, aminoglycoside-modifying enzymes).",
         True, "Bacterial Genetics (ICAR PG PYQ)"),

        ("Transposons ('jumping genes') are mobile genetic elements that differ from insertion sequences (IS elements) because transposons:",
         ["Carry structural genes (such as antibiotic resistance determinants) in addition to transposase and inverted terminal repeats", "Lack inverted terminal repeats", "Cannot move between plasmid and chromosome", "Only replicate inside bacteriophages"],
         0, "IS elements are simple insertion sequences encoding only the transposase required for their own movement; composite transposons (e.g. Tn5, Tn10) flank core passenger genes (such as kanamycin or tetracycline resistance) with IS modules.",
         True, "Bacterial Genetics (ICAR PG PYQ)"),

        ("Integrons are specialized genetic assembly platforms in Gram-negative bacteria that capture and express mobile gene cassettes via a site-specific recombinase called:",
         ["Integrase (IntI)", "Transposase", "DNA gyrase", "Topoisomerase IV"],
         0, "Integrons encode an integrase (IntI) that captures promoterless antibiotic resistance gene cassettes at a specific recombination site (attI) and expresses them under the control of a common strong promoter (Pc).",
         False, "Bacterial Genetics"),

        # 31-40: Bacterial gene regulation, mutations, sterilization
        ("In the classical lactose (lac) operon of Escherichia coli, the regulatory repressor protein encoded by the lacI gene binds to which regulatory site to block transcription?",
         ["Operator (lacO)", "Promoter (lacP)", "CAP-binding site", "Terminator"],
         0, "In the absence of lactose, the active LacI repressor protein binds to the lac operator (lacO) sequence, sterically blocking RNA polymerase from transcribing the structural genes lacZ, lacY, and lacA.",
         True, "Bacterial Genetics (ICAR PG PYQ)"),

        ("Catabolite repression of the lac operon ensures that E. coli preferentially metabolizes Glucose over Lactose, mediated by which intracellular signaling molecule?",
         ["Cyclic AMP (cAMP) complexed with Catabolite Activator Protein (CAP / CRP)", "Guanosine tetraphosphate (ppGpp)", "Cyclic GMP", "Adenosine triphosphate (ATP)"],
         0, "High glucose transport inhibits adenylate cyclase, keeping intracellular cAMP low; when glucose is exhausted, cAMP surges, binding CAP/CRP, which binds upstream of the lac promoter and stimulates transcription by 50-fold.",
         True, "Bacterial Genetics (ICAR PG PYQ)"),

        ("The Ames test is a widely used bacterial assay for screening chemical compounds for mutagenicity and potential carcinogenicity, utilizing mutant strains of:",
         ["Salmonella Typhimurium histidine auxotrophs (his- to his+ back-mutation)", "Escherichia coli tryptophan auxotrophs", "Bacillus subtilis", "Staphylococcus aureus"],
         0, "Developed by Bruce Ames, the test uses Salmonella enterica serovar Typhimurium carrying point or frameshift mutations in the histidine biosynthesis operon; exposure to mutagens causes back-mutation (reversion) to histidine prototrophy on minimal agar.",
         True, "Diagnostic Microbiology (ICAR PG PYQ)"),

        ("The 'SOS Response' in bacteria is a global error-prone DNA repair network induced by severe DNA damage, governed by the cleavage of the LexA repressor catalyzed by activated:",
         ["RecA protein (acting as a co-protease)", "DNA polymerase I", "UvrA protein", "Topoisomerase I"],
         0, "Single-stranded DNA exposed at stalled replication forks binds RecA, forming an active nucleoprotein filament that stimulates the self-cleavage (autoproteolysis) of the LexA transcriptional repressor, derepressing >40 SOS DNA repair genes.",
         True, "Bacterial Genetics (ICAR PG PYQ)"),

        ("Which physical sterilization method destroys bacterial spores by delivering 160°C to 170°C for 2 hours in an enclosed chamber?",
         ["Hot Air Oven (Dry heat sterilization)", "Autoclave (Moist heat)", "Tyndallization", "Pasteurization"],
         0, "The hot air oven uses dry heat to sterilize glassware, oils, powders, and surgical instruments that cannot tolerate moisture; it requires 160°C for 2 hours (or 170°C for 1 hour) to kill bacterial spores by protein oxidation.",
         True, "General Bacteriology (ICAR PG PYQ)"),

        ("Tyndallization (fractional or intermittent steam sterilization) is a process designed to achieve complete sterility of heat-sensitive nutrient media by:",
         ["Steaming at 100°C for 20-30 minutes on three consecutive days, allowing intervening spore germination at 37°C", "Autoclaving at 121°C for 5 minutes", "Heating to 63°C for 30 minutes", "Irradiating with gamma rays"],
         0, "John Tyndall devised fractional sterilization: Day 1 kills vegetative cells; overnight incubation at 37°C germinates heat-resistant spores into vegetative cells; Day 2 and Day 3 kill newly germinated vegetative bacteria before new spores can form.",
         True, "General Bacteriology (ICAR PG PYQ)"),

        ("Membrane filtration of biological fluids (such as serum, tissue culture media, and antibiotic solutions) employs membrane filters with a standard pore size of:",
         ["0.22 micrometers (microns), which excludes all bacteria while allowing viruses to pass", "0.45 microns", "1.0 micron", "5.0 microns"],
         0, "Cellulose acetate or polyethersulfone membrane filters with a 0.22-um pore size are the standard for sterilizing heat-labile liquids; they retain all cellular bacteria, mycoplasmas, and fungi, yielding bacteriologically sterile fluids.",
         True, "General Bacteriology (ICAR PG PYQ)"),

        ("High-Efficiency Particulate Air (HEPA) filters utilized in biological safety cabinets (laminar flow hoods) are certified to remove at least 99.97% of airborne particles down to:",
         ["0.3 micrometers (microns) in diameter", "1.0 micron", "5.0 microns", "10 microns"],
         0, "HEPA filters use a dense mat of randomly arranged borosilicate glass fibers that trap >= 99.97% of all airborne particles, bacteria, and aerosolized droplets of 0.3 um in diameter by impaction, interception, and diffusion.",
         True, "General Bacteriology (ICAR PG PYQ)"),

        ("Ethylene oxide (ETO) gas is an effective cold chemical sterilizing agent used for heat-sensitive veterinary surgical equipment, acting through:",
         ["Alkylation of sulfhydryl, amino, hydroxyl, and carboxyl groups in bacterial proteins and nucleic acids", "Generation of free hydroxyl radicals", "Lipid membrane dissolution", "Osmotic dehydration"],
         0, "Ethylene oxide is a highly penetrating alkylating agent that replaces labile hydrogen atoms on proteins, enzymes, and DNA with hydroxyethyl groups (-CH2-CH2-OH), irreversibly blocking protein synthesis and microbial replication.",
         False, "General Bacteriology"),

        ("In antimicrobial susceptibility testing, the standard depth of Mueller-Hinton Agar in Petri plates required for the Kirby-Bauer disc diffusion assay is precisely:",
         ["4 mm (too thin increases zone sizes; too thick decreases zone sizes)", "1 mm", "8 mm", "12 mm"],
         0, "Standardized CLSI Kirby-Bauer protocols require Mueller-Hinton agar poured to a uniform depth of exactly 4 mm (approx. 25-30 mL in 100-mm plate); deviation alters the lateral diffusion rate of antibiotic discs.",
         True, "Diagnostic Microbiology (ICAR PG PYQ)"),

        # 41-45: Disinfectants, culture media classification
        ("The 'Phenol Coefficient' (Rideal-Walker or Chick-Martin method) of a disinfectant measures its antimicrobial potency relative to:",
         ["Pure Phenol (carbolic acid) against a standard test strain of Salmonella enterica serovar Typhi", "Bleach (Sodium hypochlorite)", "Alcohol 70%", "Formaldehyde"],
         0, "The Phenol Coefficient is the ratio of the highest dilution of the test disinfectant killing the test organism in 10 minutes (but not 5) to the dilution of pure phenol having the same effect.",
         True, "General Bacteriology (ICAR PG PYQ)"),

        ("MacConkey Agar is a classic example of a medium that is both:",
         ["Selective (bile salts and crystal violet inhibit Gram-positive bacteria) and Differential (lactose fermentation indicated by neutral red)", "Enriched and Transport only", "Synthetic and chemically defined", "Completely non-selective"],
         0, "Bile salts and crystal violet selectively suppress Gram-positive organisms, while lactose and the pH indicator neutral red differentiate lactose-fermenting coliforms (pink colonies) from non-lactose fermenters (colorless colonies).",
         True, "General Bacteriology (ICAR PG PYQ)"),

        ("Robertson's Cooked Meat Medium (RCM) is an enriched transport and culture medium specially designed for the cultivation of:",
         ["Anaerobic spore-forming bacteria (such as Clostridium species)", "Strict aerobes", "Mycoplasmas", "Chlamydiae"],
         0, "RCM contains chopped beef heart meat particles; unsaturated fatty acids in meat absorb oxygen, while glutathione and cysteine act as reducing agents, creating a low oxidation-reduction potential (Eh) ideal for cultivating anaerobes.",
         True, "General Bacteriology (ICAR PG PYQ)"),

        ("Thioglycollate broth creates an oxygen gradient from top to bottom, allowing classification of microbial oxygen requirements. Strict obligate anaerobes grow exclusively:",
         ["At the bottom of the tube where oxygen tension is lowest (indicated by decolorized resazurin / methylene blue)", "At the very surface meniscus", "Uniformly throughout the tube", "In the top 1 cm only"],
         0, "Sodium thioglycollate and L-cystine consume dissolved oxygen; oxygen diffuses only into the top layer (pink with resazurin indicator), while the bottom remains strictly anaerobic, supporting the growth of obligate anaerobes.",
         True, "General Bacteriology (ICAR PG PYQ)"),

        ("Chocolate Agar (heated blood agar) is an enriched medium required for fastidious bacteria (such as Taylorella equigenitalis) because heating blood to 80°C:",
         ["Lyses red blood cells, releasing Hemin (X-factor) and free NAD (V-factor) while inactivating heat-labile NADase enzymes", "Destroys all bacterial endotoxins", "Caramelizes glucose into sucrose", "Converts albumin into globulin"],
         0, "Heating sheep or horse blood to 80°C ruptures erythrocytes, releasing intracellular hemin (X-factor) and NAD (V-factor) into the medium while simultaneously denaturing erythrocyte NADase, allowing fastidious bacteria to grow.",
         True, "General Bacteriology (ICAR PG PYQ)")
    ]
    return qs

if __name__ == '__main__':
    qs = get_module3_questions()
    print(f"Microbiology Module 3 loaded: {len(qs)} questions")
