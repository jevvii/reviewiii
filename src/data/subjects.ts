export interface ModuleInfo {
  id: string;
  number: number;
  title: string;
  description: string;
  itemCount: number;
  topics: string[];
  quizPath: string;
  notebookLmUrl?: string;
  downloads: {
    pdf?: string;
    docx?: string;
    json?: string;
    md?: string;
  };
}

export interface Subject {
  code: string;
  title: string;
  subtitle: string;
  description: string;
  term: string;
  category: 'core' | 'gen-ed' | 'elective';
  status: 'active' | 'upcoming';
  accentColor: string;
  tag: string;
  modules: ModuleInfo[];
}

export const SUBJECTS: Subject[] = [
  {
    code: 'NETC311',
    title: 'Networking Technologies',
    subtitle: 'Cisco CCNA v7.0 — Introduction to Networks (ITN)',
    description: 'Foundational computer network architectures, protocol suites, transmission media, Ethernet, IPv4/IPv6 addressing, network security, and Cisco IOS switch/router configurations.',
    term: 'Year III — 1st Semester',
    category: 'core',
    status: 'active',
    accentColor: '#8a9a86',
    tag: 'Cisco Networking Academy',
    modules: [
      {
        id: 'netc311-m1',
        number: 1,
        title: 'Networking Today',
        description: 'Host roles, peer-to-peer, network components, media representations, topologies, LANs/WANs, network reliability (Fault Tolerance, Scalability, QoS, Security), and networking trends.',
        itemCount: 99,
        topics: ['Host Roles', 'LAN vs WAN', 'Reliable Networks', 'Network Security', 'CCNA Foundation'],
        quizPath: 'quizzes/netc311/module1.html',
        notebookLmUrl: 'https://notebooklm.google.com/notebook/a4a23950-074d-4120-bbb5-9a482941d5ba',
        downloads: {
          pdf: 'downloads/netc311/Module 1 - Networking Today - Questionnaire.pdf',
          docx: 'downloads/netc311/Module 1 - Networking Today - Questionnaire.docx',
          json: 'downloads/netc311/Module_1_NotebookLM_Quiz.json',
          md: 'downloads/netc311/Module_1_NotebookLM_Quiz.md'
        }
      },
      {
        id: 'netc311-m2',
        number: 2,
        title: 'Basic Switch & End Device Configuration',
        description: 'Cisco IOS navigation, access methods (Console, SSH, Telnet), command modes (User EXEC, Privileged EXEC, Global Config), password encryption, banner MOTD, and SVI IP address configuration.',
        itemCount: 104,
        topics: ['Cisco IOS CLI', 'Command Modes', 'Password Security', 'Banner MOTD', 'Switch SVI Setup'],
        quizPath: 'quizzes/netc311/module2.html',
        notebookLmUrl: 'https://notebooklm.google.com/notebook/0acd2de0-cfc6-4f3a-b38f-8e92376b906e',
        downloads: {
          pdf: 'downloads/netc311/Module 2 - Basic Switch and End Device Configuration - Questionnaire.pdf',
          docx: 'downloads/netc311/Module 2 - Basic Switch and End Device Configuration - Questionnaire.docx',
          json: 'downloads/netc311/Module_2_NotebookLM_Quiz.json',
          md: 'downloads/netc311/Module_2_NotebookLM_Quiz.md'
        }
      },
      {
        id: 'netc311-m3',
        number: 3,
        title: 'Protocols & Models',
        description: 'Network communication rules, protocol suites (OSI vs TCP/IP), standards organizations (IEEE, IETF, ISO), data encapsulation & PDUs, and Layer 2 MAC vs Layer 3 IP data access.',
        itemCount: 95,
        topics: ['Communication Rules', 'Protocol Suites', 'Standards Bodies', 'OSI vs TCP/IP', 'Data Encapsulation & Access'],
        quizPath: 'quizzes/netc311/module3.html',
        notebookLmUrl: 'https://notebooklm.google.com/notebook/a4a23950-074d-4120-bbb5-9a482941d5ba',
        downloads: {
          pdf: 'downloads/netc311/Module 3 - Protocols and Models - Questionnaire.pdf',
          docx: 'downloads/netc311/Module 3 - Protocols and Models - Questionnaire.docx',
          json: 'downloads/netc311/Module_3_NotebookLM_Quiz.json',
          md: 'downloads/netc311/Module_3_NotebookLM_Quiz.md'
        }
      }
    ]
  },
  {
    code: 'HMBY311',
    title: 'Human Biology',
    subtitle: 'Biological Principles, Scientific Method & Biochemistry',
    description: 'Study of human biological systems, scientific methodology, controlled experiments, atomic chemistry, macromolecules of life (carbohydrates, lipids, proteins, nucleic acids), enzymes, and cellular physiology.',
    term: 'Year III — 1st Semester',
    category: 'gen-ed',
    status: 'active',
    accentColor: '#a89f91',
    tag: 'Natural Sciences',
    modules: [
      {
        id: 'hmby311-m1',
        number: 1,
        title: 'The Scientific Method & Basic Chemistry',
        description: 'Phases of the scientific method, hypothesis falsifiability, controlled experiments, matter, atomic structure, isotopes, covalent/ionic bonds, water properties, macromolecules, amino acids, enzymes, and DNA/RNA.',
        itemCount: 152,
        topics: ['Scientific Method', 'Atoms & Bonds', 'Water Polarity', 'Biomolecules', 'Enzymes', 'DNA vs RNA'],
        quizPath: 'quizzes/hmby311/module1.html',
        notebookLmUrl: 'https://notebooklm.google.com/notebook/ee53d9b1-22a8-4a9b-a53b-66e8af5bd0ed',
        downloads: {
          pdf: 'downloads/hmby311/Module 1 - Human Biology - Scientific Method and Basic Chemistry.pdf',
          docx: 'downloads/hmby311/Module 1 - Human Biology - Scientific Method and Basic Chemistry.docx',
          json: 'downloads/hmby311/HMBY311_Module_1_Quiz.json',
          md: 'downloads/hmby311/HMBY311_Module_1_Quiz.md'
        }
      },
      {
        id: 'hmby311-m4',
        number: 4,
        title: 'Chromosomes & Cell Division',
        description: 'Forms of chromosomes, DNA condensation around histones, somatic diploid vs gamete haploid cells, autosomes, sex chromosomes (XY/XX), cell cycle (G1, S, G2), prophase, metaphase, anaphase, telophase, and microfilament cytokinesis.',
        itemCount: 40,
        topics: ['Chromosomes & Histones', 'Human Genome Project', 'Somatic vs Gametes', 'Mitosis Phases', 'Cytokinesis'],
        quizPath: 'quizzes/hmby311/module4.html',
        downloads: {
          pdf: 'downloads/hmby311/Module 4 - Chromosomes and Cell Division - Questionnaire.pdf',
          docx: 'downloads/hmby311/Module 4 - Chromosomes and Cell Division - Questionnaire.docx',
          json: 'downloads/hmby311/HMBY311_Module_4_Quiz.json',
          md: 'downloads/hmby311/HMBY311_Module_4_Quiz.md'
        }
      },
      {
        id: 'hmby311-m5',
        number: 5,
        title: 'Genetics, Human Inheritance and Cancer',
        description: 'Mendelian genetics, Law of Segregation & Independent Assortment, Punnett squares, non-Mendelian patterns (codominance, incomplete dominance, polygenic, sex-influenced), human traits inventory, genetic disorders (amniocentesis/CVS), neoplasm biology, dysplasia, carcinoma in situ, angiogenesis, oncogenes, tumor suppressor genes, and cancer therapeutics.',
        itemCount: 60,
        topics: ['Mendelian Genetics', 'Punnett Squares', 'Human Traits Inventory', 'Amniocentesis & CVS', 'Neoplasms & Metastasis', 'Oncogenes & Apoptosis', 'Cancer Therapies'],
        quizPath: 'quizzes/hmby311/module5.html',
        downloads: {
          pdf: 'downloads/hmby311/Module 5 - Genetics, Human Inheritance and Cancer - Questionnaire.pdf',
          docx: 'downloads/hmby311/Module 5 - Genetics, Human Inheritance and Cancer - Questionnaire.docx',
          json: 'downloads/hmby311/HMBY311_Module_5_Quiz.json',
          md: 'downloads/hmby311/HMBY311_Module_5_Quiz.md'
        }
      }
    ]
  },
  {
    code: 'SOFE311',
    title: 'Software Engineering',
    subtitle: 'Software Lifecycle, Architecture & System Modeling',
    description: 'Software development life cycles (SDLC), Agile/Scrum methodologies, requirements engineering, architectural patterns, design principles, testing strategies, and CI/CD pipelines.',
    term: 'Year III — 1st Semester',
    category: 'core',
    status: 'upcoming',
    accentColor: '#7a8c99',
    tag: 'Computer Science Core',
    modules: []
  },
  {
    code: 'ITPM311',
    title: 'IT Project Management',
    subtitle: 'Project Governance, Agile Estimations & Risk Control',
    description: 'Frameworks for managing modern technology initiatives: project lifecycles, work breakdown structures (WBS), cost estimation, risk matrices, stakeholder communications, and quality assurance.',
    term: 'Year III — 1st Semester',
    category: 'core',
    status: 'upcoming',
    accentColor: '#9c8c7d',
    tag: 'Technology Management',
    modules: []
  },
  {
    code: 'CSEL311',
    title: 'CS Professional Elective',
    subtitle: 'Advanced Computing Disciplines & Applied Topics',
    description: 'Specialized elective exploring contemporary software development, system design frameworks, data architectures, and emerging computational paradigms.',
    term: 'Year III — 1st Semester',
    category: 'elective',
    status: 'upcoming',
    accentColor: '#8a9a86',
    tag: 'Elective Track',
    modules: []
  },
  {
    code: 'ATFL311',
    title: 'Automata Theory & Formal Languages',
    subtitle: 'Computation Models, Grammars & Computability',
    description: 'Mathematical foundations of computation: deterministic and non-deterministic finite automata (DFA/NFA), regular expressions, context-free grammars, pushdown automata, and Turing machines.',
    term: 'Year III — 1st Semester',
    category: 'core',
    status: 'active',
    accentColor: '#a89f91',
    tag: 'Theoretical Computer Science',
    modules: [
      {
        id: 'atfl311-m1',
        number: 1,
        title: 'Introduction to Automata Theory & Chomsky Hierarchy',
        description: 'Foundations of automata theory, Alan Turing & Turing Machines, McCulloch-Pitts neural models, Mealy & Moore transducers, Chomsky Hierarchy, and real-world automata applications.',
        itemCount: 40,
        topics: ['Automata Theory', 'Turing Machine', 'McCulloch & Pitts', 'Mealy & Moore', 'Chomsky Hierarchy', 'Real-World Applications'],
        quizPath: 'quizzes/atfl311/module1.html',
        downloads: {
          pdf: 'downloads/atfl311/Module 1 - Introduction to Automata Theory - Questionnaire.pdf',
          docx: 'downloads/atfl311/Module 1 - Introduction to Automata Theory - Questionnaire.docx',
          json: 'downloads/atfl311/ATFL311_Module_1_Quiz.json',
          md: 'downloads/atfl311/ATFL311_Module_1_Quiz.md'
        }
      },
      {
        id: 'atfl311-m2',
        number: 2,
        title: 'Finite State Machines & Prerequisites',
        description: 'FSM definitions, symbols, alphabets (Σ), strings, languages, powers of sigma (Σ^n), cardinality formulas (2^n), Kleene star (Σ*), FA with output (Moore/Mealy), and the formal 5-tuple (Q, Σ, q0, F, δ).',
        itemCount: 48,
        topics: ['FSM Concepts', 'Alphabets & Strings', 'Powers of Sigma', 'Cardinality', 'Kleene Star', 'Moore & Mealy', 'FSM 5-Tuple'],
        quizPath: 'quizzes/atfl311/module2.html',
        downloads: {
          pdf: 'downloads/atfl311/Module 2 - Finite State Machines and Prerequisites - Questionnaire.pdf',
          docx: 'downloads/atfl311/Module 2 - Finite State Machines and Prerequisites - Questionnaire.docx',
          json: 'downloads/atfl311/ATFL311_Module_2_Quiz.json',
          md: 'downloads/atfl311/ATFL311_Module_2_Quiz.md'
        }
      },
      {
        id: 'atfl311-m3',
        number: 3,
        title: 'Deterministic Finite Automata (DFA)',
        description: 'Deterministic transition constraints, no ε-moves, DFA state design, prefix matching (strings starting with 0), exact length constraints (length 2), substring matching ("aabb"), state traps, and DFA complementation via state flipping.',
        itemCount: 41,
        topics: ['DFA Definition', 'Prefix Matching', 'Length Constraints', 'Substring Matching', 'DFA Complementation', 'State Inversion', 'Trap States'],
        quizPath: 'quizzes/atfl311/module3.html',
        downloads: {
          pdf: 'downloads/atfl311/Module 3 - Deterministic Finite Automata - Questionnaire.pdf',
          docx: 'downloads/atfl311/Module 3 - Deterministic Finite Automata - Questionnaire.docx',
          json: 'downloads/atfl311/ATFL311_Module_3_Quiz.json',
          md: 'downloads/atfl311/ATFL311_Module_3_Quiz.md'
        }
      },
      {
        id: 'atfl311-m4',
        number: 4,
        title: 'Non-Deterministic Finite Automata & Subset Construction',
        description: 'Non-deterministic state transitions, ε-transitions and ε-closure, dead configurations, DFA vs NFA equivalence, subset (powerset) construction algorithm, dead state handling, and NFA-to-DFA conversion proofs.',
        itemCount: 45,
        topics: ['NFA Definition', 'Epsilon Transitions', 'DFA vs NFA Equivalence', 'Subset Construction', 'Dead Configurations', 'Powerset Transitions', 'Activity 3 Problems'],
        quizPath: 'quizzes/atfl311/module4.html',
        downloads: {
          pdf: 'downloads/atfl311/Module 4 - Non-Deterministic Finite Automata - Questionnaire.pdf',
          docx: 'downloads/atfl311/Module 4 - Non-Deterministic Finite Automata - Questionnaire.docx',
          json: 'downloads/atfl311/ATFL311_Module_4_Quiz.json',
          md: 'downloads/atfl311/ATFL311_Module_4_Quiz.md'
        }
      }
    ]
  },
  {
    code: 'SEPC311',
    title: 'Social & Ethical Issues in Computing',
    subtitle: 'Ethical Theories, Professional Codes & Cyber Jurisprudence',
    description: 'Systematic study of moral philosophy, normative theories (relativism, egoism, consequentialism, Kantian deontology), Filipino IT Code of Ethics, ACM/AITP obligations, Ten Commandments of Computer Ethics, James Moor\'s policy vacuums, and digital privacy jurisprudence.',
    term: 'Year III — 1st Semester',
    category: 'core',
    status: 'active',
    accentColor: '#9c8c7d',
    tag: 'Ethics & Computing Law',
    modules: [
      {
        id: 'sepc311-m1',
        number: 1,
        title: 'Common Ethical Theories',
        description: 'Moral philosophy (ethos), Subjective and Cultural Relativism, Divine Command Theory, Ethical Egoism vs Altruism, Consequentialism (end justifies means), Kantian deontology (duty from pure reason), three branches of government, Article II Section 26 of Philippine Constitution, and applied moral dilemmas.',
        itemCount: 51,
        topics: ['Moral Philosophy', 'Subjective Relativism', 'Cultural Relativism', 'Divine Command Theory', 'Ethical Egoism', 'Consequentialism', 'Kantianism & Duty', 'Philippine Constitutional Ethics'],
        quizPath: 'quizzes/sepc311/module1.html',
        downloads: {
          pdf: 'downloads/sepc311/Module 1 - Common Ethical Theories - Questionnaire.pdf',
          docx: 'downloads/sepc311/Module 1 - Common Ethical Theories - Questionnaire.docx',
          json: 'downloads/sepc311/SEPC311_Module_1_Quiz.json',
          md: 'downloads/sepc311/SEPC311_Module_1_Quiz.md'
        }
      },
      {
        id: 'sepc311-m2',
        number: 2,
        title: 'Computer Ethics and Professional Codes',
        description: 'Professional codes of ethics (4 benefits), Code of Ethics of Filipino IT Professionals (10 tenets), AITP obligations (6 domains), ACM/IEEE Software Engineering Code (8 principles), Ten Commandments of Computer Ethics (CEI), Hacking Community Constitution (14 beliefs), James Moor\'s policy vacuums & 3 computer properties (Logical Malleability, Invisibility Factor), 3 levels of computer ethics (Pop, Para, Theoretical), and Philippine photo consent cyber jurisprudence.',
        itemCount: 55,
        topics: ['Professional Codes', 'Filipino IT Code of Ethics', 'AITP Obligations', 'ACM/IEEE Principles', 'Ten Commandments of Computer Ethics', 'Hacker Constitution', 'James Moor & Policy Vacuums', 'Logical Malleability & Invisibility', 'Levels of Computer Ethics', 'Philippine Cyber Jurisprudence'],
        quizPath: 'quizzes/sepc311/module2.html',
        downloads: {
          pdf: 'downloads/sepc311/Module 2 - Computer Ethics and Professional Codes - Questionnaire.pdf',
          docx: 'downloads/sepc311/Module 2 - Computer Ethics and Professional Codes - Questionnaire.docx',
          json: 'downloads/sepc311/SEPC311_Module_2_Quiz.json',
          md: 'downloads/sepc311/SEPC311_Module_2_Quiz.md'
        }
      }
    ]
  },
  {
    code: 'SFCR311',
    title: 'Systems Fundamentals & Cyber Risk',
    subtitle: 'Operating System Internals, Threat Analysis & Defense',
    description: 'Hardware-operating system interface, kernel abstractions, memory management, vulnerability assessment, threat modeling, and defensive cyber security paradigms.',
    term: 'Year III — 1st Semester',
    category: 'core',
    status: 'upcoming',
    accentColor: '#8a9a86',
    tag: 'Systems & Security',
    modules: []
  }
];

export const TOTAL_QUESTIONS = SUBJECTS.reduce(
  (total, s) => total + s.modules.reduce((mTotal, m) => mTotal + m.itemCount, 0),
  0
);

export const TOTAL_MODULES = SUBJECTS.reduce((total, s) => total + s.modules.length, 0);
