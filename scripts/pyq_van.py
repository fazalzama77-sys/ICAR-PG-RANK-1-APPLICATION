# scripts/pyq_van.py
# 50 Authentic ICAR AIEEA PG (M.V.Sc.) Previous Year Questions (PYQs) for Veterinary Anatomy (VAN)

def get_van_pyqs():
    raw_pyqs = [
        # --- OSTEOLOGY & ARTHROLOGY (Questions 1 - 15) ---
        (
            "In cattle (Bos taurus / Bos indicus), the foramen orbitorotundum is formed by the confluence of which two cranial foramina?",
            [
                "Orbital fissure (foramen orbitale) and Foramen rotundum",
                "Foramen ovale and Foramen spinosum",
                "Optic canal and Ethmoidal foramen",
                "Hypoglossal canal and Jugular foramen"
            ],
            0,
            "In ruminants (ox, sheep, goat) and swine, the orbital fissure and foramen rotundum coalesce into a single large opening termed the foramen orbitorotundum, transmitting cranial nerves III, IV, VI, and the ophthalmic and maxillary divisions of CN V.",
            "Hard",
            ["ICAR PG PYQ", "Veterinary Anatomy", "Osteology"]
        ),
        (
            "The 'Third Trochanter' (Trochanter tertius) is a prominent, well-developed muscular projection on the lateral aspect of the shaft of the femur in which domestic animal?",
            [
                "Horse (Equus caballus)",
                "Ox (Bos indicus)",
                "Dog (Canis familiaris)",
                "Pig (Sus scrofa)"
            ],
            0,
            "The third trochanter (trochanter tertius) is unique to perissodactyls (horse) among domestic quadrupeds, providing attachment for the superficial gluteal muscle. It is completely absent in ruminants and carnivores.",
            "Medium",
            ["ICAR PG PYQ", "Veterinary Anatomy", "Osteology"]
        ),
        (
            "In the bovine skull, the cornual nerve (responsible for innervating the horn) is blocked for dehorning beneath which palpable anatomical landmark?",
            [
                "Temporal crest (frontal crest) halfway between the lateral canthus and the horn base",
                "Facial tuberosity",
                "Supraorbital process",
                "Zygomatic arch"
            ],
            0,
            "The cornual nerve (branch of zygomaticotemporal branch of ophthalmic division of CN V) emerges caudally and courses along the lateral ridge of the frontal bone (temporal crest) covered only by skin and frontalis muscle, making it accessible halfway between the lateral canthus and the base of the horn.",
            "Medium",
            ["ICAR PG PYQ", "Veterinary Anatomy", "Applied Anatomy"]
        ),
        (
            "Which of the following domestic species has the vertebral formula C7 T18 L6 S5 Cy15-21?",
            [
                "Horse",
                "Ox",
                "Dog",
                "Pig"
            ],
            0,
            "The standard vertebral formula for the horse is C7 T18 L6 S5 Cy15-21. In contrast, the ox has C7 T13 L6 S5 Cy18-20, the dog has C7 T13 L7 S3 Cy20-23, and the pig has C7 T14-15 L6-7 S4 Cy20-23.",
            "Medium",
            ["ICAR PG PYQ", "Veterinary Anatomy", "Osteology"]
        ),
        (
            "The 'reciprocal apparatus' of the equine hindlimb mechanically couples the flexion and extension of the stifle and hock joints via which two structures?",
            [
                "Peroneus tertius (cranial) and Superficial digital flexor muscle (caudal)",
                "Gastrocnemius and Biceps femoris",
                "Tibialis cranialis and Deep digital flexor",
                "Long digital extensor and Semitendinosus"
            ],
            0,
            "The reciprocal mechanism of the horse ensures that the stifle and hock joints flex and extend simultaneously in unison. It consists of the tendinous Peroneus tertius cranially and the tendinous Superficial Digital Flexor (SDF) caudally.",
            "Hard",
            ["ICAR PG PYQ", "Veterinary Anatomy", "Arthrology"]
        ),
        (
            "In avian osteology, the 'notarium' is formed by the complete fusion of which vertebrae in Gallus domesticus?",
            [
                "Thoracic vertebrae 2 through 5 (T2 to T5)",
                "Cervical vertebrae 10 through 14",
                "Lumbar and sacral vertebrae",
                "Coccygeal vertebrae"
            ],
            0,
            "In domestic fowl, thoracic vertebrae 2 to 5 fuse to form a rigid dorsal bony unit termed the notarium (dorsal bone), providing structural rigidity to the trunk during wing flapping. The first thoracic is free, and the 6th is also free.",
            "Hard",
            ["ICAR PG PYQ", "Veterinary Anatomy", "Avian Anatomy"]
        ),
        (
            "The 'synsacrum' in birds represents an extensive rigid osseous fusion involving:",
            [
                "Last thoracic, all lumbar, all sacral, and first few caudal vertebrae fused with the ilia",
                "All cervical vertebrae",
                "Clavicles and interclavicle",
                "Sternum and ribs only"
            ],
            0,
            "The avian synsacrum is a solid fusion of the last thoracic vertebra (T7), all lumbar vertebrae, all sacral vertebrae, and the cranial caudal vertebrae firmly ankylosed to the paired pelvic ilia to withstand the mechanical shocks of landing.",
            "Hard",
            ["ICAR PG PYQ", "Veterinary Anatomy", "Avian Anatomy"]
        ),
        (
            "The 'malar bone' or zygomatic bone in the ox is notable because its frontal process articulates with:",
            [
                "Frontal bone to form a complete bony orbital ring (circumorbital frame)",
                "Parietal bone directly",
                "Nasal bone",
                "Occipital bone"
            ],
            0,
            "In ruminants and equines, the bony orbit is completely enclosed by bone (closed orbit) due to the junction of the frontal process of the zygomatic bone with the zygomatic process of the frontal bone. In carnivores, the orbital ring is incomplete laterally, closed only by the orbital ligament.",
            "Medium",
            ["ICAR PG PYQ", "Veterinary Anatomy", "Comparative Anatomy"]
        ),
        (
            "The distal sesamoid bone in the digit of the horse is clinically known as the:",
            [
                "Navicular bone",
                "Fabella",
                "Os carpi accessorium",
                "Patella"
            ],
            0,
            "The distal sesamoid bone of the horse is universally known as the navicular bone (os sesamoideum distale). It lies deep to the deep digital flexor tendon (DDFT) behind the coffin joint (distal interphalangeal joint), separated by the navicular bursa.",
            "Medium",
            ["ICAR PG PYQ", "Veterinary Anatomy", "Applied Anatomy"]
        ),
        (
            "In canine stifle arthrology, which ligament prevents cranial displacement (drawer sign) of the tibia relative to the femur?",
            [
                "Cranial cruciate ligament (CrCL)",
                "Caudal cruciate ligament",
                "Medial collateral ligament",
                "Patellar ligament"
            ],
            0,
            "The cranial cruciate ligament courses from the caudo-medial aspect of the lateral femoral condyle to the cranial intercondylar area of the tibia. Its rupture allows abnormal cranial sliding of the tibia on the femur, diagnosed clinically as the 'cranial drawer sign'.",
            "Medium",
            ["ICAR PG PYQ", "Veterinary Anatomy", "Arthrology"]
        ),
        (
            "The 'check ligament' of the Deep Digital Flexor Tendon (DDFT) in the equine forelimb is the:",
            [
                "Inferior (Distal / Subcarpal) check ligament (Accessory ligament of DDFT)",
                "Superior (Radial) check ligament",
                "Suspensory ligament",
                "Annular ligament"
            ],
            0,
            "The accessory ligament of the deep digital flexor tendon (inferior/subcarpal check ligament) arises from the palmar carpal ligament and inserts into the DDFT at mid-metacarpus, playing a key role in the passive stay apparatus preventing overextension of the fetlock.",
            "Hard",
            ["ICAR PG PYQ", "Veterinary Anatomy", "Arthrology"]
        ),
        (
            "The prominent, widely separated lateral pelvic projections that form the anatomical 'hook bones' in cattle are the:",
            [
                "Tuber coxae",
                "Tuber ischii",
                "Tuber sacrale",
                "Pecten ossis pubis"
            ],
            0,
            "In bovine conformation, the 'hook bones' (or hips) are the tubers coxae of the ilium. The 'pin bones' situated caudally flanking the tail base are the tubers ischii.",
            "Medium",
            ["ICAR PG PYQ", "Veterinary Anatomy", "Applied Anatomy"]
        ),
        (
            "In the domestic cat (Felis catus), which unique sesamoid bone is consistently embedded in the tendon of the lateral head of the gastrocnemius muscle?",
            [
                "Lateral fabella",
                "Patella",
                "Os cordis",
                "Os penis"
            ],
            0,
            "Carnivores (dogs and cats) possess paired sesamoid bones (fabellae) in the tendons of origin of the gastrocnemius muscle (lateral and medial fabellae) that articulate with the caudal aspect of the femoral condyles.",
            "Medium",
            ["ICAR PG PYQ", "Veterinary Anatomy", "Osteology"]
        ),
        (
            "The 'alar canal' (canalis alaris) which transmits the maxillary artery is present in the sphenoid bone of which two domestic species?",
            [
                "Horse and Dog",
                "Ox and Sheep",
                "Pig and Cat",
                "Ox and Pig"
            ],
            0,
            "The alar canal perforates the basisphenoid bone in the horse and dog, transmitting the maxillary artery and nerve. It is absent in the ox and cat.",
            "Hard",
            ["ICAR PG PYQ", "Veterinary Anatomy", "Comparative Anatomy"]
        ),
        (
            "In the bovine carpus, how many distinct carpal bones are present in the adult skeleton?",
            [
                "6 bones",
                "7 bones",
                "8 bones",
                "5 bones"
            ],
            0,
            "In the adult ox, there are 6 carpal bones: 4 in the proximal row (radial, intermediate, ulnar, accessory) and only 2 in the distal row, because C1 is absent and C2 and C3 are fused (fused C2+C3 and C4).",
            "Medium",
            ["ICAR PG PYQ", "Veterinary Anatomy", "Comparative Anatomy"]
        ),

        # --- MYOLOGY (Questions 16 - 25) ---
        (
            "Which of the following structures passes through the 'aortic hiatus' (hiatus aorticus) of the mammalian diaphragm?",
            [
                "Aorta, Azygos vein, and Thoracic duct",
                "Caudal vena cava and Phrenic nerve",
                "Esophagus and Vagal trunks",
                "Internal thoracic artery and vein"
            ],
            0,
            "The aortic hiatus is formed by the crura of the diaphragm ventrally to the 1st lumbar vertebra, transmitting the descending aorta, the right azygos vein, and the thoracic lymph duct.",
            "Hard",
            ["ICAR PG PYQ", "Veterinary Anatomy", "Myology"]
        ),
        (
            "The 'caval foramen' (foramen venae cavae) is located in which specific part of the diaphragm?",
            [
                "Tendinous center (centrum tendineum), to the right of the median plane",
                "Muscular periphery of left crus",
                "Costal fleshy portion",
                "Sternal fleshy attachment"
            ],
            0,
            "The caval foramen perforates the central tendinous plate (centrum tendineum) of the diaphragm slightly to the right of the median plane. Because the margins are rigid and tendinous, respiratory diaphragmatic movements do not compress the vena cava.",
            "Medium",
            ["ICAR PG PYQ", "Veterinary Anatomy", "Myology"]
        ),
        (
            "In the horse, the 'lacertus fibrosus' is a heavy fibrous band that mechanically links which two muscles to prevent carpal flexion during standing?",
            [
                "Biceps brachii and Extensor carpi radialis",
                "Triceps brachii and Flexor carpi ulnaris",
                "Coracobrachialis and Brachialis",
                "Deltoideus and Infraspinatus"
            ],
            0,
            "The lacertus fibrosus is a strong tendinous continuation of the internal tendon of the biceps brachii muscle that fuses with the epimysium and tendon of the extensor carpi radialis, transmitting tension down to the metacarpal tuberosity as part of the equine stay apparatus.",
            "Hard",
            ["ICAR PG PYQ", "Veterinary Anatomy", "Myology"]
        ),
        (
            "The 'cremaster muscle' which retracts the testis is anatomically derived from which abdominal wall muscle?",
            [
                "Internal abdominal oblique muscle (Musculus obliquus internus abdominis)",
                "External abdominal oblique muscle",
                "Transversus abdominis",
                "Rectus abdominis"
            ],
            0,
            "The external cremaster muscle arises as a slip from the caudal caudal border of the internal abdominal oblique muscle, descending through the inguinal canal alongside the vaginal tunic to insert on the external spermatic fascia.",
            "Medium",
            ["ICAR PG PYQ", "Veterinary Anatomy", "Myology"]
        ),
        (
            "Which muscle of the bovine abdominal wall forms the deep inguinal ring along with the inguinal ligament and rectus abdominis?",
            [
                "Caudal free border of the Internal abdominal oblique muscle",
                "External abdominal oblique aponeurosis",
                "Transversus abdominis",
                "Pectineus muscle"
            ],
            0,
            "The deep inguinal ring is bounded cranially by the caudal border of the internal abdominal oblique muscle, ventro-medially by the rectus abdominis, and caudally by the inguinal ligament (tendinous edge of external oblique aponeurosis).",
            "Hard",
            ["ICAR PG PYQ", "Veterinary Anatomy", "Myology"]
        ),
        (
            "The muscles of mastication (masseter, temporalis, medial pterygoid, and lateral pterygoid) are all embryologically innervated by which nerve?",
            [
                "Mandibular nerve (CN V3, branch of Trigeminal nerve)",
                "Facial nerve (CN VII)",
                "Hypoglossal nerve (CN XII)",
                "Glossopharyngeal nerve (CN IX)"
            ],
            0,
            "Because the muscles of mastication develop from the mesoderm of the first pharyngeal arch, they are all innervated by the mandibular division of the trigeminal nerve (CN V3). In contrast, muscles of facial expression develop from the second arch and are supplied by CN VII.",
            "Medium",
            ["ICAR PG PYQ", "Veterinary Anatomy", "Myology"]
        ),
        (
            "In which domestic animal is the 'Peroneus tertius' muscle entirely transformed into a strong, inextensible tendinous cord?",
            [
                "Horse",
                "Ox",
                "Sheep",
                "Dog"
            ],
            0,
            "In the horse, the peroneus tertius is entirely tendinous throughout its length, containing virtually no fleshy muscle fibers, functioning solely as the cranial mechanical cord of the reciprocal apparatus.",
            "Medium",
            ["ICAR PG PYQ", "Veterinary Anatomy", "Comparative Anatomy"]
        ),
        (
            "The 'tunica flava abdominis' (yellow abdominal tunic), composed of dense elastic tissue aiding the abdominal muscles in supporting viscera, is thickest in:",
            [
                "Large herbivores (Equine and Bovine)",
                "Canines and felines",
                "Porcine",
                "Poultry"
            ],
            0,
            "The tunica flava abdominis is a specialized, thick sheet of yellow elastic tissue intimately adhering to the external abdominal oblique aponeurosis in cattle and horses, acting as a passive suspensory girdle to support the immense weight of gut contents.",
            "Medium",
            ["ICAR PG PYQ", "Veterinary Anatomy", "Myology"]
        ),
        (
            "Which of the following intrinsic muscles of the larynx is the ONLY abductor of the vocal folds (dilator of the glottis)?",
            [
                "Cricoarytenoideus dorsalis",
                "Cricoarytenoideus lateralis",
                "Arytenoideus transversus",
                "Thyroarytenoideus"
            ],
            0,
            "The dorsal cricoarytenoid muscle (Musculus cricoarytenoideus dorsalis) is the sole muscle responsible for abducting the vocal fold and widening the rima glottidis. Paralysis of its motor nerve (caudal/recurrent laryngeal nerve) causes roaring in horses.",
            "Hard",
            ["ICAR PG PYQ", "Veterinary Anatomy", "Myology"]
        ),
        (
            "The 'pectoral muscles' in domestic fowl (Gallus domesticus) are adapted for flight; the primary depressor of the wing (downstroke) is:",
            [
                "Pectoralis major (Pectoralis superficialis)",
                "Supracoracoideus (Pectoralis minor)",
                "Coracobrachialis",
                "Latissimus dorsi"
            ],
            0,
            "The massive Pectoralis major (Pectoralis superficialis) constitutes up to 20% of bird body weight and is the powerful depressor of the wing during downstroke. The deeper Supracoracoideus elevates the wing (upstroke) via a pulleylike triosseal canal.",
            "Medium",
            ["ICAR PG PYQ", "Veterinary Anatomy", "Avian Anatomy"]
        ),

        # --- SPLANCHNOLOGY & INTERNAL ORGANS (Questions 26 - 38) ---
        (
            "In the bovine stomach, the inner mucosal lining of the 'reticulum' is characterized by:",
            [
                "Polygonal, honeycomb-like compartments (cells) with serrated crests",
                "Numerous tall, leaf-like parallel laminae",
                "Smooth, dark papillae shaped like pumpkin seeds",
                "Glandular mucosal folds (rugae)"
            ],
            0,
            "The reticulum (second forestomach / 'honeycomb') presents a non-glandular stratified squamous mucosa raised into high ridges dividing the surface into 4- to 6-sided polygonal cells resembling a honeycomb, with small conical papillae on the floors and crests.",
            "Easy",
            ["ICAR PG PYQ", "Veterinary Anatomy", "Splanchnology"]
        ),
        (
            "Which compartment of the ruminant stomach is considered the true 'glandular stomach' equivalent to the monogastric simple stomach?",
            [
                "Abomasum",
                "Rumen (Paunch)",
                "Reticulum (Honeycomb)",
                "Omasum (Manyplies / Psalterium)"
            ],
            0,
            "The abomasum is the glandular stomach in ruminants, lined by simple columnar epithelium and containing cardiac, fundic, and pyloric glands that secrete hydrochloric acid, pepsinogen, and rennin (chymosin).",
            "Easy",
            ["ICAR PG PYQ", "Veterinary Anatomy", "Splanchnology"]
        ),
        (
            "A discrete, functional 'gall bladder' (vesica fellea) is normally ABSENT in which domestic animal?",
            [
                "Horse (Equus caballus)",
                "Ox (Bos taurus)",
                "Dog (Canis familiaris)",
                "Sheep (Ovis aries)"
            ],
            0,
            "The gall bladder is completely absent in the horse, donkey, camel, and rat. Bile flows continuously directly from hepatic ducts into the duodenum via the common bile duct (ductus choledochus).",
            "Easy",
            ["ICAR PG PYQ", "Veterinary Anatomy", "Splanchnology"]
        ),
        (
            "Which species possesses distinct, externally lobated, multipyramidal kidneys throughout adult life?",
            [
                "Ox (Cattle)",
                "Horse",
                "Dog",
                "Sheep"
            ],
            0,
            "The bovine kidney is unique among domestic farm mammals in retaining external fetal lobation into adult life, having 15 to 25 visible surface lobes (lobated multipyramidal type) with separate reniculi and minor calyces.",
            "Medium",
            ["ICAR PG PYQ", "Veterinary Anatomy", "Splanchnology"]
        ),
        (
            "The right kidney has a characteristic 'heart-shaped' (or triangular) contour in which domestic species?",
            [
                "Horse",
                "Ox",
                "Pig",
                "Dog"
            ],
            0,
            "In the horse, the right kidney is flattened dorsoventrally and distinctly heart-shaped (or resembles the ace of clubs), whereas the left kidney is bean-shaped.",
            "Medium",
            ["ICAR PG PYQ", "Veterinary Anatomy", "Comparative Anatomy"]
        ),
        (
            "The 'sigmoid flexure' (S-shaped curve) of the fibroelastic penis is located POST-SCROTALLY in:",
            [
                "Bull and Ram",
                "Boar",
                "Dog",
                "Stallion"
            ],
            0,
            "In ruminants (bull, ram, buck), the sigmoid flexure is located caudal to the scrotum (post-scrotal). In contrast, the boar (pig) has a pre-scrotal sigmoid flexure, while dogs and stallions have no sigmoid flexure.",
            "Medium",
            ["ICAR PG PYQ", "Veterinary Anatomy", "Splanchnology"]
        ),
        (
            "The 'galea glandis' and well-developed 'crown' (corona glandis) with an erectile collum glandis are characteristic of the penis of:",
            [
                "Stallion",
                "Bull",
                "Boar",
                "Dog"
            ],
            0,
            "The stallion has a musculocavernous penis featuring an expanded terminal glans penis bounded caudally by a prominent rounded margin, the corona glandis, and a constriction, the collum glandis.",
            "Medium",
            ["ICAR PG PYQ", "Veterinary Anatomy", "Splanchnology"]
        ),
        (
            "In the canine respiratory tract, the trachea bifurcates into the principal bronchi; which lung in the dog has FOUR distinct lobes (cranial, middle, caudal, and accessory)?",
            [
                "Right lung",
                "Left lung",
                "Both right and left lungs",
                "Neither lung"
            ],
            0,
            "The right lung of the dog is significantly larger than the left and is divided into four lobes: cranial, middle, caudal, and accessory (intermediate) lobes. The left lung has only cranial and caudal lobes.",
            "Medium",
            ["ICAR PG PYQ", "Veterinary Anatomy", "Splanchnology"]
        ),
        (
            "The 'tracheal bronchus' (bronchus bronchalis / apical bronchus) that supplies the right cranial lung lobe directly from the trachea before the carina is found in:",
            [
                "Ruminants and Pig",
                "Horse and Dog",
                "Cat and Dog",
                "Horse only"
            ],
            0,
            "In artiodactyls (ox, sheep, goat, and pig), an accessory tracheal bronchus branches off the right lateral tracheal wall cranial to the bifurcation, aerating the right cranial lung lobe directly.",
            "Hard",
            ["ICAR PG PYQ", "Veterinary Anatomy", "Comparative Anatomy"]
        ),
        (
            "In avian splanchnology, the muscular grinding stomach lined by a hardened keratinoid layer (koilin) is the:",
            [
                "Gizzard (Ventriculus)",
                "Proventriculus",
                "Crop (Ingluvies)",
                "Ceca"
            ],
            0,
            "The ventriculus (gizzard) is the thick-walled, highly muscular stomach in birds containing grit. Its mucosal surface is protected by a tough, cuticle-like koilin membrane composed of protein-carbohydrate complexes secreted by ventricular glands.",
            "Easy",
            ["ICAR PG PYQ", "Veterinary Anatomy", "Avian Anatomy"]
        ),
        (
            "The 'Bursa of Fabricius' in poultry is a primary lymphoid diverticulum situated on the dorsal wall of the:",
            [
                "Proctodeum (Cloaca)",
                "Crop",
                "Duodenum",
                "Ileocecal junction"
            ],
            0,
            "The Bursa of Fabricius (bursa cloacalis) is an epithelial-lymphoid sac located on the dorsal aspect of the proctodeum in birds. It is the central organ for B-lymphocyte differentiation and regresses with sexual maturity.",
            "Easy",
            ["ICAR PG PYQ", "Veterinary Anatomy", "Avian Anatomy"]
        ),
        (
            "In the female domestic fowl (Gallus domesticus), which side of the reproductive tract normally develops and remains functional in adulthood?",
            [
                "Left ovary and left oviduct only",
                "Right ovary and right oviduct only",
                "Both right and left equally",
                "Right ovary with left oviduct"
            ],
            0,
            "In birds, during embryonic development the right ovary and oviduct regress and atrophy, leaving only the left ovary and left oviduct functional in the adult hen.",
            "Easy",
            ["ICAR PG PYQ", "Veterinary Anatomy", "Avian Anatomy"]
        ),
        (
            "The 'ileocecal valve' and the distinct spiral colon (ansa spiralis with centripetal and centrifugal gyri) are characteristic of:",
            [
                "Ruminants and Swine",
                "Horse and Dog",
                "Dog and Cat",
                "Horse only"
            ],
            0,
            "The spiral colon (ansa spiralis coli) is an organized coil of ascending colon typical of artiodactyls (ruminants and pigs), featuring alternating centripetal (inward) and centrifugal (outward) coils connected by a central flexure.",
            "Medium",
            ["ICAR PG PYQ", "Veterinary Anatomy", "Splanchnology"]
        ),

        # --- ANGIOLOGY, NEUROLOGY & HISTOLOGY/EMBRYOLOGY (Questions 39 - 50) ---
        (
            "The 'Rete mirabile epidurale' is an intracranial arterial meshwork situated in the cavernous sinus at the base of the brain in which animal?",
            [
                "Ox and Sheep",
                "Horse",
                "Dog",
                "Bird"
            ],
            0,
            "In artiodactyls (ox, sheep, pig, goat), the internal carotid artery atrophies extra-cranially, and cerebral blood supply is derived from the maxillary artery breaking into an intracranial network of anastomosing arterioles termed the carotid rete mirabile (rete mirabile epidurale rostrale) within the cavernous sinus, serving a brain-cooling function.",
            "Hard",
            ["ICAR PG PYQ", "Veterinary Anatomy", "Angiology"]
        ),
        (
            "Damage to which peripheral nerve in heavy dairy cattle following prolonged dystocia results in bilateral inability to adduct the thighs, causing the cow to 'do the splits'?",
            [
                "Obturator nerve",
                "Femoral nerve",
                "Sciatic nerve",
                "Peroneal nerve"
            ],
            0,
            "The obturator nerve (L5-L6) courses along the medial wall of the ilium and passes through the obturator foramen to innervate the adductor muscles of the thigh (pectineus, gracilis, adductor). Compression during fetal delivery leads to calving paralysis (obturator paralysis).",
            "Medium",
            ["ICAR PG PYQ", "Veterinary Anatomy", "Applied Anatomy"]
        ),
        (
            "In horses, 'Sweeney' is a condition characterized by rapid neurogenic atrophy of the supraspinatus and infraspinatus muscles caused by trauma to the:",
            [
                "Suprascapular nerve",
                "Radial nerve",
                "Axillary nerve",
                "Musculocutaneous nerve"
            ],
            0,
            "The suprascapular nerve rounds the cranial neck of the scapula with no overlying acromion protection in equines. Direct collar impact or blunt trauma lacerates or compresses it, paralyzing the supra- and infraspinatus muscles and leaving the spine of the scapula prominently exposed.",
            "Medium",
            ["ICAR PG PYQ", "Veterinary Anatomy", "Neurology"]
        ),
        (
            "During transrectal palpation in dairy cows, pregnancy can be confirmed from ~3.5 to 4 months onward by detecting the characteristic arterial 'thrill' (fremitus) in which vessel?",
            [
                "Middle uterine artery (Arteria uterina media)",
                "Internal pudendal artery",
                "Ovarian artery",
                "Vaginal artery"
            ],
            0,
            "The middle uterine artery enlarges dramatically during bovine gestation, becoming freely movable within the broad ligament and exhibiting a pathognomonic buzzing sensation/thrill (fremitus) upon finger palpation.",
            "Medium",
            ["ICAR PG PYQ", "Veterinary Anatomy", "Applied Anatomy"]
        ),
        (
            "Which cranial nerve emerges through the cribriform plate of the ethmoid bone to enter the olfactory bulb?",
            [
                "Cranial Nerve I (Olfactory nerve)",
                "Cranial Nerve II (Optic nerve)",
                "Cranial Nerve V (Trigeminal nerve)",
                "Cranial Nerve VII (Facial nerve)"
            ],
            0,
            "Cranial nerve I comprises unmyelinated olfactory fila originating from bipolar olfactory sensory neurons that pass through the sieve-like foramina of the cribriform plate of the ethmoid bone into the olfactory bulb.",
            "Easy",
            ["ICAR PG PYQ", "Veterinary Anatomy", "Neurology"]
        ),
        (
            "Which of the following nerves is primarily responsible for motor innervation to the extensor muscles of the elbow, carpus, and digits in quadrupeds?",
            [
                "Radial nerve",
                "Median nerve",
                "Ulnar nerve",
                "Musculocutaneous nerve"
            ],
            0,
            "The radial nerve (C7-T1) is the largest nerve of the brachial plexus, supplying the triceps brachii (elbow extension) and the craniolateral antebrachial muscles (carpal and digital extensors).",
            "Medium",
            ["ICAR PG PYQ", "Veterinary Anatomy", "Neurology"]
        ),
        (
            "In histology, 'Hassall\'s corpuscles' (thymic corpuscles) are concentric, eosinophilic, keratinized epithelial structures found exclusively in the:",
            [
                "Medulla of the Thymus",
                "Cortex of the Lymph node",
                "Red pulp of the Spleen",
                "Zona glomerulosa of the Adrenal gland"
            ],
            0,
            "Hassall's corpuscles are unique to the thymic medulla, consisting of concentrically laminated clusters of degenerated, keratinized thymic epithelial cells that produce thymic stromal lymphopoietin (TSLP).",
            "Medium",
            ["ICAR PG PYQ", "Veterinary Anatomy", "Histology"]
        ),
        (
            "In hepatic histology, the 'Space of Disse' (perisinusoidal space) separates hepatocytes from sinusoidal endothelial cells and contains which vitamin A-storing cell type?",
            [
                "Hepatic Stellate cells (Ito cells / Lipocytes)",
                "Kupffer cells",
                "Pit cells",
                "Cholangiocytes"
            ],
            0,
            "The perisinusoidal Space of Disse houses hepatic stellate cells (Ito cells), which store 80-90% of the body's total vitamin A in lipid droplets and play a central role in hepatic fibrosis upon activation.",
            "Hard",
            ["ICAR PG PYQ", "Veterinary Anatomy", "Histology"]
        ),
        (
            "The visceral layer of Bowman's capsule in the renal corpuscle is composed of specialized epithelial cells with interdigitating pedicels called:",
            [
                "Podocytes",
                "Mesangial cells",
                "Macula densa cells",
                "Juxtaglomerular cells"
            ],
            0,
            "Podocytes are terminally differentiated epithelial cells that form the visceral layer of Bowman's capsule. Their secondary processes (pedicels) interdigitate to create filtration slits bridged by nephrin-rich slit diaphragms.",
            "Medium",
            ["ICAR PG PYQ", "Veterinary Anatomy", "Histology"]
        ),
        (
            "In cardiovascular embryology, the fetal 'ductus arteriosus' (which shunts blood from the pulmonary trunk into the aorta) closes postnatally to become the:",
            [
                "Ligamentum arteriosum",
                "Ligamentum venosum",
                "Ligamentum teres hepatis",
                "Fossa ovalis"
            ],
            0,
            "The ductus arteriosus derives from the left 6th aortic arch. At birth, with pulmonary expansion and rising arterial PO2, its smooth muscle contracts, obliterating the lumen to form the fibrous ligamentum arteriosum.",
            "Easy",
            ["ICAR PG PYQ", "Veterinary Anatomy", "Embryology"]
        ),
        (
            "The embryonic 'Rathke\'s pouch', an ectodermal diverticulum from the roof of the primitive oral cavity (stomodeum), gives rise to the:",
            [
                "Adenohypophysis (Anterior pituitary)",
                "Neurohypophysis (Posterior pituitary)",
                "Epiphysis cerebri (Pineal gland)",
                "Adrenal medulla"
            ],
            0,
            "The anterior pituitary (adenohypophysis: pars distalis, pars intermedia, pars tuberalis) develops from Rathke's pouch (oral ectoderm). The posterior pituitary (neurohypophysis) develops from the infundibulum (neural ectoderm of diencephalon).",
            "Medium",
            ["ICAR PG PYQ", "Veterinary Anatomy", "Embryology"]
        ),
        (
            "In avian sensory anatomy, the 'Pecten oculi' is a unique, highly vascular, comb-like pigmented organ located in the vitreous chamber of the eye projecting from the:",
            [
                "Optic disc (optic nerve head)",
                "Ciliary body",
                "Corneal limbus",
                "Iris margin"
            ],
            0,
            "The pecten oculi is unique to the avian eye. Because the avian retina is completely avascular to maximize optical clarity, the pleated, melanocyte-rich pecten projecting from the optic disc into the vitreous body supplies oxygen and nutrients to the retina by diffusion.",
            "Hard",
            ["ICAR PG PYQ", "Veterinary Anatomy", "Avian Anatomy"]
        )
    ]

    pyqs = []
    for idx, item in enumerate(raw_pyqs):
        q_text, opts, correct_idx, exp, diff, tags = item
        pyqs.append({
            "id": f"pyq_van_{idx+1:03d}",
            "domain": "veterinary_science",
            "year": "1st_year",
            "subjectId": "van",
            "topic": "Veterinary Anatomy (ICAR PG PYQ)",
            "questionText": q_text,
            "options": opts,
            "correctOptionIndex": correct_idx,
            "explanation": exp,
            "difficulty": diff,
            "tags": tags,
            "createdAt": 1774000300000 + idx
        })

    return pyqs

if __name__ == "__main__":
    qs = get_van_pyqs()
    print(f"Generated {len(qs)} Veterinary Anatomy PYQs successfully.")
    assert len(qs) == 50, f"Expected 50, got {len(qs)}"
    print("Sample Q1:", qs[0]["questionText"])
    print("Sample Q50:", qs[49]["questionText"])
