# scripts/path_mod6_clinpath.py
# Module 6: Clinical Pathology, Necropsy & Lab Techniques (30 Questions)
# Aligned with ICAR AIEEA (PG) M.V.Sc. Syllabus Code 13 Units II & III

def get_module6_questions():
    qs = [
        # 1-10: Necropsy protocols & fixatives
        ("During a routine post-mortem examination of a bovine carcass, the recommended position of the carcass for external opening is:",
         ["Left lateral recumbency (left side down, right side up to keep the rumen underneath)", "Right lateral recumbency", "Dorsal recumbency", "Ventral recumbency"],
         0, "Ruminants are positioned in left lateral recumbency so that the enormous rumen remains on the table/floor surface, allowing unobstructed visualization, inspection, and evisceration of the intestinal tract, liver, and right kidney.",
         True, "Necropsy Techniques (ICAR PG PYQ)"),

        ("In equines, the standard recommended positioning for post-mortem examination is:",
         ["Right lateral recumbency (left side up)", "Left lateral recumbency", "Dorsal recumbency", "Suspension by hindlimbs"],
         0, "Horses are classically placed in right lateral recumbency (left side up) to allow convenient exposure and untangling of the large cecum and great colon.",
         False, "Necropsy Techniques"),

        ("The standard universal fixative employed for routine diagnostic veterinary histopathology is:",
         ["10% Neutral Buffered Formalin (NBF, approximately 4% formaldehyde, pH 7.2 - 7.4)", "100% Absolute ethanol", "Glutaraldehyde 10%", "Pure glacial acetic acid"],
         0, "10% NBF (4% formaldehyde gas dissolved in water, buffered with sodium phosphate salts to neutral pH 7.2-7.4) prevents acid hematin pigment precipitation, cross-links lysine residues, and provides optimal morphological preservation.",
         True, "Histopathological Techniques (ICAR PG PYQ)"),

        ("The recommended minimum volumetric ratio of fixative fluid to tissue volume for adequate histopathological fixation is:",
         ["10:1 to 20:1 (fixative to tissue volume)", "1:1", "2:1", "50:1"],
         0, "Adequate fixation requires a fixative-to-tissue ratio of at least 10:1 (ideally 20:1); using insufficient volume depletes unreacted formaldehyde, leading to central autolysis and poor staining.",
         True, "Histopathological Techniques (ICAR PG PYQ)"),

        ("To ensure rapid and complete penetration of 10% neutral buffered formalin, tissue specimens submitted for histopathology should not exceed a maximum thickness of:",
         ["5 to 6 mm (approximately the thickness of a coin or pencil)", "25 mm (1 inch)", "50 mm (2 inches)", "100 mm"],
         0, "Formaldehyde penetrates tissue at a rate of approximately 1 mm per hour, slowing down as deeper layers fix; slices thicker than 5-6 mm suffer autolysis in their centers before fixative can reach them.",
         True, "Histopathological Techniques (ICAR PG PYQ)"),

        ("Bouin's fixative contains picric acid, formalin, and glacial acetic acid, and is considered the fixative of choice for preserving:",
         ["Testicular biopsies, delicate ocular structures, and endocrine glands", "Mineralized bone without decalcification", "Large fatty livers", "Skeletal muscle for glycogen analysis"],
         0, "Bouin's fluid penetrates rapidly with minimal tissue shrinkage and imparts excellent nuclear crispness, making it the premier fixative for soft, delicate architectural tissues like the testicle, embryo, and retina.",
         True, "Histopathological Techniques (ICAR PG PYQ)"),

        ("Carnoy's fluid (absolute ethanol, chloroform, and glacial acetic acid) is a rapid coagulating fixative that is specifically recommended when the objective is to preserve:",
         ["Glycogen, nucleic acids, and rapid diagnostic cytology", "Phospholipids and neutral lipids", "Myelin sheaths", "RBC integrity (it lyses RBCs)"],
         0, "Carnoy's fluid penetrates extremely rapidly (fixing small blocks in 1-2 hours) and preserves intracellular glycogen and nucleic acids, although it lyses erythrocytes and dissolves lipids.",
         False, "Histopathological Techniques"),

        ("Glutaraldehyde (2.5% buffered solution) is the specialized fixative utilized when tissues are prepared for:",
         ["Transmission Electron Microscopy (TEM) and Scanning Electron Microscopy (SEM)", "Routine brightfield light microscopy with H&E", "Standard paraffin block wax embedding", "Frozen section fat staining"],
         0, "Glutaraldehyde possesses two dialdehyde functional groups that form extensive, irreversible cross-links between proteins, providing the exquisite ultrastructural preservation required for electron microscopy.",
         True, "Diagnostic Techniques (ICAR PG PYQ)"),

        ("The chronological sequence of steps involved in standard automated paraffin wax tissue processing is:",
         ["Fixation -> Dehydration (graded alcohols) -> Clearing (xylene) -> Infiltration / Embedding (molten paraffin wax)", "Fixation -> Staining -> Clearing -> Embedding", "Embedding -> Clearing -> Dehydration -> Fixation", "Dehydration -> Fixation -> Infiltration -> Clearing"],
         0, "Water in tissues must be replaced by molten paraffin. Because paraffin is immiscible with water, tissues are dehydrated through ascending grades of alcohol (70%->100%), cleared in an organic solvent miscible with both alcohol and wax (xylene), and then infiltrated with molten paraffin wax at 56-58°C.",
         True, "Histopathological Techniques (ICAR PG PYQ)"),

        ("The standard nominal section thickness cut on a rotary microtome for routine veterinary diagnostic histopathology is:",
         ["4 to 5 micrometers (microns)", "10 to 15 micrometers", "0.5 to 1 micrometer", "25 to 50 micrometers"],
         0, "Paraffin-embedded tissue blocks are routinely sectioned at 4 to 5 microns (um) thickness using steel or disposable microtome blades, providing a single monolayer of cells for microscopic examination.",
         True, "Histopathological Techniques (ICAR PG PYQ)"),

        # 11-20: Special stains, Decalcification, artifact identification
        ("In routine Hematoxylin and Eosin (H&E) staining of tissue sections, Hematoxylin is a basic dye that stains acidic nuclear DNA:",
         ["Blue to purple (basophilic), while Eosin is an acidic dye that stains basic cytoplasmic proteins pink to red (eosinophilic)", "Pink, while Eosin stains nuclei dark blue", "Green, while Eosin stains cytoplasm yellow", "Black, while Eosin stains cytoplasm brown"],
         0, "Hematein (oxidized hematin with an aluminum mordant) acts as a basic dye binding negatively charged phosphate groups of nuclear nucleic acids (basophilic blue/purple); eosin Y is an anionic dye binding positively charged basic amino acids in cytoplasmic proteins (eosinophilic pink/red).",
         True, "Histopathological Techniques (ICAR PG PYQ)"),

        ("The histochemical stain utilized to specifically highlight collagen fibers in green (or blue) while staining skeletal/smooth muscle fibers red and nuclei dark brown/black is:",
         ["Masson's Trichrome stain", "Periodic Acid-Schiff (PAS) stain", "Grocott's Methenamine Silver (GMS)", "Alcian Blue stain"],
         0, "Masson's trichrome uses Weigert's iron hematoxylin (nuclei black), Biebrich scarlet-acid fuchsin (muscle and cytoplasm red), and Light green / Aniline blue (collagen fibers green/blue) to differentiate fibrosis and cirrhosis from muscle.",
         True, "Histopathological Techniques (ICAR PG PYQ)"),

        ("Periodic Acid-Schiff (PAS) stain demonstrates carbohydrates (such as glycogen, mucin, basement membranes, and fungal cell walls) as brilliant magenta/rose-pink through:",
         ["Periodic acid oxidizing 1,2-glycol groups to aldehydes, which react with Schiff reagent (leucofuchsin) to form a pink adduct", "Silver reduction by phenolic groups", "Metachromatic shift of azure dyes", "Enzymatic cleavage by beta-galactosidase"],
         0, "Periodic acid oxidizes vicinal diols of carbohydrates into dialdehydes; Schiff reagent (decolorized basic fuchsin treated with sulfurous acid) reacts with free aldehydes to regenerate a bright magenta-purple quinoid chromophore.",
         True, "Histopathological Techniques (ICAR PG PYQ)"),

        ("To demonstrate Mycobacterium bovis or Mycobacterium avium in histological sections of tuberculous lesions, the diagnostic stain of choice is:",
         ["Ziehl-Neelsen (ZN) acid-fast stain", "Gram stain (Brown and Brenn)", "Warthin-Starry silver stain", "Mucicarmine stain"],
         0, "Mycobacterial cell walls are rich in lipidic mycolic acids, which retain hot carbol fuchsin despite decolorization with acid-alcohol (3% HCl in ethanol), staining acid-fast bacilli bright red against a methylene blue background.",
         True, "Histopathological Techniques (ICAR PG PYQ)"),

        ("The Grocott-Gomori Methenamine Silver (GMS) stain demonstrates fungal hyphae and yeasts (e.g. Aspergillus, Blastomyces, Histoplasma) by staining their cell walls:",
         ["Intense jet black against a light green counterstained background", "Brilliant yellow", "Deep blue", "Bright red"],
         0, "Chromic acid oxidizes fungal cell wall polysaccharides to aldehydes, which reduce alkaline methenamine silver nitrate to black metallic silver, outlining fungal walls in sharp jet-black contrast.",
         True, "Histopathological Techniques (ICAR PG PYQ)"),

        ("Warthin-Starry or Steiner silver impregnation stains are essential in veterinary histopathology for identifying which group of fastidious organisms?",
         ["Spirochaetes (Leptospira, Brachyspira, Borrelia) and Campylobacter", "Gram-positive cocci (Staphylococcus)", "Capsulated yeasts (Cryptococcus)", "Acid-fast bacilli"],
         0, "Spirochaetes and microaerophilic flagellated bacteria (Leptospira, Borrelia, Campylobacter, Helicobacter) stain poorly with routine H&E and Gram stains; argyrophilic silver stains (Warthin-Starry) coat their surfaces with black silver precipitate.",
         True, "Histopathological Techniques (ICAR PG PYQ)"),

        ("The definitive histological method used to confirm whether intracytoplasmic PAS-positive granules within hepatocytes represent Glycogen is:",
         ["Diastase (alpha-amylase) digestion prior to PAS staining (glycogen is digested and vanishes)", "Staining with Sudan Black B", "Decalcification with EDTA", "Bleaching with potassium permanganate"],
         0, "Diastase (amylase) hydrolyzes glycogen polymers into soluble maltose. If a serial section pre-treated with diastase loses its PAS-positive staining, the substance is definitively confirmed to be glycogen (diastase-sensitive).",
         True, "Histopathological Techniques (ICAR PG PYQ)"),

        ("In the preparation of bone and tooth specimens for histological sectioning, the chemical decalcifying agent that preserves tissue antigenicity and enzymatic activity for immunohistochemistry is:",
         ["EDTA (Ethylenediaminetetraacetic acid, a chelating agent at neutral pH)", "Concentrated Nitric Acid (10%)", "Formic acid 20%", "Hydrochloric acid 5%"],
         0, "Mineral acids (nitric, HCl) decalcify rapidly but degrade cellular DNA, RNA, and protein epitopes; neutral EDTA (a calcium chelator) acts slowly without acidity, fully preserving tissue morphology and antigens for IHC.",
         True, "Histopathological Techniques (ICAR PG PYQ)"),

        ("The presence of 'knife chatter' or microtome vibration lines (alternating thick and thin horizontal parallel bands across a tissue section) is primarily caused by:",
         ["An excessively loose knife/block holder, incorrect blade clearance angle, or an excessively hard tissue block", "Over-staining with hematoxylin", "Using expired xylene in the clearing bath", "Fixing in cold formalin"],
         0, "Chatter artifact results from microscopic mechanical vibration of the microtome knife as it encounters hard tissue (e.g. calcification, keratin, dense fibrosis), caused by an insecurely clamped blade or inappropriate clearance angle.",
         False, "Histopathological Techniques"),

        ("Crush artifact (nuclear pyknosis and elongation of nuclei resembling spindle cells, termed 'smudge cells') in biopsy samples is most commonly produced by:",
         ["Rough handling or crushing of delicate tissues with surgical forceps prior to fixation", "Prolonged immersion in paraffin wax", "Exposure to sunlight", "Over-dehydration in 100% alcohol"],
         0, "Forceful squeezing of friable biopsies (especially small endoscopic biopsies or lymphoid tissues) with toothed tissue forceps mechanically disrupts cell membranes and smears chromatin, producing uninterpretable 'smudge' artifacts.",
         False, "Histopathological Techniques"),

        # 21-30: Body fluid analysis, Transudate vs Exudate, Hematology alterations
        ("In the laboratory analysis of cavitary effusions (peritoneal, pleural, pericardial), a 'Transudate' is distinguished from an 'Exudate' by having:",
         ["Total protein < 2.5 g/dL, Total nucleated cell count (TNCC) < 1,500/uL, and low specific gravity (<1.015)", "Total protein > 3.0 g/dL and TNCC > 5,000/uL", "Abundant degenerative neutrophils and bacteria", "Positive Rivalta reaction"],
         0, "A pure transudate results from increased hydrostatic pressure or hypoalbuminemia across intact capillaries, containing low protein (<2.5 g/dL), low cellularity (<1,500 cells/uL, mostly mononuclear), and low specific gravity (<1.015).",
         True, "Clinical Pathology (ICAR PG PYQ)"),

        ("The Rivalta test is a simple bedside laboratory assay commonly used in feline medicine to differentiate FIP effusions from transudates, where a positive test is indicated by:",
         ["A drop of effusion forming a distinct jellyfish-like precipitate or droplet that slowly sinks to the bottom of dilute acetic acid solution without dissolving", "Immediate clearing and disappearance of the drop", "A color change from clear to deep purple", "Formation of gas bubbles at the surface"],
         0, "The Rivalta test detects high concentrations of protein, fibrinogen, and inflammatory mediators in FIP effusions; when added to dilute acetic acid (pH ~4.0), a precipitate forms and floats or sinks intact to the bottom.",
         True, "Clinical Pathology (ICAR PG PYQ)"),

        ("In synovial fluid analysis in horses, normal healthy equine joint fluid is characterized by:",
         ["High viscosity (stringing > 2.5-5 cm), total protein < 2.0 g/dL, and TNCC < 500-1,000 cells/uL (predominantly large mononuclear cells)", "Low viscosity resembling water with TNCC > 50,000 cells/uL", "Cloudy turbid appearance with abundant degenerate neutrophils", "Presence of visible fibrin clots"],
         0, "Normal synovial fluid is clear to pale straw-colored, highly viscous due to high hyaluronic acid concentration, low in protein (<2 g/dL), low in cellularity (<1,000/uL), and does not clot due to the absence of fibrinogen.",
         True, "Clinical Pathology (ICAR PG PYQ)"),

        ("A 'Leukemoid Reaction' is characterized by extreme leukocytosis (>50,000 to 100,000/uL) that mimics granulocytic leukemia, but is differentiated from true leukemia because a leukemoid reaction:",
         ["Is an orderly, non-neoplastic, hyper-reactive response to severe inflammation (e.g. closed pyometra, abscess) with a mature left shift and absence of blast cells", "Is an autonomous clonal proliferation of malignant blast cells", "Always shows chromosomal translocations", "Is refractory to resolving the underlying infection"],
         0, "A leukemoid reaction is an exaggerated physiological bone marrow release of mature and band neutrophils triggered by severe suppuration; upon resolving the underlying septic focus, the leukocytosis completely resolves.",
         True, "Clinical Pathology (ICAR PG PYQ)"),

        ("A 'Degenerative Left Shift' on a canine or feline complete blood count (CBC) is defined as:",
         ["Immature neutrophil forms (band cells, metamyelocytes) exceeding the number of mature segmented neutrophils, indicating severe bone marrow exhaustion and a poor prognosis", "Presence of a few band neutrophils alongside a massive mature neutrophilia", "Absence of any neutrophils in peripheral blood", "Elevated eosinophils and basophils only"],
         0, "A degenerative left shift occurs when tissue demand for neutrophils outstrips the bone marrow's storage and production capacity; band cells outnumber mature segmented neutrophils, reflecting severe overwhelming sepsis and a grave prognosis.",
         True, "Clinical Pathology (ICAR PG PYQ)"),

        ("'Toxic changes' in circulating neutrophils (such as Döhle bodies, cytoplasmic basophilia, vacuolation, and toxic granulation) indicate:",
         ["Accelerated granulopoiesis and premature release from the bone marrow during severe systemic inflammation or endotoxemia", "Direct bacterial invasion of the neutrophil cytoplasm", "Storage artifact from prolonged EDTA exposure", "Congenital failure of nuclear segmentation"],
         0, "Toxic changes are structural abnormalities induced by high cytokine and endotoxin levels in the bone marrow microenvironment, driving accelerated maturation and causing retained RNA (basophilia, Döhle bodies) and autophagocytosis (foamy vacuoles).",
         True, "Clinical Pathology (ICAR PG PYQ)"),

        ("Pelger-Huët anomaly, an inherited or acquired benign condition in dogs and cats, is recognized on blood smears by:",
         ["Failure of normal nuclear segmentation of granulocytes, resulting in hyposegmented (bilobed, peanut-shaped, or round) mature neutrophils with normal mature chromatin and function", "Hypersegmentation of neutrophils with >5 nuclear lobes", "Total absence of cytoplasmic granules in eosinophils", "Presence of giant platelets"],
         0, "Pelger-Huët anomaly is caused by a defect in the lamin B receptor; neutrophil nuclei fail to segment into 3-5 lobes, appearing unsegmented or bilobed despite possessing mature, dense, non-toxic chromatin and normal phagocytic function.",
         True, "Clinical Pathology (ICAR PG PYQ)"),

        ("The primary laboratory test utilized to definitively distinguish between Intravascular Hemolysis and Extravascular Hemolysis in a jaundiced dog is:",
         ["Presence of free Hemoglobinemia and Hemoglobinuria (present in intravascular, absent in extravascular)", "Total leukocyte count", "Serum alanine aminotransferase (ALT)", "Platelet count"],
         0, "In intravascular hemolysis, RBCs lyse within blood vessels, saturating haptoglobin and spilling free hemoglobin into plasma (pink/red serum = hemoglobinemia) and urine (hemoglobinuria); extravascular hemolysis occurs inside macrophages of the spleen/liver without free hemoglobinemia.",
         True, "Clinical Pathology (ICAR PG PYQ)"),

        ("Rouleaux formation of erythrocytes (stack of coins appearance) is a normal, prominent physiological feature on routine blood films of healthy:",
         ["Horses (and to a lesser degree cats)", "Dogs and ruminants", "Birds and reptiles", "Sheep and goats"],
         0, "Equine erythrocytes have a low negative surface zeta potential and higher physiological fibrinogen/globulin concentrations, causing normal prominent spontaneous rouleaux formation; in dogs or ruminants, pronounced rouleaux indicates elevated acute-phase proteins.",
         True, "Clinical Pathology (ICAR PG PYQ)"),

        ("A true immune-mediated Agglutination of erythrocytes on a glass slide (autoagglutination) is definitively distinguished from physiological Rouleaux by:",
         ["The Saline Dilution Test: adding a drop of physiological saline disperses rouleaux but does not disperse true antibody-mediated agglutination", "Warming the slide to 37°C", "Staining with New Methylene Blue", "Centrifuging the sample at high speed"],
         0, "In the saline dispersion test, one drop of whole blood is mixed with 4 to 10 drops of 0.9% saline; linear stacks of rouleaux disperse into single cells, whereas true immune-complex cross-linked RBC aggregates remain tightly clustered.",
         True, "Clinical Pathology (ICAR PG PYQ)")
    ]
    return qs

if __name__ == '__main__':
    qs = get_module6_questions()
    print(f"Pathology Module 6 loaded: {len(qs)} questions")
