"""
HMBY311 Module 4 and Module 5 Comprehensive Datasets
Based on:
- /home/javvii/YearIII/HMBY311/module4/CHROMOSOMES and CELL DIVISION 4th TOPIC.pptx
- /home/javvii/YearIII/HMBY311/module5/Genetics, Human Inheritance and Cancer.pptx
"""

import json

HMBY_MODULE_4_ITEMS = [
    {
        "q": "The condensed form of DNA in a cell that surrounds and wraps around spool-like proteins called histones is known as what structure?",
        "a": "Chromosome",
        "distractors": ["Ribosome", "Centriole", "Nucleolus"],
        "explanation": "A chromosome contains DNA in its condensed form wrapped around proteins called histones.",
        "topic": "Forms of Chromosomes"
    },
    {
        "q": "What proteins serve as the molecular spools around which DNA coils and condenses into chromatin and chromosomes?",
        "a": "Histones",
        "distractors": ["Ribosomes", "Centrosomes", "Spindle fibers"],
        "explanation": "DNA wraps around proteins called histones to form compact chromatin and chromosomes, preventing breakage during cell division.",
        "topic": "Forms of Chromosomes"
    },
    {
        "q": "A specific sequence of DNA that codes for a protein with a structural or functional role in the cell is defined as a what?",
        "a": "Gene",
        "distractors": ["Codon", "Centromere", "Histone"],
        "explanation": "A gene is a sequence of DNA arranged in a specific manner that codes for a protein with a structural or functional role in the cell.",
        "topic": "Forms of Chromosomes"
    },
    {
        "q": "How many different kinds of chromosomes are present in human cells?",
        "a": "23 kinds",
        "distractors": ["46 kinds", "22 kinds", "2 kinds"],
        "explanation": "Each of the 23 different kinds of chromosomes in human cells contains a specific sequence of genes.",
        "topic": "Forms of Chromosomes"
    },
    {
        "q": "According to findings from the Human Genome Project, approximately how many base pairs are in the human genome?",
        "a": "3.2 billion base pairs",
        "distractors": ["3.2 million base pairs", "46 billion base pairs", "23 million base pairs"],
        "explanation": "Researchers have sequenced approximately 3.2 billion base pairs in the human genome (about 99% of the genome).",
        "topic": "Human Genome Project"
    },
    {
        "q": "What percentage of our modern human DNA is unique to modern humans and distinct from early human ancestors?",
        "a": "7%",
        "distractors": ["99%", "23%", "1%"],
        "explanation": "Out of the 99% of sequenced human genome, 7% of our DNA is unique to modern humans compared to early ancestors.",
        "topic": "Human Genome Project"
    },
    {
        "q": "All cells within the human body except for reproductive cells (eggs and sperm) are classified as what type of cells?",
        "a": "Somatic cells",
        "distractors": ["Gametes", "Sex cells", "Zygotes"],
        "explanation": "Somatic cells refer to all cells within the human body and are diploid (46 chromosomes) except eggs and sperm.",
        "topic": "Somatic Cells"
    },
    {
        "q": "What is the total diploid chromosome number present in normal human somatic cells?",
        "a": "46 chromosomes",
        "distractors": ["23 chromosomes", "92 chromosomes", "44 chromosomes"],
        "explanation": "Somatic cells are diploid, containing 46 chromosomes (23 homologous pairs).",
        "topic": "Somatic Cells"
    },
    {
        "q": "What term describes human reproductive cells (eggs and sperm) that contain only one set of 23 chromosomes?",
        "a": "Haploid",
        "distractors": ["Diploid", "Tetraploid", "Polyploid"],
        "explanation": "Eggs and sperm are haploid, meaning they contain only one set of 23 chromosomes.",
        "topic": "Gametes"
    },
    {
        "q": "Chromosomes that occur in pairs and contain genes that code for or affect the same biological traits are called what?",
        "a": "Homologous chromosomes",
        "distractors": ["Analogous chromosomes", "Heterozygous chromosomes", "Sister chromatids"],
        "explanation": "Homologous chromosomes are pairs that contain genes coding for or affecting the same traits, one from each parent.",
        "topic": "Homologous Chromosomes"
    },
    {
        "q": "How many homologous chromosome pairs are found in a normal human somatic cell?",
        "a": "23 pairs",
        "distractors": ["46 pairs", "22 pairs", "1 pair"],
        "explanation": "The diploid number of 46 chromosomes translates to 23 homologous pairs in each somatic cell.",
        "topic": "Homologous Chromosomes"
    },
    {
        "q": "The single pair of human chromosomes that determines biological gender is designated as what?",
        "a": "Sex chromosomes",
        "distractors": ["Autosomes", "Centrosomes", "Histones"],
        "explanation": "One pair of chromosomes determines gender and is called the sex chromosomes (XY in males, XX in females).",
        "topic": "Sex Chromosomes"
    },
    {
        "q": "Which sex chromosome combination corresponds to biological males in humans?",
        "a": "XY",
        "distractors": ["XX", "YY", "XO"],
        "explanation": "Males have XY chromosomes, while females have XX chromosomes.",
        "topic": "Sex Chromosomes"
    },
    {
        "q": "Which sex chromosome combination corresponds to biological females in humans?",
        "a": "XX",
        "distractors": ["XY", "YY", "XXY"],
        "explanation": "Females possess two X chromosomes (XX).",
        "topic": "Sex Chromosomes"
    },
    {
        "q": "The 22 pairs of human chromosomes that do not determine gender are called what?",
        "a": "Autosomes",
        "distractors": ["Sex chromosomes", "Centrosomes", "Chromatids"],
        "explanation": "There are 22 pairs of non-sex chromosomes, which are termed autosomes.",
        "topic": "Autosomes"
    },
    {
        "q": "Which type of nuclear division produces two genetically identical daughter cells with the same number of chromosomes as the parent cell for growth and tissue repair?",
        "a": "Mitosis",
        "distractors": ["Meiosis", "Binary fission", "Fertilization"],
        "explanation": "Mitosis creates daughter cells with the exact same number of chromosomes as the original cell, functioning in growth and tissue repair.",
        "topic": "Types of Cell Division"
    },
    {
        "q": "Which type of nuclear division reduces the chromosome number by half and occurs specifically during the production of gametes?",
        "a": "Meiosis",
        "distractors": ["Mitosis", "Cytokinesis", "Interphase"],
        "explanation": "Meiosis creates cells with half the number of chromosomes (haploid) as the original cell and occurs during gamete production.",
        "topic": "Types of Cell Division"
    },
    {
        "q": "What are the two major phases that comprise the eukaryotic cell cycle?",
        "a": "Interphase and cell division",
        "distractors": ["Prophase and telophase", "Mitosis and meiosis", "G1 and G2"],
        "explanation": "The cell cycle consists of two major phases: interphase and cell division (mitosis + cytokinesis).",
        "topic": "Cell Cycle"
    },
    {
        "q": "The period between cell divisions during which the cell grows and replicates its DNA and organelles is called what?",
        "a": "Interphase",
        "distractors": ["Anaphase", "Metaphase", "Cytokinesis"],
        "explanation": "Interphase is the period between cell divisions during which DNA and organelles replicate in preparation for division.",
        "topic": "Cell Cycle"
    },
    {
        "q": "What are the three sequential sub-phases of interphase?",
        "a": "G1, S, and G2",
        "distractors": ["Prophase, metaphase, and anaphase", "Mitosis, meiosis, and cytokinesis", "G0, G1, and G2"],
        "explanation": "Interphase is divided into G1 (First Gap), S (Synthesis), and G2 (Second Gap) phases.",
        "topic": "Interphase"
    },
    {
        "q": "During which sub-phase of interphase does major cell growth occur before DNA synthesis begins?",
        "a": "G1 phase",
        "distractors": ["S phase", "G2 phase", "M phase"],
        "explanation": "G1 (First Gap) is the stage where major cell growth occurs before DNA synthesis begins.",
        "topic": "Interphase"
    },
    {
        "q": "During which specific sub-phase of interphase does DNA synthesis (replication) take place?",
        "a": "S phase",
        "distractors": ["G1 phase", "G2 phase", "Prophase"],
        "explanation": "During the S phase (Synthesis), DNA replication occurs, producing identical copies of genetic material.",
        "topic": "Interphase"
    },
    {
        "q": "During which sub-phase of interphase does the cell undergo a second stage of growth in final preparation for mitosis?",
        "a": "G2 phase",
        "distractors": ["G1 phase", "S phase", "Cytokinesis"],
        "explanation": "In the G2 phase, another stage of growth and protein synthesis occurs before mitosis begins.",
        "topic": "Interphase"
    },
    {
        "q": "In which phase of mitosis does chromatin condense into visible chromosomes, the nuclear membrane break down, and centrioles move to opposite poles?",
        "a": "Prophase",
        "distractors": ["Metaphase", "Anaphase", "Telophase"],
        "explanation": "During prophase, chromatin condenses, the nuclear membrane breaks down, and centrioles migrate toward opposite ends of the cell.",
        "topic": "Mitosis Phases"
    },
    {
        "q": "Why is the condensation of DNA around histones during prophase critical for cell division?",
        "a": "It makes it easier to separate sister chromatids without breaking them",
        "distractors": ["It speeds up DNA replication", "It synthesizes new spindle fibers", "It dissolves the cell membrane"],
        "explanation": "DNA wrapping tightly around histones prevents long DNA strands from tangling and breaking during chromatid separation.",
        "topic": "Mitosis Phases"
    },
    {
        "q": "During which phase of mitosis do chromosomes attach to spindle fibers and line up along the equator (center) of the mitotic spindle?",
        "a": "Metaphase",
        "distractors": ["Prophase", "Anaphase", "Telophase"],
        "explanation": "During metaphase, chromosomes attach to spindle fibers and migrate to the equator (metaphase plate) of the mitotic spindle.",
        "topic": "Mitosis Phases"
    },
    {
        "q": "During which phase of mitosis do sister chromatids split at the centromere and get pulled toward opposite poles of the cell?",
        "a": "Anaphase",
        "distractors": ["Prophase", "Metaphase", "Telophase"],
        "explanation": "During anaphase, sister chromatids separate at the centromere and are pulled toward opposite cell poles.",
        "topic": "Mitosis Phases"
    },
    {
        "q": "What specialized chromosomal region holds sister chromatids together until it splits during anaphase?",
        "a": "Centromere",
        "distractors": ["Centrosome", "Centriole", "Telomere"],
        "explanation": "Chromosomes split at the centromere during anaphase as spindle fibers pull them apart.",
        "topic": "Mitosis Phases"
    },
    {
        "q": "In which phase of mitosis does a nuclear envelope reform around each group of chromosomes, the spindle disassemble, and chromosomes decondense?",
        "a": "Telophase",
        "distractors": ["Prophase", "Metaphase", "Anaphase"],
        "explanation": "During telophase, nuclear envelopes reform, the mitotic spindle disassembles, and chromosomes decondense back into chromatin.",
        "topic": "Mitosis Phases"
    },
    {
        "q": "What is the separate cellular process involving the physical division of the cytoplasm into two daughter cells?",
        "a": "Cytokinesis",
        "distractors": ["Karyokinesis", "Interphase", "Apoptosis"],
        "explanation": "Cytokinesis is the process involving the division of cytoplasm, beginning during telophase.",
        "topic": "Cytokinesis"
    },
    {
        "q": "At what stage of mitosis does cytokinesis usually begin in human cells?",
        "a": "Telophase",
        "distractors": ["Prophase", "Metaphase", "G1 phase"],
        "explanation": "Cytokinesis usually begins sometime during telophase.",
        "topic": "Cytokinesis"
    },
    {
        "q": "What cytoskeletal structure contracts at the midline of a dividing animal cell to create a cleavage furrow during cytokinesis?",
        "a": "A band of microfilaments",
        "distractors": ["Microtubules", "Histone octamer", "Centrioles"],
        "explanation": "A band of microfilaments located at the cell midline contracts, forming a furrow that pinches the cell in two.",
        "topic": "Cytokinesis"
    },
    {
        "q": "What groove or indentation forms at the cell equator as contracting microfilaments deepen to pinch the cell into two?",
        "a": "Cleavage furrow",
        "distractors": ["Equatorial plate", "Centromere", "Cell plate"],
        "explanation": "The contracting microfilament band forms a furrow that pinches the cell into two daughter cells once it deepens.",
        "topic": "Cytokinesis"
    },
    {
        "q": "Skin, bone, blood, and internal organ cells are all examples of what category of cells?",
        "a": "Somatic cells",
        "distractors": ["Gametes", "Sex cells", "Germ cells"],
        "explanation": "Examples of somatic cells include cells of internal organs, skin, bones, blood, and connective tissues.",
        "topic": "Somatic Cells"
    },
    {
        "q": "How many autosomes (individual non-sex chromosomes) are present in a human somatic cell?",
        "a": "44 autosomes",
        "distractors": ["22 autosomes", "46 autosomes", "23 autosomes"],
        "explanation": "There are 22 pairs of autosomes, which equals 44 individual autosomes (plus 2 sex chromosomes = 46 total).",
        "topic": "Autosomes"
    },
    {
        "q": "Which cellular organelle pairs migrate away from each other toward opposite poles during prophase to organize the spindle apparatus?",
        "a": "Centrioles",
        "distractors": ["Ribosomes", "Lysosomes", "Golgi bodies"],
        "explanation": "During prophase, centrioles move away from each other toward opposite ends of the cell to form the mitotic spindle.",
        "topic": "Mitosis Phases"
    },
    {
        "q": "What structure is composed of microtubules that attach to chromosomes and direct their alignment and separation during mitosis?",
        "a": "Mitotic spindle",
        "distractors": ["Nuclear envelope", "Cleavage furrow", "Cell cortex"],
        "explanation": "The mitotic spindle is composed of spindle fibers that attach to chromosomes at metaphase and pull them apart at anaphase.",
        "topic": "Mitosis Phases"
    },
    {
        "q": "What happens to the mitotic spindle during telophase?",
        "a": "It disassembles and disappears",
        "distractors": ["It duplicates", "It pulls chromatids to the center", "It forms the cell membrane"],
        "explanation": "During telophase, the mitotic spindle that caused chromosomes to migrate disassembles and disappears.",
        "topic": "Mitosis Phases"
    },
    {
        "q": "In which stage of the cell cycle does a cell spend the majority of its functional life performing daily metabolic activities and preparing for division?",
        "a": "Interphase",
        "distractors": ["Mitosis", "Cytokinesis", "Anaphase"],
        "explanation": "Interphase is the longest phase of the cell cycle, consisting of G1, S, and G2 phases.",
        "topic": "Cell Cycle"
    },
    {
        "q": "What is the primary biological outcome of mitosis followed by cytokinesis?",
        "a": "Two genetically identical diploid daughter cells",
        "distractors": ["Four genetically diverse haploid gametes", "A single tetraploid cell", "Two non-identical haploid cells"],
        "explanation": "Mitosis distributes replicated genetic material equally between two daughter cells, producing identical diploid cells.",
        "topic": "Types of Cell Division"
    }
]

print(f"Total HMBY Module 4 items crafted: {len(HMBY_MODULE_4_ITEMS)}")
