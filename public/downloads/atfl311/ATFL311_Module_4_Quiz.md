# ATFL311: Automata Theory & Formal Languages — Module 4: Non-Deterministic Finite Automata & Conversion
*Total Questions: 45 Items | Format: Identification with Multiple Choices*

---

### Question 1
**_____ 1. A state machine where a single input symbol can lead to multiple next states or no next state at all is a ____ Finite Automaton.**

- a.) Turing ❌
  > *Rationale:* Incorrect. 'Turing' is a distractor. The correct answer is 'Non-Deterministic'.

- b.) Non-Deterministic ✅ **[CORRECT]**
  > *Rationale:* Correct! [NFA Core Definition] A Non-Deterministic Finite Automaton (NFA) allows zero, one, or multiple outgoing transitions from a state on a single input symbol.

- c.) Deterministic ❌
  > *Rationale:* Incorrect. 'Deterministic' is a distractor. The correct answer is 'Non-Deterministic'.

- d.) Linear Bounded ❌
  > *Rationale:* Incorrect. 'Linear Bounded' is a distractor. The correct answer is 'Non-Deterministic'.

💡 *Hint:* Concept: NFA Core Definition

---

### Question 2
**_____ 2. Unlike a DFA, an NFA is permitted to make transitions without consuming any input symbol, which are known as ____-moves.**

- a.) Σ (Sigma) ❌
  > *Rationale:* Incorrect. 'Σ (Sigma)' is a distractor. The correct answer is 'ε (Epsilon)'.

- b.) Q ❌
  > *Rationale:* Incorrect. 'Q' is a distractor. The correct answer is 'ε (Epsilon)'.

- c.) δ (Delta) ❌
  > *Rationale:* Incorrect. 'δ (Delta)' is a distractor. The correct answer is 'ε (Epsilon)'.

- d.) ε (Epsilon) ✅ **[CORRECT]**
  > *Rationale:* Correct! [Epsilon Moves in NFA] NFAs can incorporate ε-transitions (empty moves), enabling state changes without consuming input symbols.

💡 *Hint:* Concept: Epsilon Moves in NFA

---

### Question 3
**_____ 3. For an NFA, the transition function δ maps each state and input symbol (including ε) to ____.**

- a.) a subset of states (2^Q or power set) ✅ **[CORRECT]**
  > *Rationale:* Correct! [NFA Transition Function Signature] The NFA transition function is defined as δ: Q x (Σ U {ε}) -> 2^Q, meaning its output is a set of states (element of the power set).

- b.) a stack of tokens ❌
  > *Rationale:* Incorrect. 'a stack of tokens' is a distractor. The correct answer is 'a subset of states (2^Q or power set)'.

- c.) the alphabet (Σ) ❌
  > *Rationale:* Incorrect. 'the alphabet (Σ)' is a distractor. The correct answer is 'a subset of states (2^Q or power set)'.

- d.) exactly one single state (Q) ❌
  > *Rationale:* Incorrect. 'exactly one single state (Q)' is a distractor. The correct answer is 'a subset of states (2^Q or power set)'.

💡 *Hint:* Concept: NFA Transition Function Signature

---

### Question 4
**_____ 4. If for a given state q and symbol a there is no valid transition in an NFA, the transition maps to the ____ set (ϕ).**

- a.) empty ✅ **[CORRECT]**
  > *Rationale:* Correct! [Empty Set Transition] In an NFA, having no next state for an input symbol means δ(q, a) = ∅, representing a dead computational branch.

- b.) universal ❌
  > *Rationale:* Incorrect. 'universal' is a distractor. The correct answer is 'empty'.

- c.) initial ❌
  > *Rationale:* Incorrect. 'initial' is a distractor. The correct answer is 'empty'.

- d.) final ❌
  > *Rationale:* Incorrect. 'final' is a distractor. The correct answer is 'empty'.

💡 *Hint:* Concept: Empty Set Transition

---

### Question 5
**_____ 5. A computational branch in an NFA that reaches the empty set (ϕ) with no available transitions is known as a dead ____.**

- a.) symbol ❌
  > *Rationale:* Incorrect. 'symbol' is a distractor. The correct answer is 'configuration'.

- b.) tape ❌
  > *Rationale:* Incorrect. 'tape' is a distractor. The correct answer is 'configuration'.

- c.) stack ❌
  > *Rationale:* Incorrect. 'stack' is a distractor. The correct answer is 'configuration'.

- d.) configuration ✅ **[CORRECT]**
  > *Rationale:* Correct! [Dead Configuration] When an NFA computational path encounters a state with no transition for the current input symbol, that branch enters a dead configuration and terminates.

💡 *Hint:* Concept: Dead Configuration

---

### Question 6
**_____ 6. In terms of language recognition capability, how does the expressive computational power of an NFA compare to that of a DFA?**

- a.) They are exactly equal (both recognize Regular Languages) ✅ **[CORRECT]**
  > *Rationale:* Correct! [DFA vs NFA Equivalence] By the Rabin-Scott powerset construction theorem, any language recognized by an NFA can also be recognized by an equivalent DFA.

- b.) NFA is strictly more powerful ❌
  > *Rationale:* Incorrect. 'NFA is strictly more powerful' is a distractor. The correct answer is 'They are exactly equal (both recognize Regular Languages)'.

- c.) DFA is strictly more powerful ❌
  > *Rationale:* Incorrect. 'DFA is strictly more powerful' is a distractor. The correct answer is 'They are exactly equal (both recognize Regular Languages)'.

- d.) NFA recognizes Context-Free languages ❌
  > *Rationale:* Incorrect. 'NFA recognizes Context-Free languages' is a distractor. The correct answer is 'They are exactly equal (both recognize Regular Languages)'.

💡 *Hint:* Concept: DFA vs NFA Equivalence

---

### Question 7
**_____ 7. While DFAs and NFAs recognize the exact same class of languages, NFAs are often much easier to design and can have ____ states than equivalent DFAs.**

- a.) fractionally more ❌
  > *Rationale:* Incorrect. 'fractionally more' is a distractor. The correct answer is 'exponentially fewer'.

- b.) exponentially fewer ✅ **[CORRECT]**
  > *Rationale:* Correct! [State Conciseness of NFA] An NFA with n states may require up to 2^n states when converted into a minimal equivalent DFA.

- c.) infinitely more ❌
  > *Rationale:* Incorrect. 'infinitely more' is a distractor. The correct answer is 'exponentially fewer'.

- d.) exactly double ❌
  > *Rationale:* Incorrect. 'exactly double' is a distractor. The correct answer is 'exponentially fewer'.

💡 *Hint:* Concept: State Conciseness of NFA

---

### Question 8
**_____ 8. In a DFA, how many next states must exist for every (state, input symbol) pair?**

- a.) Zero or more ❌
  > *Rationale:* Incorrect. 'Zero or more' is a distractor. The correct answer is 'Exactly one'.

- b.) At least two ❌
  > *Rationale:* Incorrect. 'At least two' is a distractor. The correct answer is 'Exactly one'.

- c.) Any arbitrary subset ❌
  > *Rationale:* Incorrect. 'Any arbitrary subset' is a distractor. The correct answer is 'Exactly one'.

- d.) Exactly one ✅ **[CORRECT]**
  > *Rationale:* Correct! [DFA Uniqueness Constraint] A DFA requires exactly one deterministic next state for every combination of state and input symbol.

💡 *Hint:* Concept: DFA Uniqueness Constraint

---

### Question 9
**_____ 9. According to the formal acceptance rule, an NFA accepts an input string if ____.**

- a.) at least one computational branch ends in an accept/final state ✅ **[CORRECT]**
  > *Rationale:* Correct! [NFA Acceptance Criterion] An NFA accepts if there exists at least one valid sequence of transitions that consumes the entire string and terminates in a final state F.

- b.) the majority of branches accept ❌
  > *Rationale:* Incorrect. 'the majority of branches accept' is a distractor. The correct answer is 'at least one computational branch ends in an accept/final state'.

- c.) all computational branches end in an accept state ❌
  > *Rationale:* Incorrect. 'all computational branches end in an accept state' is a distractor. The correct answer is 'at least one computational branch ends in an accept/final state'.

- d.) the machine has no dead configurations ❌
  > *Rationale:* Incorrect. 'the machine has no dead configurations' is a distractor. The correct answer is 'at least one computational branch ends in an accept/final state'.

💡 *Hint:* Concept: NFA Acceptance Criterion

---

### Question 10
**_____ 10. An NFA rejects an input string if and only if ____.**

- a.) at least one path fails ❌
  > *Rationale:* Incorrect. 'at least one path fails' is a distractor. The correct answer is 'ALL computational paths fail to reach any final state'.

- b.) a dead configuration is encountered on one path ❌
  > *Rationale:* Incorrect. 'a dead configuration is encountered on one path' is a distractor. The correct answer is 'ALL computational paths fail to reach any final state'.

- c.) the string contains an odd number of zeros ❌
  > *Rationale:* Incorrect. 'the string contains an odd number of zeros' is a distractor. The correct answer is 'ALL computational paths fail to reach any final state'.

- d.) ALL computational paths fail to reach any final state ✅ **[CORRECT]**
  > *Rationale:* Correct! [NFA Rejection Rule] Rejection requires that none of the possible parallel computational branches terminate in an accepting state.

💡 *Hint:* Concept: NFA Rejection Rule

---

### Question 11
**_____ 11. In the formal 5-tuple M = (Q, Σ, q0, F, δ) of an NFA, the power set of states Q is mathematically represented as ____.**

- a.) Q^2 ❌
  > *Rationale:* Incorrect. 'Q^2' is a distractor. The correct answer is '2^Q'.

- b.) Σ^Q ❌
  > *Rationale:* Incorrect. 'Σ^Q' is a distractor. The correct answer is '2^Q'.

- c.) Q! ❌
  > *Rationale:* Incorrect. 'Q!' is a distractor. The correct answer is '2^Q'.

- d.) 2^Q ✅ **[CORRECT]**
  > *Rationale:* Correct! [Power Set Notation] 2^Q denotes the set of all subsets of Q (the power set), which is the co-domain of the NFA transition function.

💡 *Hint:* Concept: Power Set Notation

---

### Question 12
**_____ 12. If an NFA has 3 states, how many elements are in its power set 2^Q?**

- a.) 8 (2^3) ✅ **[CORRECT]**
  > *Rationale:* Correct! [Power Set Size] The power set of a set with |Q| = 3 contains 2^3 = 8 possible subsets.

- b.) 6 ❌
  > *Rationale:* Incorrect. '6' is a distractor. The correct answer is '8 (2^3)'.

- c.) 3 ❌
  > *Rationale:* Incorrect. '3' is a distractor. The correct answer is '8 (2^3)'.

- d.) 9 ❌
  > *Rationale:* Incorrect. '9' is a distractor. The correct answer is '8 (2^3)'.

💡 *Hint:* Concept: Power Set Size

---

### Question 13
**_____ 13. In Week 4 Example 1 (NFA for strings ending with '0'), state A loops on {0, 1} and transitions on '0' to state B. When input '100' is processed, what is the set of states occupied at the end?**

- a.) ϕ ❌
  > *Rationale:* Incorrect. 'ϕ' is a distractor. The correct answer is '{A, B}'.

- b.) {A} ❌
  > *Rationale:* Incorrect. '{A}' is a distractor. The correct answer is '{A, B}'.

- c.) {B} ❌
  > *Rationale:* Incorrect. '{B}' is a distractor. The correct answer is '{A, B}'.

- d.) {A, B} ✅ **[CORRECT]**
  > *Rationale:* Correct! [Example 1 Trace '100'] After '100', branch A remains at A, and the '0' transition also moves to B, resulting in active state subset {A, B}.

💡 *Hint:* Concept: Example 1 Trace '100'

---

### Question 14
**_____ 14. In Week 4 Example 1, why is the input string '100' accepted by the NFA?**

- a.) Because the string has 3 symbols ❌
  > *Rationale:* Incorrect. 'Because the string has 3 symbols' is a distractor. The correct answer is 'Because state B is in {A, B} and B is an accepting state'.

- b.) Because state B is in {A, B} and B is an accepting state ✅ **[CORRECT]**
  > *Rationale:* Correct! [Example 1 Acceptance Rationale] Since state B is a final state and B ∈ {A, B}, at least one path ends in a final state, so the string is accepted.

- c.) Because state A is an accepting state ❌
  > *Rationale:* Incorrect. 'Because state A is an accepting state' is a distractor. The correct answer is 'Because state B is in {A, B} and B is an accepting state'.

- d.) Because there are no 1s at the end ❌
  > *Rationale:* Incorrect. 'Because there are no 1s at the end' is a distractor. The correct answer is 'Because state B is in {A, B} and B is an accepting state'.

💡 *Hint:* Concept: Example 1 Acceptance Rationale

---

### Question 15
**_____ 15. In Week 4 Example 2 (NFA for strings starting with '0'), what occurs if the first input symbol is '1'?**

- a.) The machine transitions to state B ❌
  > *Rationale:* Incorrect. 'The machine transitions to state B' is a distractor. The correct answer is 'The machine enters a dead configuration (ϕ) and rejects'.

- b.) The machine loops at state A ❌
  > *Rationale:* Incorrect. 'The machine loops at state A' is a distractor. The correct answer is 'The machine enters a dead configuration (ϕ) and rejects'.

- c.) The machine enters a dead configuration (ϕ) and rejects ✅ **[CORRECT]**
  > *Rationale:* Correct! [Example 2 Dead Configuration on '1'] State A has no transition defined for '1', resulting in δ(A, 1) = ∅ (dead configuration).

- d.) The machine complements the string ❌
  > *Rationale:* Incorrect. 'The machine complements the string' is a distractor. The correct answer is 'The machine enters a dead configuration (ϕ) and rejects'.

💡 *Hint:* Concept: Example 2 Dead Configuration on '1'

---

### Question 16
**_____ 16. In Week 4 Example 3, an NFA accepts all strings over {0, 1} of length exactly 2 with states A -> B -> C. Why is string '01' accepted?**

- a.) Because it has no trap states ❌
  > *Rationale:* Incorrect. 'Because it has no trap states' is a distractor. The correct answer is 'A transitions on 0 to B, and B transitions on 1 to final state C'.

- b.) Because C loops on all inputs ❌
  > *Rationale:* Incorrect. 'Because C loops on all inputs' is a distractor. The correct answer is 'A transitions on 0 to B, and B transitions on 1 to final state C'.

- c.) Because A is an accepting state ❌
  > *Rationale:* Incorrect. 'Because A is an accepting state' is a distractor. The correct answer is 'A transitions on 0 to B, and B transitions on 1 to final state C'.

- d.) A transitions on 0 to B, and B transitions on 1 to final state C ✅ **[CORRECT]**
  > *Rationale:* Correct! [Example 3 Length 2 Trace] The sequence A --0--> B --1--> C lands in final state C after 2 symbols.

💡 *Hint:* Concept: Example 3 Length 2 Trace

---

### Question 17
**_____ 17. The algorithmic method used to convert any Non-Deterministic Finite Automaton (NFA) into an equivalent Deterministic Finite Automaton (DFA) is known as the ____ construction.**

- a.) subset (powerset) ✅ **[CORRECT]**
  > *Rationale:* Correct! [Subset Construction Name] The subset construction (or powerset construction) algorithm systematically models sets of NFA states as individual DFA states.

- b.) Chomsky ❌
  > *Rationale:* Incorrect. 'Chomsky' is a distractor. The correct answer is 'subset (powerset)'.

- c.) Turing ❌
  > *Rationale:* Incorrect. 'Turing' is a distractor. The correct answer is 'subset (powerset)'.

- d.) pumping ❌
  > *Rationale:* Incorrect. 'pumping' is a distractor. The correct answer is 'subset (powerset)'.

💡 *Hint:* Concept: Subset Construction Name

---

### Question 18
**_____ 18. In the subset construction algorithm, each individual state in the resulting DFA represents a ____ of states from the original NFA.**

- a.) quotient ❌
  > *Rationale:* Incorrect. 'quotient' is a distractor. The correct answer is 'subset (or set)'.

- b.) permutation ❌
  > *Rationale:* Incorrect. 'permutation' is a distractor. The correct answer is 'subset (or set)'.

- c.) derivative ❌
  > *Rationale:* Incorrect. 'derivative' is a distractor. The correct answer is 'subset (or set)'.

- d.) subset (or set) ✅ **[CORRECT]**
  > *Rationale:* Correct! [DFA States as NFA Subsets] A state in the converted DFA corresponds to a subset of NFA states that could be reached simultaneously.

💡 *Hint:* Concept: DFA States as NFA Subsets

---

### Question 19
**_____ 19. If an NFA has n states, what is the theoretical maximum number of states the converted DFA could possess before minimization?**

- a.) n^2 ❌
  > *Rationale:* Incorrect. 'n^2' is a distractor. The correct answer is '2^n'.

- b.) 2n ❌
  > *Rationale:* Incorrect. '2n' is a distractor. The correct answer is '2^n'.

- c.) 2^n ✅ **[CORRECT]**
  > *Rationale:* Correct! [Maximum DFA State Bound] Since there are 2^n subsets of a set of n states, the converted DFA has at most 2^n states.

- d.) n! ❌
  > *Rationale:* Incorrect. 'n!' is a distractor. The correct answer is '2^n'.

💡 *Hint:* Concept: Maximum DFA State Bound

---

### Question 20
**_____ 20. During subset construction, how is the transition on symbol 'a' from a composite DFA state S = {q1, q2} computed?**

- a.) By taking the union of transitions: δ(q1, a) U δ(q2, a) ✅ **[CORRECT]**
  > *Rationale:* Correct! [Subset Transition Union Rule] The DFA transition on symbol 'a' from set S is the union of all NFA transitions from each state in S on symbol 'a'.

- b.) By choosing only the transition from q1 ❌
  > *Rationale:* Incorrect. 'By choosing only the transition from q1' is a distractor. The correct answer is 'By taking the union of transitions: δ(q1, a) U δ(q2, a)'.

- c.) By taking the intersection: δ(q1, a) ∩ δ(q2, a) ❌
  > *Rationale:* Incorrect. 'By taking the intersection: δ(q1, a) ∩ δ(q2, a)' is a distractor. The correct answer is 'By taking the union of transitions: δ(q1, a) U δ(q2, a)'.

- d.) By taking the Cartesian product ❌
  > *Rationale:* Incorrect. 'By taking the Cartesian product' is a distractor. The correct answer is 'By taking the union of transitions: δ(q1, a) U δ(q2, a)'.

💡 *Hint:* Concept: Subset Transition Union Rule

---

### Question 21
**_____ 21. In subset construction, which subsets of NFA states are designated as final (accepting) states in the converted DFA?**

- a.) Only subsets containing exclusively final states ❌
  > *Rationale:* Incorrect. 'Only subsets containing exclusively final states' is a distractor. The correct answer is 'Any subset that contains at least one final state of the NFA'.

- b.) Only the initial subset ❌
  > *Rationale:* Incorrect. 'Only the initial subset' is a distractor. The correct answer is 'Any subset that contains at least one final state of the NFA'.

- c.) Subsets containing the empty set ❌
  > *Rationale:* Incorrect. 'Subsets containing the empty set' is a distractor. The correct answer is 'Any subset that contains at least one final state of the NFA'.

- d.) Any subset that contains at least one final state of the NFA ✅ **[CORRECT]**
  > *Rationale:* Correct! [DFA Accepting State Condition] A DFA state S is an accepting state if S ∩ F_NFA ≠ ∅ (it contains at least one state that was an accepting state in the NFA).

💡 *Hint:* Concept: DFA Accepting State Condition

---

### Question 22
**_____ 22. In subset construction, if a state transition leads to the empty set (ϕ), how is this represented in the equivalent DFA?**

- a.) It is completely removed from the DFA ❌
  > *Rationale:* Incorrect. 'It is completely removed from the DFA' is a distractor. The correct answer is 'As a dead (trap) state that loops on all input symbols'.

- b.) It becomes an accepting state ❌
  > *Rationale:* Incorrect. 'It becomes an accepting state' is a distractor. The correct answer is 'As a dead (trap) state that loops on all input symbols'.

- c.) As a dead (trap) state that loops on all input symbols ✅ **[CORRECT]**
  > *Rationale:* Correct! [Dead State Representation in DFA] The empty set ϕ becomes an explicit trap state in the DFA with self-loops on all alphabet symbols.

- d.) It is designated as the start state ❌
  > *Rationale:* Incorrect. 'It is designated as the start state' is a distractor. The correct answer is 'As a dead (trap) state that loops on all input symbols'.

💡 *Hint:* Concept: Dead State Representation in DFA

---

### Question 23
**_____ 23. According to the set algebra rule cited in Slide 10 of Week 4, what is the result of taking the union of set A with the empty set ϕ (A U ϕ)?**

- a.) ϕ ❌
  > *Rationale:* Incorrect. 'ϕ' is a distractor. The correct answer is 'A'.

- b.) {A, ϕ} ❌
  > *Rationale:* Incorrect. '{A, ϕ}' is a distractor. The correct answer is 'A'.

- c.) A ✅ **[CORRECT]**
  > *Rationale:* Correct! [Set Union with Empty Set] Union with the empty set is identity: A ∪ ∅ = A.

- d.) U ❌
  > *Rationale:* Incorrect. 'U' is a distractor. The correct answer is 'A'.

💡 *Hint:* Concept: Set Union with Empty Set

---

### Question 24
**_____ 24. In Slide 10 (NFA to DFA conversion for strings ending with '1'), the NFA has states {A, B} where A is start and B is final. What are the states in the converted DFA?**

- a.) Only State A ❌
  > *Rationale:* Incorrect. 'Only State A' is a distractor. The correct answer is 'State A and State AB (where AB is accepting)'.

- b.) State A and State B ❌
  > *Rationale:* Incorrect. 'State A and State B' is a distractor. The correct answer is 'State A and State AB (where AB is accepting)'.

- c.) State A and State AB (where AB is accepting) ✅ **[CORRECT]**
  > *Rationale:* Correct! [Slide 10 Converted DFA States] The reachable subsets are {A} and {A, B}, where {A, B} is accepting because it contains NFA final state B.

- d.) State A, State B, State C ❌
  > *Rationale:* Incorrect. 'State A, State B, State C' is a distractor. The correct answer is 'State A and State AB (where AB is accepting)'.

💡 *Hint:* Concept: Slide 10 Converted DFA States

---

### Question 25
**_____ 25. In Slide 10, what is the transition from DFA state AB on input '0'?**

- a.) It loops on state AB ❌
  > *Rationale:* Incorrect. 'It loops on state AB' is a distractor. The correct answer is 'It transitions back to state A'.

- b.) It transitions to a dead state ❌
  > *Rationale:* Incorrect. 'It transitions to a dead state' is a distractor. The correct answer is 'It transitions back to state A'.

- c.) It transitions back to state A ✅ **[CORRECT]**
  > *Rationale:* Correct! [Slide 10 Transition on 0] From AB, on input 0: δ(A, 0) ∪ δ(B, 0) = A ∪ ∅ = A. Thus it returns to state A.

- d.) It transitions to state B ❌
  > *Rationale:* Incorrect. 'It transitions to state B' is a distractor. The correct answer is 'It transitions back to state A'.

💡 *Hint:* Concept: Slide 10 Transition on 0

---

### Question 26
**_____ 26. In Slide 10, what is the transition from DFA state AB on input '1'?**

- a.) It loops on state AB ✅ **[CORRECT]**
  > *Rationale:* Correct! [Slide 10 Transition on 1] From AB, on input 1: δ(A, 1) ∪ δ(B, 1) = {A, B} ∪ ∅ = {A, B} = AB, looping on itself.

- b.) It enters a trap state ❌
  > *Rationale:* Incorrect. 'It enters a trap state' is a distractor. The correct answer is 'It loops on state AB'.

- c.) It halts ❌
  > *Rationale:* Incorrect. 'It halts' is a distractor. The correct answer is 'It loops on state AB'.

- d.) It transitions to state A ❌
  > *Rationale:* Incorrect. 'It transitions to state A' is a distractor. The correct answer is 'It loops on state AB'.

💡 *Hint:* Concept: Slide 10 Transition on 1

---

### Question 27
**_____ 27. In Activity 3 Problem 1 ($L1 = {strings containing '01'}$), what is the regular expression for the language?**

- a.) (0 + 1)* 01 (0 + 1)* ✅ **[CORRECT]**
  > *Rationale:* Correct! [Regex for Containing '01'] Strings containing '01' anywhere have the regex (0 + 1)* 01 (0 + 1)*.

- b.) (0 + 1)* 01 ❌
  > *Rationale:* Incorrect. '(0 + 1)* 01' is a distractor. The correct answer is '(0 + 1)* 01 (0 + 1)*'.

- c.) 01 (0 + 1)* ❌
  > *Rationale:* Incorrect. '01 (0 + 1)*' is a distractor. The correct answer is '(0 + 1)* 01 (0 + 1)*'.

- d.) (01)* ❌
  > *Rationale:* Incorrect. '(01)*' is a distractor. The correct answer is '(0 + 1)* 01 (0 + 1)*'.

💡 *Hint:* Concept: Regex for Containing '01'

---

### Question 28
**_____ 28. In Activity 3 Problem 1 ($L1 = {strings containing '01'}$), how many states does the minimal DFA have?**

- a.) 5 states ❌
  > *Rationale:* Incorrect. '5 states' is a distractor. The correct answer is '3 states'.

- b.) 2 states ❌
  > *Rationale:* Incorrect. '2 states' is a distractor. The correct answer is '3 states'.

- c.) 3 states ✅ **[CORRECT]**
  > *Rationale:* Correct! [Minimal DFA for Containing '01'] The minimal DFA requires 3 states: S0 (not seen 0), S1 (seen 0), and S2 (seen 01, accepting).

- d.) 4 states ❌
  > *Rationale:* Incorrect. '4 states' is a distractor. The correct answer is '3 states'.

💡 *Hint:* Concept: Minimal DFA for Containing '01'

---

### Question 29
**_____ 29. In Activity 3 Problem 2 ($L2 = {strings starting with '10'}$), what is the regular expression?**

- a.) 10 (0 + 1)* ✅ **[CORRECT]**
  > *Rationale:* Correct! [Regex for Starting with '10'] Strings that start with '10' followed by any sequence of symbols are given by 10 (0 + 1)*.

- b.) (10)* ❌
  > *Rationale:* Incorrect. '(10)*' is a distractor. The correct answer is '10 (0 + 1)*'.

- c.) (0 + 1)* 10 ❌
  > *Rationale:* Incorrect. '(0 + 1)* 10' is a distractor. The correct answer is '10 (0 + 1)*'.

- d.) 1 (0 + 1)* 0 ❌
  > *Rationale:* Incorrect. '1 (0 + 1)* 0' is a distractor. The correct answer is '10 (0 + 1)*'.

💡 *Hint:* Concept: Regex for Starting with '10'

---

### Question 30
**_____ 30. In Activity 3 Problem 2 ($L2 = {strings starting with '10'}$), why does the converted DFA require a Trap state?**

- a.) To permanently reject any string whose prefix is not '10' ✅ **[CORRECT]**
  > *Rationale:* Correct! [Trap State in Starting with '10'] Any string starting with '0' or '11' violates the required prefix '10' and must be diverted to an inescapable trap state.

- b.) To loop on final states ❌
  > *Rationale:* Incorrect. 'To loop on final states' is a distractor. The correct answer is 'To permanently reject any string whose prefix is not '10''.

- c.) To handle epsilon transitions ❌
  > *Rationale:* Incorrect. 'To handle epsilon transitions' is a distractor. The correct answer is 'To permanently reject any string whose prefix is not '10''.

- d.) To store stack memory ❌
  > *Rationale:* Incorrect. 'To store stack memory' is a distractor. The correct answer is 'To permanently reject any string whose prefix is not '10''.

💡 *Hint:* Concept: Trap State in Starting with '10'

---

### Question 31
**_____ 31. In Activity 3 Problem 4 ($L4 = {strings ending with '1'}$), what is the regular expression?**

- a.) 1 (0 + 1)* ❌
  > *Rationale:* Incorrect. '1 (0 + 1)*' is a distractor. The correct answer is '(0 + 1)* 1'.

- b.) (0 + 1)* 1 ✅ **[CORRECT]**
  > *Rationale:* Correct! [Regex for Ending with '1'] Any string ending with '1' is matched by (0 + 1)* 1.

- c.) (01)* ❌
  > *Rationale:* Incorrect. '(01)*' is a distractor. The correct answer is '(0 + 1)* 1'.

- d.) (1)* ❌
  > *Rationale:* Incorrect. '(1)*' is a distractor. The correct answer is '(0 + 1)* 1'.

💡 *Hint:* Concept: Regex for Ending with '1'

---

### Question 32
**_____ 32. In Activity 3 Problem 5 ($L5 = {strings ending with '11'}$), how many states does the equivalent minimal DFA contain?**

- a.) 4 states ❌
  > *Rationale:* Incorrect. '4 states' is a distractor. The correct answer is '3 states'.

- b.) 2 states ❌
  > *Rationale:* Incorrect. '2 states' is a distractor. The correct answer is '3 states'.

- c.) 3 states ✅ **[CORRECT]**
  > *Rationale:* Correct! [DFA for Ending with '11'] Matching strings ending with '11' requires 3 DFA states: S0 (no trailing 1), S1 (one trailing 1), and S2 (two or more trailing 1s, accepting).

- d.) 5 states ❌
  > *Rationale:* Incorrect. '5 states' is a distractor. The correct answer is '3 states'.

💡 *Hint:* Concept: DFA for Ending with '11'

---

### Question 33
**_____ 33. In Activity 3 Problem 3 ($L3 = {strings containing '0'}$), what is the minimal number of states in the equivalent DFA?**

- a.) 4 states ❌
  > *Rationale:* Incorrect. '4 states' is a distractor. The correct answer is '2 states'.

- b.) 2 states ✅ **[CORRECT]**
  > *Rationale:* Correct! [DFA for Containing '0'] Only 2 states are needed: state A (seen only 1s, non-accepting) and state B (seen at least one 0, accepting).

- c.) 3 states ❌
  > *Rationale:* Incorrect. '3 states' is a distractor. The correct answer is '2 states'.

- d.) 1 state ❌
  > *Rationale:* Incorrect. '1 state' is a distractor. The correct answer is '2 states'.

💡 *Hint:* Concept: DFA for Containing '0'

---

### Question 34
**_____ 34. In an ε-NFA, the set of all states that can be reached from a state q using only empty transitions (ε-moves) without consuming any input is called the ____ of q.**

- a.) transition matrix ❌
  > *Rationale:* Incorrect. 'transition matrix' is a distractor. The correct answer is 'ε-closure (Epsilon closure)'.

- b.) power set ❌
  > *Rationale:* Incorrect. 'power set' is a distractor. The correct answer is 'ε-closure (Epsilon closure)'.

- c.) ε-closure (Epsilon closure) ✅ **[CORRECT]**
  > *Rationale:* Correct! [Epsilon Closure Definition] The ε-closure(q) is the set of all states reachable from state q by following zero or more ε-transitions.

- d.) Kleene closure ❌
  > *Rationale:* Incorrect. 'Kleene closure' is a distractor. The correct answer is 'ε-closure (Epsilon closure)'.

💡 *Hint:* Concept: Epsilon Closure Definition

---

### Question 35
**_____ 35. The ε-closure of any state q always contains at least ____.**

- a.) the initial state ❌
  > *Rationale:* Incorrect. 'the initial state' is a distractor. The correct answer is 'the state q itself'.

- b.) the empty set ❌
  > *Rationale:* Incorrect. 'the empty set' is a distractor. The correct answer is 'the state q itself'.

- c.) the state q itself ✅ **[CORRECT]**
  > *Rationale:* Correct! [Epsilon Closure Self-Inclusion] Because a state is reachable from itself via zero ε-moves (path of length 0), q ∈ ε-closure(q) always.

- d.) the final state ❌
  > *Rationale:* Incorrect. 'the final state' is a distractor. The correct answer is 'the state q itself'.

💡 *Hint:* Concept: Epsilon Closure Self-Inclusion

---

### Question 36
**_____ 36. In Activity 3 Problem 1 ($L1 = {strings containing '01'}$), the DFA created by subset construction has 4 reachable states before minimization: A = {q0}, B = {q0, q1}, C = {q0, q2}, and D = {q0, q1, q2}. Which states are accepting?**

- a.) Only State C ❌
  > *Rationale:* Incorrect. 'Only State C' is a distractor. The correct answer is 'States C and D (both contain q2)'.

- b.) States C and D (both contain q2) ✅ **[CORRECT]**
  > *Rationale:* Correct! [Activity 3 Problem 1 Accepting States] Because q2 is the accepting state in the NFA, any subset containing q2 (namely C and D) is an accepting state in the DFA.

- c.) States A and B ❌
  > *Rationale:* Incorrect. 'States A and B' is a distractor. The correct answer is 'States C and D (both contain q2)'.

- d.) Only State D ❌
  > *Rationale:* Incorrect. 'Only State D' is a distractor. The correct answer is 'States C and D (both contain q2)'.

💡 *Hint:* Concept: Activity 3 Problem 1 Accepting States

---

### Question 37
**_____ 37. In Activity 3 Problem 1, why can states C = {q0, q2} and D = {q0, q1, q2} be merged during DFA minimization?**

- a.) Because both have dead configurations ❌
  > *Rationale:* Incorrect. 'Because both have dead configurations' is a distractor. The correct answer is 'Both states transition to D on '0' and to C on '1', making them equivalent'.

- b.) Because state D is unreachable ❌
  > *Rationale:* Incorrect. 'Because state D is unreachable' is a distractor. The correct answer is 'Both states transition to D on '0' and to C on '1', making them equivalent'.

- c.) Because both are initial states ❌
  > *Rationale:* Incorrect. 'Because both are initial states' is a distractor. The correct answer is 'Both states transition to D on '0' and to C on '1', making them equivalent'.

- d.) Both states transition to D on '0' and to C on '1', making them equivalent ✅ **[CORRECT]**
  > *Rationale:* Correct! [State Equivalence in Minimization] States C and D have identical transition outputs on all alphabet symbols (0 -> D, 1 -> C) and are both accepting, proving they are indistinguishable/equivalent.

💡 *Hint:* Concept: State Equivalence in Minimization

---

### Question 38
**_____ 38. In subset construction, states in the power set that cannot be reached by any sequence of transitions starting from the initial state are called ____ states.**

- a.) trap ❌
  > *Rationale:* Incorrect. 'trap' is a distractor. The correct answer is 'unreachable (inaccessible)'.

- b.) unreachable (inaccessible) ✅ **[CORRECT]**
  > *Rationale:* Correct! [Unreachable States in Subset Construction] While 2^Q possible subsets exist, typically only a small fraction are reachable from the start state, and unreachable subsets are discarded.

- c.) deterministic ❌
  > *Rationale:* Incorrect. 'deterministic' is a distractor. The correct answer is 'unreachable (inaccessible)'.

- d.) final ❌
  > *Rationale:* Incorrect. 'final' is a distractor. The correct answer is 'unreachable (inaccessible)'.

💡 *Hint:* Concept: Unreachable States in Subset Construction

---

### Question 39
**_____ 39. The famous algorithmic technique that converts any Regular Expression into an equivalent ε-NFA is known as ____ Construction.**

- a.) Thompson's ✅ **[CORRECT]**
  > *Rationale:* Correct! [Thompson's Construction] Thompson's construction algorithm systematically converts regular expressions into ε-NFAs using base cases and structural induction.

- b.) Moore's ❌
  > *Rationale:* Incorrect. 'Moore's' is a distractor. The correct answer is 'Thompson's'.

- c.) Turing's ❌
  > *Rationale:* Incorrect. 'Turing's' is a distractor. The correct answer is 'Thompson's'.

- d.) Chomsky's ❌
  > *Rationale:* Incorrect. 'Chomsky's' is a distractor. The correct answer is 'Thompson's'.

💡 *Hint:* Concept: Thompson's Construction

---

### Question 40
**_____ 40. In an NFA, when multiple transitions exist for the same input symbol from a single state, how does the machine conceptually process them?**

- a.) It crashes with a runtime error ❌
  > *Rationale:* Incorrect. 'It crashes with a runtime error' is a distractor. The correct answer is 'It explores all possible execution paths simultaneously in parallel'.

- b.) It prompts the user for a choice ❌
  > *Rationale:* Incorrect. 'It prompts the user for a choice' is a distractor. The correct answer is 'It explores all possible execution paths simultaneously in parallel'.

- c.) It explores all possible execution paths simultaneously in parallel ✅ **[CORRECT]**
  > *Rationale:* Correct! [Parallel Branching Concept] Non-determinism can be conceptualized as cloning the machine at each branch point to explore all computational trajectories in parallel.

- d.) It always chooses the alphabetically first state ❌
  > *Rationale:* Incorrect. 'It always chooses the alphabetically first state' is a distractor. The correct answer is 'It explores all possible execution paths simultaneously in parallel'.

💡 *Hint:* Concept: Parallel Branching Concept

---

### Question 41
**_____ 41. An NFA with n states that recognizes a language can always be converted into an equivalent DFA with at most ____ states.**

- a.) 2^n ✅ **[CORRECT]**
  > *Rationale:* Correct! [NFA to DFA State Upper Bound] By subset construction, the maximum number of states in the equivalent DFA is 2^n.

- b.) n! ❌
  > *Rationale:* Incorrect. 'n!' is a distractor. The correct answer is '2^n'.

- c.) n^2 ❌
  > *Rationale:* Incorrect. 'n^2' is a distractor. The correct answer is '2^n'.

- d.) 2n ❌
  > *Rationale:* Incorrect. '2n' is a distractor. The correct answer is '2^n'.

💡 *Hint:* Concept: NFA to DFA State Upper Bound

---

### Question 42
**_____ 42. In an NFA transition table, an entry with the symbol ϕ indicates that ____.**

- a.) the state is an accepting state ❌
  > *Rationale:* Incorrect. 'the state is an accepting state' is a distractor. The correct answer is 'no transition is defined for that state and input symbol'.

- b.) an epsilon transition occurs ❌
  > *Rationale:* Incorrect. 'an epsilon transition occurs' is a distractor. The correct answer is 'no transition is defined for that state and input symbol'.

- c.) no transition is defined for that state and input symbol ✅ **[CORRECT]**
  > *Rationale:* Correct! [Phi Symbol in Transition Table] The symbol ϕ (or ∅) in a transition table denotes the empty set, indicating no valid next state exists for that input.

- d.) the machine loops infinitely ❌
  > *Rationale:* Incorrect. 'the machine loops infinitely' is a distractor. The correct answer is 'no transition is defined for that state and input symbol'.

💡 *Hint:* Concept: Phi Symbol in Transition Table

---

### Question 43
**_____ 43. In Activity 3 Problem 5 (strings ending with '11'), what is the transition from DFA state B = {q0, q1} on input '1'?**

- a.) State A = {q0} ❌
  > *Rationale:* Incorrect. 'State A = {q0}' is a distractor. The correct answer is 'State C = {q0, q1, q2} (Accepting)'.

- b.) Trap state ❌
  > *Rationale:* Incorrect. 'Trap state' is a distractor. The correct answer is 'State C = {q0, q1, q2} (Accepting)'.

- c.) State C = {q0, q1, q2} (Accepting) ✅ **[CORRECT]**
  > *Rationale:* Correct! [Activity 3 Problem 5 Transition on '1'] From B = {q0, q1}, on input 1: δ(q0, 1) = {q0, q1} and δ(q1, 1) = {q2}. The union is {q0, q1, q2} = C (accepting).

- d.) State B = {q0, q1} ❌
  > *Rationale:* Incorrect. 'State B = {q0, q1}' is a distractor. The correct answer is 'State C = {q0, q1, q2} (Accepting)'.

💡 *Hint:* Concept: Activity 3 Problem 5 Transition on '1'

---

### Question 44
**_____ 44. In Activity 3 Problem 5 (strings ending with '11'), what is the transition from DFA state C = {q0, q1, q2} on input '0'?**

- a.) State B = {q0, q1} ❌
  > *Rationale:* Incorrect. 'State B = {q0, q1}' is a distractor. The correct answer is 'State A = {q0}'.

- b.) Trap state ❌
  > *Rationale:* Incorrect. 'Trap state' is a distractor. The correct answer is 'State A = {q0}'.

- c.) State A = {q0} ✅ **[CORRECT]**
  > *Rationale:* Correct! [Activity 3 Problem 5 Transition on '0'] From C, on input 0: δ(q0, 0) = {q0}, δ(q1, 0) = ∅, and δ(q2, 0) = ∅. The union is {q0} = State A.

- d.) State C = {q0, q1, q2} ❌
  > *Rationale:* Incorrect. 'State C = {q0, q1, q2}' is a distractor. The correct answer is 'State A = {q0}'.

💡 *Hint:* Concept: Activity 3 Problem 5 Transition on '0'

---

### Question 45
**_____ 45. Which of the following computational characteristics is shared by BOTH DFAs and NFAs?**

- a.) Both allow epsilon transitions ❌
  > *Rationale:* Incorrect. 'Both allow epsilon transitions' is a distractor. The correct answer is 'Both recognize exactly the class of Regular Languages'.

- b.) Both require exactly one next state per symbol ❌
  > *Rationale:* Incorrect. 'Both require exactly one next state per symbol' is a distractor. The correct answer is 'Both recognize exactly the class of Regular Languages'.

- c.) Both require unique deterministic transitions ❌
  > *Rationale:* Incorrect. 'Both require unique deterministic transitions' is a distractor. The correct answer is 'Both recognize exactly the class of Regular Languages'.

- d.) Both recognize exactly the class of Regular Languages ✅ **[CORRECT]**
  > *Rationale:* Correct! [Shared DFA and NFA Characteristics] DFAs and NFAs are computationally equivalent in language recognition power—both define and recognize Regular Languages.

💡 *Hint:* Concept: Shared DFA and NFA Characteristics

---
