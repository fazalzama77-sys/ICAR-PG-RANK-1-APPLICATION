# scripts/micro2_mod2.py
# Module 2: Systematic Bacteriology (Gram +ve, Gram -ve, Acid-Fast, Spirochetes & Mycoplasma) (75 questions)

TOPIC = "Systematic Bacteriology (Gram +ve, Gram -ve, Acid-Fast, Spirochetes & Mycoplasma)"

def get_module2_questions():
    return [
        (
            "The Beta-hemolysin (beta-toxin) of Staphylococcus aureus exhibits 'Hot-Cold Lysis' (incomplete hemolysis at 37°C that turns into complete lysis at 4°C) and is enzymatically a:",
            [
                "Sphingomyelinase C that hydrolyzes membrane sphingomyelin",
                "Phospholipase D that cleaves phosphatidylcholine into phosphatidic acid",
                "Cholesterol-dependent cytolysin forming transmembrane beta-barrel pores",
                "Calcium-dependent RTX leukotoxin targeting beta-2 integrin receptors"
            ],
            0,
            "Staphylococcus aureus beta-hemolysin is a Mg2+-dependent Sphingomyelinase C. Sheep erythrocytes are exceptionally rich in sphingomyelin, so chilling the plate to 4°C after 37°C incubation collapses the destabilized lipid bilayer ('hot-cold hemolysis').",
            True,
            TOPIC
        ),
        (
            "In diagnostic bacteriology, the rapid 'Slide Coagulase Test' for Staphylococcus aureus differs mechanistically from the 'Tube Coagulase Test' because the slide test detects:",
            [
                "Secreted free extracellular staphylocoagulase activating prothrombin (CRF)",
                "Cell-wall-bound Clumping Factor (ClfA) binding directly to fibrinogen",
                "Extracellular staphylokinase (fibrinolysin) activating host plasminogen",
                "Heat-stable thermonuclease (TNase) hydrolyzing DNA and RNA in plasma"
            ],
            1,
            "The slide coagulase test detects cell-wall-bound 'clumping factor' (ClfA, a fibrinogen-binding adhesin) which directly precipitates fibrinogen without needing Coagulase-Reacting Factor (CRF), whereas the definitive tube test detects secreted free coagulase.",
            True,
            TOPIC
        ),
        (
            "On Baird-Parker agar (egg-yolk tellurite glycine pyruvate agar), coagulase-positive Staphylococcus aureus forms characteristic diagnostic colonies that appear as:",
            [
                "Brick-red mucoid colonies surrounded by a bright yellow zone of mannitol fermentation",
                "Chalky white rough colonies with a deep brown halo of tyrosine hydrolysis",
                "Jet-black shiny colonies (tellurite reduction) with an opaque zone and clear halo (lecithinase/lipase)",
                "Colorless translucent colonies with a swarming wave edge and fishy odor"
            ],
            2,
            "On Baird-Parker medium, S. aureus reduces potassium tellurite to metallic tellurium (forming jet-black colonies) and hydrolyzes egg-yolk lecithin and lipids via lipase/lecithinase to produce a surrounding clear halo with an inner opaque precipitation ring.",
            True,
            TOPIC
        ),
        (
            "The Exfoliative Toxins (ExhA, ExhB, ExhC, ExhD) of Staphylococcus hyicus causing Greasy Pig Disease (Exudative Epidermitis) induce intraepidermal splitting by acting as:",
            [
                "Adenylate cyclases that elevate intracellular cAMP in basal keratinocytes",
                "ADP-ribosyltransferases that inactivate elongation factor-2 (EF-2) in the dermis",
                "Zinc metalloproteases that degrade type IV collagen in the basement membrane",
                "Glutamate-specific serine proteases that selectively cleave Desmoglein-1"
            ],
            3,
            "Exfoliative toxins of S. hyicus (ExhA–D) and S. aureus (ETA/ETB) are trypsin-like serine proteases that specifically cleave the desmosomal cadherin Desmoglein-1 in the stratum granulosum of the epidermis.",
            False,
            TOPIC
        ),
        (
            "On Edwards' medium (blood agar containing crystal violet and esculin) used for bovine mastitis diagnosis, Streptococcus uberis is differentiated from Streptococcus agalactiae because S. uberis:",
            [
                "Hydrolyzes esculin into esculetin, producing dark brown-to-black colonies",
                "Fails to hydrolyze esculin and forms colorless pinpoint beta-hemolytic colonies",
                "Produces a bright golden-yellow carotenoid pigment and coagulates rabbit plasma",
                "Swarms across the agar surface and produces hydrogen sulfide gas"
            ],
            0,
            "Edwards' medium is selective for streptococci (crystal violet inhibits staphylococci). Streptococcus uberis hydrolyzes esculin to esculetin, which reacts with ferric ions to turn colonies black, whereas S. agalactiae is esculin-negative and CAMP-positive.",
            True,
            TOPIC
        ),
        (
            "Which capsular serotype of Streptococcus suis is globally the most virulent and prevalent cause of porcine meningitis, arthritis, septicemia, and zoonotic meningitis/deafness in pig handlers?",
            [
                "Capsular Serotype 14 (expressing muramidase-released protein variant)",
                "Capsular Serotype 2 (expressing suilysin, MRP, and extracellular factor EF)",
                "Capsular Serotype 9 (restricted exclusively to avian respiratory infections)",
                "Capsular Serotype 35 (recently reclassified outside the genus Streptococcus)"
            ],
            1,
            "Streptococcus suis Capsular Serotype 2 is the premier virulent serotype worldwide causing meningitis, polyserositis, arthritis, and endocarditis in weaned piglets, as well as occupational zoonotic meningitis and permanent sensorineural hearing loss in abattoir workers.",
            True,
            TOPIC
        ),
        (
            "What is the standard selective agar medium used to isolate Bacillus anthracis from heavily contaminated environmental soil, hides, or bone meal samples?",
            [
                "Baird-Parker egg-yolk tellurite pyruvate glycine agar",
                "PALCAM lithium chloride ceftazidime acriflavine esculin agar",
                "PLET medium (Polymyxin, Lysozyme, EDTA, and Thallous acetate agar)",
                "Skirrow's vancomycin polymyxin trimethoprim lysed horse blood agar"
            ],
            2,
            "PLET medium (Heart Infusion Agar containing Polymyxin B, Lysozyme, EDTA, and Thallous acetate) selectively inhibits environmental contaminants and other Bacillus species while permitting the growth of Bacillus anthracis.",
            True,
            TOPIC
        ),
        (
            "In reference laboratories, virulent Bacillus anthracis is definitively differentiated from closely related Bacillus cereus because B. anthracis is:",
            [
                "Actively motile by peritrichous flagella, strongly beta-hemolytic, and penicillin-resistant",
                "Motile at 22°C, lecithinase-negative on egg yolk agar, and resistant to Gamma phage",
                "Acid-fast on Ziehl-Neelsen stain, urease-positive, and grows only at 42°C",
                "Non-motile, non-hemolytic (or weakly gamma-hemolytic), penicillin-sensitive, and lysed by Gamma phage"
            ],
            3,
            "Unlike Bacillus cereus (which is motile, strongly beta-hemolytic on sheep blood agar, penicillin-resistant via beta-lactamase, and resistant to gamma phage), B. anthracis is non-motile, non-hemolytic, susceptible to Penicillin G (10 units), and specifically lysed by Gamma bacteriophage.",
            True,
            TOPIC
        ),
        (
            "Within the tripartite anthrax toxin complex encoded on plasmid pXO1, what are the exact intracellular enzymatic activities of Edema Factor (EF) and Lethal Factor (LF)?",
            [
                "EF is a calmodulin-dependent adenylate cyclase; LF is a Zn2+ metalloprotease cleaving MAPKKs",
                "EF is a phospholipase C; LF is an ADP-ribosyltransferase targeting elongation factor-2",
                "EF is a guanylyl cyclase elevating cGMP; LF is a glucosyltransferase inactivating Rho GTPases",
                "EF is a sphingomyelinase C; LF is a neurotoxin cleaving synaptobrevin-2"
            ],
            0,
            "Protective Antigen (PA) forms a heptameric translocation pore in the endosomal membrane. Edema Factor (EF) is a calmodulin- and Ca2+-dependent adenylate cyclase that massively elevates host cAMP, while Lethal Factor (LF) is a Zn2+-dependent metalloprotease that cleaves Mitogen-Activated Protein Kinase Kinases (MAPKKs/MEKs).",
            True,
            TOPIC
        ),
        (
            "How does the live attenuated 'Sterne 34F2' veterinary anthrax vaccine strain differ genetically from the classical 'Pasteur' vaccine strain of Bacillus anthracis?",
            [
                "Sterne strain lacks pXO1 (pXO1-, pXO2+), whereas Pasteur strain lacks pXO2 (pXO1+, pXO2-)",
                "Sterne strain retains toxigenic pXO1 but lacks capsular pXO2 (pXO1+, pXO2-), whereas Pasteur lacks pXO1",
                "Sterne strain is a formalin-inactivated cell-free culture filtrate devoid of both plasmids",
                "Sterne strain carries a recombinant capB gene integrated into a Bacillus subtilis vector"
            ],
            1,
            "Max Sterne (1937) isolated the rough, avirulent 34F2 variant that spontaneously lost the capsule plasmid pXO2 while retaining the toxin plasmid pXO1 (pXO1+, pXO2-), so it stimulates protective anti-PA antibodies without causing anthrax. Pasteur's heat-attenuated (42.5°C) strain lost pXO1 (pXO1-, pXO2+).",
            True,
            TOPIC
        ),
        (
            "Rhodococcus equi (Prescottella equi), a major cause of chronic suppurative bronchopneumonia with abscesses and ulcerative enterotyphlocolitis ('rattles') in foals aged 1 to 6 months, requires which plasmid-encoded virulence factor to survive inside alveolar macrophages?",
            [
                "Phospholipase D (PLD) dermonecrotic sphingomyelinase",
                "Listeriolysin O (LLO) cholesterol-dependent pore-forming cytolysin",
                "Virulence-Associated Protein A (VapA) encoded on an 80–90 kb plasmid",
                "Internalin A (InlA) surface E-cadherin binding adhesin"
            ],
            2,
            "Virulent equine isolates of Rhodococcus equi harbor a large conjugative plasmid encoding the surface lipoprotein VapA (Virulence-Associated Protein A, 15–17 kDa), which prevents acidification and phagolysosomal maturation inside foal alveolar macrophages.",
            True,
            TOPIC
        ),
        (
            "When Corynebacterium pseudotuberculosis and Staphylococcus aureus are streaked perpendicular to each other on sheep blood agar, what diagnostic hemolytic interaction occurs?",
            [
                "An enhanced arrowhead zone of complete beta-hemolysis (Classical positive CAMP reaction)",
                "A spade-shaped synergistic hemolysis zone identical to Rhodococcus equi",
                "Complete green alpha-hemolysis converting the entire plate to methemoglobin",
                "Inhibition of S. aureus beta-hemolysin, creating a crescentic zone of no lysis ('Reverse CAMP reaction')"
            ],
            3,
            "Phospholipase D (PLD) secreted by Corynebacterium pseudotuberculosis hydrolyzes membrane choline phospholipids and inhibits the action of Staphylococcus aureus beta-hemolysin (sphingomyelinase C), producing a diagnostic 'Reverse CAMP' inhibition zone (while showing synergistic hemolysis with Rhodococcus equi).",
            True,
            TOPIC
        ),
        (
            "Which urease-positive Corynebacterium species is the specific etiological agent of Ulcerative Posthitis and Vulvitis ('Pizzle Rot' / Enzootic Balanoposthitis) in castrated male sheep (wethers) grazing high-protein legume pastures?",
            [
                "Corynebacterium renale (Type I)",
                "Corynebacterium pseudotuberculosis (biovar ovis)",
                "Corynebacterium urealyticum",
                "Corynebacterium diphtheriae"
            ],
            0,
            "Corynebacterium renale rapidly hydrolyzes high urinary urea excreted by wethers and rams on high-protein pastures into cytotoxic ammonia, causing preputial ulceration and scabbing ('pizzle rot'), in addition to ascending bovine pyelonephritis.",
            True,
            TOPIC
        ),
        (
            "Once Listeria monocytogenes escapes from the phagolysosome into the host cell cytosol via Listeriolysin O, which bacterial surface protein nucleates host actin filaments into 'actin comet tails' for direct cell-to-cell spread?",
            [
                "Internalin B (InlB, which binds hepatocyte growth factor receptor Met)",
                "ActA (actin-assembly inducing surface protein)",
                "Protein A (Spa, which binds the Fc region of IgG)",
                "Vip (surface virulence protein binding endoplasmic reticulum Gp96)"
            ],
            1,
            "The polar surface protein ActA mimics host WASP proteins to recruit and activate the Arp2/3 complex, polymerizing host globular actin into filamentous 'comet tails' that push Listeria into adjacent cells via double-membrane pseudopods ('listeriopods') without exposure to extracellular antibodies.",
            True,
            TOPIC
        ),
        (
            "On PALCAM or Oxford selective agar used for isolating Listeria monocytogenes from food and clinical specimens, Listeria colonies are presumptively recognized by producing:",
            [
                "Bright pink colonies due to rapid fermentation of lactose and sucrose",
                "Colorless colonies with a black center due to reduction of sodium thiosulfate to H2S",
                "Gray-green colonies surrounded by a black halo resulting from esculin hydrolysis in the presence of ferric ions",
                "Metallic golden colonies surrounded by a clear zone of egg-yolk lecithinase activity"
            ],
            2,
            "PALCAM and Oxford media contain esculin and ferric ammonium citrate; all Listeria species hydrolyze esculin into esculetin, which reacts with Fe3+ ions to form a black phenolic iron complex around the gray-green colonies.",
            False,
            TOPIC
        ),
        (
            "In swine, the subacute cutaneous form of Erysipelothrix rhusiopathiae infection is clinically and pathologically pathognomonic due to the appearance of:",
            [
                "Generalized vesicular eruptions on the snout, coronary band, and interdigital cleft",
                "Symmetric gangrenous sloughing of the ear tips and tail induced by ergotism",
                "Pustular greasy brown exudative crusts covering the entire nursing piglet",
                "Rhomboid or rectangular raised erythematous skin plaques ('Diamond Skin Disease')"
            ],
            3,
            "Subacute swine erysipelas is characterized by 'Diamond Skin Disease'—well-demarcated, raised, rhomboid (diamond-shaped) erythematous to purplish cutaneous infarcts caused by bacterial vasculitis and thrombosis of dermal arterioles.",
            True,
            TOPIC
        ),
        (
            "Which biotype of Clostridium perfringens causes 'Lamb Dysentery' in neonatal lambs (under 2 weeks of age) and produces Alpha, Beta, and Epsilon major lethal toxins?",
            [
                "Clostridium perfringens Type B",
                "Clostridium perfringens Type A",
                "Clostridium perfringens Type C",
                "Clostridium perfringens Type E"
            ],
            0,
            "Clostridium perfringens is typed into five classical toxinotypes (A–E): Type A (alpha only), Type B (alpha, beta, epsilon; causes Lamb Dysentery), Type C (alpha, beta; causes 'Struck' in adult sheep and necrotic enteritis in neonatal piglets), Type D (alpha, epsilon; causes Pulpy Kidney), and Type E (alpha, iota).",
            True,
            TOPIC
        ),
        (
            "Why are newborn piglets and lambs uniquely susceptible to necrotic enteritis caused by Clostridium perfringens Type C, whereas older animals are resistant?",
            [
                "Neonatal enterocytes transiently express high levels of ganglioside GM1 receptors during the first 48 hours",
                "The primary lethal Beta-toxin is highly sensitive to trypsin, and colostrum contains potent trypsin inhibitors",
                "Beta-toxin requires activation by chymotrypsin, which is present only in neonatal meconium",
                "Older animals lack bile salts required to trigger germination of C. perfringens Type C spores"
            ],
            1,
            "The necrotizing Beta-toxin of C. perfringens Types B and C is extremely labile to proteolytic inactivation by pancreatic trypsin. Neonates have low pancreatic trypsin secretion and ingest colostrum rich in trypsin inhibitors, allowing intact Beta-toxin to cause hemorrhagic necrotizing enteritis.",
            True,
            TOPIC
        ),
        (
            "'Black Disease' (Infectious Necrotic Hepatitis) in sheep and cattle occurs when latent hepatic endospores of which bacterium germinate inside anaerobic necrotic tracks created by migrating immature Fasciola hepatica flukes?",
            [
                "Clostridium chauvoei (producing alpha and beta histotoxins)",
                "Clostridium septicum (producing pore-forming aerolysin-like alpha-toxin)",
                "Clostridium novyi Type B (producing necrotizing glucosylating alpha-toxin)",
                "Clostridium sordellii (producing lethal and hemorrhagic toxins)"
            ],
            2,
            "Spores of Clostridium novyi Type B ingested from pasture remain dormant in Kupffer cells of the liver. When immature liver flukes (Fasciola hepatica) migrate through hepatic parenchyma, the localized ischemic necrosis triggers spore germination and secretion of alpha-toxin. Subcutaneous venous congestion darkens the underside of the pelt ('Black Disease').",
            True,
            TOPIC
        ),
        (
            "Bacillary Hemoglobinuria ('Red Water Disease'), an acute fatal toxemia of cattle characterized by a single large ischemic hepatic infarct and intravascular hemolysis (port-wine colored urine), is caused by:",
            [
                "Clostridium perfringens Type A",
                "Clostridium chauvoei",
                "Clostridium tetani",
                "Clostridium haemolyticum (Clostridium novyi Type D)"
            ],
            3,
            "Clostridium haemolyticum (formerly C. novyi Type D) germinates in fluke-damaged bovine liver tissue and secretes massive amounts of beta-toxin (a necrotizing and hemolytic phospholipase C / lecithinase), causing massive intravascular hemolysis, hemoglobinuria, and a pathognomonic single large pale hepatic infarct.",
            True,
            TOPIC
        ),
        (
            "Which Clostridium species causes 'Braxy' (acute hemorrhagic and necrotizing abomasitis) in young sheep during winter following the ingestion of frosted root crops or frozen grass?",
            [
                "Clostridium septicum",
                "Clostridium chauvoei",
                "Clostridium botulinum Type C",
                "Clostridium perfringens Type D"
            ],
            0,
            "Clostridium septicum invades the abomasal mucosa damaged by frozen feed, causing acute fatal toxemic abomasitis known as 'Braxy' (Bradsot) in sheep, as well as exogenous Malignant Edema in wounds and 'Clostridial Dermatitis' in turkeys.",
            True,
            TOPIC
        ),
        (
            "'Tyzzer's Disease'—characterized by triad lesions of multifocal necrotizing hepatitis, necrotizing typhlocolitis, and myocarditis in foals (aged 1–6 weeks), laboratory rodents, and rabbits—is caused by which obligate intracellular, spore-forming filamentous bacterium demonstrated by Warthin-Starry silver stain?",
            [
                "Lawsonia intracellularis",
                "Clostridium piliforme (formerly Bacillus piliformis)",
                "Erysipelothrix rhusiopathiae",
                "Streptobacillus moniliformis"
            ],
            1,
            "Clostridium piliforme (formerly Bacillus piliformis) cannot be grown on cell-free bacteriological media; it is an obligate intracellular, Gram-negative-staining clostridial rod that forms characteristic bundles of parallel 'pick-up sticks' inside hepatocytes at the periphery of necrotic liver foci on Warthin-Starry silver stain.",
            True,
            TOPIC
        ),
        (
            "Contagious Ovine Footrot (interdigital dermatitis and underrunning of the hoof horn) is caused by a classic synergistic dual infection between Fusobacterium necrophorum and which essential primary hoof-matrix-degrading anaerobe?",
            [
                "Trueperella pyogenes (producing pyolysin)",
                "Bacteroides melaninogenicus (producing black-pigmented colonies)",
                "Dichelobacter nodosus (producing thermostable keratinolytic serine proteases AprV2)",
                "Treponema pedis (producing spirochetal digital dermatitis)"
            ],
            2,
            "While Fusobacterium necrophorum initiates interdigital skin maceration and produces leukotoxin, virulent Contagious Footrot strictly requires the obligate anaerobe Dichelobacter nodosus (possessing polar Type IV fimbriae and secreting extracellular thermostable elastase/keratinase AprV2 that digests the hard hoof horn).",
            True,
            TOPIC
        ),
        (
            "'Calf Diphtheria' (acute necrotizing laryngitis and stomatitis in young calves) and the 'Rumenitis-Liver Abscess Complex' in feedlot cattle are caused by which pleomorphic, filamentous Gram-negative obligate anaerobe?",
            [
                "Actinobacillus lignieresii",
                "Histophilus somni",
                "Pasteurella multocida Type B:2",
                "Fusobacterium necrophorum (subsp. necrophorum)"
            ],
            3,
            "Fusobacterium necrophorum subsp. necrophorum (Biovar A) is a normal inhabitant of the alimentary tract that invades acidotic ruminal mucosa to cause bovine liver abscesses (via its high-molecular-weight leukotoxin LktA), as well as Calf Diphtheria and bovine interdigital necrobacillosis ('foot rot').",
            True,
            TOPIC
        ),
        (
            "Biochemically and pharmacologically, how is Mycobacterium bovis definitively distinguished from Mycobacterium tuberculosis in reference laboratories?",
            [
                "M. bovis is Niacin-negative, Nitrate-negative, Pyrazinamide-resistant, and TCH-susceptible",
                "M. bovis is Niacin-positive, Nitrate-positive, Pyrazinamide-susceptible, and TCH-resistant",
                "M. bovis is Eugonic on glycerol agar, Catalase-negative at 22°C, and Urease-negative",
                "M. bovis is Rapidly growing (3 days), Pigment-producing in the dark, and Optochin-sensitive"
            ],
            0,
            "Unlike M. tuberculosis (which is eugonic, niacin-positive, nitrate-positive, pyrazinamide-sensitive, and resistant to thiophene-2-carboxylic acid hydrazide [TCH]), Mycobacterium bovis is dysgonic, niacin-negative, nitrate-negative, intrinsically resistant to pyrazinamide (due to a point mutation in pncA), and susceptible to TCH.",
            True,
            TOPIC
        ),
        (
            "The virulence glycolipid 'Cord Factor', which causes virulent Mycobacterium bovis and M. tuberculosis to grow in serpentine microscopic cords, inhibits leukocyte migration, and blocks phagosome-lysosome fusion, is chemically:",
            [
                "Lipoarabinomannan (LAM) capped with mannose residues",
                "Trehalose-6,6'-dimycolate (TDM)",
                "Phthiocerol dimycocerosate (PDIM)",
                "Phosphatidylinositol mannoside (PIM)"
            ],
            1,
            "Cord factor is Trehalose-6,6'-dimycolate (TDM), an abundant surface glycolipid composed of two mycolic acid molecules esterified to the disaccharide trehalose; it is recognized by the macrophage C-type lectin receptor Mincle and drives caseous granuloma formation.",
            True,
            TOPIC
        ),
        (
            "In Enterotoxigenic Escherichia coli (ETEC) causing neonatal diarrhea, how does Heat-Stable Enterotoxin A (STa) differ in its intracellular signaling mechanism from Heat-Labile Enterotoxin (LT)?",
            [
                "STa ADP-ribosylates Gi-alpha to inhibit adenylate cyclase, whereas LT activates phospholipase C",
                "STa cleaves 28S rRNA to halt protein synthesis, whereas LT opens voltage-gated Ca2+ channels",
                "STa binds guanylyl cyclase C (GC-C) to elevate intracellular cGMP, whereas LT ADP-ribosylates Gs-alpha to elevate cAMP",
                "STa forms transmembrane pores in crypt cells, whereas LT hydrolyzes brush-border sphingomyelin"
            ],
            2,
            "ETEC Heat-Labile toxin (LT, an AB5 toxin homologous to cholera toxin) ADP-ribosylates the Gs-alpha regulatory subunit to permanently activate adenylate cyclase (increasing cAMP), whereas Heat-Stable toxin A (STa, a small non-immunogenic peptide) binds brush-border guanylyl cyclase C (GC-C), elevating intracellular cGMP.",
            True,
            TOPIC
        ),
        (
            "'Edema Disease' (enterotoxemic colibacillosis) in rapidly growing pigs 1–2 weeks post-weaning, characterized by palpebral edema, gastric submucosal edema, and neurological ataxia (cerebrospinal angiopathy), is caused by E. coli strains expressing F18ab fimbriae and:",
            [
                "Heat-labile enterotoxin (LT-I) and East-1 peptide",
                "Cytotoxic Necrotizing Factor 1 (CNF1) and alpha-hemolysin",
                "Intimin (eae) outer membrane adhesin and bundle-forming pili",
                "Shiga toxin 2e (Stx2e / Verotoxin VT2e)"
            ],
            3,
            "Edema disease of swine is caused by specific serogroups of E. coli (O138, O139, O141) that colonize the small intestine via F18ab fimbriae and secrete Shiga toxin 2e (Stx2e / Edema Disease Principle), which enters the circulation and binds globotetraosylceramide (Gb4) receptors on vascular endothelial cells.",
            True,
            TOPIC
        ),
        (
            "On Sorbitol MacConkey Agar (SMAC), enterohemorrhagic Escherichia coli serotype O157:H7 is presumptively distinguished from commensal E. coli strains because E. coli O157:H7 is:",
            [
                "Sorbitol-negative (forming colorless colonies) and beta-D-glucuronidase (MUG)-negative",
                "Sorbitol-positive (forming bright pink colonies) and strongly beta-D-glucuronidase (MUG)-positive",
                "Hydrogen sulfide-positive (forming jet-black colonies) and urease-positive",
                "Oxidase-positive (forming purple colonies) and non-fermentative on glucose"
            ],
            0,
            "Whereas >93% of commensal E. coli strains ferment D-sorbitol rapidly (pink colonies on SMAC) and express beta-D-glucuronidase (cleaving MUG to a fluorescent product), E. coli O157:H7 does not ferment sorbitol within 24 hours (colorless colonies) and is MUG-negative.",
            True,
            TOPIC
        ),
        (
            "Both Salmonella Pullorum and Salmonella Gallinarum are non-motile avian-adapted serovars belonging to Kauffmann-White Serogroup D1 (O1,9,12). How are they biochemically differentiated from one another?",
            [
                "S. Pullorum ferments dulcitol rapidly without gas; S. Gallinarum is dulcitol-negative and gas-positive",
                "S. Pullorum decarboxylates ornithine and is dulcitol-negative; S. Gallinarum is ornithine-negative and ferments dulcitol",
                "S. Pullorum is strongly urease-positive and indole-positive; S. Gallinarum is urease-negative and citrate-positive",
                "S. Pullorum is oxidase-positive and liquefies gelatin; S. Gallinarum is oxidase-negative and coagulase-positive"
            ],
            1,
            "Salmonella Pullorum (Pullorum disease) is ornithine decarboxylase-positive, produces gas from glucose/mannitol, and fails to ferment dulcitol or maltose. Conversely, Salmonella Gallinarum (Fowl Typhoid) is ornithine decarboxylase-negative, anaerogenic (no gas from glucose), and ferments both dulcitol and maltose.",
            True,
            TOPIC
        ),
        (
            "On Xylose Lysine Deoxycholate (XLD) selective agar, typical Salmonella enterica colonies display which characteristic appearance after 24 hours of incubation?",
            [
                "Bright yellow opaque colonies surrounded by a yellow zone of unreversed acid production",
                "Blue-green mucoid colonies with a fruity grape-like odor and metallic sheen",
                "Red-pink colonies with black centers (due to xylose fermentation, lysine decarboxylation reversion, and H2S production)",
                "Pinpoint white fried-egg colonies embedded deep into the agar matrix"
            ],
            2,
            "On XLD agar, Salmonella ferments the limited xylose (briefly turning yellow), then exhausts xylose and decarboxylates lysine to cadaverine, reverting the pH to alkaline (red colony), while reducing sodium thiosulfate in the presence of ferric ammonium citrate to form a black H2S center.",
            True,
            TOPIC
        ),
        (
            "Which host-adapted Salmonella enterica serovar is a specific cause of contagious late-term abortion in mares and septic polyarthritis in neonatal foals?",
            [
                "Salmonella enterica serovar Dublin",
                "Salmonella enterica serovar Choleraesuis",
                "Salmonella enterica serovar Abortusovis",
                "Salmonella enterica serovar Abortusequi"
            ],
            3,
            "Host-adapted veterinary Salmonella serovars include S. Abortusequi (horses), S. Abortusovis (sheep), S. Dublin (cattle), S. Choleraesuis and S. Typhisuis (swine), and S. Pullorum / S. Gallinarum (poultry).",
            False,
            TOPIC
        ),
        (
            "Yersinia pestis, the causative agent of Plague transmitted by the oriental rat flea (Xenopsylla cheopis), produces which characteristic cultural appearance when grown undisturbed in nutrient broth overlaid with a drop of oil or ghee?",
            [
                "'Stalactite growth' (festoons of bacterial threads hanging downward from oil droplets)",
                "'Inverted fir-tree' or 'test-tube brush' lateral projections along the stab line",
                "Thick wrinkled dry surface pellicle with a violet pigment ring at the meniscus",
                "Concentric waves of swarming growth climbing up the glass wall of the tube"
            ],
            0,
            "When Yersinia pestis is grown without agitation in nutrient broth containing a surface layer of oil or clarified butter (ghee), threads of cohesive bacteria hang down from the underside of the oil droplets into the clear broth like 'stalactites' from a cave ceiling.",
            True,
            TOPIC
        ),
        (
            "The classical 'Weil-Felix reaction' used for presumptive serological diagnosis of Rickettsial infections is a heterophile tube agglutination test based on cross-reactive carbohydrate antigens shared between Rickettsia species and non-motile strains of:",
            [
                "Escherichia coli serotypes O157, O111, and O26",
                "Proteus vulgaris (OX19, OX2) and Proteus mirabilis (OXK)",
                "Brucella abortus (smooth lipopolysaccharide O-chain)",
                "Salmonella enterica serovar Typhi (Vi capsular antigen)"
            ],
            1,
            "In the Weil-Felix reaction, sera from patients/animals with rickettsial infections agglutinate non-motile 'O' variants (OX19, OX2, OXK) of Proteus vulgaris and Proteus mirabilis due to shared alkali-stable lipopolysaccharide epitopes.",
            True,
            TOPIC
        ),
        (
            "In Progressive Atrophic Rhinitis of swine, how does the Pasteurella multocida Toxin (PMT, a 146-kDa dermonecrotic toxin produced by capsular Type D strains) cause complete disappearance of the ventral nasal turbinate bones?",
            [
                "It directly chelates hydroxyapatite calcium crystals from mineralized bone matrix",
                "It acts as a bacterial collagenase that digests osteoid type I collagen fibers",
                "It deamidates host Gq and Gi alpha-subunits, blocking osteoblast differentiation while activating osteoclasts",
                "It induces autoimmune anti-osteocalcin IgE antibodies that trigger mast cell degranulation"
            ],
            2,
            "PMT is a potent intracellular mitogen that deamidates a critical glutamine residue in heterotrimeric G-proteins (Gq/11, Gi, G12/13), activating Rho GTPase and PLC-beta signaling; this arrests osteoblastic bone synthesis while hyper-activating osteoclastic bone resorption.",
            True,
            TOPIC
        ),
        (
            "Which member of the family Pasteurellaceae, formerly classified as Pasteurella haemolytica Biotype T, causes acute systemic septicemia and necrotizing pharyngitis/esophagitis in young feeder lambs (6–10 months old) and is distinguished from Mannheimia haemolytica by fermenting trehalose?",
            [
                "Avibacterium paragallinarum",
                "Gallibacterium anatis",
                "Actinobacillus seminis",
                "Bibersteinia trehalosi"
            ],
            3,
            "Bibersteinia trehalosi (formerly Pasteurella haemolytica Biotype T) ferments trehalose (but not arabinose) and causes acute systemic pasteurellosis (septicemia with subcutaneous hemorrhages and necrotic plaques on the pharynx, tonsils, and esophagus) in young adult sheep.",
            True,
            TOPIC
        ),
        (
            "Actinobacillus pleuropneumoniae (APP), the causative agent of severe fibrinohemorrhagic and necrotizing pleuropneumonia in swine, produces four RTX pore-forming toxins (ApxI–IV). Which toxin is expressed ONLY in vivo by all APP serotypes and is used in DIVA ELISAs to differentiate infected from subunit/bacterin-vaccinated pigs?",
            [
                "ApxIVA (species-specific RTX toxin induced exclusively in vivo)",
                "ApxI (strongly hemolytic and cytotoxic toxin of serotypes 1, 5, 9, 11)",
                "ApxII (weakly hemolytic toxin shared with Actinobacillus suis)",
                "ApxIII (non-hemolytic macrophage-specific cytotoxin of serotypes 2, 4, 6, 8)"
            ],
            0,
            "Unlike ApxI, ApxII, and ApxIII (which are secreted in vitro and included in subunit vaccines), ApxIVA is conserved across all 19 serotypes of A. pleuropneumoniae and is expressed strictly in vivo during active infection, making anti-ApxIVA ELISA an ideal species-specific and DIVA test.",
            True,
            TOPIC
        ),
        (
            "Histophilus somni (formerly Haemophilus somnus) is a fastidious capnophilic Gram-negative pleomorphic rod that causes which signature neurological syndrome in feedlot cattle?",
            [
                "Polioencephalomalacia (cerebrocortical necrosis responsive to thiamine)",
                "Thrombotic Meningoencephalitis (TME / 'Sleeper Syndrome') with multifocal hemorrhagic brain infarcts",
                "Unilateral facial nerve paralysis and trigeminal neuritis ('Circling Disease')",
                "Ascending flaccid paralysis starting from the tail and hindlimbs ('Loin Disease')"
            ],
            1,
            "Histophilus somni adheres to and induces apoptosis of vascular endothelial cells, exposing subendothelial collagen and triggering septic vasculitis and thrombosis throughout the brain (Thrombotic Meningoencephalitis, TME), myocardium, pleura, and joints.",
            True,
            TOPIC
        ),
        (
            "'New Duck Disease' (Infectious Serositis), an acute to chronic septicemic disease of 1-to-8-week-old ducklings characterized by fibrinous pericarditis, perihepatitis, airsacculitis, and torticollis, is caused by:",
            [
                "Pasteurella multocida subsp. septica",
                "Erysipelothrix rhusiopathiae",
                "Riemerella anatipestifer (family Weeksellaceae / Flavobacteriaceae)",
                "Avibacterium paragallinarum"
            ],
            2,
            "Riemerella anatipestifer (formerly Pasteurella anatipestifer / Moraxella anatipestifer) is a non-motile, non-spore-forming Gram-negative rod belonging to the family Weeksellaceae (order Flavobacteriales) that causes Infectious Serositis ('New Duck Disease') in ducks, geese, and turkeys.",
            True,
            TOPIC
        ),
        (
            "Infectious Bovine Keratoconjunctivitis (IBK / 'Pinkeye'), the most common contagious ocular disease of cattle worldwide, is caused by Moraxella bovis, whose two indispensable virulence factors are:",
            [
                "Capsular hyaluronic acid and neuraminidase",
                "Lipooligosaccharide endotoxin and IgA1 protease",
                "Heat-stable enterotoxin and bundle-forming fimbriae",
                "Type IV fimbriae (Q/I pili for corneal attachment) and an RTX beta-hemolysin/cytotoxin (MbxA)"
            ],
            3,
            "Moraxella bovis requires Type IV fimbriae (specifically the Q-pilus / I-pilus phase variants) to adhere to corneal epithelial cells against tear flushing, and secretes a calcium-dependent pore-forming RTX cytotoxin/hemolysin (MbxA) that lyses corneal epithelium and bovine neutrophils.",
            True,
            TOPIC
        ),
        (
            "In the classical biotyping of Brucella species, how do typical wild-type strains of Brucella abortus (Biovar 1) and Brucella melitensis (Biovar 1) differ in CO2 requirement, H2S production, and dye sensitivity (Thionin vs Basic Fuchsin at 1:50,000)?",
            [
                "B. abortus requires CO2, produces H2S, and is inhibited by Thionin; B. melitensis needs no CO2, produces no H2S, and grows in both dyes",
                "B. abortus needs no CO2, produces no H2S, and grows in both dyes; B. melitensis requires CO2, produces H2S, and is inhibited by Basic Fuchsin",
                "Both species require 10% CO2, produce abundant H2S, and are completely inhibited by both Thionin and Basic Fuchsin",
                "B. abortus grows in Thionin but is inhibited by Basic Fuchsin; B. melitensis is inhibited by both Thionin and Basic Fuchsin"
            ],
            0,
            "Classical differential table for Brucella: B. abortus (Biovar 1) requires 5–10% CO2 on primary isolation, produces H2S (blackening lead acetate strips), is inhibited by Thionin, and grows in Basic Fuchsin. B. melitensis requires no CO2, produces no H2S, and grows in the presence of both Thionin and Basic Fuchsin (whereas B. suis grows in Thionin and is inhibited by Basic Fuchsin).",
            True,
            TOPIC
        ),
        (
            "Why does vaccination of cattle with the Brucella abortus 'RB51' vaccine strain NOT cause false-positive reactions on standard smooth-lipopolysaccharide serological tests (such as RBPT, STAT, and indirect ELISA), unlike the classical 'Strain 19' vaccine?",
            [
                "RB51 is a recombinant subunit vaccine containing only purified outer membrane protein Omp25",
                "RB51 is a stable rough mutant (wboA gene disruption) lacking the immunodominant LPS O-polysaccharide chain",
                "RB51 is administered exclusively via the intranasal route and induces only secretory IgA in tears",
                "RB51 is heat-killed and adjuvanted with aluminum hydroxide, preventing IgG1 class switching"
            ],
            1,
            "Brucella abortus Strain RB51 is a rifampicin-resistant, stable rough mutant bearing an IS711 insertion in the wboA glycosyltransferase gene. Because it lacks the smooth LPS O-antigen chain recognized by RBPT, STAT, and smooth-LPS ELISAs, vaccinated cattle remain seronegative on routine surveillance tests (enabling DIVA).",
            True,
            TOPIC
        ),
        (
            "Which naturally rough Brucella species causes contagious epididymitis, tunica vaginalis adhesions, and sperm granulomas in rams (and sporadic placentitis in ewes) without possessing zoonotic potential for humans?",
            [
                "Brucella melitensis",
                "Brucella suis",
                "Brucella ovis",
                "Brucella neotomae"
            ],
            2,
            "Brucella ovis and Brucella canis are the two classical Brucella species that are naturally rough (lacking the LPS O-side chain) in their virulent wild-type state. B. ovis causes ovine contagious epididymitis in rams, requires 5–10% CO2, is non-urease producing, and is non-zoonotic.",
            True,
            TOPIC
        ),
        (
            "Francisella tularensis, the causative agent of Tularemia ('rabbit fever') in lagomorphs, rodents, cats, and sheep, is a minute, fastidious Gram-negative coccobacillus that strictly requires supplementation of blood agar with which amino acid?",
            [
                "D-Glutamic acid",
                "L-Tryptophan",
                "Meso-diaminopimelic acid",
                "L-Cysteine (or cystine)"
            ],
            3,
            "Francisella tularensis is an obligate aerobic, facultative intracellular pathogen that cannot synthesize sulfhydryl compounds and requires media enriched with L-cysteine or cystine (such as Francis's glucose-cystine blood agar or Buffered Charcoal Yeast Extract [BCYE] with cysteine).",
            True,
            TOPIC
        ),
        (
            "Chromobacterium violaceum, an environmental water and soil bacterium that causes fatal pyogranulomatous pneumonia and hepatic abscesses in swine, cattle, and dogs in tropical regions, is immediately recognized in culture by producing:",
            [
                "An insoluble deep violet-purple pigment called violacein",
                "A water-soluble blue-green phenazine pigment called pyocyanin",
                "A brick-red prodigiosin pigment synthesized only at 25°C",
                "A fluorescent yellow-green siderophore pigment called pyoverdine"
            ],
            0,
            "Chromobacterium violaceum is a facultative anaerobic, motile Gram-negative rod that synthesizes violacein—an ethanol-soluble, water-insoluble deep violet tryptophan derivative with antioxidant and antimicrobial properties.",
            False,
            TOPIC
        ),
        (
            "In diagnostic veterinary microbiology, Campylobacter fetus subsp. venerealis (the obligate venereal agent of bovine infertility) is differentiated biochemically from Campylobacter fetus subsp. fetus (cause of sporadic ovine and bovine abortion) based on its:",
            [
                "Ability to grow rapidly at 42°C and hydrolyze sodium hippurate",
                "Inability to grow in media containing 1% Glycine (glycine intolerance)",
                "Production of abundant urease and resistance to nalidixic acid",
                "Strict requirement for 20% atmospheric oxygen and absence of catalase"
            ],
            1,
            "Both subspecies of Campylobacter fetus grow at 25°C and 37°C (but not 42°C) and are catalase-positive; however, C. fetus subsp. venerealis is intolerant of 1% glycine (no growth) and does not produce H2S in cysteine medium, whereas C. fetus subsp. fetus grows in 1% glycine.",
            True,
            TOPIC
        ),
        (
            "Which thermophilic Campylobacter species grows optimally at 42°C to 43°C and is differentiated from Campylobacter coli in food safety and veterinary laboratories by its positive 'Hippurate Hydrolysis Test' (forming a deep purple color with ninhydrin)?",
            [
                "Campylobacter fetus subsp. venerealis",
                "Campylobacter sputorum biovar bubulus",
                "Campylobacter jejuni",
                "Campylobacter hyointestinalis"
            ],
            2,
            "Campylobacter jejuni is a thermophilic campylobacter (growing optimally at 42°C) and is the only major veterinary/zoonotic Campylobacter species that possesses the hipO gene encoding hippuricase, which hydrolyzes sodium hippurate into benzoic acid and glycine (detected with ninhydrin).",
            True,
            TOPIC
        ),
        (
            "In Leptospira epidemiology, cattle serve as the natural maintenance (reservoir) host—characterized by chronic renal colonization, mild clinical signs, and persistent reproductive failure/milk drop syndrome—for which specific serovar?",
            [
                "Leptospira interrogans serovar Icterohaemorrhagiae",
                "Leptospira interrogans serovar Canicola",
                "Leptospira interrogans serovar Pomona",
                "Leptospira borgpetersenii / interrogans serovar Hardjo"
            ],
            3,
            "Each Leptospira serovar is adapted to a specific maintenance reservoir host: Hardjo in cattle, Pomona and Tarassovi in swine, Canicola in dogs, Icterohaemorrhagiae and Copenhageni in rats, and Bratislava in horses and pigs.",
            True,
            TOPIC
        ),
        (
            "When Leptospira interrogans is inoculated into semi-solid Fletcher's or EMJH medium (containing 0.1–0.2% agar), growth characteristically appears 0.5 to 1.5 cm below the surface of the medium as a dense translucent disc known as:",
            [
                "Dinger's ring (or Dinger's disk)",
                "The stalactite festoon",
                "The bottle-brush zone",
                "Pfeiffer's phenomenon"
            ],
            0,
            "In semi-solid leptospiral media (Fletcher's or semi-solid EMJH), leptospires migrate to their optimal oxygen tension slightly below the meniscus, forming a well-defined flat horizontal band of turbidity called Dinger's ring (or Dinger's disk).",
            True,
            TOPIC
        ),
        (
            "How are non-pathogenic, free-living water saprophytes (Leptospira biflexa) differentiated in the laboratory from pathogenic strains (Leptospira interrogans)?",
            [
                "L. biflexa fails to grow below 37°C and is lysed by 1% bile salts",
                "L. biflexa grows at 13°C and in the presence of 8-azaguanine (225 ug/mL), whereas L. interrogans is inhibited",
                "L. biflexa lacks periplasmic endoflagella and is strongly Gram-positive",
                "L. biflexa requires Mycobactin J and 10% carbon dioxide for growth"
            ],
            1,
            "Saprophytic Leptospira biflexa can replicate at low temperatures (13°C), grows in the presence of the purine analog 8-azaguanine (225 ug/mL), and converts to spherical bodies in 1 M NaCl, whereas pathogenic L. interrogans cannot grow at 13°C and is inhibited by 8-azaguanine.",
            True,
            TOPIC
        ),
        (
            "Avian Spirochetosis—an acute fatal septicemic disease of chickens, turkeys, and ducks characterized by high fever, greenish diarrhea, paresis, and mottled enlarged spleen—is caused by Borrelia anserina and transmitted biologically by:",
            [
                "The hard prostriate deer tick Ixodes scapularis",
                "The poultry red mite Dermanyssus gallinae",
                "The soft argasid fowl tick Argas persicus",
                "The biting midge Culicoides imicola"
            ],
            2,
            "Borrelia anserina causes Avian Spirochetosis and is biologically transmitted (with transovarial and transstadial transmission) by the cosmopolitan soft fowl tick Argas persicus.",
            True,
            TOPIC
        ),
        (
            "While Brachyspira hyodysenteriae causes severe mucohemorrhagic Swine Dysentery, which weakly beta-hemolytic, hippurate-positive spirochete attaches by one pole to colonic enterocytes ('false brush border') to cause milder Porcine Intestinal Spirochetosis?",
            [
                "Brachyspira suanatina",
                "Treponema paraluiscuniculi",
                "Leptospira interrogans serovar Pomona",
                "Brachyspira pilosicoli"
            ],
            3,
            "Brachyspira pilosicoli is weakly beta-hemolytic on trypticase soy blood agar (unlike strongly beta-hemolytic, indole-positive B. hyodysenteriae), hydrolyzes hippurate, and causes Porcine Colonic Spirochetosis ('gray cement-like diarrhea') in grower pigs.",
            False,
            TOPIC
        ),
        (
            "In poultry mycoplasmosis, how is Mycoplasma synoviae (the agent of infectious synovitis and airsacculitis) nutritionally distinguished from Mycoplasma gallisepticum during primary isolation on Frey's or PPLO medium?",
            [
                "Mycoplasma synoviae strictly requires supplementation with beta-NAD (Coenzyme I / V-factor) and cysteine",
                "Mycoplasma synoviae grows rapidly on nutrient agar without serum or cholesterol",
                "Mycoplasma synoviae requires Mycobactin J and sodium pyruvate at pH 5.5",
                "Mycoplasma synoviae is an obligate anaerobe that is killed by 5% carbon dioxide"
            ],
            0,
            "Mycoplasma synoviae is fastidious and strictly requires reduced nicotinamide adenine dinucleotide (beta-NAD, 0.01%) and cysteine hydrochloride for in vitro growth on Frey's medium, whereas Mycoplasma gallisepticum grows without exogenous NAD.",
            True,
            TOPIC
        ),
        (
            "Which specialized staining procedure is used to examine intact Mycoplasma colonies directly on agar blocks, staining the dense central core dark royal blue and the peripheral surface zone light blue without decolorization?",
            [
                "Stamp's modified Ziehl-Neelsen stain",
                "Dienes stain (methylene blue, azure II, and maltose)",
                "Schaeffer-Fulton malachite green stain",
                "Seller's basic fuchsin and methylene blue stain"
            ],
            1,
            "Dienes stain (an alcoholic/aqueous solution of methylene blue, azure II, maltose, and sodium carbonate) is applied to a coverslip placed directly over Mycoplasma colonies on agar. Live Mycoplasma colonies stay stained two-tone blue (dense dark blue center, light blue periphery), whereas bacterial L-forms or artifacts often reduce/decolorize the dye.",
            True,
            TOPIC
        ),
        (
            "Mycoplasma haemofelis (formerly Haemobartonella felis) and Mycoplasma suis (formerly Eperythrozoon suis) belong to the 'Hemotropic Mycoplasmas' (hemoplasmas), which are characterized by:",
            [
                "Growing abundantly on MacConkey agar into bright pink mucoid colonies within 18 hours",
                "Multiplying exclusively inside the nucleus of circulating polymorphonuclear neutrophils",
                "Attaching epicellularly to the outer surface of host erythrocytes and remain uncultivable on cell-free media",
                "Synthesizing a thick peptidoglycan cell wall that renders them susceptible to penicillin G"
            ],
            2,
            "Hemotropic mycoplasmas (hemoplasmas) are wall-less epicellular bacteria that adhere tightly to indentations on the plasma membrane of host erythrocytes (inducing immune-mediated hemolytic anemia), have never been cultivated in vitro on cell-free media, and are treated with tetracyclines (doxycycline/oxytetracycline).",
            True,
            TOPIC
        ),
        (
            "Coxiella burnetii displays 'Phase Variation' analogous to smooth-rough LPS variation in Enterobacteriaceae. In the serodiagnosis of human and ruminant Q Fever, what is the clinical significance of Phase I vs Phase II antibodies?",
            [
                "Phase I antibodies appear only after vaccination, whereas Phase II antibodies indicate absence of infection",
                "Phase I organisms lack LPS and grow only in cell culture, whereas Phase II organisms have full-length LPS",
                "Phase II antibodies are restricted to horses, whereas Phase I antibodies occur only in poultry",
                "Anti-Phase II antibodies predominate in acute Q fever, whereas high anti-Phase I IgG titers indicate chronic Q fever"
            ],
            3,
            "Virulent Coxiella burnetii in animals possesses smooth full-length LPS (Phase I), which sterically masks surface proteins. Consequently, the host mounts an early antibody response against exposed surface proteins (Phase II antigen) during acute infection, whereas sustained high IgG titers against Phase I LPS antigen are diagnostic of chronic Q fever (e.g., endocarditis/placentitis).",
            True,
            TOPIC
        ),
        (
            "'Heartwater' (Cowdriosis)—a high-mortality tick-borne disease of cattle, sheep, and goats in sub-Saharan Africa and the Caribbean characterized by hydropericardium, hydrothorax, and neurological paddling—is caused by Ehrlichia ruminantium and transmitted by:",
            [
                "Amblyomma ticks (such as Amblyomma variegatum and Amblyomma hebraeum)",
                "Rhipicephalus (Boophilus) microplus one-host cattle ticks",
                "Hyalomma anatolicum two-host ticks",
                "Ornithodoros moubata soft argasid ticks"
            ],
            0,
            "Ehrlichia ruminantium (formerly Cowdria ruminantium) is transmitted biologically by three-host bont ticks of the genus Amblyomma (A. variegatum, A. hebraeum) and is diagnosed post-mortem by demonstrating purplish colonies (morulae) inside capillary endothelial cells in Giemsa-stained cerebral cortex squash smears.",
            True,
            TOPIC
        ),
        (
            "'Salmon Poisoning Disease'—an acute, highly fatal hemorrhagic enteritis and generalized lymphadenopathy in dogs that consume raw salmonid fish in the Pacific Northwest—is caused by which intracellular rickettsial bacterium carried inside the trematode vector Nanophyetus salmincola?",
            [
                "Rickettsia rickettsii",
                "Neorickettsia helminthoeca",
                "Anaplasma phagocytophilum",
                "Ehrlichia ewingii"
            ],
            1,
            "Neorickettsia helminthoeca is an obligate intracellular endosymbiont of the digenean fluke Nanophyetus salmincola. When dogs eat raw salmon or trout containing encysted fluke metacercariae, the adult flukes attach to the canine intestinal mucosa and inoculate N. helminthoeca into macrophages.",
            True,
            TOPIC
        ),
        (
            "Potomac Horse Fever (Equine Neorickettsiosis / Equine Monocytic Ehrlichiosis), characterized by acute fever, depression, profuse watery diarrhea, colic, and severe laminitis in horses near freshwater streams during summer, is caused by:",
            [
                "Ehrlichia canis transmitted by Rhipicephalus sanguineus",
                "Anaplasma marginale transmitted by Dermacentor variabilis",
                "Neorickettsia risticii transmitted via ingestion of aquatic insects (caddisflies/mayflies) harboring trematode metacercariae",
                "Coxiella burnetii transmitted by inhalation of desiccated placental aerosols"
            ],
            2,
            "Neorickettsia risticii (formerly Ehrlichia risticii) infects equine blood monocytes and colonic crypt epithelial cells. Horses acquire infection by accidentally ingesting emergent aquatic insects (mayflies, caddisflies, damselflies) carrying metacercariae of freshwater snail trematodes (Acanthatrium/Lecithodendrium).",
            True,
            TOPIC
        ),
        (
            "Enzootic Abortion of Ewes (EAE / Ovine Enzootic Abortion), a major cause of late-gestation abortion, stillbirth, and necrotizing placentitis with thickened leathery intercotyledonary membranes in sheep and goats, is caused by:",
            [
                "Campylobacter jejuni",
                "Coxiella burnetii",
                "Listeria ivanovii",
                "Chlamydia abortus (formerly Chlamydophila abortus)"
            ],
            3,
            "Chlamydia abortus is the premier infectious cause of abortion in sheep and goats in Europe and North America. Ewes infected in one pregnancy often abort in the final 2–3 weeks of the subsequent gestation, shedding vast numbers of elementary bodies visible as red coccoid clusters on Stamp's or Gimenez stain.",
            True,
            TOPIC
        ),
        (
            "In the 'Gimenez Staining' protocol for demonstrating intracellular Chlamydia abortus elementary bodies and Rickettsia species in impression smears, how do the organisms appear microscopically?",
            [
                "Bright red intracellular coccobacilli against a bluish-green host cell background (counterstained with malachite green)",
                "Dark purple rods surrounded by an unstained halo against a yellow picric acid background",
                "Apple-green fluorescent filaments against a black potassium permanganate background",
                "Jet-black spiral filaments against a golden-brown silver-impregnated background"
            ],
            0,
            "In the Gimenez stain, carbol basic fuchsin buffered with sodium phosphate stains Chlamydia elementary bodies, Rickettsia, and Coxiella bright red, while 0.8% aqueous malachite green oxalate counterstains the background host cells and debris bluish-green.",
            True,
            TOPIC
        ),
        (
            "Haalstra's method for isolating Dermatophilus congolensis from dry, crusty scabs of cattle with rain scald (streptothricosis) exploits which specific biological behavior of its infective zoospores?",
            [
                "Resistance of mature endospores to heating at 80°C for 30 minutes in ethanol",
                "Release of motile zoospores upon moistening in distilled water followed by positive chemotaxis toward a 10% CO2 atmosphere",
                "Psychrophilic replication in nutrient broth held at 4°C for 6 weeks",
                "Selective survival in 10% potassium hydroxide and 5% sodium hypochlorite"
            ],
            1,
            "In Haalstra's technique, small fragments of crust are placed in sterile distilled water at room temperature for 3.5 hours to stimulate release of motile zoospores, then transferred to a candle jar (CO2-enriched atmosphere) for 15 minutes; zoospores swim chemotactically to the surface meniscus toward CO2 and are streaked onto blood agar.",
            True,
            TOPIC
        ),
        (
            "Streptobacillus moniliformis, the etiological agent of Rat-Bite Fever (and Haverhill fever) in rodents and humans, is culturally and morphologically notable in microbiology because it:",
            [
                "Requires 42°C microaerophilic incubation and forms seagull-shaped rods",
                "Produces a bright violet pigment and grows on MacConkey agar without serum",
                "Forms pleomorphic filamentous chains with bulbous yeast-like swellings ('string of beads') and spontaneously produces L-forms",
                "Is a strict obligate intracellular rickettsia transmitted by the rat flea Xenopsylla cheopis"
            ],
            2,
            "Streptobacillus moniliformis is a fastidious Gram-negative pleomorphic rod (requiring 20% serum, blood, or ascitic fluid) that forms long tangled filaments with spherical/fusiform bulbous swellings ('moniliform' / string of beads) and spontaneously gives rise to cell-wall-deficient L-phase colonies ('fried-egg' appearance).",
            False,
            TOPIC
        ),
        (
            "Which fastidious, Gram-negative intra-erythrocytic and endotheliotropic bacterium is maintained in a chronic subclinical bacteremia in domestic cats, transmitted between cats by the cat flea (Ctenocephalides felis), and causes zoonotic 'Cat Scratch Disease' in humans?",
            [
                "Pasteurella multocida subsp. multocida",
                "Mycoplasma haemofelis",
                "Francisella tularensis",
                "Bartonella henselae"
            ],
            3,
            "Bartonella henselae resides inside feline erythrocytes and is transmitted among cats via infected flea feces (Ctenocephalides felis) inoculated by scratching; in humans, a cat scratch or bite causes regional lymphadenopathy ('Cat Scratch Disease') or bacillary angiomatosis in immunocompromised individuals.",
            True,
            TOPIC
        ),
        (
            "'Summer Mastitis' in dry dairy cows and pregnant heifers pastured in wooded areas is a severe suppurative mastitis characterized by thick, foul-smelling greenish pus, transmitted mechanically by the sheep headfly (Hydrotaea irritans), and caused by a synergistic infection of:",
            [
                "Trueperella pyogenes and the obligate anaerobe Peptoniphilus (Peptostreptococcus) indolicus",
                "Staphylococcus aureus and Streptococcus agalactiae",
                "Escherichia coli O157:H7 and Klebsiella pneumoniae",
                "Mycoplasma bovis and Nocardia asteroides"
            ],
            0,
            "Summer mastitis is a classic polymicrobial synergistic infection in which Trueperella pyogenes (formerly Arcanobacterium/Corynebacterium pyogenes) combines with the strict anaerobe Peptoniphilus indolicus (and Fusobacterium necrophorum), transmitted to the teat orifice by the fly Hydrotaea irritans.",
            True,
            TOPIC
        ),
        (
            "How is Trueperella pyogenes culturally differentiated from beta-hemolytic Streptococci when isolated from bovine suppurative lesions or mastitis milk?",
            [
                "T. pyogenes is strongly catalase-positive, oxidase-positive, and grows on MacConkey agar",
                "T. pyogenes is a pleomorphic Gram-positive diphtheroid that pits (liquefies) Loeffler's coagulated serum slopes and expresses pyolysin",
                "T. pyogenes forms large mucoid colonies within 6 hours and is resistant to bacitracin and penicillin",
                "T. pyogenes is an obligate intracellular organism that grows only in yolk sacs of embryonated eggs"
            ],
            1,
            "Trueperella pyogenes is a catalase-negative, pinpoint beta-hemolytic, pleomorphic Gram-positive rod (coryneform/actinomycete) whose colonies become visible at 48 hours, secrete the cholesterol-dependent cytolysin Pyolysin (PLO), and characteristically pit (liquefy) Loeffler's coagulated serum slants.",
            True,
            TOPIC
        ),
        (
            "Ornithobacterium rhinotracheale (ORT) has emerged globally as a major respiratory pathogen of turkeys and broiler chickens, causing:",
            [
                "Diphtheritic pseudomembranes in the larynx and hemorrhagic tracheitis with intranuclear inclusions",
                "Hard nodular caseous granulomas ('yellow buttons') in the lungs and air sacs of newly hatched chicks",
                "Fibrinopurulent pneumonia and airsacculitis with characteristic 'yogurt-like' foamy exudate in the abdominal air sacs",
                "Acute watery white diarrhea with chalky urate pasting around the vent in 3-day-old chicks"
            ],
            2,
            "Ornithobacterium rhinotracheale is a slow-growing, pleomorphic Gram-negative rod (family Weeksrellaceae) that causes contagious respiratory disease, growth retardation, osteitis/meningitis, and a pathognomonic thick, white-to-yellow 'yogurt-like' fibrinopurulent exudate in the air sacs of turkeys and broilers.",
            False,
            TOPIC
        ),
        (
            "Avian Pathogenic Escherichia coli (APEC), the cause of avian colibacillosis (airsacculitis, fibrinous perihepatitis, pericarditis, salpingitis, and omphalitis), predominantly belongs to which three somatic (O) serogroups worldwide?",
            [
                "O157, O111, and O26",
                "O138, O139, and O141",
                "O8, O9, and O101",
                "O1, O2, and O78"
            ],
            3,
            "While O157/O111/O26 are enterohemorrhagic (STEC) and O138/O139/O141 cause porcine edema disease, Avian Pathogenic E. coli (APEC) strains causing systemic colisepticemia and polyserositis in poultry predominantly belong to serogroups O1, O2, and O78.",
            True,
            TOPIC
        ),
        (
            "In sheep, Listeria ivanovii (formerly Listeria monocytogenes serovar 5) differs from Listeria monocytogenes in both its clinical spectrum and its hemolysis on sheep blood agar because L. ivanovii:",
            [
                "Causes ovine abortion and enteritis (without meningoencephalitis) and produces a wide, bizonal beta-hemolytic zone with a positive CAMP reaction with Rhodococcus equi",
                "Causes exclusively neural circling disease in adult rams and is completely non-hemolytic on blood agar",
                "Is an obligate anaerobe that fails to hydrolyze esculin and is CAMP-positive only with Staphylococcus aureus",
                "Grows only at 42°C and produces black colonies on Xylose Lysine Deoxycholate (XLD) agar"
            ],
            0,
            "Listeria ivanovii is strongly beta-hemolytic on sheep blood agar (owing to ivanolysin O and sphingomyelinase C), gives a spade-shaped positive CAMP reaction with Rhodococcus equi (not S. aureus), ferments D-xylose (not L-rhamnose), and causes abortion in ewes without causing neural encephalitis.",
            True,
            TOPIC
        ),
        (
            "What is the definitive biochemical and cultural difference between Burkholderia pseudomallei (agent of Melioidosis) and Burkholderia mallei (agent of Glanders)?",
            [
                "B. pseudomallei is non-motile, oxidase-negative, and fails to grow on MacConkey agar",
                "B. pseudomallei is motile by polar flagella, grows at 42°C, and forms wrinkled 'cornflower head' colonies on Ashdown's medium",
                "B. pseudomallei is an obligate intracellular organism that requires L-cysteine and heated horse blood",
                "B. pseudomallei is a Gram-positive branching filament that is partially acid-fast on Kinyoun stain"
            ],
            1,
            "Unlike Burkholderia mallei (an obligate mammalian pathogen that is non-motile due to deletion/frameshift in flagellar genes and grows poorly on selective media), B. pseudomallei is an environmental saprophyte that is actively motile via polar tuft of flagella, grows at 42°C, is gentamicin/polymyxin-resistant, and forms dry wrinkled purple colonies on Ashdown's agar.",
            True,
            TOPIC
        ),
        (
            "In dogs and pigs, Bordetella bronchiseptica (a primary agent of Canine Infectious Respiratory Disease Complex / 'Kennel Cough' and non-progressive porcine atrophic rhinitis) is biochemically characterized as a Gram-negative coccobacillus that is:",
            [
                "Non-motile, lactose-fermenting, urease-negative, and oxidase-negative",
                "Obligately anaerobic, H2S-positive on TSI agar, and indole-positive",
                "Strictly aerobic, motile by peritrichous flagella, non-fermentative, oxidase-positive, citrate-positive, and rapidly urease-positive",
                "Microaerophilic, darting-motile by a single polar flagellum, and hippurate-positive"
            ],
            2,
            "Unlike Bordetella pertussis (which is non-motile, urease-negative, and citrate-negative), Bordetella bronchiseptica is motile via peritrichous flagella, grows on MacConkey agar (non-lactose fermenter), is oxidase-positive, citrate-positive, and rapidly hydrolyzes urea within 4 hours.",
            True,
            TOPIC
        ),
        (
            "Anaplasma phagocytophilum (formerly Ehrlichia phagocytophila / Ehrlichia equi), the tick-borne agent of 'Tick-Borne Fever' in sheep and cattle and Granulocytic Anaplasmosis in horses and dogs, forms intracytoplasmic morulae predominantly inside:",
            [
                "Mature circulating erythrocytes (at the extreme cell margin)",
                "Circulating blood platelets (thrombocytes)",
                "Cerebral capillary vascular endothelial cells",
                "Granulocytes (primarily neutrophils and eosinophils)"
            ],
            3,
            "Whereas Anaplasma marginale/centrale infect erythrocytes, Anaplasma platys infects platelets, and Ehrlichia canis/chaffeensis infect monocytes, Anaplasma phagocytophilum (and Ehrlichia ewingii) selectively infects granulocytes (neutrophils and eosinophils), causing severe neutropenia and immunosuppression ('tick-borne fever' in lambs).",
            True,
            TOPIC
        ),
        (
            "In guinea pigs, cervical lymphadenitis ('Lumps') characterized by massive abscessation of the submandibular and cervical lymph nodes is classically caused by which beta-hemolytic Lancefield Group C streptococcus?",
            [
                "Streptococcus equi subsp. zooepidemicus",
                "Streptococcus agalactiae",
                "Streptococcus suis serotype 2",
                "Streptococcus pneumoniae"
            ],
            0,
            "Streptococcus equi subsp. zooepidemicus (Lancefield Group C, which ferments sorbitol and lactose unlike S. equi subsp. equi) is a normal mucosal commensal of cavies that invades Oral abrasions from coarse feed to cause classic Cervical Lymphadenitis ('Lumps') in guinea pigs, as well as Opportunistic endometritis and pneumonia in horses.",
            False,
            TOPIC
        ),
        (
            "How is Streptococcus equi subsp. equi (the obligate agent of equine Strangles) biochemically differentiated from the closely related opportunist Streptococcus equi subsp. zooepidemicus (both in Lancefield Group C)?",
            [
                "S. equi subsp. equi ferments both sorbitol and lactose; S. zooepidemicus ferments neither",
                "S. equi subsp. equi fails to ferment sorbitol, lactose, and trehalose; S. zooepidemicus ferments sorbitol and lactose",
                "S. equi subsp. equi is strongly catalase-positive and grows in 6.5% NaCl broth",
                "S. equi subsp. equi hydrolyzes esculin and hippurate, whereas S. zooepidemicus is negative for both"
            ],
            1,
            "Sugar fermentation is the gold-standard phenotypic test to distinguish the Lancefield Group C equine streptococci: Streptococcus equi subsp. equi is negative for sorbitol, lactose, and trehalose fermentation, whereas S. equi subsp. zooepidemicus ferments both sorbitol and lactose.",
            True,
            TOPIC
        ),
        (
            "The antiphagocytic cell-wall protein of Streptococcus equi subsp. equi that binds host fibrinogen and complement factor H, induces protective mucosal immunity, and serves as the basis for serotyping and subunit strangles vaccines is:",
            [
                "Protein A (Spa)",
                "Internalin A (InlA)",
                "SeM protein (M-like protein)",
                "VapA lipoprotein"
            ],
            2,
            "Streptococcus equi subsp. equi expresses a surface-anchored M-like fibrillar protein designated SeM, which binds fibrinogen and IgG-Fc to block C3b deposition and neutrophil phagocytosis; SeM is the principal protective immunogen in equine strangles.",
            True,
            TOPIC
        ),
        (
            "In pigs and sheep, 'Glässer's Disease' (fibrinous polyserositis, polyarthritis, and meningitis) is caused by Glaesserella parasuis (Haemophilus parasuis), which requires which specific growth factor when cultured on blood agar?",
            [
                "X-factor (hemin / protoporphyrin IX) only",
                "Both X-factor (hemin) and V-factor (NAD)",
                "Mycobactin J and 0.5% sodium pyruvate",
                "V-factor (Nicotinamide Adenine Dinucleotide, NAD) only, without X-factor"
            ],
            3,
            "Glaesserella parasuis (formerly Haemophilus parasuis), like Avibacterium paragallinarum and Actinobacillus pleuropneumoniae Biovar 1, is V-factor (NAD) dependent and does NOT require X-factor (hemin), allowing it to grow on plain nutrient/blood agar as satellite colonies around an NAD-secreting Staphylococcus aureus streak.",
            True,
            TOPIC
        ),
        (
            "Which selective medium containing polymyxin B, bacitracin, and cycloheximide (actidione) in a heart infusion blood agar base is classically used for the selective isolation of Brucella species from contaminated fetal membranes and milk?",
            [
                "Farrell's medium (or Kuzdas and Morse medium)",
                "PLET medium (Polymyxin, Lysozyme, EDTA, Thallous acetate)",
                "Ashdown's crystal violet gentamicin neutral red agar",
                "Stonebrink's pyruvate malachite green egg medium"
            ],
            0,
            "Farrell's medium (serum dextrose agar containing six antimicrobials: polymyxin B, bacitracin, natamycin/cycloheximide, nalidixic acid, nystatin, and vancomycin) is the WOAH-recommended selective medium for primary isolation of Brucella from contaminated field samples.",
            True,
            TOPIC
        ),
        (
            "Why is Castaneda's Biphasic Medium (consisting of both an agar slant and a broth phase in the same bottle) traditionally advocated for culturing Brucella from blood or bone marrow?",
            [
                "It allows anaerobic growth at the bottom and aerobic growth at the top simultaneously",
                "Tilting the closed bottle inoculates the agar slant without opening it, minimizing aerosol infection",
                "It separates motile flagellated Brucella from non-motile rough environmental contaminants",
                "It neutralizes intracellular erythritol that would otherwise lyse Brucella in blood cultures"
            ],
            1,
            "Brucella species have an extremely low infectious dose by aerosol and are a leading cause of laboratory-acquired infections. Castaneda's biphasic bottle contains a solid agar slant and liquid broth; tilting the closed bottle inoculates the slant periodically without unstoppering.",
            True,
            TOPIC
        ),
        (
            "In Contagious Bovine Pleuropneumonia (CBPP) caused by Mycoplasma mycoides subsp. mycoides, which heat-stable carbohydrate antigen is secreted in high concentrations into lung exudate, plasma, and urine, and is used in precipitin and latex agglutination tests?",
            [
                "Arabinogalactan mycolic acid ester",
                "Poly-gamma-D-glutamic acid polypeptide",
                "Galactan (galactofuranose homopolysaccharide)",
                "Phosphorylcholine teichoic acid polymer"
            ],
            2,
            "Mycoplasma mycoides subsp. mycoides synthesizes an abundant capsular and extracellular polysaccharide called Galactan (beta-1,6-galactofuranose polymer), which circulates in blood and urine during CBPP and triggers pulmonary thrombosis and edema.",
            True,
            TOPIC
        ),
        (
            "How are saprophytic Acholeplasma species (such as Acholeplasma laidlawii) differentiated in the diagnostic mycology/mycoplasma laboratory from true Mycoplasma species?",
            [
                "Acholeplasma species synthesize a rigid peptidoglycan cell wall and stain Gram-positive",
                "Acholeplasma species are obligate intracellular pathogens that grow only in tissue culture",
                "Acholeplasma species hydrolyze urea within 2 hours to form tiny pinpoint brown colonies",
                "Acholeplasma species grow on sterol-free (serum-free) media and are resistant to 1.5% Digitonin"
            ],
            3,
            "Unlike Mycoplasma and Ureaplasma (which are sterol-auxotrophic and lysed by the cholesterol-complexing saponin digitonin, giving a >5 mm inhibition zone), Acholeplasma species synthesize carotenoids instead of requiring sterols, grow on serum-free media, and are digitonin-resistant.",
            True,
            TOPIC
        ),
        (
            "'Limberneck' in wild waterfowl and domestic poultry (characterized by flaccid paralysis of the neck, wings, and nictitating membrane) and 'Lamziekte' (lamsiekte) in phosphorus-deficient cattle chewing carrion bones are caused by which Clostridium botulinum neurotoxin types?",
            [
                "Type C (specifically C1) in avian limberneck, and Types C and D in bovine lamziekte",
                "Type A exclusively in avian limberneck, and Type E exclusively in bovine lamziekte",
                "Type B exclusively in avian limberneck, and Type G exclusively in bovine lamziekte",
                "Type F exclusively in avian limberneck, and Type A exclusively in bovine lamziekte"
            ],
            0,
            "Avian botulism ('limberneck' in ducks and chickens ingesting maggots from carcasses) is caused predominantly by Clostridium botulinum Type C1 neurotoxin (encoded by a bacteriophage), whereas bovine botulism ('lamziekte' in phosphorus-deficient cattle exhibiting osteophagia) is caused by Types C and D.",
            True,
            TOPIC
        ),
        (
            "Which multi-copy insertion sequence element (present at 14 to 18 copies per genome) serves as the gold-standard species-specific PCR amplification target for the molecular identification of Mycobacterium avium subsp. paratuberculosis (MAP)?",
            [
                "IS6110 (characteristic of the Mycobacterium tuberculosis complex)",
                "IS900 (specific to Mycobacterium avium subsp. paratuberculosis)",
                "IS711 (characteristic of the genus Brucella)",
                "IS1111 (characteristic of Coxiella burnetii)"
            ],
            1,
            "IS900 is a 1,451-bp insertion sequence present in 14–18 copies uniquely within the genome of Mycobacterium avium subsp. paratuberculosis (MAP), making IS900-PCR the primary molecular assay for diagnosing Johne's disease in feces, milk, and tissues.",
            True,
            TOPIC
        ),
        (
            "In non-serological phenotypic typing of Pasteurella multocida, Capsular Type A strains (whose capsule is composed of hyaluronic acid) and Capsular Type D strains are rapidly identified using which pair of non-immunological tests?",
            [
                "Optochin disc inhibition for Type A, and Bacitracin disc inhibition for Type D",
                "CAMP synergistic hemolysis for Type A, and Reverse CAMP inhibition for Type D",
                "Staphylococcal hyaluronidase decapsulation for Type A, and Acriflavine flocculation for Type D",
                "Potassium hydroxide string test for Type A, and Digitonin lysis test for Type D"
            ],
            2,
            "Carter's Capsular Type A strains of Pasteurella multocida possess a hyaluronic acid capsule that is visibly depolymerized (colony flattening) adjacent to a hyaluronidase-producing Staphylococcus aureus streak, whereas Capsular Type D strains flocculate specifically in 1:1,000 neutral acriflavine dye.",
            True,
            TOPIC
        ),
        (
            "Exotoxin A, the single most lethal extracellular virulence factor secreted by Pseudomonas aeruginosa, kills host cells through a molecular mechanism identical to Diphtheria toxin by:",
            [
                "Cleaving SNARE proteins at peripheral cholinergic neuromuscular junctions",
                "Activating brush-border guanylyl cyclase C to cause hypersecretory diarrhea",
                "Forming heptameric beta-barrel pores in polymorphonuclear leukocyte membranes",
                "Catalyzing NAD+-dependent ADP-ribosylation of eukaryotic Elongation Factor-2 (eEF-2)"
            ],
            3,
            "Pseudomonas aeruginosa Exotoxin A (along with Exoenzyme S) is an AB toxin whose enzymatic A domain transfers an ADP-ribose moiety from NAD+ onto the modified histidine residue (diphthamide) of eukaryotic Elongation Factor-2 (eEF-2), irreversibly halting polypeptide chain elongation.",
            True,
            TOPIC
        ),
        (
            "Which tick-borne rickettsial pathogen of dogs—transmitted by the Lone Star tick (Amblyomma americanum)—selectively infects neutrophils (forming granulocytic morulae) and clinically manifests with fever and acute neutrophilic polyarthritis?",
            [
                "Ehrlichia ewingii (agent of Canine Granulocytic Ehrlichiosis)",
                "Ehrlichia canis (agent of Canine Monocytic Ehrlichiosis)",
                "Anaplasma platys (agent of Canine Cyclic Thrombocytopenia)",
                "Neorickettsia helminthoeca (agent of Salmon Poisoning Disease)"
            ],
            0,
            "Unlike Ehrlichia canis (which infects monocytes and is transmitted by Rhipicephalus sanguineus), Ehrlichia ewingii (along with Anaplasma phagocytophilum) is a granulocytotropic organism transmitted by Amblyomma americanum that forms morulae in neutrophils and causes acute lameness/polyarthritis in dogs.",
            False,
            TOPIC
        ),
        (
            "Gallibacterium anatis biovar haemolyticum (formerly Pasteurella haemolytica-like or Actinobacillus salpingitidis) is an important opportunistic pathogen of commercial laying hens that primarily causes:",
            [
                "Caseous airsacculitis and cerebellar encephalomalacia in day-old chicks",
                "Hemorrhagic oophoritis, salpingitis, egg peritonitis, and drop in egg production",
                "Ulcerative plantar pododermatitis ('bumblefoot') and keel bursitis",
                "Gangrenous dermatitis of the wing tips and breast muscle myonecrosis"
            ],
            1,
            "Gallibacterium anatis (family Pasteurellaceae) inhabits the upper respiratory and lower reproductive tracts of chickens; its beta-hemolytic biovar secretes a potent leukotoxic/hemolytic RTX toxin (GtxA) and causes oophoritis, salpingitis, and fatal peritonitis in laying hens.",
            False,
            TOPIC
        )
    ]

