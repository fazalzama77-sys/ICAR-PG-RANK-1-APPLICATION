# scripts/anat_mod1_osteology.py
# Module 1: Comparative Osteology & Arthrology (40 Questions)
# Aligned with ICAR AIEEA (PG) M.V.Sc. Syllabus Code 13 Unit I

def get_module1_questions():
    qs = [
        # 1-10: Comparative skull, vertebral column
        ("In the bovine skull, which cranial foramen represents the confluent fusion of the foramen rotundum and the orbital fissure (foramen lacerum anterius)?",
         ["Foramen orbitorotundum", "Foramen ovale", "Foramen lacerum", "Stylomastoid foramen"],
         0, "In ruminants and pigs, the orbital fissure and foramen rotundum merge into a single large oval opening termed the foramen orbitorotundum, through which cranial nerves III, IV, VI, and the ophthalmic and maxillary branches of CN V pass.",
         True, "Comparative Osteology (ICAR PG PYQ)"),

        ("The 'Facial Crest' (crista facialis), a prominent subcutaneous horizontal bony ridge on the lateral aspect of the face, is a characteristic anatomical feature of the skull of the:",
         ["Horse (Equine)", "Ox (Bovine)", "Dog (Canine)", "Pig (Porcine)"],
         0, "The facial crest is a prominent landmark on the lateral maxilla and zygomatic bone of the horse; in cattle, it is replaced by a blunt, circumscribed 'facial tuberosity' (tuber faciale) located dorsal to the 3rd-4th upper premolar.",
         True, "Comparative Osteology (ICAR PG PYQ)"),

        ("The 'Cornual Process' (processus cornus), which supports the horn in horned ruminants, is an osseous outgrowth arising directly from which cranial bone?",
         ["Frontal bone", "Parietal bone", "Temporal bone", "Occipital bone"],
         0, "In cattle, sheep, and goats, horns are supported by the cornual processes, which are hollow bony projections extending from the caudal angles of the frontal bones, pneumatized by the frontal sinus.",
         True, "Comparative Osteology (ICAR PG PYQ)"),

        ("The Atlas (1st cervical vertebra) of the dog differs from that of the horse and ox because its modified transverse processes (wings of atlas) feature:",
         ["An 'Alar Notch' (incisura alaris) on its cranial border instead of an alar foramen", "A complete alar foramen", "An absence of transverse foramina", "A high dorsal spinous process"],
         0, "In carnivores, the cranial border of the wing of the atlas has an open notch (alar notch / incisura alaris), whereas in horses, cattle, and sheep, this is enclosed by bone to form a true alar foramen (foramen alare).",
         True, "Comparative Osteology (ICAR PG PYQ)"),

        ("The dens (odontoid process) of the Axis (2nd cervical vertebra) in cattle and horses exhibits which comparative anatomical shape?",
         ["Spout-shaped (semicylindrical, concave dorsally)", "Cylindrical (peg-like / conical)", "Flat and square", "Completely bifurcated"],
         0, "In ruminants and equines, the dens of the axis is broad, semicylindrical, and spout-shaped (concave dorsally and rounded ventrally); in dogs and cats, it is a rounded, cylindrical, peg-like process.",
         True, "Comparative Osteology (ICAR PG PYQ)"),

        ("The total number of cervical vertebrae present in almost all domestic mammals (Ox, Horse, Dog, Pig, Sheep, Cat, and Camel) is universally:",
         ["7", "6", "8", "14"],
         0, "All mammalian domestic species (from the smallest cat to the camel and giraffe) consistently possess precisely 7 cervical vertebrae, whereas birds (such as Gallus domesticus) possess 14 cervical vertebrae.",
         True, "Comparative Osteology (ICAR PG PYQ)"),

        ("The 'Anticlinal Vertebra' (the thoracic vertebra whose spinous process is oriented perpendicular / vertical to the long axis of the vertebral column) is:",
         ["T11 in the Dog (T13 in Ox, T16 in Horse)", "T7 in all species", "T1 in the Dog", "L1 in all species"],
         0, "The anticlinal vertebra represents the anatomical transition point of spinous process angulation (cranial spinous processes slope caudally; caudal processes slope cranially); it is T11 in dogs and cats, T13 in ruminants, and T16 in equines.",
         True, "Comparative Osteology (ICAR PG PYQ)"),

        ("The Sacrum is formed by the complete fusion of how many sacral vertebrae in the Horse and Ox versus the Dog?",
         ["5 in the Horse and Ox, 3 in the Dog (and 4 in the Pig)", "3 in all species", "7 in the Horse and 5 in the Ox", "4 in the Dog and 3 in the Horse"],
         0, "The sacral segment consists of 5 fused vertebrae in equines and bovines (Os sacrum), 4 fused vertebrae in swine, and 3 fused vertebrae in dogs and cats.",
         True, "Comparative Osteology (ICAR PG PYQ)"),

        ("The 'Foramen Triosseum' (triosseal canal) in the avian pectoral girdle, through which the tendon of the supracoracoideus muscle passes like a pulley to elevate the wing, is formed by the junction of:",
         ["Scapula, Coracoid, and Clavicle", "Humerus, Radius, and Ulna", "Ilium, Ischium, and Pubis", "Sternum and Ribs"],
         0, "In birds, the dorsal extremities of the scapula, coracoid bone, and clavicle articulate to bound the triosseal canal; the tendon of the deep pectoral (supracoracoideus) passes through it, acting as a pulley to raise the wing.",
         True, "Comparative Osteology (ICAR PG PYQ)"),

        ("The 'Pygostyle' of the avian skeleton is a plowshare-shaped bone formed by the fusion of the:",
         ["Terminal 4 to 6 caudal (coccygeal) vertebrae, supporting the tail rectrices", "Pelvic bones", "Lumbar vertebrae", "Cervical vertebrae"],
         0, "The avian tail skeleton terminates in the pygostyle, a compressed blade-like bone formed by the fusion of the last 4-6 caudal vertebrae that anchors the tail flight feathers (rectrices) and uropygial gland.",
         True, "Comparative Osteology (ICAR PG PYQ)"),

        # 11-20: Forelimb comparative osteology
        ("The Scapula of the horse differs from that of the ox, sheep, and dog because the horse scapula:",
         ["Lacks an Acromion process and possesses a prominent Tuber Spinae at the middle of the scapular spine", "Has a massive hook-like acromion", "Possesses a clavicle", "Has a supraspinous fossa twice as large as the infraspinous fossa"],
         0, "In the horse, the spine of the scapula gradually subsides distally without forming an acromion process, and features a roughened, thick tuber spinae in its middle; cattle and dogs have prominent acromion processes.",
         True, "Comparative Osteology (ICAR PG PYQ)"),

        ("In the domestic cat, the distal end of the scapular spine features which unique projection extending caudally over the infraspinous fossa?",
         ["Suprahamate process (processus suprahamatus)", "Coracoid process", "Glenoid notch", "Tuber spinae"],
         0, "The feline scapula is distinguished by having both a hamate process (the distal tip of the acromion) and a distinct, caudally projecting suprahamate process situated immediately dorsal to the hamate process.",
         True, "Comparative Osteology (ICAR PG PYQ)"),

        ("In the equine humerus, the bicipital groove (sulcus intertubercularis) on the cranial aspect of the proximal extremity is unique because it is:",
         ["Divided into two distinct channels by a central 'intermediate ridge' (sagittal ridge)", "A single undivided shallow groove as in the ox and dog", "Completely absent", "Enclosed by a bony bridge into a foramen"],
         0, "In the horse, the tendon of the biceps brachii muscle is accommodated by a wide bicipital groove divided into medial and lateral channels by a prominent intermediate ridge, whereas in the ox, pig, and dog, it is a single undivided groove.",
         True, "Comparative Osteology (ICAR PG PYQ)"),

        ("The 'Supratrochlear Foramen' (a perforation through the thin bony septum between the radial and olecranon fossae of the humerus) is normally present in the:",
         ["Dog (Canine)", "Horse (Equine)", "Ox (Bovine)", "Pig (Porcine)"],
         0, "The dog humerus consistently possesses a supratrochlear foramen through which no major nerve or vessel passes; in contrast, the domestic cat possesses a 'supracondylar foramen' on the medial epicondyle transmitting the median nerve and brachial artery.",
         True, "Comparative Osteology (ICAR PG PYQ)"),

        ("In the feline humerus, which vital neurovascular structures pass through the 'Supracondylar Foramen' located on the medial supracondylar crest?",
         ["Median nerve and Brachial artery", "Radial nerve and Deep brachial artery", "Ulnar nerve and Collateral ulnar artery", "Musculocutaneous nerve"],
         0, "The supracondylar foramen is present in felids on the distomedial humerus; fractures of the distal humerus risk severe iatrogenic or traumatic laceration of the median nerve and brachial artery passing through it.",
         True, "Comparative Osteology (ICAR PG PYQ)"),

        ("The 'Musculospiral Groove' (sulcus musculi brachialis) is a prominent spiral depression winding laterally around the shaft of the:",
         ["Humerus, accommodating the brachialis muscle", "Femur", "Radius", "Tibia"],
         0, "The musculospiral groove winds from the caudal neck obliquely across the lateral surface of the humeral shaft to the cranial surface, housing the fleshy brachialis muscle.",
         True, "Comparative Osteology (ICAR PG PYQ)"),

        ("In the antebrachium of the Ox, the Radius and Ulna are characterized by having:",
         ["Two distinct interosseous spaces (proximal and distal interosseous spaces) with complete fusion along their shafts in adults", "A single proximal interosseous space with a free, mobile ulna", "Complete freedom of pronation and supination", "Absence of the olecranon process"],
         0, "In ruminants, the ulna extends the entire length of the antebrachium and fuses with the radius, leaving two permanent openings: a proximal interosseous space and a small distal interosseous space.",
         True, "Comparative Osteology (ICAR PG PYQ)"),

        ("The 'Accessory Carpal Bone' (Os carpi accessorium) is projected palmarward, providing insertion to the tendon of the:",
         ["Flexor carpi ulnaris muscle (and abductor digiti quinti)", "Extensor carpi radialis", "Common digital extensor", "Biceps brachii"],
         0, "The accessory carpal bone forms the lateral boundary of the carpal canal and acts as a lever arm for the flexor carpi ulnaris and ulnaris lateralis muscles during carpal flexion.",
         False, "Comparative Osteology"),

        ("The total number of functional carpal bones present in the carpus of the adult Horse is typically:",
         ["7 or 8 (Radial, Intermediate, Ulnar, Accessory in proximal row; II, III, IV, and inconsistently I in distal row)", "6", "5", "10"],
         0, "The horse carpus has 7 or 8 bones: proximal row (radial, intermediate, ulnar, accessory) and distal row (second, third, fourth carpal bones, with the first carpal bone present in ~30-50% of horses).",
         True, "Comparative Osteology (ICAR PG PYQ)"),

        ("In the bovine forelimb, the 'Large Metacarpal Bone' (Cannon bone) is formed by the prenatal embryonic fusion of:",
         ["Metacarpal III and Metacarpal IV (marked by a longitudinal vascular groove)", "Metacarpal II and III", "Metacarpal I and II", "Metacarpal IV and V"],
         0, "In ruminants, the large cannon bone represents the developmental fusion of the 3rd and 4th metacarpals, featuring a vertical dorsal longitudinal groove and two distal articular condyles separated by an intertrochlear notch.",
         True, "Comparative Osteology (ICAR PG PYQ)"),

        # 21-30: Hindlimb comparative osteology & heterotopic bones
        ("The 'Psoas Tubercle' (tuberculum psoas minus), providing insertion for the psoas minor muscle, is located on the ventral surface of the shaft of the:",
         ["Ilium (along the iliopectineal line)", "Ischium", "Pubis", "Sacrum"],
         0, "The psoas tubercle is a distinct rough ridge or tubercle located on the medial/ventral border of the shaft of the ilium in horses and cattle, providing insertion for the tendon of the psoas minor.",
         False, "Comparative Osteology"),

        ("In the bovine pelvis, the Tuber Ischiadicum ('Pin bone') differs from that of the horse because the bovine tuber ischiadicum is:",
         ["Trifid (possessing three distinct blunt bony tuberosities: dorsal, ventral, and lateral)", "A smooth, single rounded plate", "Completely absent", "Pointed like a needle"],
         0, "In cattle, the tuber ischiadicum is thick, rugged, and trifid (three-pointed), forming the anatomical 'pin bone' used in linear body measurements; in the horse, it forms a flat, rounded, single-crested plate.",
         True, "Comparative Osteology (ICAR PG PYQ)"),

        ("The 'Third Trochanter' (trochanter tertius), a massive flattened curved bony crest on the lateral border of the femoral shaft, is uniquely prominent in the:",
         ["Horse (Equine)", "Ox (Bovine)", "Dog (Canine)", "Pig (Porcine)"],
         0, "The equine femur is distinguished by a large, prominent third trochanter on its lateral border providing insertion to the superficial gluteal muscle; it is completely absent in ruminants, dogs, and pigs.",
         True, "Comparative Osteology (ICAR PG PYQ)"),

        ("The 'Extensor Fossa' (fossa extensoria), a distinct depression on the distal extremity of the femur providing origin to the peroneus tertius and long digital extensor muscles, is located on the:",
         ["Lateral epicondyle / lateral condyle of the femur", "Medial epicondyle", "Trochlea", "Greater trochanter"],
         0, "The extensor fossa is a small, deep pit situated between the lateral condyle and the lateral lip of the femoral trochlea, giving origin to the common tendon of the peroneus tertius and long digital extensor in ruminants and equines.",
         True, "Comparative Osteology (ICAR PG PYQ)"),

        ("In cattle, the distal extremity of the fibula persists throughout adult life as an independent, separate tarsal bone termed the:",
         ["Os malleolare (Malleolar bone / external malleolus)", "Os penis", "Patella", "Os cordis"],
         0, "In ruminants, the shaft of the fibula is absent, but its distal end develops as a separate, fully articulated quadrilateral bone called the os malleolare, articulating with the distal tibia, talus, and calcaneus.",
         True, "Comparative Osteology (ICAR PG PYQ)"),

        ("In the equine tarsus (hock joint), the total number of tarsal bones typically present is:",
         ["6 (Talus, Calcaneus, Central, Tarsal I+II fused, Tarsal III, and Tarsal IV)", "5 (Central and IV fused)", "7", "4"],
         0, "The equine tarsus contains 6 bones: proximal row (talus, calcaneus), middle row (central tarsal), and distal row (fused 1st and 2nd tarsal, 3rd tarsal, and 4th tarsal); in cattle, central and 4th are fused and 2nd and 3rd are fused, yielding 5 bones.",
         True, "Comparative Osteology (ICAR PG PYQ)"),

        ("Heterotopic (visceral / splanchnic) bones are osseous elements that develop within soft tissues or organs. The 'Os Cordis' is normally present in the heart of:",
         ["Cattle (Bovine, typically two bones in the aortic fibrous ring)", "Dogs", "Horses", "Fowl"],
         0, "In cattle (and older sheep/goats), two heterotopic bones (os cordis dextrum and sinistrum) develop within the cardiac skeleton surrounding the aortic fibrous ring, providing support to the aortic valve and atrioventricular valves.",
         True, "Comparative Osteology (ICAR PG PYQ)"),

        ("The 'Os Penis' (Baculum) of the male canine skeleton is grooved along its ventral surface to accommodate the:",
         ["Penile Urethra", "Dorsal artery of the penis", "Deep dorsal vein", "Internal pudendal nerve"],
         0, "The canine os penis is a heterotopic ossification within the glans penis; its ventral surface is excavated by a deep urethral sulcus (sulcus urethralis) that houses and protects the penile urethra.",
         True, "Comparative Osteology (ICAR PG PYQ)"),

        ("The 'Os Rostri' is a splanchnic bone found in the muzzle of which domestic animal, serving to strengthen the snout for rooting behavior?",
         ["Pig (Porcine)", "Dog", "Ox", "Horse"],
         0, "The os rostri (rostral bone / os snout) is a triangular heterotopic bone situated within the cartilaginous nasal septum and rostral plate of swine, providing rigid support for burrowing and rooting.",
         True, "Comparative Osteology (ICAR PG PYQ)"),

        ("Scleral Ossicles (a ring of overlapping thin bony plates embedded within the sclera of the eye) are a characteristic feature of:",
         ["Birds (Avian eye)", "Dogs", "Horses", "Ruminants"],
         0, "Birds possess a ring of 10 to 18 overlapping scleral ossicles surrounding the cornea, providing rigid mechanical support to maintain the non-spherical shape of the large avian eye and resist intraocular pressure changes.",
         True, "Comparative Osteology (ICAR PG PYQ)"),

        # 31-40: Arthrology, ligaments, specific joints
        ("The 'Accessory Ligament of the Femur' (Ligamentum accessorium ossis femoris) is an intra-articular ligament of the hip joint uniquely present in the:",
         ["Horse (Equine, originating from the prepubic tendon and preventing abduction)", "Ox (Bovine)", "Dog (Canine)", "Pig (Porcine)"],
         0, "The horse uniquely possesses an accessory ligament of the hip joint (in addition to the ligament of the head of the femur); it arises from the prepubic tendon of the abdominal muscles, passes through the acetabular notch, and inserts into the femoral fovea capitis, preventing kicking outward.",
         True, "Arthrology (ICAR PG PYQ)"),

        ("The Stifle Joint (Femoropatellar joint) of the Horse and Ox possesses how many Patellar Ligaments connecting the patella to the tibial tuberosity?",
         ["3 (Medial, Middle / Intermediate, and Lateral patellar ligaments)", "1 single straight ligament", "2 ligaments", "4 ligaments"],
         0, "Large ungulates (equines and bovines) possess three distinct patellar ligaments: lateral, intermediate (middle), and medial; in carnivores and humans, there is only a single straight patellar tendon/ligament.",
         True, "Arthrology (ICAR PG PYQ)"),

        ("The 'Patellar Locking Mechanism' in the horse, which enables equines to rest while standing with minimal muscular energy (part of the stay apparatus), operates by hooking the medial patellar ligament and patellar fibrocartilage over the:",
         ["Medial ridge of the femoral trochlea", "Lateral ridge of the femoral trochlea", "Extensor fossa", "Intercondyloid fossa"],
         0, "The medial ridge of the equine femoral trochlea is markedly larger than the lateral ridge and terminates proximally in a round tubercle; rotating the patella medially hooks the looped medial ligament over this tubercle, locking the stifle in extension.",
         True, "Arthrology (ICAR PG PYQ)"),

        ("The cranial and caudal Cruciate Ligaments (Ligamenta cruciata genus) of the stifle joint cross each other within which anatomical space?",
         ["Intercondylar fossa of the femur and intercondylar area of the tibia (intra-articular but extrasynovial)", "Subcutaneous prepatellar bursa", "Tarsal canal", "Extensor fossa"],
         0, "The cruciate ligaments reside inside the fibrous joint capsule (intra-articular) between the condyles of the femur and tibia, but are wrapped in reflections of synovial membrane (extrasynovial); the cranial cruciate prevents cranial tibial translation.",
         True, "Arthrology (ICAR PG PYQ)"),

        ("A 'Ginglymus' (Hinge Joint) is a synovial joint that permits movement predominantly in one plane (flexion and extension). A classic anatomical example in the canine skeleton is the:",
         ["Elbow joint (Cubital joint)", "Shoulder joint", "Hip joint", "Atlanto-axial joint"],
         0, "The elbow joint (between the humeral condyle and the trochlear notch of the ulna/fovea of the radius) is a typical uniaxial ginglymus joint permitting only flexion and extension.",
         False, "Arthrology"),

        ("The Atlanto-Axial Joint (articulatio atlantoaxialis) between the first and second cervical vertebrae is classified structurally and functionally as a:",
         ["Pivot joint (Trochoid joint) permitting axial rotation of the head", "Ball-and-socket joint", "Saddle joint", "Suture"],
         0, "The atlanto-axial joint is a uniaxial pivot (trochoid) joint; the peg-like or spout-shaped dens of the axis rotates within the ring formed by the ventral arch and transverse ligament of the atlas, producing rotational 'no' head movements.",
         True, "Arthrology (ICAR PG PYQ)"),

        ("The 'Nuchal Ligament' (Ligamentum nuchae), which assists in supporting the heavy weight of the head, consists of a Funicular part (cord) and a Lamellar part (sheet) in the Horse and Ox, but in the Dog it:",
         ["Consists solely of a Funicular part extending from the axis to the first thoracic spine, and lacks a lamellar part entirely", "Is completely absent", "Is identical to the ox", "Has only a lamellar part"],
         0, "In the dog, the nuchal ligament is represented only by a slender funicular band stretching from the spinous process of the axis to the spinous process of T1; cats and pigs lack a nuchal ligament entirely.",
         True, "Arthrology (ICAR PG PYQ)"),

        ("Which domestic animal species completely lacks a Nuchal Ligament?",
         ["Pig (Porcine) and Cat (Feline)", "Dog and Sheep", "Horse and Ox", "Camel"],
         0, "Because the pig carries its head low on a short, muscular neck, and the cat has an exceptionally flexible neck with independent head mobility, both pigs and cats completely lack a ligamentum nuchae.",
         True, "Comparative Osteology (ICAR PG PYQ)"),

        ("The 'Suspensory Ligament' of the equine and bovine distal limb (Interosseous muscle / Musculus interosseus medius) functions to:",
         ["Prevent excessive hyperextension (dorsiflexion) of the fetlock (metacarpophalangeal) joint during weight-bearing", "Flex the carpus", "Rotate the digit", "Retract the hoof"],
         0, "The suspensory ligament (entirely tendinous in the adult horse, partially muscular in cattle) originates on the proximal metacarpus/carpus and bifurcates onto the proximal sesamoid bones, forming the primary tension band of the stay apparatus preventing fetlock sinking.",
         True, "Arthrology (ICAR PG PYQ)"),

        ("The 'Check Ligaments' (accessory ligaments) of the equine distal limb include the Superior Check Ligament and Inferior Check Ligament, which reinforce which respective flexor tendons?",
         ["Superior reinforces Superficial Digital Flexor tendon; Inferior reinforces Deep Digital Flexor tendon", "Superior reinforces DDFT; Inferior reinforces SDFT", "Both reinforce Extensor carpi radialis", "Both reinforce Common digital extensor"],
         0, "The superior (radial) check ligament arises from the distal caudal radius and blends with the superficial digital flexor tendon; the inferior (subcarpal) check ligament arises from the palmar carpal ligament and anchors to the deep digital flexor tendon.",
         True, "Arthrology (ICAR PG PYQ)")
    ]
    return qs

if __name__ == '__main__':
    qs = get_module1_questions()
    print(f"Anatomy Module 1 loaded: {len(qs)} questions")
