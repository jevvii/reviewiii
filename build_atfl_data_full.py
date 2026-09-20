import json

# Define the 4 modules for ATFL311: Automata Theory and Formal Languages

ATFL_MODULE_1_ITEMS = [
    # Topic 1: What is Automata & Theory of Computation
    {
        "q": "The foundational branch of computer science and mathematics that focuses on the study of abstract computing machines and the formal languages they recognize is ____ theory.",
        "a": "automata",
        "distractors": ["relational", "compiler", "cryptographic"],
        "topic": "Automata Theory Definition",
        "explanation": "Automata Theory is the foundational branch of computer science and mathematics focusing on abstract computing machines (automata) and the formal languages they recognize."
    },
    {
        "q": "Automata theory provides the theoretical foundation for understanding how computer software and hardware process inputs, perform step-by-step logic, and ____ problems.",
        "a": "solve",
        "distractors": ["compile", "randomize", "obfuscate"],
        "topic": "Purpose of Automata Theory",
        "explanation": "Automata theory explains the fundamental mechanisms of how computing systems process inputs, execute sequential algorithmic logic, and solve computational problems."
    },
    {
        "q": "In automata theory, theoretical computational models that operate according to predetermined rules and laws are referred to as ____ computing machines.",
        "a": "abstract",
        "distractors": ["biological", "quantum", "mechanical"],
        "topic": "Abstract Machines",
        "explanation": "Automata are abstract, idealized mathematical models of computing machines rather than physical electronic implementations."
    },
    {
        "q": "Automata theory is intimately connected to the study of ____ languages that abstract machines are capable of recognizing and generating.",
        "a": "formal",
        "distractors": ["natural", "spoken", "colloquial"],
        "topic": "Formal Languages",
        "explanation": "Formal languages (defined mathematically by precise grammatical rules) form the core input domains recognized by automata."
    },

    # Topic 2: 20th Century Historical Pioneers
    {
        "q": "In 1936, the British mathematician who introduced an abstract mathematical model of computation that proved an elementary machine could perform any mathematical computation was Alan ____.",
        "a": "Turing",
        "distractors": ["McCulloch", "Pitts", "Moore"],
        "topic": "Alan Turing (1936)",
        "explanation": "Alan Turing introduced the Turing Machine in 1936, demonstrating that a simple machine manipulating symbols on a tape could perform any algorithmic computation."
    },
    {
        "q": "The abstract mathematical model of computation introduced by Alan Turing in 1936 that laid the logical foundation for modern software and hardware is the ____ Machine.",
        "a": "Turing",
        "distractors": ["Mealy", "Moore", "McCulloch"],
        "topic": "Turing Machine",
        "explanation": "The Turing Machine serves as the fundamental theoretical model of universal general-purpose computers."
    },
    {
        "q": "Alan Turing proved that an elementary machine could perform any possible mathematical computation, establishing the logical foundation for modern ____ and software.",
        "a": "hardware",
        "distractors": ["cryptography", "transducers", "circuits"],
        "topic": "Turing Machine Impact",
        "explanation": "Turing's universal computation model established the universal architecture that underlies all modern computer hardware and software design."
    },
    {
        "q": "In 1943, a mathematical model of biological neurons showing that networks of simple logical gates could compute any logical function was introduced by Walter Pitts and Warren ____.",
        "a": "McCulloch",
        "distractors": ["Turing", "Mealy", "Chomsky"],
        "topic": "McCulloch and Pitts (1943)",
        "explanation": "Warren McCulloch and Walter Pitts (1943) modeled biological neural networks using threshold logic units, establishing a mathematical basis for computational neural networks."
    },
    {
        "q": "The 1943 pioneering work on threshold logic units and artificial biological neurons by McCulloch and Pitts directly inspired the invention of ____ State Machines.",
        "a": "Finite",
        "distractors": ["Pushdown", "Infinite", "Turing"],
        "topic": "Inspiration for Finite State Machines",
        "explanation": "McCulloch and Pitts's neural network logic demonstrated that networks of states and transitions could perform logical decisions, directly inspiring Finite State Machines (FSMs)."
    },
    {
        "q": "McCulloch and Pitts were by profession ____ who applied mathematical modeling to understand brain function and logic computation.",
        "a": "neurophysiologists",
        "distractors": ["mechanical engineers", "astronomers", "quantum physicists"],
        "topic": "McCulloch and Pitts Profession",
        "explanation": "Warren McCulloch and Walter Pitts were neurophysiologists who combined neurophysiology with symbolic mathematical logic."
    },
    {
        "q": "In 1955–1956, the two primary structural models of finite-state transducers (machines with output) were formalized by Edward F. Moore and George H. ____.",
        "a": "Mealy",
        "distractors": ["Turing", "Pitts", "McCulloch"],
        "topic": "Mealy and Moore (1955–1956)",
        "explanation": "George H. Mealy (1955) and Edward F. Moore (1956) developed Mealy machines and Moore machines, the foundational finite-state transducer models."
    },
    {
        "q": "Finite-state machines equipped with output capabilities, as formalized by Mealy and Moore, are scientifically known as finite-state ____.",
        "a": "transducers",
        "distractors": ["acceptors", "parsers", "recognizers"],
        "topic": "Finite State Transducers",
        "explanation": "Finite automata that generate output sequences in response to input sequences are termed transducers (e.g., Mealy and Moore machines)."
    },
    {
        "q": "The structural transducer models developed by Mealy and Moore in the mid-1950s remain fundamental today in the design of digital ____.",
        "a": "circuits",
        "distractors": ["compilers", "operating systems", "relational databases"],
        "topic": "Digital Circuit Design",
        "explanation": "Mealy and Moore models are the industry standard architectural patterns used in synchronous sequential digital circuit design (VLSI, FPGA, microcontrollers)."
    },

    # Topic 3: The Chomsky Hierarchy of Automata
    {
        "q": "In the Chomsky Hierarchy, the simplest machine model that recognizes Regular Languages without requiring external memory is the ____ Automaton.",
        "a": "Finite",
        "distractors": ["Pushdown", "Linear Bounded", "Turing"],
        "topic": "Chomsky Hierarchy: Finite Automata",
        "explanation": "Finite Automata (FA/FSM) recognize Type-3 Regular Languages and possess no auxiliary memory beyond their internal states."
    },
    {
        "q": "Finite Automata have no auxiliary memory storage and rely strictly on their finite set of internal ____ to process input.",
        "a": "states",
        "distractors": ["stacks", "tapes", "registers"],
        "topic": "Finite Automata Memory Type",
        "explanation": "Finite Automata possess 'None (States only)' memory type—they can only remember what state they currently occupy."
    },
    {
        "q": "According to the Chomsky Hierarchy, Finite Automata correspond to the language class known as ____ Languages.",
        "a": "Regular",
        "distractors": ["Context-Free", "Context-Sensitive", "Unrestricted"],
        "topic": "Regular Languages",
        "explanation": "Regular Languages are the simplest language class in the Chomsky hierarchy, recognized precisely by Finite Automata."
    },
    {
        "q": "Real-world computational examples of Finite Automata applications include text search and ____ expressions.",
        "a": "regular",
        "distractors": ["algebraic", "differential", "boolean"],
        "topic": "Regular Expressions Application",
        "explanation": "Regular expressions and pattern matching engines in text editors and command-line search tools are direct implementations of Finite Automata."
    },
    {
        "q": "The machine model in the Chomsky Hierarchy that recognizes Context-Free Languages by utilizing an auxiliary Stack memory is the ____ Automaton.",
        "a": "Pushdown",
        "distractors": ["Finite", "Linear Bounded", "Turing"],
        "topic": "Pushdown Automata (PDA)",
        "explanation": "Pushdown Automata (PDA) augment finite control with a Last-In First-Out (LIFO) stack memory to recognize Context-Free Languages (Type-2)."
    },
    {
        "q": "Pushdown Automata (PDA) utilize an auxiliary memory structure organized specifically as a ____.",
        "a": "stack",
        "distractors": ["queue", "bounded tape", "infinite grid"],
        "topic": "PDA Memory Type",
        "explanation": "Pushdown Automata use stack memory, allowing push and pop operations to handle nested syntactic structures."
    },
    {
        "q": "Pushdown Automata are used in compiler construction to parse programming language ____ and matching nested parentheses.",
        "a": "syntax",
        "distractors": ["tokens", "semantics", "binaries"],
        "topic": "Programming Language Syntax",
        "explanation": "Programming language syntax parsing (CFG parsing) relies on Pushdown Automata to validate nested constructs like parentheses, braces, and function calls."
    },
    {
        "q": "The machine model that recognizes Context-Sensitive Languages and utilizes a memory tape constrained to the length of the input is the ____ Bounded Automaton.",
        "a": "Linear",
        "distractors": ["Pushdown", "Finite", "Infinite"],
        "topic": "Linear Bounded Automata (LBA)",
        "explanation": "Linear Bounded Automata (LBA) are non-deterministic Turing machines whose tape is bounded by a constant multiple of the input length."
    },
    {
        "q": "Linear Bounded Automata (LBA) possess a memory type classified as a ____ tape.",
        "a": "bounded",
        "distractors": ["infinite", "stack", "circular"],
        "topic": "LBA Memory Type",
        "explanation": "An LBA uses a bounded tape whose usable length cannot exceed a linear function of the input string length."
    },
    {
        "q": "Linear Bounded Automata recognize Context-Sensitive Languages, which in real-world computer science model advanced ____ structures.",
        "a": "linguistic",
        "distractors": ["arithmetic", "network", "microprocessor"],
        "topic": "Advanced Linguistic Structures",
        "explanation": "Context-sensitive grammars and LBAs are used to model complex linguistic syntax and natural language semantic agreements."
    },
    {
        "q": "The most powerful machine model in the Chomsky Hierarchy, capable of recognizing Unrestricted Languages using an infinite tape, is the ____ Machine.",
        "a": "Turing",
        "distractors": ["Pushdown", "Mealy", "Moore"],
        "topic": "Turing Machine Hierarchy",
        "explanation": "Turing Machines recognize Unrestricted (Recursively Enumerable) Languages (Type-0) and possess infinite computational capacity."
    },
    {
        "q": "The memory type associated with a Turing Machine is an ____ tape.",
        "a": "infinite",
        "distractors": ["stack", "bounded", "state-only"],
        "topic": "Turing Machine Memory Type",
        "explanation": "A Turing machine has access to an unbounded, infinite tape divided into discrete cells that can be read and written in both directions."
    },
    {
        "q": "Turing Machines provide the mathematical and theoretical model for modern programmable ____.",
        "a": "computers",
        "distractors": ["switches", "cables", "sensors"],
        "topic": "Modern Programmable Computers",
        "explanation": "All modern general-purpose digital computers (laptops, servers, supercomputers) are Turing-equivalent in computational power (Church-Turing thesis)."
    },

    # Topic 4: Real-World Applications of Automata
    {
        "q": "Municipal traffic intersection systems utilize Finite State Machines to safely switch between red, yellow, and green states based on timers or ____.",
        "a": "sensors",
        "distractors": ["compilers", "tapes", "parsers"],
        "topic": "Traffic Light Controllers",
        "explanation": "Traffic light controllers use FSMs where inputs from vehicle road sensors or countdown timers trigger deterministic state transitions between signal colors."
    },
    {
        "q": "The control logic of a commercial vending machine relies on state transitions to track inserted coins, selected items, and ____ actions.",
        "a": "dispensing",
        "distractors": ["compiling", "encrypting", "routing"],
        "topic": "Vending Machines",
        "explanation": "Vending machines model credit accumulation and item selection through state transitions, entering a dispensing state once sufficient funds are reached."
    },
    {
        "q": "In software development, search utilities (like grep) and code editors use finite automata to find patterns and match strings via Regular Expression ____.",
        "a": "Engines",
        "distractors": ["Parsers", "Compilers", "Transducers"],
        "topic": "Regex Engines",
        "explanation": "Regular Expression Engines convert regex patterns into DFAs or NFAs to scan text at high throughput ($O(n)$ time complexity)."
    },
    {
        "q": "In compiler design, lexical analyzers (scanners) use Finite Automata to break down source code characters into ____.",
        "a": "tokens",
        "distractors": ["parse trees", "opcodes", "registers"],
        "topic": "Lexical Analysis",
        "explanation": "Lexical analyzers (such as Lex or Flex) convert stream of source characters into syntactic tokens (keywords, identifiers, numbers) using Finite Automata."
    },
    {
        "q": "While lexical analyzers rely on Finite Automata, compiler syntax parsers rely on Pushdown Automata to handle syntax parsing and nested ____.",
        "a": "parentheses",
        "distractors": ["tokens", "identifiers", "keywords"],
        "topic": "Syntax Parsing & Nested Parentheses",
        "explanation": "Finite automata cannot count arbitrarily nested parentheses or brackets; a pushdown automaton with a stack is required for syntax parsing."
    },
    {
        "q": "Communication network protocols like TCP connection establishment and TLS security handshakes use state machines to validate packet delivery and message ____.",
        "a": "sequences",
        "distractors": ["voltages", "frequencies", "amplitudes"],
        "topic": "Network Protocols & Security Handshakes",
        "explanation": "TCP (SYN, SYN-ACK, ESTABLISHED, FIN-WAIT) and TLS handshakes use formal state machines to enforce strict chronological message sequences."
    },
    {
        "q": "In Natural Language Processing (NLP), spell checkers, tokenizers, and grammar validators use automata to analyze word structures and parse ____.",
        "a": "sentences",
        "distractors": ["microchips", "circuits", "voltages"],
        "topic": "Natural Language Processing (NLP)",
        "explanation": "NLP pipelines use morphological finite-state transducers to parse prefixes/suffixes and automata to segment sentences and validate grammatical agreements."
    },
    {
        "q": "In game development and robotics, autonomous robot movement controls and non-player character (NPC) behavior trees are modeled using state ____.",
        "a": "transitions",
        "distractors": ["compilations", "permutations", "syntheses"],
        "topic": "Robotics & Game AI",
        "explanation": "Game AI agents switch behaviors (e.g., Idle, Patrol, Chase, Attack) using state transitions governed by environmental perception."
    },
    {
        "q": "An elementary computing unit in Automata Theory that can take inputs, change its internal state, and produce an accept/reject decision is called an ____.",
        "a": "automaton",
        "distractors": ["algorithm", "arithmetic logic unit", "operating system"],
        "topic": "Automaton Concept",
        "explanation": "An automaton (plural: automata) is a self-operating mathematical model that processes a sequence of inputs to determine language membership."
    },
    {
        "q": "The plural form of the word 'automaton' is ____.",
        "a": "automata",
        "distractors": ["automatons", "automataes", "automatics"],
        "topic": "Automata Terminology",
        "explanation": "The correct Greek-derived plural of automaton is automata."
    },
    {
        "q": "In the Chomsky Hierarchy, language classes are arranged in a strict ____ where each inner language class is a subset of the outer class.",
        "a": "hierarchy",
        "distractors": ["randomness", "divergence", "contradiction"],
        "topic": "Hierarchy Structure",
        "explanation": "The Chomsky Hierarchy is nested: Regular Languages ⊂ Context-Free Languages ⊂ Context-Sensitive Languages ⊂ Unrestricted Languages."
    },
    {
        "q": "Which Chomsky Hierarchy machine model corresponds to Context-Free Languages?",
        "a": "Pushdown Automata",
        "distractors": ["Finite Automata", "Linear Bounded Automata", "Turing Machine"],
        "topic": "PDA to Context-Free Mapping",
        "explanation": "Pushdown Automata (PDA) are the exact theoretical computational model that accepts all Context-Free Languages."
    },
    {
        "q": "Which Chomsky Hierarchy machine model corresponds to Context-Sensitive Languages?",
        "a": "Linear Bounded Automata",
        "distractors": ["Finite Automata", "Pushdown Automata", "Moore Machine"],
        "topic": "LBA to Context-Sensitive Mapping",
        "explanation": "Linear Bounded Automata (LBA) are the machine model corresponding to Type-1 Context-Sensitive Languages."
    },
    {
        "q": "Which Chomsky Hierarchy machine model corresponds to Unrestricted (Recursively Enumerable) Languages?",
        "a": "Turing Machine",
        "distractors": ["Finite Automata", "Pushdown Automata", "Linear Bounded Automata"],
        "topic": "Turing Machine to Unrestricted Mapping",
        "explanation": "Turing Machines accept Type-0 Unrestricted Languages."
    }
]

print(f"ATFL Module 1 items: {len(ATFL_MODULE_1_ITEMS)}")

ATFL_MODULE_2_ITEMS = [
    # Topic 1: What is Finite State Machine (FSM)?
    {
        "q": "A computational model that is in exactly one state at any given time, transitioning to a new state based on an incoming input, is a ____ State Machine.",
        "a": "Finite",
        "distractors": ["Turing", "Infinite", "Pushdown"],
        "topic": "Finite State Machine Definition",
        "explanation": "A Finite State Machine (FSM) is a model of computation that is in exactly one state at any given time and changes state in response to inputs."
    },
    {
        "q": "In a Finite State Machine, the property of being in ____ state at any given moment distinguishes its operation.",
        "a": "exactly one",
        "distractors": ["every", "multiple parallel", "zero"],
        "topic": "FSM State Exclusivity",
        "explanation": "At any discrete computational time step, a standard FSM occupies exactly one active state."
    },
    {
        "q": "A Finite State Machine changes from its current state to a subsequent state based on an incoming ____.",
        "a": "input",
        "distractors": ["power surge", "stack overflow", "memory dump"],
        "topic": "State Transitions",
        "explanation": "State transitions in an FSM are triggered deterministically or non-deterministically by input symbols provided to the machine."
    },

    # Topic 2: FSM Prerequisites (Symbol, Alphabet, String, Language)
    {
        "q": "In formal language theory, an indivisible, atomic unit such as a character or digit (e.g., 'a', 'b', '0', '1') is defined as a ____.",
        "a": "symbol",
        "distractors": ["string", "language", "grammar"],
        "topic": "Symbol Definition",
        "explanation": "A symbol is an atomic, fundamental entity (letter, digit, or punctuation) that cannot be broken down further."
    },
    {
        "q": "A finite, non-empty set of symbols is called an ____ and is standardly denoted by the Greek capital letter Sigma (Σ).",
        "a": "alphabet",
        "distractors": ["language", "automaton", "transducer"],
        "topic": "Alphabet Definition",
        "explanation": "An alphabet (Σ) is defined as any finite, non-empty set of symbols (e.g., Σ = {0, 1} or Σ = {a, b})."
    },
    {
        "q": "The standard Greek letter used in theoretical computer science to represent an alphabet of symbols is ____.",
        "a": "Sigma (Σ)",
        "distractors": ["Delta (δ)", "Lambda (λ)", "Epsilon (ε)"],
        "topic": "Alphabet Notation",
        "explanation": "The capital Greek letter Sigma (Σ) is standardly used to denote the input alphabet in automata theory."
    },
    {
        "q": "A finite sequence formed by concatenating symbols chosen from an alphabet is called a ____.",
        "a": "string",
        "distractors": ["cardinality", "language", "symbol"],
        "topic": "String Definition",
        "explanation": "A string (or word) is a finite sequence of symbols chosen from a designated alphabet (e.g., '01', 'abb', '1101')."
    },
    {
        "q": "In formal language theory, a collection or set of strings formed over an alphabet Σ is defined as a ____.",
        "a": "language",
        "distractors": ["grammar", "symbol", "transducer"],
        "topic": "Language Definition",
        "explanation": "A formal language L is mathematically defined as a set of strings over an alphabet Σ (i.e., L ⊆ Σ*)."
    },
    {
        "q": "If alphabet Σ = {a, b}, the language L1 containing all strings of length exactly 2 consists of ____ strings.",
        "a": "4",
        "distractors": ["2", "8", "16"],
        "topic": "Language of Length 2",
        "explanation": "For Σ = {a, b}, the strings of length 2 are {aa, ab, ba, bb}, yielding a total of 2^2 = 4 strings."
    },
    {
        "q": "If alphabet Σ = {a, b}, which of the following represents the complete set of strings of length 2?",
        "a": "{aa, ab, ba, bb}",
        "distractors": ["{a, b}", "{aaa, aab, aba, abb}", "{a, b, ab, ba}"],
        "topic": "Strings of Length 2 Set",
        "explanation": "The set of all strings of length 2 over {a, b} is {aa, ab, ba, bb}."
    },
    {
        "q": "If alphabet Σ = {a, b}, the language L2 consisting of all strings of length exactly 3 contains a total of ____ strings.",
        "a": "8",
        "distractors": ["3", "6", "9"],
        "topic": "Language of Length 3",
        "explanation": "For an alphabet of size 2, the number of strings of length 3 is 2^3 = 8."
    },
    {
        "q": "If alphabet Σ = {a, b}, which of the following strings belongs to the language L3 defined as 'Set of all strings that begin with a'?",
        "a": "abb",
        "distractors": ["baa", "bba", "bbb"],
        "topic": "Prefix Language Membership",
        "explanation": "The string 'abb' begins with the symbol 'a', satisfying the language condition L3."
    },

    # Topic 3: Power of Sigma (Σ^n) & Empty String (ε)
    {
        "q": "The special symbol representing the empty string (a string with a length of zero containing no symbols) is ____.",
        "a": "Epsilon (ε)",
        "distractors": ["Sigma (Σ)", "Delta (δ)", "Phi (ϕ)"],
        "topic": "Empty String Epsilon",
        "explanation": "Epsilon (ε) standardly denotes the empty string, which has a length of zero (|ε| = 0)."
    },
    {
        "q": "In the powers of alphabet notation, Σ^0 represents the set of all strings of length 0, which is equal to ____.",
        "a": "{ ε }",
        "distractors": ["{ 0 }", "ϕ (empty set)", "{ 0, 1 }"],
        "topic": "Sigma Power 0",
        "explanation": "Σ^0 contains exactly one string—the string of length zero, denoted as { ε }."
    },
    {
        "q": "For the binary alphabet Σ = {0, 1}, Σ^1 represents the set of all strings of length 1, which is ____.",
        "a": "{ 0, 1 }",
        "distractors": ["{ ε }", "{ 00, 11 }", "{ 01, 10 }"],
        "topic": "Sigma Power 1",
        "explanation": "Σ^1 consists of all single-symbol strings over {0, 1}, which is {0, 1}."
    },
    {
        "q": "For the binary alphabet Σ = {0, 1}, Σ^2 represents the set of all strings of length 2, which is ____.",
        "a": "{ 00, 01, 10, 11 }",
        "distractors": ["{ 0, 1 }", "{ 000, 111 }", "{ ε, 01 }"],
        "topic": "Sigma Power 2",
        "explanation": "Σ^2 consists of {00, 01, 10, 11}."
    },
    {
        "q": "For the binary alphabet Σ = {0, 1}, Σ^3 represents the set of all strings of length 3, containing ____ distinct strings.",
        "a": "8",
        "distractors": ["6", "4", "16"],
        "topic": "Sigma Power 3 Count",
        "explanation": "Σ^3 contains 2^3 = 8 binary strings: {000, 001, 010, 011, 100, 101, 110, 111}."
    },
    {
        "q": "In general formal automata notation, Σ^n represents the set of all strings of length ____ over alphabet Σ.",
        "a": "n",
        "distractors": ["n - 1", "2n", "n^2"],
        "topic": "Sigma Power n",
        "explanation": "Σ^n is the set of all strings of length n formed from the symbols in alphabet Σ."
    },

    # Topic 4: Cardinality
    {
        "q": "The total number of elements contained in a set is defined in mathematics and automata theory as the set's ____.",
        "a": "cardinality",
        "distractors": ["permutation", "closure", "transition"],
        "topic": "Cardinality Definition",
        "explanation": "Cardinality (denoted |S| or C) is the measure of the number of elements in a set."
    },
    {
        "q": "For a binary alphabet Σ = {0, 1}, the cardinality of Σ^1 is ____.",
        "a": "2",
        "distractors": ["1", "4", "0"],
        "topic": "Cardinality of Sigma 1",
        "explanation": "Σ^1 = {0, 1}, which has a cardinality of 2 elements (2^1 = 2)."
    },
    {
        "q": "For a binary alphabet Σ = {0, 1}, the cardinality of Σ^2 is ____.",
        "a": "4",
        "distractors": ["2", "8", "6"],
        "topic": "Cardinality of Sigma 2",
        "explanation": "Σ^2 = {00, 01, 10, 11}, which has a cardinality of 4 elements (2^2 = 4)."
    },
    {
        "q": "For a binary alphabet Σ = {0, 1}, the cardinality of Σ^3 is ____.",
        "a": "8",
        "distractors": ["6", "12", "16"],
        "topic": "Cardinality of Sigma 3",
        "explanation": "Σ^3 has 2^3 = 8 elements."
    },
    {
        "q": "For any binary alphabet Σ = {0, 1}, the mathematical formula for the cardinality of Σ^n is ____.",
        "a": "2^n",
        "distractors": ["n^2", "2n", "n!"],
        "topic": "Binary Cardinality Formula",
        "explanation": "Since each position in a string of length n has 2 possible binary choices, the total number of strings is 2^n."
    },
    {
        "q": "If an alphabet has 3 symbols (such as Σ = {a, b, c}), the cardinality of Σ^2 is ____.",
        "a": "9",
        "distractors": ["6", "8", "27"],
        "topic": "Ternary Alphabet Cardinality",
        "explanation": "For an alphabet of size k, the number of strings of length n is k^n. Here 3^2 = 9."
    },

    # Topic 5: Kleene Star (*) & Kleene Plus
    {
        "q": "The unary operator that represents the infinite union of all powers of an alphabet (Σ^0 U Σ^1 U Σ^2 U ...) is the ____ star.",
        "a": "Kleene",
        "distractors": ["Chomsky", "Turing", "Moore"],
        "topic": "Kleene Star Definition",
        "explanation": "The Kleene star (denoted Σ*) is the operation that forms the set of all possible strings of all finite lengths over Σ, including ε."
    },
    {
        "q": "The Kleene closure of an alphabet Σ, denoted Σ*, always contains the ____ string.",
        "a": "empty",
        "distractors": ["infinite", "negative", "undefined"],
        "topic": "Kleene Star Contains Epsilon",
        "explanation": "Because Σ* includes Σ^0, it always contains the empty string ε."
    },
    {
        "q": "For alphabet Σ = {0, 1}, the language defined by Σ* represents the set of all possible strings of ____ lengths over {0, 1}.",
        "a": "all",
        "distractors": ["even", "odd", "prime"],
        "topic": "Universal String Set",
        "explanation": "Σ* is the universal set of all finite strings constructible from the alphabet."
    },
    {
        "q": "The Kleene star operation on an alphabet Σ produces a set that is ____ in size.",
        "a": "countably infinite",
        "distractors": ["strictly finite", "empty", "uncountable"],
        "topic": "Infinite Nature of Kleene Star",
        "explanation": "Although each individual string in Σ* is finite in length, the set Σ* itself contains an infinite number of strings."
    },

    # Topic 6: Branches of Finite Automata
    {
        "q": "Finite Automata are primarily divided into two main branches: FA without output and FA ____ output.",
        "a": "with",
        "distractors": ["against", "rejecting", "beyond"],
        "topic": "Branches of Finite Automata",
        "explanation": "Finite Automata divide into FA with output (transducers) and FA without output (acceptors/recognizers)."
    },
    {
        "q": "Finite Automata with output include the Mealy Machine and the ____ Machine.",
        "a": "Moore",
        "distractors": ["Turing", "Pushdown", "Chomsky"],
        "topic": "Moore and Mealy Machines",
        "explanation": "The two primary finite-state machines with output are Moore machines and Mealy machines."
    },
    {
        "q": "In a Moore Machine, the output generated by the automaton depends exclusively on the ____.",
        "a": "current state",
        "distractors": ["current input symbol", "tape head position", "stack depth"],
        "topic": "Moore Machine Output Logic",
        "explanation": "In a Moore machine, output values are determined solely by the current state."
    },
    {
        "q": "In a Mealy Machine, the output depends on both the current state and the ____.",
        "a": "current input symbol",
        "distractors": ["initial state", "stack pointer", "memory bus"],
        "topic": "Mealy Machine Output Logic",
        "explanation": "In a Mealy machine, output values are determined by both the current state and the current input symbol."
    },
    {
        "q": "Which of the following is categorized as a Finite Automaton WITHOUT output (an acceptor/language recognizer)?",
        "a": "DFA",
        "distractors": ["Moore Machine", "Mealy Machine", "Transducer"],
        "topic": "FA Without Output Category",
        "explanation": "DFAs, NFAs, and ε-NFAs are language recognizers (acceptors) that do not generate output sequences beyond accepting or rejecting."
    },
    {
        "q": "The three standard variants of Finite Automata without output are DFA, NFA, and ____-NFA.",
        "a": "ε (Epsilon)",
        "distractors": ["Σ (Sigma)", "δ (Delta)", "Q"],
        "topic": "Three FA Acceptor Types",
        "explanation": "The three non-output finite automata are Deterministic (DFA), Non-deterministic (NFA), and NFA with Epsilon transitions (ε-NFA)."
    },

    # Topic 7: Finite State Machine 5 Variables (5-Tuple Formal Definition)
    {
        "q": "A Finite State Machine is formally defined by how many mathematical components (tuple variables)?",
        "a": "5",
        "distractors": ["3", "4", "7"],
        "topic": "5-Tuple Definition",
        "explanation": "Both DFAs and NFAs are formally defined as 5-tuples: (Q, Σ, q0, F, δ)."
    },
    {
        "q": "In the formal 5-tuple definition of an FSM, the variable Q represents the finite set of all ____.",
        "a": "states",
        "distractors": ["inputs", "outputs", "transitions"],
        "topic": "Variable Q: States",
        "explanation": "Q represents the finite non-empty set of internal states of the machine."
    },
    {
        "q": "In the formal 5-tuple definition of an FSM, the symbol Σ represents the set of all ____.",
        "a": "inputs (alphabet)",
        "distractors": ["final states", "transition rules", "state registers"],
        "topic": "Variable Sigma: Alphabet",
        "explanation": "Σ represents the finite input alphabet."
    },
    {
        "q": "In the formal 5-tuple definition of an FSM, q0 denotes the unique ____ state.",
        "a": "start (initial)",
        "distractors": ["final", "trap", "dead"],
        "topic": "Variable q0: Start State",
        "explanation": "q0 ∈ Q represents the initial state where computation begins."
    },
    {
        "q": "In the formal 5-tuple definition of an FSM, F represents the set of all ____ states.",
        "a": "final (accepting)",
        "distractors": ["initial", "intermediate", "rejected"],
        "topic": "Variable F: Final States",
        "explanation": "F ⊆ Q represents the set of accept or final states."
    },
    {
        "q": "In state transition diagrams, an accepting or final state is graphically depicted using a ____ circle.",
        "a": "double",
        "distractors": ["dotted", "filled black", "triangular"],
        "topic": "Double Circle Graphical Notation",
        "explanation": "In standard automata transition diagrams, accepting/final states are indicated by concentric double circles."
    },
    {
        "q": "In state transition diagrams, the start state is graphically indicated by an incoming arrow from ____.",
        "a": "nowhere (outside)",
        "distractors": ["the final state", "the trap state", "a double circle"],
        "topic": "Start State Arrow Notation",
        "explanation": "The initial start state is distinguished by an unlabelled arrow entering it from outside the graph."
    },
    {
        "q": "In the formal 5-tuple definition of an FSM, the transition function mapping state-input pairs to a next state is represented by the Greek letter ____.",
        "a": "Delta (δ)",
        "distractors": ["Sigma (Σ)", "Epsilon (ε)", "Theta (θ)"],
        "topic": "Transition Function Delta (δ)",
        "explanation": "The lowercase Greek letter Delta (δ) standardly designates the state transition function."
    },
    {
        "q": "For a DFA, the mathematical domain and co-domain of the transition function δ is ____.",
        "a": "Q x Σ -> Q",
        "distractors": ["Q x Q -> Σ", "Σ x Σ -> Q", "Q x (Σ U {ε}) -> 2^Q"],
        "topic": "DFA Transition Function Signature",
        "explanation": "For a DFA, δ maps a state and an input symbol deterministically to exactly one state: δ: Q x Σ -> Q."
    },

    # Topic 8: Slide 8 Machine Analysis
    {
        "q": "In the Week 2 Slide 8 FSM diagram with states {A, B, C, D}, start state A, and final state D, what is the destination state from state A on input '0'?",
        "a": "C",
        "distractors": ["B", "D", "A"],
        "topic": "Slide 8 Transition from A on 0",
        "explanation": "In the Slide 8 transition diagram, the transition from state A labeled with 0 points directly down to state C."
    },
    {
        "q": "In the Week 2 Slide 8 FSM diagram, what is the destination state from state A on input '1'?",
        "a": "B",
        "distractors": ["C", "D", "A"],
        "topic": "Slide 8 Transition from A on 1",
        "explanation": "In the Slide 8 transition diagram, the horizontal transition from state A labeled with 1 points to state B."
    },
    {
        "q": "In the Week 2 Slide 8 FSM diagram, transitioning from state B on input '0' leads directly to state ____.",
        "a": "D",
        "distractors": ["A", "C", "B"],
        "topic": "Slide 8 Transition from B on 0",
        "explanation": "In the Slide 8 transition diagram, state B on input 0 transitions to state D."
    },
    {
        "q": "In the Week 2 Slide 8 FSM diagram, transitioning from state C on input '1' leads directly to state ____.",
        "a": "D",
        "distractors": ["A", "B", "C"],
        "topic": "Slide 8 Transition from C on 1",
        "explanation": "In the Slide 8 transition diagram, state C on input 1 transitions to state D."
    },
    {
        "q": "In the Week 2 Slide 8 FSM diagram, if the machine receives the input string '01' starting at state A, the machine terminates in state ____.",
        "a": "D (Accepting)",
        "distractors": ["B (Non-accepting)", "C (Non-accepting)", "A (Non-accepting)"],
        "topic": "Slide 8 String Trace '01'",
        "explanation": "From A, on 0 the machine moves to C. From C, on 1 the machine moves to D. Since D is a final state, string '01' is accepted."
    }
]

print(f"ATFL Module 2 items: {len(ATFL_MODULE_2_ITEMS)}")

ATFL_MODULE_3_ITEMS = [
    # Topic 1: Deterministic Finite Automata (DFA) Definition & Principles
    {
        "q": "A finite state machine where for every state and for every input symbol there is exactly one unique next state, with no empty transitions allowed, is a ____ Finite Automaton.",
        "a": "Deterministic",
        "distractors": ["Non-Deterministic", "Pushdown", "Linear Bounded"],
        "topic": "DFA Core Definition",
        "explanation": "In a Deterministic Finite Automaton (DFA), the transition function is deterministic—for each state and input symbol, there is exactly one specified next state."
    },
    {
        "q": "A fundamental rule of Deterministic Finite Automata is that empty moves (transitions without consuming an input symbol, known as ε-moves) are ____.",
        "a": "strictly prohibited (not allowed)",
        "distractors": ["required at every state", "optional in final states", "unrestricted"],
        "topic": "No Epsilon Moves in DFA",
        "explanation": "DFAs never permit empty ε-transitions; every transition must consume exactly one symbol from the input alphabet."
    },
    {
        "q": "Because a DFA has exactly one transition for each (state, symbol) pair, the computational path for any given input string is completely ____.",
        "a": "unique and predictable",
        "distractors": ["random", "branching into parallel universes", "probabilistic"],
        "topic": "Deterministic Execution",
        "explanation": "Given an initial state and input string, a DFA follows a single, unambiguous sequence of state transitions."
    },
    {
        "q": "A non-accepting state in a DFA from which the machine can never escape, looping on all input symbols, is known as a dead state or ____ state.",
        "a": "trap",
        "distractors": ["initial", "transducer", "subordinate"],
        "topic": "Trap / Dead State Concept",
        "explanation": "A dead state (or trap state) is an absorbing non-final state where all outgoing transitions loop back to itself, ensuring rejection of the string."
    },

    # Topic 2: DFA Example 1: Strings Starting with '0'
    {
        "q": "In the DFA that accepts all strings starting with '0' over Σ = {0, 1} (Example 1), what happens when the first symbol read from start state A is '0'?",
        "a": "The machine transitions to accepting state B",
        "distractors": ["The machine enters trap state C", "The machine halts and rejects", "The machine resets to state A"],
        "topic": "Strings Starting with '0' Acceptance",
        "explanation": "In Example 1, on input '0' from start state A, the machine moves to state B (double circle), which is accepting."
    },
    {
        "q": "In the DFA for strings starting with '0' (Example 1), what happens when the first symbol read from start state A is '1'?",
        "a": "The machine transitions to dead/trap state C",
        "distractors": ["The machine transitions to accepting state B", "The machine loops at state A", "The machine produces an output token"],
        "topic": "Strings Starting with '0' Rejection",
        "explanation": "Any string beginning with '1' violates the condition and is routed immediately to trap state C, where it remains."
    },
    {
        "q": "In the DFA for strings starting with '0' (Example 1), once the machine reaches accepting state B, what are its transitions on inputs 0 and 1?",
        "a": "It loops on state B for both 0 and 1",
        "distractors": ["It transitions to state C on 1", "It returns to start state A on 0", "It halts immediately"],
        "topic": "State B Self-Loop",
        "explanation": "Once a string is confirmed to start with '0', any subsequent symbols (0 or 1) do not change the fact that it started with '0', so state B loops on 0,1."
    },
    {
        "q": "How many total states are required in the minimal DFA for the language L = {strings starting with '0'} over alphabet Σ = {0, 1}?",
        "a": "3 states (Start A, Final B, Trap C)",
        "distractors": ["2 states", "4 states", "5 states"],
        "topic": "State Count for Prefix Language",
        "explanation": "The minimal DFA requires exactly 3 states: A (start), B (accepting), and C (trap state for strings starting with 1)."
    },

    # Topic 3: DFA Example 2: Strings of Exact Length 2
    {
        "q": "In DFA Example 2, the language consists of all strings over Σ = {0, 1} of length exactly 2. How many strings are in this language?",
        "a": "4 strings ({00, 01, 10, 11})",
        "distractors": ["2 strings", "8 strings", "16 strings"],
        "topic": "Length 2 Language Cardinality",
        "explanation": "Over Σ = {0, 1}, the strings of length 2 are 00, 01, 10, and 11, giving a cardinality of 4."
    },
    {
        "q": "In the DFA for strings of exact length 2 (Example 2), state C represents having consumed a string of length ____.",
        "a": "2",
        "distractors": ["0", "1", "3"],
        "topic": "Length 2 Accepting State",
        "explanation": "State A represents length 0, state B represents length 1, and state C represents length 2 (accepting)."
    },
    {
        "q": "In the DFA for strings of exact length 2 (Example 2), which state is the ONLY accepting / final state?",
        "a": "State C",
        "distractors": ["State A", "State B", "State D"],
        "topic": "Exact Length 2 Final State",
        "explanation": "State C is the only state designated with a double circle, representing acceptance of strings with length exactly 2."
    },
    {
        "q": "In the DFA for strings of exact length 2 (Example 2), what happens if a third symbol is read after reaching state C?",
        "a": "The machine transitions to dead/trap state D",
        "distractors": ["The machine remains in state C", "The machine resets to state A", "The machine accepts"],
        "topic": "Exceeding Length 2",
        "explanation": "Reading a third symbol exceeds the required length of 2, transitioning the automaton to trap state D, which loops on 0,1."
    },

    # Topic 4: DFA Example 3: Substring Matching ("aabb")
    {
        "q": "In DFA Example 3, the language requires accepting all strings over Σ = {a, b} that contain the substring '____'.",
        "a": "aabb",
        "distractors": ["abba", "bbaa", "abab"],
        "topic": "Substring 'aabb' Language",
        "explanation": "Example 3 constructs a pattern matcher for the specific substring 'aabb'."
    },
    {
        "q": "In the DFA for substring 'aabb', how many sequential prefix tracking states are used to reach the final state?",
        "a": "5 states (A, B, C, D, E)",
        "distractors": ["3 states", "4 states", "6 states"],
        "topic": "Substring Matching State Count",
        "explanation": "States correspond to prefix lengths: A (empty), B (saw 'a'), C (saw 'aa'), D (saw 'aab'), and E (saw 'aabb', accepting)."
    },
    {
        "q": "In the DFA for substring 'aabb', what is the transition from state C (which represents having seen 'aa') on input 'a'?",
        "a": "It loops back to state C",
        "distractors": ["It transitions to state B", "It resets to start state A", "It advances to state D"],
        "topic": "State C Overlap Loop",
        "explanation": "If the automaton has seen 'aa' (state C) and receives another 'a', the longest relevant prefix is still 'aa', so it loops at state C."
    },
    {
        "q": "In the DFA for substring 'aabb', from state D (having seen 'aab'), what happens if the next input is 'a'?",
        "a": "It returns to state B (representing prefix 'a')",
        "distractors": ["It resets to start state A", "It loops at state D", "It advances to final state E"],
        "topic": "State D Mismatch Fallback",
        "explanation": "After 'aab', receiving 'a' yields suffix 'a', which is represented by state B (prefix 'a')."
    },
    {
        "q": "In the DFA for substring 'aabb', once final state E is reached, what are its outgoing transitions?",
        "a": "It loops on both 'a' and 'b'",
        "distractors": ["It returns to state A on 'b'", "It halts immediately", "It transitions to a trap state"],
        "topic": "Substring Found Absorbing State",
        "explanation": "Once the substring 'aabb' has appeared anywhere in the string, the condition is satisfied forever, so state E loops on {a, b}."
    },

    # Topic 5: DFA Example 3a: Complement of a DFA (Inverting States)
    {
        "q": "To construct a DFA that accepts strings that DO NOT contain the substring 'aabb' (the complement language), what systematic transformation is applied to the DFA that accepts 'aabb'?",
        "a": "Invert (flip) all final and non-final states",
        "distractors": ["Reverse all transition arrow directions", "Remove all self-loops", "Add an epsilon transition"],
        "topic": "DFA Complementation Algorithm",
        "explanation": "To complement a DFA, keep the exact same state set and transitions, but set F' = Q \\ F (non-accepting states become accepting, and vice-versa)."
    },
    {
        "q": "In Example 3a (the complement of 'aabb'), which states become the accepting (final) states?",
        "a": "{A, B, C, D}",
        "distractors": ["{E}", "{A, E}", "{B, C, D}"],
        "topic": "Complement Accepting States",
        "explanation": "The original non-accepting states {A, B, C, D} all become accepting states (marked with double circles)."
    },
    {
        "q": "In Example 3a (the complement of 'aabb'), what state becomes the sole non-accepting (rejecting) state?",
        "a": "State E",
        "distractors": ["State A", "State B", "State C"],
        "topic": "Complement Rejecting State",
        "explanation": "State E (which previously accepted 'aabb') becomes the only non-accepting state."
    },
    {
        "q": "The closure property of Regular Languages demonstrating that the complement of any regular language is also regular is proven by the ability to ____ a DFA.",
        "a": "invert (complement)",
        "distractors": ["minimize", "nondeterminize", "tokenize"],
        "topic": "Closure Under Complementation",
        "explanation": "Because flipping the accept/reject status of DFA states yields another valid DFA, Regular Languages are closed under complementation."
    },

    # Topic 6: DFA Example 4: Figure Recognition
    {
        "q": "In Example 4, an automaton has start state A, intermediate states B and D, accepting states C and E, and dead state X. Tracing path A -> B -> C on inputs 1 then 0 accepts the string '____'.",
        "a": "10",
        "distractors": ["01", "00", "11"],
        "topic": "Example 4 Path Trace '10'",
        "explanation": "From A, on input 1 it reaches B; from B, on input 0 it reaches accepting state C. Thus '10' is accepted."
    },
    {
        "q": "In Example 4, tracing path A -> D -> E on inputs 0 then 1 accepts the string '____'.",
        "a": "01",
        "distractors": ["10", "11", "00"],
        "topic": "Example 4 Path Trace '01'",
        "explanation": "From A, on input 0 it reaches D; from D, on input 1 it reaches accepting state E. Thus '01' is accepted."
    },
    {
        "q": "In Example 4, what happens if any additional symbol is received after reaching accepting state C or E?",
        "a": "The machine transitions to dead state X and rejects",
        "distractors": ["The machine loops in the accepting state", "The machine resets to state A", "The machine halts"],
        "topic": "Example 4 Transition to Dead State",
        "explanation": "States C and E have transitions on 0,1 pointing to dead state X, meaning only strings of length 2 ('10' and '01') are accepted."
    },
    {
        "q": "The language recognized by the DFA in Example 4 is L = {____}.",
        "a": "{01, 10}",
        "distractors": ["{00, 11}", "{0, 1}", "{01, 10, 00, 11}"],
        "topic": "Example 4 Language Identification",
        "explanation": "The DFA in Example 4 accepts strictly the two binary strings of length 2 with alternating digits: {01, 10}."
    },

    # Topic 7: Week 3 Activities
    {
        "q": "In Activity 1, a DFA is constructed to accept all strings over alphabet Σ = {a, b, c} of length exactly 3. How many total strings are in this language?",
        "a": "27 strings (3^3)",
        "distractors": ["9 strings", "8 strings", "81 strings"],
        "topic": "Ternary Alphabet Length 3",
        "explanation": "With an alphabet of 3 symbols {a, b, c}, the number of strings of length 3 is 3^3 = 27."
    },
    {
        "q": "In Activity 2, for the language L2 = {strings that start with '0' and end with '1'}, what happens to any string starting with '1'?",
        "a": "It transitions immediately from the start state to a trap state",
        "distractors": ["It is accepted", "It loops at the start state", "It transitions to the final state"],
        "topic": "Start 0 End 1 Rejection",
        "explanation": "Since the string must start with '0', any string beginning with '1' violates the prefix requirement and is trapped."
    },
    {
        "q": "In Activity 4, the given transition diagram has start state A looping on {0, 1}, transitioning on '1' to state B, and transitioning from B on {0, 1} to accepting state C. What language does this automaton recognize?",
        "a": "All strings where the second symbol from the end is '1'",
        "distractors": ["All strings that end in '01'", "All strings of length 2", "All strings that start with '1'"],
        "topic": "Second from Last Symbol '1'",
        "explanation": "Transitioning on 1 to B followed by any single symbol {0, 1} to final state C means the string must have '1' as its penultimate (second from end) symbol."
    },
    {
        "q": "In a DFA with alphabet Σ = {a, b, c} accepting strings containing substring 'abbc' (Activity 3), how many states are required in the forward matching sequence from start to final state?",
        "a": "5 states",
        "distractors": ["4 states", "3 states", "6 states"],
        "topic": "Substring 'abbc' State Count",
        "explanation": "Matching a 4-character substring 'abbc' requires 5 states in sequence: ε, 'a', 'ab', 'abb', 'abbc' (accepting)."
    }
]

print(f"ATFL Module 3 items: {len(ATFL_MODULE_3_ITEMS)}")

ATFL_MODULE_3_EXPANSION = [
    {
        "q": "In a DFA, if the start state q0 is also an accepting state (q0 ∈ F), the automaton accepts the ____ string.",
        "a": "empty (ε)",
        "distractors": ["infinite", "undefined", "dead"],
        "topic": "Empty String Acceptance in DFA",
        "explanation": "If the initial state q0 is a member of F, the machine accepts without reading any input symbols, meaning ε ∈ L(M)."
    },
    {
        "q": "The property of a DFA that requires EVERY state to have an outgoing transition defined for EVERY symbol in alphabet Σ is known as the ____ condition.",
        "a": "completeness (totality)",
        "distractors": ["non-deterministic", "transductive", "recursive"],
        "topic": "Completeness Condition of DFA",
        "explanation": "A DFA's transition function is total: for every state q ∈ Q and symbol a ∈ Σ, δ(q, a) must be explicitly defined."
    },
    {
        "q": "In automata theory, the extended transition function that maps a state and an entire string w of symbols to a resulting state is standardly denoted as ____.",
        "a": "δ* (Delta star)",
        "distractors": ["Σ* (Sigma star)", "ε* (Epsilon star)", "Q* (Q star)"],
        "topic": "Extended Transition Function",
        "explanation": "The extended transition function δ*: Q x Σ* -> Q computes the cumulative state transition resulting from processing an entire string."
    },
    {
        "q": "A formal representation of an automaton that uses a tabular matrix with current states as rows and input symbols as columns is a transition ____.",
        "a": "table",
        "distractors": ["tree", "stack", "tape"],
        "topic": "Transition Table",
        "explanation": "A transition table lists current states along the vertical axis and alphabet symbols along the horizontal axis, specifying next states in cell entries."
    },
    {
        "q": "In a transition table, the start state is standardly annotated with an arrow (->) and accepting states are annotated with an ____.",
        "a": "asterisk (*)",
        "distractors": ["ampersand (&)", "hashtag (#)", "exclamation mark (!)"],
        "topic": "Transition Table Annotations",
        "explanation": "In standard textbook notation, '->' marks the start state and '*' marks accepting/final states in a transition table."
    },
    {
        "q": "In the DFA for substring 'aabb' (Example 3), if the machine is in state B (prefix 'a') and receives input 'b', why does it return to state A?",
        "a": "Because 'ab' cannot be part of the prefix 'aa', resetting progress",
        "distractors": ["Because 'b' is not in the alphabet", "Because state A is an accepting state", "Because it enters a dead state"],
        "topic": "Prefix Reset Logic",
        "explanation": "The sequence 'ab' breaks the prefix 'aa'. Since 'b' cannot extend 'aa', the machine must restart matching from state A."
    },
    {
        "q": "In the DFA for substring 'aabb' (Example 3), what is the state trajectory when processing the input string 'baabb'?",
        "a": "A -> A -> B -> C -> D -> E",
        "distractors": ["A -> B -> C -> D -> E -> E", "A -> C -> D -> E -> E", "A -> B -> A -> B -> E"],
        "topic": "String Trace 'baabb'",
        "explanation": "From A, on 'b' it stays at A. Then 'a' moves to B, 'a' to C, 'b' to D, and 'b' to E (accepted)."
    },
    {
        "q": "In the DFA for substring 'aabb' (Example 3), does the machine accept the string 'aaabb'?",
        "a": "Yes, because state C loops on 'a', reaching E on 'bb'",
        "distractors": ["No, because of too many 'a' symbols", "No, it enters a trap state", "Only if complemented"],
        "topic": "String Trace 'aaabb'",
        "explanation": "From A: on 'a' -> B, on 'a' -> C, on 'a' -> C (loops), on 'b' -> D, on 'b' -> E (accepts)."
    },
    {
        "q": "In DFA design, if an automaton with 5 states is complemented by flipping final and non-final states, how many total states does the complement DFA have?",
        "a": "5 states",
        "distractors": ["4 states", "6 states", "10 states"],
        "topic": "Complement State Preservation",
        "explanation": "Complementation changes only the subset of accepting states (F' = Q \\ F); the state set Q and transition function δ remain unchanged."
    },
    {
        "q": "For a DFA M = (Q, Σ, q0, F, δ), a string w is formally accepted by M if and only if ____.",
        "a": "δ*(q0, w) ∈ F",
        "distractors": ["δ*(q0, w) ∉ F", "δ*(q0, w) = q0", "δ*(q0, w) = ϕ"],
        "topic": "Formal Language Acceptance Definition",
        "explanation": "A string w is accepted by DFA M if the state reached after processing w starting from q0 belongs to F."
    },
    {
        "q": "The set of all strings accepted by a DFA M is called the language accepted by M, formally denoted as ____.",
        "a": "L(M)",
        "distractors": ["Σ(M)", "F(M)", "Q(M)"],
        "topic": "Language of a Machine Notation",
        "explanation": "L(M) = {w ∈ Σ* | δ*(q0, w) ∈ F} denotes the language recognized by automaton M."
    },
    {
        "q": "Two DFAs M1 and M2 are defined to be equivalent if and only if they ____.",
        "a": "accept the exact same language (L(M1) = L(M2))",
        "distractors": ["have the exact same number of states", "share the same alphabet", "have identical transition tables"],
        "topic": "DFA Equivalence Definition",
        "explanation": "Two automata are computationally equivalent if and only if they recognize the identical formal language."
    }
]

ATFL_MODULE_3_ITEMS.extend(ATFL_MODULE_3_EXPANSION)
print(f"Updated ATFL Module 3 items: {len(ATFL_MODULE_3_ITEMS)}")

ATFL_MODULE_4_ITEMS = [
    # Topic 1: Non-Deterministic Finite Automata (NFA) Definition & Principles
    {
        "q": "A state machine where a single input symbol can lead to multiple next states or no next state at all is a ____ Finite Automaton.",
        "a": "Non-Deterministic",
        "distractors": ["Deterministic", "Linear Bounded", "Turing"],
        "topic": "NFA Core Definition",
        "explanation": "A Non-Deterministic Finite Automaton (NFA) allows zero, one, or multiple outgoing transitions from a state on a single input symbol."
    },
    {
        "q": "Unlike a DFA, an NFA is permitted to make transitions without consuming any input symbol, which are known as ____-moves.",
        "a": "ε (Epsilon)",
        "distractors": ["Σ (Sigma)", "δ (Delta)", "Q"],
        "topic": "Epsilon Moves in NFA",
        "explanation": "NFAs can incorporate ε-transitions (empty moves), enabling state changes without consuming input symbols."
    },
    {
        "q": "For an NFA, the transition function δ maps each state and input symbol (including ε) to ____.",
        "a": "a subset of states (2^Q or power set)",
        "distractors": ["exactly one single state (Q)", "the alphabet (Σ)", "a stack of tokens"],
        "topic": "NFA Transition Function Signature",
        "explanation": "The NFA transition function is defined as δ: Q x (Σ U {ε}) -> 2^Q, meaning its output is a set of states (element of the power set)."
    },
    {
        "q": "If for a given state q and symbol a there is no valid transition in an NFA, the transition maps to the ____ set (ϕ).",
        "a": "empty",
        "distractors": ["universal", "final", "initial"],
        "topic": "Empty Set Transition",
        "explanation": "In an NFA, having no next state for an input symbol means δ(q, a) = ∅, representing a dead computational branch."
    },
    {
        "q": "A computational branch in an NFA that reaches the empty set (ϕ) with no available transitions is known as a dead ____.",
        "a": "configuration",
        "distractors": ["stack", "symbol", "tape"],
        "topic": "Dead Configuration",
        "explanation": "When an NFA computational path encounters a state with no transition for the current input symbol, that branch enters a dead configuration and terminates."
    },

    # Topic 2: DFA vs NFA Comparison
    {
        "q": "In terms of language recognition capability, how does the expressive computational power of an NFA compare to that of a DFA?",
        "a": "They are exactly equal (both recognize Regular Languages)",
        "distractors": ["NFA is strictly more powerful", "DFA is strictly more powerful", "NFA recognizes Context-Free languages"],
        "topic": "DFA vs NFA Equivalence",
        "explanation": "By the Rabin-Scott powerset construction theorem, any language recognized by an NFA can also be recognized by an equivalent DFA."
    },
    {
        "q": "While DFAs and NFAs recognize the exact same class of languages, NFAs are often much easier to design and can have ____ states than equivalent DFAs.",
        "a": "exponentially fewer",
        "distractors": ["infinitely more", "exactly double", "fractionally more"],
        "topic": "State Conciseness of NFA",
        "explanation": "An NFA with n states may require up to 2^n states when converted into a minimal equivalent DFA."
    },
    {
        "q": "In a DFA, how many next states must exist for every (state, input symbol) pair?",
        "a": "Exactly one",
        "distractors": ["Zero or more", "At least two", "Any arbitrary subset"],
        "topic": "DFA Uniqueness Constraint",
        "explanation": "A DFA requires exactly one deterministic next state for every combination of state and input symbol."
    },

    # Topic 3: Acceptance Criteria for NFA
    {
        "q": "According to the formal acceptance rule, an NFA accepts an input string if ____.",
        "a": "at least one computational branch ends in an accept/final state",
        "distractors": ["all computational branches end in an accept state", "the majority of branches accept", "the machine has no dead configurations"],
        "topic": "NFA Acceptance Criterion",
        "explanation": "An NFA accepts if there exists at least one valid sequence of transitions that consumes the entire string and terminates in a final state F."
    },
    {
        "q": "An NFA rejects an input string if and only if ____.",
        "a": "ALL computational paths fail to reach any final state",
        "distractors": ["at least one path fails", "the string contains an odd number of zeros", "a dead configuration is encountered on one path"],
        "topic": "NFA Rejection Rule",
        "explanation": "Rejection requires that none of the possible parallel computational branches terminate in an accepting state."
    },

    # Topic 4: NFA Formal 5-Tuple Definition
    {
        "q": "In the formal 5-tuple M = (Q, Σ, q0, F, δ) of an NFA, the power set of states Q is mathematically represented as ____.",
        "a": "2^Q",
        "distractors": ["Q^2", "Σ^Q", "Q!"],
        "topic": "Power Set Notation",
        "explanation": "2^Q denotes the set of all subsets of Q (the power set), which is the co-domain of the NFA transition function."
    },
    {
        "q": "If an NFA has 3 states, how many elements are in its power set 2^Q?",
        "a": "8 (2^3)",
        "distractors": ["3", "6", "9"],
        "topic": "Power Set Size",
        "explanation": "The power set of a set with |Q| = 3 contains 2^3 = 8 possible subsets."
    },

    # Topic 5: NFA Examples from Slides
    {
        "q": "In Week 4 Example 1 (NFA for strings ending with '0'), state A loops on {0, 1} and transitions on '0' to state B. When input '100' is processed, what is the set of states occupied at the end?",
        "a": "{A, B}",
        "distractors": ["{A}", "{B}", "ϕ"],
        "topic": "Example 1 Trace '100'",
        "explanation": "After '100', branch A remains at A, and the '0' transition also moves to B, resulting in active state subset {A, B}."
    },
    {
        "q": "In Week 4 Example 1, why is the input string '100' accepted by the NFA?",
        "a": "Because state B is in {A, B} and B is an accepting state",
        "distractors": ["Because state A is an accepting state", "Because the string has 3 symbols", "Because there are no 1s at the end"],
        "topic": "Example 1 Acceptance Rationale",
        "explanation": "Since state B is a final state and B ∈ {A, B}, at least one path ends in a final state, so the string is accepted."
    },
    {
        "q": "In Week 4 Example 2 (NFA for strings starting with '0'), what occurs if the first input symbol is '1'?",
        "a": "The machine enters a dead configuration (ϕ) and rejects",
        "distractors": ["The machine transitions to state B", "The machine loops at state A", "The machine complements the string"],
        "topic": "Example 2 Dead Configuration on '1'",
        "explanation": "State A has no transition defined for '1', resulting in δ(A, 1) = ∅ (dead configuration)."
    },
    {
        "q": "In Week 4 Example 3, an NFA accepts all strings over {0, 1} of length exactly 2 with states A -> B -> C. Why is string '01' accepted?",
        "a": "A transitions on 0 to B, and B transitions on 1 to final state C",
        "distractors": ["Because C loops on all inputs", "Because A is an accepting state", "Because it has no trap states"],
        "topic": "Example 3 Length 2 Trace",
        "explanation": "The sequence A --0--> B --1--> C lands in final state C after 2 symbols."
    },

    # Topic 6: Conversion of NFA to DFA (Subset Construction / Powerset Construction)
    {
        "q": "The algorithmic method used to convert any Non-Deterministic Finite Automaton (NFA) into an equivalent Deterministic Finite Automaton (DFA) is known as the ____ construction.",
        "a": "subset (powerset)",
        "distractors": ["pumping", "Chomsky", "Turing"],
        "topic": "Subset Construction Name",
        "explanation": "The subset construction (or powerset construction) algorithm systematically models sets of NFA states as individual DFA states."
    },
    {
        "q": "In the subset construction algorithm, each individual state in the resulting DFA represents a ____ of states from the original NFA.",
        "a": "subset (or set)",
        "distractors": ["permutation", "quotient", "derivative"],
        "topic": "DFA States as NFA Subsets",
        "explanation": "A state in the converted DFA corresponds to a subset of NFA states that could be reached simultaneously."
    },
    {
        "q": "If an NFA has n states, what is the theoretical maximum number of states the converted DFA could possess before minimization?",
        "a": "2^n",
        "distractors": ["n^2", "2n", "n!"],
        "topic": "Maximum DFA State Bound",
        "explanation": "Since there are 2^n subsets of a set of n states, the converted DFA has at most 2^n states."
    },
    {
        "q": "During subset construction, how is the transition on symbol 'a' from a composite DFA state S = {q1, q2} computed?",
        "a": "By taking the union of transitions: δ(q1, a) U δ(q2, a)",
        "distractors": ["By taking the intersection: δ(q1, a) ∩ δ(q2, a)", "By choosing only the transition from q1", "By taking the Cartesian product"],
        "topic": "Subset Transition Union Rule",
        "explanation": "The DFA transition on symbol 'a' from set S is the union of all NFA transitions from each state in S on symbol 'a'."
    },
    {
        "q": "In subset construction, which subsets of NFA states are designated as final (accepting) states in the converted DFA?",
        "a": "Any subset that contains at least one final state of the NFA",
        "distractors": ["Only subsets containing exclusively final states", "Only the initial subset", "Subsets containing the empty set"],
        "topic": "DFA Accepting State Condition",
        "explanation": "A DFA state S is an accepting state if S ∩ F_NFA ≠ ∅ (it contains at least one state that was an accepting state in the NFA)."
    },
    {
        "q": "In subset construction, if a state transition leads to the empty set (ϕ), how is this represented in the equivalent DFA?",
        "a": "As a dead (trap) state that loops on all input symbols",
        "distractors": ["It is completely removed from the DFA", "It is designated as the start state", "It becomes an accepting state"],
        "topic": "Dead State Representation in DFA",
        "explanation": "The empty set ϕ becomes an explicit trap state in the DFA with self-loops on all alphabet symbols."
    },
    {
        "q": "According to the set algebra rule cited in Slide 10 of Week 4, what is the result of taking the union of set A with the empty set ϕ (A U ϕ)?",
        "a": "A",
        "distractors": ["ϕ", "{A, ϕ}", "U"],
        "topic": "Set Union with Empty Set",
        "explanation": "Union with the empty set is identity: A ∪ ∅ = A."
    },
    {
        "q": "In Slide 10 (NFA to DFA conversion for strings ending with '1'), the NFA has states {A, B} where A is start and B is final. What are the states in the converted DFA?",
        "a": "State A and State AB (where AB is accepting)",
        "distractors": ["State A, State B, State C", "Only State A", "State A and State B"],
        "topic": "Slide 10 Converted DFA States",
        "explanation": "The reachable subsets are {A} and {A, B}, where {A, B} is accepting because it contains NFA final state B."
    },
    {
        "q": "In Slide 10, what is the transition from DFA state AB on input '0'?",
        "a": "It transitions back to state A",
        "distractors": ["It loops on state AB", "It transitions to a dead state", "It transitions to state B"],
        "topic": "Slide 10 Transition on 0",
        "explanation": "From AB, on input 0: δ(A, 0) ∪ δ(B, 0) = A ∪ ∅ = A. Thus it returns to state A."
    },
    {
        "q": "In Slide 10, what is the transition from DFA state AB on input '1'?",
        "a": "It loops on state AB",
        "distractors": ["It transitions to state A", "It enters a trap state", "It halts"],
        "topic": "Slide 10 Transition on 1",
        "explanation": "From AB, on input 1: δ(A, 1) ∪ δ(B, 1) = {A, B} ∪ ∅ = {A, B} = AB, looping on itself."
    },

    # Topic 7: Activity Problems (Activity 3 & Slide 11)
    {
        "q": "In Activity 3 Problem 1 ($L1 = {strings containing '01'}$), what is the regular expression for the language?",
        "a": "(0 + 1)* 01 (0 + 1)*",
        "distractors": ["01 (0 + 1)*", "(0 + 1)* 01", "(01)*"],
        "topic": "Regex for Containing '01'",
        "explanation": "Strings containing '01' anywhere have the regex (0 + 1)* 01 (0 + 1)*."
    },
    {
        "q": "In Activity 3 Problem 1 ($L1 = {strings containing '01'}$), how many states does the minimal DFA have?",
        "a": "3 states",
        "distractors": ["2 states", "4 states", "5 states"],
        "topic": "Minimal DFA for Containing '01'",
        "explanation": "The minimal DFA requires 3 states: S0 (not seen 0), S1 (seen 0), and S2 (seen 01, accepting)."
    },
    {
        "q": "In Activity 3 Problem 2 ($L2 = {strings starting with '10'}$), what is the regular expression?",
        "a": "10 (0 + 1)*",
        "distractors": ["(10)*", "(0 + 1)* 10", "1 (0 + 1)* 0"],
        "topic": "Regex for Starting with '10'",
        "explanation": "Strings that start with '10' followed by any sequence of symbols are given by 10 (0 + 1)*."
    },
    {
        "q": "In Activity 3 Problem 2 ($L2 = {strings starting with '10'}$), why does the converted DFA require a Trap state?",
        "a": "To permanently reject any string whose prefix is not '10'",
        "distractors": ["To store stack memory", "To loop on final states", "To handle epsilon transitions"],
        "topic": "Trap State in Starting with '10'",
        "explanation": "Any string starting with '0' or '11' violates the required prefix '10' and must be diverted to an inescapable trap state."
    },
    {
        "q": "In Activity 3 Problem 4 ($L4 = {strings ending with '1'}$), what is the regular expression?",
        "a": "(0 + 1)* 1",
        "distractors": ["1 (0 + 1)*", "(1)*", "(01)*"],
        "topic": "Regex for Ending with '1'",
        "explanation": "Any string ending with '1' is matched by (0 + 1)* 1."
    },
    {
        "q": "In Activity 3 Problem 5 ($L5 = {strings ending with '11'}$), how many states does the equivalent minimal DFA contain?",
        "a": "3 states",
        "distractors": ["2 states", "4 states", "5 states"],
        "topic": "DFA for Ending with '11'",
        "explanation": "Matching strings ending with '11' requires 3 DFA states: S0 (no trailing 1), S1 (one trailing 1), and S2 (two or more trailing 1s, accepting)."
    },
    {
        "q": "In Activity 3 Problem 3 ($L3 = {strings containing '0'}$), what is the minimal number of states in the equivalent DFA?",
        "a": "2 states",
        "distractors": ["3 states", "4 states", "1 state"],
        "topic": "DFA for Containing '0'",
        "explanation": "Only 2 states are needed: state A (seen only 1s, non-accepting) and state B (seen at least one 0, accepting)."
    }
]

print(f"ATFL Module 4 items: {len(ATFL_MODULE_4_ITEMS)}")

ATFL_MODULE_4_EXPANSION = [
    {
        "q": "In an ε-NFA, the set of all states that can be reached from a state q using only empty transitions (ε-moves) without consuming any input is called the ____ of q.",
        "a": "ε-closure (Epsilon closure)",
        "distractors": ["Kleene closure", "transition matrix", "power set"],
        "topic": "Epsilon Closure Definition",
        "explanation": "The ε-closure(q) is the set of all states reachable from state q by following zero or more ε-transitions."
    },
    {
        "q": "The ε-closure of any state q always contains at least ____.",
        "a": "the state q itself",
        "distractors": ["the initial state", "the final state", "the empty set"],
        "topic": "Epsilon Closure Self-Inclusion",
        "explanation": "Because a state is reachable from itself via zero ε-moves (path of length 0), q ∈ ε-closure(q) always."
    },
    {
        "q": "In Activity 3 Problem 1 ($L1 = {strings containing '01'}$), the DFA created by subset construction has 4 reachable states before minimization: A = {q0}, B = {q0, q1}, C = {q0, q2}, and D = {q0, q1, q2}. Which states are accepting?",
        "a": "States C and D (both contain q2)",
        "distractors": ["States A and B", "Only State D", "Only State C"],
        "topic": "Activity 3 Problem 1 Accepting States",
        "explanation": "Because q2 is the accepting state in the NFA, any subset containing q2 (namely C and D) is an accepting state in the DFA."
    },
    {
        "q": "In Activity 3 Problem 1, why can states C = {q0, q2} and D = {q0, q1, q2} be merged during DFA minimization?",
        "a": "Both states transition to D on '0' and to C on '1', making them equivalent",
        "distractors": ["Because both are initial states", "Because state D is unreachable", "Because both have dead configurations"],
        "topic": "State Equivalence in Minimization",
        "explanation": "States C and D have identical transition outputs on all alphabet symbols (0 -> D, 1 -> C) and are both accepting, proving they are indistinguishable/equivalent."
    },
    {
        "q": "In subset construction, states in the power set that cannot be reached by any sequence of transitions starting from the initial state are called ____ states.",
        "a": "unreachable (inaccessible)",
        "distractors": ["final", "trap", "deterministic"],
        "topic": "Unreachable States in Subset Construction",
        "explanation": "While 2^Q possible subsets exist, typically only a small fraction are reachable from the start state, and unreachable subsets are discarded."
    },
    {
        "q": "The famous algorithmic technique that converts any Regular Expression into an equivalent ε-NFA is known as ____ Construction.",
        "a": "Thompson's",
        "distractors": ["Turing's", "Chomsky's", "Moore's"],
        "topic": "Thompson's Construction",
        "explanation": "Thompson's construction algorithm systematically converts regular expressions into ε-NFAs using base cases and structural induction."
    },
    {
        "q": "In an NFA, when multiple transitions exist for the same input symbol from a single state, how does the machine conceptually process them?",
        "a": "It explores all possible execution paths simultaneously in parallel",
        "distractors": ["It crashes with a runtime error", "It always chooses the alphabetically first state", "It prompts the user for a choice"],
        "topic": "Parallel Branching Concept",
        "explanation": "Non-determinism can be conceptualized as cloning the machine at each branch point to explore all computational trajectories in parallel."
    },
    {
        "q": "An NFA with n states that recognizes a language can always be converted into an equivalent DFA with at most ____ states.",
        "a": "2^n",
        "distractors": ["n!", "n^2", "2n"],
        "topic": "NFA to DFA State Upper Bound",
        "explanation": "By subset construction, the maximum number of states in the equivalent DFA is 2^n."
    },
    {
        "q": "In an NFA transition table, an entry with the symbol ϕ indicates that ____.",
        "a": "no transition is defined for that state and input symbol",
        "distractors": ["the state is an accepting state", "the machine loops infinitely", "an epsilon transition occurs"],
        "topic": "Phi Symbol in Transition Table",
        "explanation": "The symbol ϕ (or ∅) in a transition table denotes the empty set, indicating no valid next state exists for that input."
    },
    {
        "q": "In Activity 3 Problem 5 (strings ending with '11'), what is the transition from DFA state B = {q0, q1} on input '1'?",
        "a": "State C = {q0, q1, q2} (Accepting)",
        "distractors": ["State A = {q0}", "State B = {q0, q1}", "Trap state"],
        "topic": "Activity 3 Problem 5 Transition on '1'",
        "explanation": "From B = {q0, q1}, on input 1: δ(q0, 1) = {q0, q1} and δ(q1, 1) = {q2}. The union is {q0, q1, q2} = C (accepting)."
    },
    {
        "q": "In Activity 3 Problem 5 (strings ending with '11'), what is the transition from DFA state C = {q0, q1, q2} on input '0'?",
        "a": "State A = {q0}",
        "distractors": ["State B = {q0, q1}", "State C = {q0, q1, q2}", "Trap state"],
        "topic": "Activity 3 Problem 5 Transition on '0'",
        "explanation": "From C, on input 0: δ(q0, 0) = {q0}, δ(q1, 0) = ∅, and δ(q2, 0) = ∅. The union is {q0} = State A."
    },
    {
        "q": "Which of the following computational characteristics is shared by BOTH DFAs and NFAs?",
        "a": "Both recognize exactly the class of Regular Languages",
        "distractors": ["Both require unique deterministic transitions", "Both allow epsilon transitions", "Both require exactly one next state per symbol"],
        "topic": "Shared DFA and NFA Characteristics",
        "explanation": "DFAs and NFAs are computationally equivalent in language recognition power—both define and recognize Regular Languages."
    }
]

ATFL_MODULE_4_ITEMS.extend(ATFL_MODULE_4_EXPANSION)
print(f"Updated ATFL Module 4 items: {len(ATFL_MODULE_4_ITEMS)}")

total_atfl = len(ATFL_MODULE_1_ITEMS) + len(ATFL_MODULE_2_ITEMS) + len(ATFL_MODULE_3_ITEMS) + len(ATFL_MODULE_4_ITEMS)
print(f"TOTAL ATFL311 ITEMS ACROSS 4 MODULES: {total_atfl}")
