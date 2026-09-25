# scripts/path_mod3_avian.py
# Module 3: Avian Pathology & Poultry Diseases (50 Questions)
# Aligned with ICAR AIEEA (PG) M.V.Sc. Syllabus Code 13 Unit II

def get_module3_questions():
    qs = [
        # 1-10: Marek's, IBD, Avian Leukosis, Gout
        ("The primary oncogene encoded by Gallid alphaherpesvirus 2 responsible for T-cell transformation in Marek's Disease is:",
         ["Meq oncogene", "v-src", "v-myc", "Tax protein"],
         0, "The Meq (Marek's EcoRI-Q-encoded protein) gene is a basic leucine zipper (bZIP) transcription factor unique to oncogenic strains of Marek's disease virus; it inhibits apoptosis and transforms CD4+ T-lymphocytes.",
         True, "Avian Pathology (ICAR PG PYQ)"),

        ("In poultry, 'ocular lymphomatosis' ('gray eye' / 'fish eye' / pearly eye) causing irregular eccentric pupil and blindness is a clinical manifestation of:",
         ["Marek's Disease", "Infectious Bursal Disease", "Avian Encephalomyelitis", "Infectious Coryza"],
         0, "Infiltration of neoplastic pleomorphic lymphocytes into the iris in Marek's disease causes depigmentation (turning the normal orange iris into grayish-white) and an irregular, pinpoint, non-reactive pupil.",
         True, "Avian Pathology (ICAR PG PYQ)"),

        ("The definitive microscopic lesion distinguishing the Bursa of Fabricius in acute Infectious Bursal Disease (IBD) from Marek's disease is:",
         ["Extensive necrosis and apoptosis of B-lymphocytes in lymphoid follicles with interfollicular gelatinous edema", "Neoplastic pleomorphic T-lymphocytic infiltration without follicle depletion", "Diffuse squamous metaplasia of bursal plicae", "Caseocalcareous mineralization without cell loss"],
         0, "IBD virus selectively destroys dividing B-lymphoblasts in the germinal centers of bursal follicles, resulting in severe follicular necrosis, lymphoid depletion, and heterophil infiltration, whereas MD produces neoplastic lymphomatosis.",
         True, "Avian Pathology (ICAR PG PYQ)"),

        ("In broiler chicks, intramuscular hemorrhages on the pectoral (breast) and thigh muscles are a prominent gross necropsy finding in:",
         ["Infectious Bursal Disease (IBD / Gumboro)", "Fowl Pox", "Infectious Bronchitis", "Egg Drop Syndrome"],
         0, "IBD virus causes severe immune-complex vasculitis and thrombocytopenia, producing diagnostic linear and brush-like ecchymotic hemorrhages in the skeletal muscles of the thigh and breast.",
         True, "Avian Pathology (ICAR PG PYQ)"),

        ("Visceral gout in poultry is pathologically characterized by chalky white deposits of uric acid and monosodium urate crystals on serosal membranes, primarily because avian species:",
         ["Are uricotelic and lack the enzyme uricase (urate oxidase)", "Are ammonotelic and lack arginase", "Produce excessive amounts of urea via the ornithine cycle", "Excrete purines exclusively as allantoin"],
         0, "Birds are uricotelic; they convert nitrogenous waste to insoluble uric acid to conserve water. Because they lack uricase to oxidize uric acid to allantoin, any renal tubular dysfunction causes hyperuricemia and urate precipitation on viscera.",
         True, "Avian Pathology (ICAR PG PYQ)"),

        ("The primary histological reaction elicited in tissues by articular gout tophi in poultry consists of:",
         ["Foreign-body granulomas with radial urate crystals surrounded by multinucleated giant cells and macrophages", "Pure suppurative microabscesses rich in heterophils", "Dense coagulative necrosis with no cellular response", "Eosinophilic granulomas rich in Charcot-Leyden crystals"],
         0, "Precipitated monosodium urate needle-like crystals in articular and periarticular tissues act as foreign bodies, exciting a chronic granulomatous reaction characterized by radiating crystalline clefts encircled by macrophages and multinucleated foreign-body giant cells.",
         False, "Avian Pathology"),

        ("Avian Leukosis / Sarcoma group of viruses belong to which family of animal viruses?",
         ["Retroviridae (Alpharetrovirus)", "Herpesviridae", "Poxviridae", "Birnaviridae"],
         0, "Avian leukosis viruses are members of the genus Alpharetrovirus (family Retroviridae) that cause lymphoid leukosis, erythroblastosis, and myeloblastosis in chickens older than 14-16 weeks.",
         True, "Avian Pathology"),

        ("In Lymphoid Leukosis, the neoplastic cells that infiltrate the liver, spleen, and bursa are morphologically characterized as:",
         ["Uniform, monomorphic B-lymphoblasts with pyroninophilic cytoplasm", "Heterogeneous pleomorphic T-lymphocytes of varying sizes", "Mature plasma cells packed with Russell bodies", "Anaplastic spindle-shaped mesenchymal cells"],
         0, "Unlike Marek's disease (which exhibits a polymorphic population of small, medium, and large T-lymphocytes), lymphoid leukosis displays a uniform, monomorphic sheet of large, blast-transformed B-lymphocytes with identical nuclear features.",
         True, "Avian Pathology (ICAR PG PYQ)"),

        ("The characteristic post-mortem finding of 'marble spleen' (diffuse splenomegaly with gray-white marbling) in ring-necked pheasants is caused by:",
         ["Siadenovirus (Marble Spleen Disease Virus)", "Avipoxvirus", "Birnavirus", "Circovirus"],
         0, "Marble Spleen Disease of pheasants is caused by an Aviadenovirus (Siadenovirus) that causes severe splenomegaly with reticuloendothelial cell hyperplasia, producing a distinct marbled appearance, alongside pulmonary edema.",
         False, "Avian Pathology"),

        ("Chicken Anemia Virus (CAV / Blue Wing disease) belongs to which viral family?",
         ["Anelloviridae (Gyrovirus)", "Circoviridae", "Parvoviridae", "Picornaviridae"],
         0, "Chicken Anemia Virus, possessing a circular negative-sense single-stranded DNA genome, is classified in the genus Gyrovirus (family Anelloviridae); it induces severe aplastic anemia and thymic/bursal atrophy.",
         True, "Avian Pathology (ICAR PG PYQ)"),

        # 11-20: Respiratory, digestive, and systemic avian diseases
        ("The 'Intracerebral Pathogenicity Index' (ICPI) and 'Mean Death Time' (MDT) are standard laboratory parameters used to determine the virulence of:",
         ["Newcastle Disease Virus (NDV / APMV-1)", "Infectious Bronchitis Virus", "Avian Reovirus", "Infectious Bursal Disease Virus"],
         0, "NDV isolates are officially classified into velogenic (ICPI 1.5-2.0, MDT < 60 hrs), mesogenic (ICPI 1.0-1.5, MDT 60-90 hrs), and lentogenic (ICPI 0.0-0.5, MDT > 90 hrs) using ICPI in day-old chicks and MDT in chicken embryos.",
         True, "Avian Pathology (ICAR PG PYQ)"),

        ("The primary molecular determinant of systemic virulence in Newcastle Disease Virus is:",
         ["Presence of multiple basic amino acids (arginine and lysine) at the cleavage site of the F0 fusion glycoprotein", "A mutation in the matrix (M) protein", "Deletion of the neuraminidase gene", "Duplication of the phosphoprotein gene"],
         0, "Virulent (velogenic/mesogenic) NDV strains have multiple basic residues at the F0 cleavage site (Arg-X-Lys/Arg-Arg-Phe), allowing cleavage by ubiquitous host furin-like proteases in all tissues, whereas lentogenic strains are cleaved only by trypsin-like enzymes in the gut/trachea.",
         True, "Avian Pathology (ICAR PG PYQ)"),

        ("In chickens suffering from Avian Influenza caused by Highly Pathogenic Avian Influenza (HPAI) H5N1, the classical gross lesions include:",
         ["Cyanosis and edema of the comb and wattles, subcutaneous petechial hemorrhages on the shanks, and diffuse necrosis in multiple organs", "Proliferative nodular scabs on comb and eyelids", "Enlarged sciatic nerves with loss of striations", "Thickened, corrugated ileum mucosa"],
         0, "HPAI viruses possess polybasic hemagglutinin cleavage sites that allow systemic replication in endothelial cells, causing massive microvascular thrombosis, severe edema/cyanosis of head appendages, petechiae on shanks/feet, and multi-organ necrosis.",
         True, "Avian Pathology (ICAR PG PYQ)"),

        ("The diagnostic lesion of 'caseous tracheal plug' obstructing the syrinx and tracheal bifurcation, causing death by suffocation in young chicks, is characteristic of:",
         ["Infectious Bronchitis (IB)", "Fowl Pox", "Avian Encephalomyelitis", "Lymphoid Leukosis"],
         0, "Infectious Bronchitis Virus causes acute catarrhal to caseous tracheitis; in young chicks, thick caseous exudate accumulates at the syrinx and tracheal bifurcation, causing gasping, asphyxiation, and high mortality.",
         True, "Avian Pathology (ICAR PG PYQ)"),

        ("The 'false layer' syndrome in adult hens, where birds show normal secondary sex characteristics, visit nests, but fail to lay eggs, is a permanent sequela of early chick infection by:",
         ["Infectious Bronchitis Virus (IBV)", "Egg Drop Syndrome Virus (EDS-76)", "Avian Reovirus", "Marek's Disease Virus"],
         0, "Infection of young pullets (<2-3 weeks old) with IBV damages the developing oviduct, causing permanent aplasia, hypoplasia, or cystic dilation of the middle and lower oviduct; ovulated yolks fall into the peritoneal cavity (internal layers).",
         True, "Avian Pathology (ICAR PG PYQ)"),

        ("Egg Drop Syndrome 1976 (EDS-76), characterized by sudden loss of shell quality (soft-shelled, shell-less, thin-shelled, depigmented eggs) in healthy-appearing hens, is caused by:",
         ["Duck atadenovirus A (EDS-76 adenovirus)", "Gallid alphaherpesvirus 1", "Avian Metapneumovirus", "Avian Orthoreovirus"],
         0, "Duck atadenovirus A (EDS-76 virus) targets the pouch shell gland (uterus) of the oviduct, producing severe decalcification and loss of pigment in eggshells without affecting the general health of the flock.",
         True, "Avian Pathology (ICAR PG PYQ)"),

        ("Infectious Coryza of chickens, characterized by facial edema, foul-smelling nasal discharge, and swollen infraorbital sinuses, is caused by:",
         ["Avibacterium paragallinarum", "Pasteurella multocida", "Gallibacterium anatis", "Ornithobacterium rhinotracheale"],
         0, "Avibacterium paragallinarum (formerly Haemophilus paragallinarum) is a fastidious, V-factor (NAD) dependent bacterium causing acute upper respiratory disease with classic swelling of facial tissues and infraorbital sinuses.",
         True, "Avian Pathology (ICAR PG PYQ)"),

        ("The distinctive necropsy appearance of the liver in turkeys suffering from 'Blackhead' (Histomoniasis / Enterohepatitis) is:",
         ["Circular, depressed, saucer-shaped necrotic areas with raised borders (target-like / bulls-eye lesions)", "Diffuse bronze green discoloration without necrosis", "Extensive caseous granulomas with concentric calcification", "Multiple pinpoint petechial hemorrhages with fatty change"],
         0, "Histomonas meleagridis produces severe necrotizing typhlitis (cecal cores) and migrates to the liver via the portal vein, producing pathognomonic crater-like, saucer-shaped circular necrotic areas with raised erythematous margins.",
         True, "Avian Pathology (ICAR PG PYQ)"),

        ("The intermediate vector responsible for transmitting the protozoan Histomonas meleagridis inside its eggs to turkeys is:",
         ["Heterakis gallinarum (the cecal nematode)", "Ascaridia galli", "Syngamus trachea", "Capillaria annulata"],
         0, "Histomonas meleagridis is incorporated into the ova of the avian cecal roundworm Heterakis gallinarum; these ova can survive in the soil for years and transmit blackhead when ingested by susceptible birds.",
         True, "Parasitic Pathology (ICAR PG PYQ)"),

        ("The pathognomonic lesion of 'Syngamiasis' (Gapeworm disease) in game birds and young poultry caused by Syngamus trachea is:",
         ["Permanent in copula 'Y-shaped' red nematodes attached to the tracheal mucosa, causing hemorrhagic tracheitis and gasping ('gapes')", "Massive nodular lesions in the gizzard", "Caseous plugs in the cecum", "Severe thickening of the crop mucosa"],
         0, "Syngamus trachea adults live permanently coupled in copula forming a distinctive Y-shape attached to tracheal mucosa, sucking blood and causing severe catarrhal/hemorrhagic tracheitis with dyspnea and head stretching ('gaping').",
         True, "Parasitic Pathology (ICAR PG PYQ)"),

        # 21-30: Coccidiosis, Salmonella, fungal infections
        ("In broiler chickens, the species of Eimeria responsible for acute, fatal cecal coccidiosis characterized by ballooned ceca distended with pure blood is:",
         ["Eimeria tenella", "Eimeria necatrix", "Eimeria acervulina", "Eimeria maxima"],
         0, "Eimeria tenella selectively parasitizes the cecal epithelial cells; second-generation schizonts deep in the lamina propria rupture large blood vessels, filling the ceca with fresh blood and sloughed mucosa.",
         True, "Avian Pathology (ICAR PG PYQ)"),

        ("Which species of Eimeria targets the mid-gut (jejunum) in older chickens, producing severe ballooning, white spots (schizonts), and extensive petechiae on the serosal surface?",
         ["Eimeria necatrix", "Eimeria tenella", "Eimeria mitis", "Eimeria praecox"],
         0, "Eimeria necatrix attacks the middle third of the small intestine; second-generation schizonts appear as white opacities interspersed with dark red petechiae visible through the serosa, producing severe mucohemorrhagic enteritis.",
         True, "Avian Pathology (ICAR PG PYQ)"),

        ("Eimeria acervulina infection in poultry is characterized pathologically by which distinctive mucosal lesions in the duodenum?",
         ["Transverse white ladder-like or staircase-like streaks and plaques on the mucosal surface", "Massive hemorrhagic distension of the cecal pouches", "Deep necrotic crater ulcers in the ileum", "Ulcerative stomatitis with pseudomembrane"],
         0, "Eimeria acervulina develops in the duodenal loop and upper jejunum, where large numbers of oocysts form pathognomonic whitish, transverse, ladder-like streaks easily visible from the mucosal surface.",
         True, "Avian Pathology (ICAR PG PYQ)"),

        ("In adult carrier hens, Pullorum Disease (Salmonella enterica serovar Pullorum) produces pathognomonic macroscopic ovarian lesions consisting of:",
         ["Misshapen, pedunculated, angular, greenish-brown or cystic ovarian follicles containing caseous material", "Complete absence of the left ovary", "Diffuse squamous cell carcinoma of the oviduct", "Multiple hydatid cysts in the ovary"],
         0, "Salmonella Pullorum localizes in the ovary of mature birds, causing chronic oophoritis; normal spherical yellow follicles become irregular, discolored (dull green-brown), pedunculated, and filled with cheesy, inspissated yolk.",
         True, "Avian Pathology (ICAR PG PYQ)"),

        ("The pathognomonic necropsy finding in the liver of adult birds suffering from Fowl Typhoid (Salmonella enterica serovar Gallinarum) is:",
         ["Enlarged, friable liver exhibiting a characteristic greenish-bronze metallic sheen", "Miliary white pinpoint foci without discoloration", "Extensive nutmeg pattern of chronic congestion", "Severe hepatic amyloidosis"],
         0, "In acute Fowl Typhoid, Salmonella Gallinarum causes bacteremic hepatocellular necrosis and bile stasis, imparting a diagnostic dark greenish-bronze or copper metallic appearance to the enlarged liver upon exposure to air.",
         True, "Avian Pathology (ICAR PG PYQ)"),

        ("Necrotic Enteritis in broiler chickens is caused by which toxigenic bacterium proliferating in the small intestine?",
         ["Clostridium perfringens (Types A and C producing NetB toxin)", "Clostridium difficile", "Escherichia coli", "Campylobacter jejuni"],
         0, "Necrotic Enteritis is caused by Clostridium perfringens Type A (and Type C) strains encoding the pore-forming NetB (necrotic enteritis toxin B) toxin, producing a pathognomonic 'Turkish towel' appearance of friable diphtheritic intestinal mucosa.",
         True, "Avian Pathology (ICAR PG PYQ)"),

        ("In chicks, 'Brooder Pneumonia' (Mycotic Pneumonia) characterized by yellowish-white caseous nodules in the lungs and air sacs is caused by:",
         ["Aspergillus fumigatus", "Candida albicans", "Cryptococcus neoformans", "Trichophyton gallinae"],
         0, "Inhalation of conidia from moldy litter or feed causes acute Aspergillus fumigatus infection in young chicks, characterized by disc-shaped granulomatous pulmonary nodules showing dichotomously branched (45°) septate hyphae.",
         True, "Avian Pathology (ICAR PG PYQ)"),

        ("In poultry, 'Thrush' (Sour Crop / Moniliasis) is characterized by a thick, white, circular, curd-like pseudomembrane on the mucosa of the crop, caused by:",
         ["Candida albicans", "Aspergillus flavus", "Mucor pusillus", "Rhizopus microsporus"],
         0, "Candida albicans invades the stratified squamous epithelium of the crop, upper esophagus, and proventriculus, producing a corrugated, curd-like, whitish diphtheritic membrane resembling a Turkish towel.",
         True, "Avian Pathology (ICAR PG PYQ)"),

        ("Favus ('White Comb') in domestic fowl is a chronic dermatophytosis characterized by white chalky scaling on the comb and wattles, caused by:",
         ["Microsporum gallinae (Lophophyton gallinae)", "Trichophyton verrucosum", "Microsporum canis", "Epidermophyton floccosum"],
         0, "Microsporum gallinae causes favus in poultry, producing dry, powdery, white crusts that start at the comb and can spread to feathered areas, causing feather loss and honeycomb-like scutula.",
         True, "Avian Pathology (ICAR PG PYQ)"),

        ("Avian Encephalomyelitis (AE / Epidemic Tremor) in young chicks is characterized histopathologically by pathognomonic:",
         ["Central chromatolysis of neurons in brainstem nuclei (e.g. nucleus motorius) and perivascular lymphocytic cuffing", "Demyelination of the optic nerve only", "Suppurative microabscesses in the cerebral cortex", "Spongiform encephalopathy in the obex"],
         0, "Picornavirus infection in chicks under 4 weeks produces fine tremors of head and neck; the diagnostic hallmark is axonal reaction / central chromatolysis (swelling, eccentric nucleus, loss of Nissl granules) in large motor neurons of the medulla and spinal cord.",
         True, "Avian Pathology (ICAR PG PYQ)"),

        # 31-40: Avian metabolic, nutritional, skeletal pathology
        ("Perosis ('Slipped Tendon') in young growing chicks and poults is caused by a nutritional deficiency of:",
         ["Manganese and Choline", "Calcium and Phosphorus", "Vitamin D3", "Vitamin C"],
         0, "Manganese deficiency (often aggravated by deficiency of choline, biotin, or folic acid) impairs chondrogenesis in the epiphyseal growth plate of the tibiotarsus, causing flattening of the condyles and lateral slipping of the gastrocnemius tendon from its groove.",
         True, "Nutritional Pathology (ICAR PG PYQ)"),

        ("Tibial Dyschondroplasia (TD) in fast-growing broiler chickens is pathologically characterized by:",
         ["A persistent, unvascularized, unmineralized plug of avascular cartilage in the proximal metaphysis of the tibiotarsus", "Complete failure of the periosteum to form bone", "Suppurative osteomyelitis caused by Staphylococcus aureus", "Excessive calcification of articular cartilage"],
         0, "TD is an endochondral ossification failure where hypertrophic chondrocytes in the prehypertrophic zone fail to mature, undergo apoptosis, or vascularize, leaving an opaque, cone-shaped mass of white cartilage below the growth plate.",
         True, "Skeletal Pathology (ICAR PG PYQ)"),

        ("Rickets in young growing broilers differs histologically from Osteomalacia in adult laying hens in that Rickets:",
         ["Involves defective mineralization of the cartilaginous growth plate and newly formed osteoid", "Involves defective mineralization of pre-existing mature osteoid in remodeling bone only", "Exclusively results from excessive fluoride intake", "Is characterized by increased osteoclast numbers without osteoid buildup"],
         0, "Rickets occurs in growing birds with active growth plates, leading to failure of provisional calcification and expansion of the zone of hypertrophy; osteomalacia occurs in adult birds with closed growth plates, featuring accumulation of unmineralized osteoid on trabeculae.",
         True, "Nutritional Pathology (ICAR PG PYQ)"),

        ("Cage Layer Fatigue in commercial caged laying hens is characterized by acute paralysis and osteoporosis caused by:",
         ["Depletion of structural medullary and cortical bone calcium to maintain shell calcification under high egg production", "Traumatic fracture of the sciatic nerve by cage wire", "Vitamin B1 deficiency due to feed rancidity", "Botulism poisoning from water nipples"],
         0, "High-producing laying hens mobilize medullary and then cortical bone to provide eggshell calcium; when dietary intake is inadequate, severe bone resorption leads to pathological fractures of ribs and thoracic vertebrae, compressing the spinal cord.",
         True, "Nutritional Pathology (ICAR PG PYQ)"),

        ("Ascites Syndrome (Pulmonary Hypertension Syndrome / Water Belly) in fast-growing meat-type broilers is fundamentally initiated by:",
         ["Mismatch between rapid muscle growth and inadequate pulmonary vascular capacity, leading to hypoxia, pulmonary hypertension, and right-sided congestive heart failure", "Excessive dietary sodium chloride leading to primary renal failure", "Primary hepatic cirrhosis caused by aflatoxins", "Congenital absence of the pericardial sac"],
         0, "Modern broilers have massive pectoral muscle mass relative to lung volume. High metabolic demand causes tissue hypoxia, triggering compensatory polycythemia, increased pulmonary vascular resistance, right ventricular hypertrophy, and right heart failure with transudative ascites.",
         True, "Cardiopulmonary Pathology (ICAR PG PYQ)"),

        ("Deep Pectoral Myopathy ('Green Muscle Disease') in heavy broilers and turkeys is an ischemic necrosis of which specific muscle?",
         ["Supracoracoideus (pectoralis minor) muscle encased within an inelastic fascial sheath", "Pectoralis major muscle", "Gastrocnemius muscle", "Sartorius muscle"],
         0, "Violent wing flapping causes the supracoracoideus muscle to expand; because it is enclosed in a rigid, non-yielding osteofascial compartment, increased intramuscular pressure occludes arterial blood supply, causing ischemic coagulative necrosis that turns green due to hemoglobin breakdown.",
         True, "Musculoskeletal Pathology (ICAR PG PYQ)"),

        ("In poultry, Gout is classified anatomically into two distinct syndromes:",
         ["Visceral gout (pericardial/hepatic/serosal urate deposits) and Articular gout (synovial/periarticular deposits)", "Renal gout and Hepatic gout", "Cutaneous gout and Ocular gout", "Gastric gout and Intestinal gout"],
         0, "Avian gout manifests either as acute visceral gout (precipitation of urate crystals on internal organs from acute dehydration or renal damage) or chronic articular gout (precipitation in joints and tendon sheaths due to genetic or prolonged dietary excess).",
         True, "Avian Pathology (ICAR PG PYQ)"),

        ("Nutritional muscular dystrophy ('White Muscle Disease') in turkey poults and ducklings produces pale, waxy streaks of coagulative necrosis in which muscular structure in addition to skeletal muscles?",
         ["Gizzard musculature", "Crop smooth muscle", "Oviduct wall", "Tongue muscle"],
         0, "In poultry, Vitamin E and selenium deficiency selectively affects both skeletal muscles (breast, legs) and the smooth muscle of the gizzard and heart, causing multifocal Zenker's degeneration and mineralization.",
         False, "Nutritional Pathology"),

        ("In chicks, 'Exudative Diathesis' is characterized by extensive subcutaneous edema with greenish-blue discoloration over the breast and abdomen, caused by deficiency of:",
         ["Vitamin E and Selenium", "Vitamin K", "Biotin", "Copper"],
         0, "Deficiency of Vitamin E and Selenium reduces glutathione peroxidase activity, causing free-radical damage to capillary endothelial membranes, leakage of plasma into subcutaneous tissues, and breakdown of extravasated hemoglobin into green biliverdin.",
         True, "Nutritional Pathology (ICAR PG PYQ)"),

        ("The primary macroscopic lesion of 'Inclusion Body Hepatitis' (IBH) in broiler chickens is:",
         ["Swollen, pale, yellow-tan liver with multifocal petechiae and ecchymoses, containing basophilic intranuclear inclusion bodies in hepatocytes", "Diffuse granulomatous hepatitis with giant cells", "Extensive bile duct carcinoma with metastases", "Severe gallbladder distension with clear fluid"],
         0, "Fowl Adenovirus strains cause acute necrosis of hepatocytes; the liver is markedly enlarged, friable, pale yellowish, and speckled with petechial hemorrhages, exhibiting pathognomonic basophilic or amphophilic intranuclear inclusion bodies.",
         True, "Avian Pathology (ICAR PG PYQ)"),

        # 41-50: Infectious avian pathology specifics
        ("Ulcerative Enteritis ('Quail Disease') in captive quail and young chickens is caused by which anaerobic spore-forming bacterium?",
         ["Clostridium colinum", "Clostridium perfringens Type D", "Clostridium septicum", "Clostridium tetani"],
         0, "Clostridium colinum causes acute ulcerative enteritis in gallinaceous birds, characterized by button-like necrotic ulcers in the intestine and hemorrhagic/necrotic areas with yellow halos in the liver.",
         True, "Avian Pathology (ICAR PG PYQ)"),

        ("In ducks, Duck Viral Enteritis (Duck Plague) is caused by an Anatid alphaherpesvirus that produces pathognomonic:",
         ["Eruptive, hemorrhagic, and necrotizing mucosal lesions with longitudinal diphtheritic bands in the esophagus and cloaca", "Pure suppurative pneumonia with pulmonary marbling", "Severe osteopetrosis with thickening of long bones", "Loss of all flight feathers without visceral changes"],
         0, "Duck Plague virus targets vascular endothelium and mucosal epithelium, producing petechiae and pathognomonic longitudinal hemorrhagic/diphtheritic crusts in the esophagus and annular hemorrhagic bands in the intestines.",
         True, "Avian Pathology (ICAR PG PYQ)"),

        ("Duck Viral Hepatitis (DVH Type 1) in ducklings under 3 weeks of age is an acute, rapidly fatal picornavirus infection characterized by:",
         ["Sudden death with ducklings dying in opisthotonos ('stargazing') position and swollen liver covered with punctate hemorrhages", "Chronic respiratory rales and air sacculitis", "Extensive subcutaneous edema of the neck only", "Complete blindness due to keratitis"],
         0, "Avihepatovirus (DVH-1) causes acute hepatocellular necrosis; affected ducklings die within hours in a characteristic opisthotonos posture (head and neck arched backward over the back) with enlarged livers speckled with hemorrhages.",
         True, "Avian Pathology (ICAR PG PYQ)"),

        ("Avian Leukosis virus induces 'Osteopetrosis' ('Marble Bone' / 'Boot-leg Disease') in growing chickens by stimulating:",
         ["Excessive periosteal and endosteal bone formation of the diaphysis of long bones (especially the tarsometatarsus), obliteration of the marrow cavity", "Rapid osteoclastic bone resorption with fibrous tissue replacement", "Purulent inflammation of articular cartilage", "Multiple subchondral cysts in the femur"],
         0, "Osteopetrosis is caused by certain subgroup A or B retroviruses that stimulate continuous, abnormal proliferation of periosteal and endosteal osteoblasts, resulting in symmetrically thickened, dense, hot, spindle-shaped long bones.",
         True, "Avian Pathology (ICAR PG PYQ)"),

        ("In poultry, 'Bumblefoot' is a chronic, deep, ulcerative pododermatitis that typically begins with plantar epidermal injury and secondary infection by:",
         ["Staphylococcus aureus", "Salmonella Pullorum", "Pasteurella multocida", "Mycobacterium avium"],
         0, "Mechanical trauma from rough perches or wet litter breaches the plantar skin, allowing Staphylococcus aureus to invade and produce chronic granulomatous and suppurative pododermatitis ('bumblefoot') with caseous cores.",
         True, "Avian Pathology"),

        ("In turkeys, Avian Bordetellosis ('Turkey Coryza') is an acute upper respiratory infection characterized by tracheal collapse and distortion caused by:",
         ["Bordetella avium", "Bordetella bronchiseptica", "Mycoplasma synoviae", "Pasteurella gallinarum"],
         0, "Bordetella avium produces dermonecrotic toxins that selectively target ciliated tracheal epithelium and soften cartilage rings, leading to dorsoventral flattening and tracheal collapse with severe sneezing and snicking.",
         False, "Avian Pathology"),

        ("The specific anatomical site of choice for collecting diagnostic tissue sections to demonstrate Cowdry Type A intranuclear inclusions in chickens with Infectious Laryngotracheitis is:",
         ["Tracheal epithelium and conjunctival mucosa during the early acute stage (first 3 to 5 days)", "Spleen red pulp on day 10", "Bursal follicles on day 14", "Brainstem neurons"],
         0, "Cowdry Type A inclusions are transient; they appear within syncytia of tracheal and conjunctival epithelial cells only during the first 3-5 days of infection before the necrotic epithelium sloughs off into the lumen.",
         True, "Diagnostic Pathology (ICAR PG PYQ)"),

        ("In chickens, Infectious Stunting Syndrome (Runting-Stunting Syndrome / Malabsorption Syndrome) is characterized by pancreatic atrophy and cystic dilation of crypts, commonly associated with:",
         ["Avian Astroviruses, Reoviruses, and Parvoviruses", "Avian Leukosis Virus", "Fowl Poxvirus", "Duck Enteritis Virus"],
         0, "Runting-stunting syndrome is a multifactorial enteric condition associated with small round viruses (astroviruses, enteric parvoviruses, reoviruses) causing villus blunting, cystic crypt dilation, pancreatic acinar atrophy, and severe malabsorption.",
         False, "Avian Pathology"),

        ("Avian Infectious Synovitis, characterized by fibrinous synovitis, tenosynovitis, and bursitis with pale-creamy exudate in the hock joints and keel bursa, is caused by:",
         ["Mycoplasma synoviae", "Mycoplasma gallisepticum", "Mycoplasma meleagridis", "Mycoplasma iowae"],
         0, "Mycoplasma synoviae infection causes systemic disease involving synovial membranes; gross necropsy reveals yellowish-gray, viscous exudate in joint cavities, tendon sheaths, and sternal (keel) bursa.",
         True, "Avian Pathology (ICAR PG PYQ)"),

        ("The diagnostic feature that confirms Avian Chlamydiosis (Ornithosis / Psittacosis caused by Chlamydia psittaci) in air sac and liver smears stained with Macchiavello, Stamp's, or Gimenez stain is:",
         ["Tiny, red-staining intracytoplasmic elementary bodies within mononuclear phagocytic cells", "Large, blue-staining encapsulated yeasts", "Gram-positive branching filaments", "Silver-positive spiral organisms"],
         0, "Chlamydia psittaci replicates within macrophages; elementary bodies and reticulate bodies appear as bright red intracellular inclusions against a blue background with modified acid-fast stains (Stamp's or Gimenez).",
         True, "Diagnostic Pathology (ICAR PG PYQ)")
    ]
    return qs

if __name__ == '__main__':
    qs = get_module3_questions()
    print(f"Pathology Module 3 loaded: {len(qs)} questions")
