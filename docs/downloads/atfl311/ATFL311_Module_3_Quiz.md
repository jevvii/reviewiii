# ATFL311: Automata Theory & Formal Languages — Module 3: Deterministic Finite Automata (DFA)
*Total Questions: 41 Items | Format: Identification with Multiple Choices*

---

### Question 1
**_____ 1. A finite state machine where for every state and for every input symbol there is exactly one unique next state, with no empty transitions allowed, is a ____ Finite Automaton.**

- a.) Deterministic ✅ **[CORRECT]**
  > *Rationale:* Correct! [DFA Core Definition] In a Deterministic Finite Automaton (DFA), the transition function is deterministic—for each state and input symbol, there is exactly one specified next state.

- b.) Non-Deterministic ❌
  > *Rationale:* Incorrect. 'Non-Deterministic' is a distractor. The correct answer is 'Deterministic'.

- c.) Linear Bounded ❌
  > *Rationale:* Incorrect. 'Linear Bounded' is a distractor. The correct answer is 'Deterministic'.

- d.) Pushdown ❌
  > *Rationale:* Incorrect. 'Pushdown' is a distractor. The correct answer is 'Deterministic'.

💡 *Hint:* Concept: DFA Core Definition

---

### Question 2
**_____ 2. A fundamental rule of Deterministic Finite Automata is that empty moves (transitions without consuming an input symbol, known as ε-moves) are ____.**

- a.) required at every state ❌
  > *Rationale:* Incorrect. 'required at every state' is a distractor. The correct answer is 'strictly prohibited (not allowed)'.

- b.) unrestricted ❌
  > *Rationale:* Incorrect. 'unrestricted' is a distractor. The correct answer is 'strictly prohibited (not allowed)'.

- c.) strictly prohibited (not allowed) ✅ **[CORRECT]**
  > *Rationale:* Correct! [No Epsilon Moves in DFA] DFAs never permit empty ε-transitions; every transition must consume exactly one symbol from the input alphabet.

- d.) optional in final states ❌
  > *Rationale:* Incorrect. 'optional in final states' is a distractor. The correct answer is 'strictly prohibited (not allowed)'.

💡 *Hint:* Concept: No Epsilon Moves in DFA

---

### Question 3
**_____ 3. Because a DFA has exactly one transition for each (state, symbol) pair, the computational path for any given input string is completely ____.**

- a.) branching into parallel universes ❌
  > *Rationale:* Incorrect. 'branching into parallel universes' is a distractor. The correct answer is 'unique and predictable'.

- b.) unique and predictable ✅ **[CORRECT]**
  > *Rationale:* Correct! [Deterministic Execution] Given an initial state and input string, a DFA follows a single, unambiguous sequence of state transitions.

- c.) random ❌
  > *Rationale:* Incorrect. 'random' is a distractor. The correct answer is 'unique and predictable'.

- d.) probabilistic ❌
  > *Rationale:* Incorrect. 'probabilistic' is a distractor. The correct answer is 'unique and predictable'.

💡 *Hint:* Concept: Deterministic Execution

---

### Question 4
**_____ 4. A non-accepting state in a DFA from which the machine can never escape, looping on all input symbols, is known as a dead state or ____ state.**

- a.) transducer ❌
  > *Rationale:* Incorrect. 'transducer' is a distractor. The correct answer is 'trap'.

- b.) trap ✅ **[CORRECT]**
  > *Rationale:* Correct! [Trap / Dead State Concept] A dead state (or trap state) is an absorbing non-final state where all outgoing transitions loop back to itself, ensuring rejection of the string.

- c.) subordinate ❌
  > *Rationale:* Incorrect. 'subordinate' is a distractor. The correct answer is 'trap'.

- d.) initial ❌
  > *Rationale:* Incorrect. 'initial' is a distractor. The correct answer is 'trap'.

💡 *Hint:* Concept: Trap / Dead State Concept

---

### Question 5
**_____ 5. In the DFA that accepts all strings starting with '0' over Σ = {0, 1} (Example 1), what happens when the first symbol read from start state A is '0'?**

- a.) The machine transitions to accepting state B ✅ **[CORRECT]**
  > *Rationale:* Correct! [Strings Starting with '0' Acceptance] In Example 1, on input '0' from start state A, the machine moves to state B (double circle), which is accepting.

- b.) The machine halts and rejects ❌
  > *Rationale:* Incorrect. 'The machine halts and rejects' is a distractor. The correct answer is 'The machine transitions to accepting state B'.

- c.) The machine resets to state A ❌
  > *Rationale:* Incorrect. 'The machine resets to state A' is a distractor. The correct answer is 'The machine transitions to accepting state B'.

- d.) The machine enters trap state C ❌
  > *Rationale:* Incorrect. 'The machine enters trap state C' is a distractor. The correct answer is 'The machine transitions to accepting state B'.

💡 *Hint:* Concept: Strings Starting with '0' Acceptance

---

### Question 6
**_____ 6. In the DFA for strings starting with '0' (Example 1), what happens when the first symbol read from start state A is '1'?**

- a.) The machine loops at state A ❌
  > *Rationale:* Incorrect. 'The machine loops at state A' is a distractor. The correct answer is 'The machine transitions to dead/trap state C'.

- b.) The machine transitions to dead/trap state C ✅ **[CORRECT]**
  > *Rationale:* Correct! [Strings Starting with '0' Rejection] Any string beginning with '1' violates the condition and is routed immediately to trap state C, where it remains.

- c.) The machine transitions to accepting state B ❌
  > *Rationale:* Incorrect. 'The machine transitions to accepting state B' is a distractor. The correct answer is 'The machine transitions to dead/trap state C'.

- d.) The machine produces an output token ❌
  > *Rationale:* Incorrect. 'The machine produces an output token' is a distractor. The correct answer is 'The machine transitions to dead/trap state C'.

💡 *Hint:* Concept: Strings Starting with '0' Rejection

---

### Question 7
**_____ 7. In the DFA for strings starting with '0' (Example 1), once the machine reaches accepting state B, what are its transitions on inputs 0 and 1?**

- a.) It returns to start state A on 0 ❌
  > *Rationale:* Incorrect. 'It returns to start state A on 0' is a distractor. The correct answer is 'It loops on state B for both 0 and 1'.

- b.) It transitions to state C on 1 ❌
  > *Rationale:* Incorrect. 'It transitions to state C on 1' is a distractor. The correct answer is 'It loops on state B for both 0 and 1'.

- c.) It loops on state B for both 0 and 1 ✅ **[CORRECT]**
  > *Rationale:* Correct! [State B Self-Loop] Once a string is confirmed to start with '0', any subsequent symbols (0 or 1) do not change the fact that it started with '0', so state B loops on 0,1.

- d.) It halts immediately ❌
  > *Rationale:* Incorrect. 'It halts immediately' is a distractor. The correct answer is 'It loops on state B for both 0 and 1'.

💡 *Hint:* Concept: State B Self-Loop

---

### Question 8
**_____ 8. How many total states are required in the minimal DFA for the language L = {strings starting with '0'} over alphabet Σ = {0, 1}?**

- a.) 3 states (Start A, Final B, Trap C) ✅ **[CORRECT]**
  > *Rationale:* Correct! [State Count for Prefix Language] The minimal DFA requires exactly 3 states: A (start), B (accepting), and C (trap state for strings starting with 1).

- b.) 5 states ❌
  > *Rationale:* Incorrect. '5 states' is a distractor. The correct answer is '3 states (Start A, Final B, Trap C)'.

- c.) 4 states ❌
  > *Rationale:* Incorrect. '4 states' is a distractor. The correct answer is '3 states (Start A, Final B, Trap C)'.

- d.) 2 states ❌
  > *Rationale:* Incorrect. '2 states' is a distractor. The correct answer is '3 states (Start A, Final B, Trap C)'.

💡 *Hint:* Concept: State Count for Prefix Language

---

### Question 9
**_____ 9. In DFA Example 2, the language consists of all strings over Σ = {0, 1} of length exactly 2. How many strings are in this language?**

- a.) 4 strings ({00, 01, 10, 11}) ✅ **[CORRECT]**
  > *Rationale:* Correct! [Length 2 Language Cardinality] Over Σ = {0, 1}, the strings of length 2 are 00, 01, 10, and 11, giving a cardinality of 4.

- b.) 16 strings ❌
  > *Rationale:* Incorrect. '16 strings' is a distractor. The correct answer is '4 strings ({00, 01, 10, 11})'.

- c.) 2 strings ❌
  > *Rationale:* Incorrect. '2 strings' is a distractor. The correct answer is '4 strings ({00, 01, 10, 11})'.

- d.) 8 strings ❌
  > *Rationale:* Incorrect. '8 strings' is a distractor. The correct answer is '4 strings ({00, 01, 10, 11})'.

💡 *Hint:* Concept: Length 2 Language Cardinality

---

### Question 10
**_____ 10. In the DFA for strings of exact length 2 (Example 2), state C represents having consumed a string of length ____.**

- a.) 3 ❌
  > *Rationale:* Incorrect. '3' is a distractor. The correct answer is '2'.

- b.) 2 ✅ **[CORRECT]**
  > *Rationale:* Correct! [Length 2 Accepting State] State A represents length 0, state B represents length 1, and state C represents length 2 (accepting).

- c.) 0 ❌
  > *Rationale:* Incorrect. '0' is a distractor. The correct answer is '2'.

- d.) 1 ❌
  > *Rationale:* Incorrect. '1' is a distractor. The correct answer is '2'.

💡 *Hint:* Concept: Length 2 Accepting State

---

### Question 11
**_____ 11. In the DFA for strings of exact length 2 (Example 2), which state is the ONLY accepting / final state?**

- a.) State A ❌
  > *Rationale:* Incorrect. 'State A' is a distractor. The correct answer is 'State C'.

- b.) State B ❌
  > *Rationale:* Incorrect. 'State B' is a distractor. The correct answer is 'State C'.

- c.) State D ❌
  > *Rationale:* Incorrect. 'State D' is a distractor. The correct answer is 'State C'.

- d.) State C ✅ **[CORRECT]**
  > *Rationale:* Correct! [Exact Length 2 Final State] State C is the only state designated with a double circle, representing acceptance of strings with length exactly 2.

💡 *Hint:* Concept: Exact Length 2 Final State

---

### Question 12
**_____ 12. In the DFA for strings of exact length 2 (Example 2), what happens if a third symbol is read after reaching state C?**

- a.) The machine remains in state C ❌
  > *Rationale:* Incorrect. 'The machine remains in state C' is a distractor. The correct answer is 'The machine transitions to dead/trap state D'.

- b.) The machine resets to state A ❌
  > *Rationale:* Incorrect. 'The machine resets to state A' is a distractor. The correct answer is 'The machine transitions to dead/trap state D'.

- c.) The machine accepts ❌
  > *Rationale:* Incorrect. 'The machine accepts' is a distractor. The correct answer is 'The machine transitions to dead/trap state D'.

- d.) The machine transitions to dead/trap state D ✅ **[CORRECT]**
  > *Rationale:* Correct! [Exceeding Length 2] Reading a third symbol exceeds the required length of 2, transitioning the automaton to trap state D, which loops on 0,1.

💡 *Hint:* Concept: Exceeding Length 2

---

### Question 13
**_____ 13. In DFA Example 3, the language requires accepting all strings over Σ = {a, b} that contain the substring '____'.**

- a.) abab ❌
  > *Rationale:* Incorrect. 'abab' is a distractor. The correct answer is 'aabb'.

- b.) aabb ✅ **[CORRECT]**
  > *Rationale:* Correct! [Substring 'aabb' Language] Example 3 constructs a pattern matcher for the specific substring 'aabb'.

- c.) abba ❌
  > *Rationale:* Incorrect. 'abba' is a distractor. The correct answer is 'aabb'.

- d.) bbaa ❌
  > *Rationale:* Incorrect. 'bbaa' is a distractor. The correct answer is 'aabb'.

💡 *Hint:* Concept: Substring 'aabb' Language

---

### Question 14
**_____ 14. In the DFA for substring 'aabb', how many sequential prefix tracking states are used to reach the final state?**

- a.) 4 states ❌
  > *Rationale:* Incorrect. '4 states' is a distractor. The correct answer is '5 states (A, B, C, D, E)'.

- b.) 6 states ❌
  > *Rationale:* Incorrect. '6 states' is a distractor. The correct answer is '5 states (A, B, C, D, E)'.

- c.) 3 states ❌
  > *Rationale:* Incorrect. '3 states' is a distractor. The correct answer is '5 states (A, B, C, D, E)'.

- d.) 5 states (A, B, C, D, E) ✅ **[CORRECT]**
  > *Rationale:* Correct! [Substring Matching State Count] States correspond to prefix lengths: A (empty), B (saw 'a'), C (saw 'aa'), D (saw 'aab'), and E (saw 'aabb', accepting).

💡 *Hint:* Concept: Substring Matching State Count

---

### Question 15
**_____ 15. In the DFA for substring 'aabb', what is the transition from state C (which represents having seen 'aa') on input 'a'?**

- a.) It loops back to state C ✅ **[CORRECT]**
  > *Rationale:* Correct! [State C Overlap Loop] If the automaton has seen 'aa' (state C) and receives another 'a', the longest relevant prefix is still 'aa', so it loops at state C.

- b.) It resets to start state A ❌
  > *Rationale:* Incorrect. 'It resets to start state A' is a distractor. The correct answer is 'It loops back to state C'.

- c.) It transitions to state B ❌
  > *Rationale:* Incorrect. 'It transitions to state B' is a distractor. The correct answer is 'It loops back to state C'.

- d.) It advances to state D ❌
  > *Rationale:* Incorrect. 'It advances to state D' is a distractor. The correct answer is 'It loops back to state C'.

💡 *Hint:* Concept: State C Overlap Loop

---

### Question 16
**_____ 16. In the DFA for substring 'aabb', from state D (having seen 'aab'), what happens if the next input is 'a'?**

- a.) It returns to state B (representing prefix 'a') ✅ **[CORRECT]**
  > *Rationale:* Correct! [State D Mismatch Fallback] After 'aab', receiving 'a' yields suffix 'a', which is represented by state B (prefix 'a').

- b.) It loops at state D ❌
  > *Rationale:* Incorrect. 'It loops at state D' is a distractor. The correct answer is 'It returns to state B (representing prefix 'a')'.

- c.) It advances to final state E ❌
  > *Rationale:* Incorrect. 'It advances to final state E' is a distractor. The correct answer is 'It returns to state B (representing prefix 'a')'.

- d.) It resets to start state A ❌
  > *Rationale:* Incorrect. 'It resets to start state A' is a distractor. The correct answer is 'It returns to state B (representing prefix 'a')'.

💡 *Hint:* Concept: State D Mismatch Fallback

---

### Question 17
**_____ 17. In the DFA for substring 'aabb', once final state E is reached, what are its outgoing transitions?**

- a.) It loops on both 'a' and 'b' ✅ **[CORRECT]**
  > *Rationale:* Correct! [Substring Found Absorbing State] Once the substring 'aabb' has appeared anywhere in the string, the condition is satisfied forever, so state E loops on {a, b}.

- b.) It transitions to a trap state ❌
  > *Rationale:* Incorrect. 'It transitions to a trap state' is a distractor. The correct answer is 'It loops on both 'a' and 'b''.

- c.) It halts immediately ❌
  > *Rationale:* Incorrect. 'It halts immediately' is a distractor. The correct answer is 'It loops on both 'a' and 'b''.

- d.) It returns to state A on 'b' ❌
  > *Rationale:* Incorrect. 'It returns to state A on 'b'' is a distractor. The correct answer is 'It loops on both 'a' and 'b''.

💡 *Hint:* Concept: Substring Found Absorbing State

---

### Question 18
**_____ 18. To construct a DFA that accepts strings that DO NOT contain the substring 'aabb' (the complement language), what systematic transformation is applied to the DFA that accepts 'aabb'?**

- a.) Add an epsilon transition ❌
  > *Rationale:* Incorrect. 'Add an epsilon transition' is a distractor. The correct answer is 'Invert (flip) all final and non-final states'.

- b.) Invert (flip) all final and non-final states ✅ **[CORRECT]**
  > *Rationale:* Correct! [DFA Complementation Algorithm] To complement a DFA, keep the exact same state set and transitions, but set F' = Q \ F (non-accepting states become accepting, and vice-versa).

- c.) Reverse all transition arrow directions ❌
  > *Rationale:* Incorrect. 'Reverse all transition arrow directions' is a distractor. The correct answer is 'Invert (flip) all final and non-final states'.

- d.) Remove all self-loops ❌
  > *Rationale:* Incorrect. 'Remove all self-loops' is a distractor. The correct answer is 'Invert (flip) all final and non-final states'.

💡 *Hint:* Concept: DFA Complementation Algorithm

---

### Question 19
**_____ 19. In Example 3a (the complement of 'aabb'), which states become the accepting (final) states?**

- a.) {A, B, C, D} ✅ **[CORRECT]**
  > *Rationale:* Correct! [Complement Accepting States] The original non-accepting states {A, B, C, D} all become accepting states (marked with double circles).

- b.) {B, C, D} ❌
  > *Rationale:* Incorrect. '{B, C, D}' is a distractor. The correct answer is '{A, B, C, D}'.

- c.) {E} ❌
  > *Rationale:* Incorrect. '{E}' is a distractor. The correct answer is '{A, B, C, D}'.

- d.) {A, E} ❌
  > *Rationale:* Incorrect. '{A, E}' is a distractor. The correct answer is '{A, B, C, D}'.

💡 *Hint:* Concept: Complement Accepting States

---

### Question 20
**_____ 20. In Example 3a (the complement of 'aabb'), what state becomes the sole non-accepting (rejecting) state?**

- a.) State A ❌
  > *Rationale:* Incorrect. 'State A' is a distractor. The correct answer is 'State E'.

- b.) State E ✅ **[CORRECT]**
  > *Rationale:* Correct! [Complement Rejecting State] State E (which previously accepted 'aabb') becomes the only non-accepting state.

- c.) State C ❌
  > *Rationale:* Incorrect. 'State C' is a distractor. The correct answer is 'State E'.

- d.) State B ❌
  > *Rationale:* Incorrect. 'State B' is a distractor. The correct answer is 'State E'.

💡 *Hint:* Concept: Complement Rejecting State

---

### Question 21
**_____ 21. The closure property of Regular Languages demonstrating that the complement of any regular language is also regular is proven by the ability to ____ a DFA.**

- a.) tokenize ❌
  > *Rationale:* Incorrect. 'tokenize' is a distractor. The correct answer is 'invert (complement)'.

- b.) nondeterminize ❌
  > *Rationale:* Incorrect. 'nondeterminize' is a distractor. The correct answer is 'invert (complement)'.

- c.) minimize ❌
  > *Rationale:* Incorrect. 'minimize' is a distractor. The correct answer is 'invert (complement)'.

- d.) invert (complement) ✅ **[CORRECT]**
  > *Rationale:* Correct! [Closure Under Complementation] Because flipping the accept/reject status of DFA states yields another valid DFA, Regular Languages are closed under complementation.

💡 *Hint:* Concept: Closure Under Complementation

---

### Question 22
**_____ 22. In Example 4, an automaton has start state A, intermediate states B and D, accepting states C and E, and dead state X. Tracing path A -> B -> C on inputs 1 then 0 accepts the string '____'.**

- a.) 01 ❌
  > *Rationale:* Incorrect. '01' is a distractor. The correct answer is '10'.

- b.) 00 ❌
  > *Rationale:* Incorrect. '00' is a distractor. The correct answer is '10'.

- c.) 10 ✅ **[CORRECT]**
  > *Rationale:* Correct! [Example 4 Path Trace '10'] From A, on input 1 it reaches B; from B, on input 0 it reaches accepting state C. Thus '10' is accepted.

- d.) 11 ❌
  > *Rationale:* Incorrect. '11' is a distractor. The correct answer is '10'.

💡 *Hint:* Concept: Example 4 Path Trace '10'

---

### Question 23
**_____ 23. In Example 4, tracing path A -> D -> E on inputs 0 then 1 accepts the string '____'.**

- a.) 00 ❌
  > *Rationale:* Incorrect. '00' is a distractor. The correct answer is '01'.

- b.) 01 ✅ **[CORRECT]**
  > *Rationale:* Correct! [Example 4 Path Trace '01'] From A, on input 0 it reaches D; from D, on input 1 it reaches accepting state E. Thus '01' is accepted.

- c.) 10 ❌
  > *Rationale:* Incorrect. '10' is a distractor. The correct answer is '01'.

- d.) 11 ❌
  > *Rationale:* Incorrect. '11' is a distractor. The correct answer is '01'.

💡 *Hint:* Concept: Example 4 Path Trace '01'

---

### Question 24
**_____ 24. In Example 4, what happens if any additional symbol is received after reaching accepting state C or E?**

- a.) The machine halts ❌
  > *Rationale:* Incorrect. 'The machine halts' is a distractor. The correct answer is 'The machine transitions to dead state X and rejects'.

- b.) The machine transitions to dead state X and rejects ✅ **[CORRECT]**
  > *Rationale:* Correct! [Example 4 Transition to Dead State] States C and E have transitions on 0,1 pointing to dead state X, meaning only strings of length 2 ('10' and '01') are accepted.

- c.) The machine resets to state A ❌
  > *Rationale:* Incorrect. 'The machine resets to state A' is a distractor. The correct answer is 'The machine transitions to dead state X and rejects'.

- d.) The machine loops in the accepting state ❌
  > *Rationale:* Incorrect. 'The machine loops in the accepting state' is a distractor. The correct answer is 'The machine transitions to dead state X and rejects'.

💡 *Hint:* Concept: Example 4 Transition to Dead State

---

### Question 25
**_____ 25. The language recognized by the DFA in Example 4 is L = {____}.**

- a.) {0, 1} ❌
  > *Rationale:* Incorrect. '{0, 1}' is a distractor. The correct answer is '{01, 10}'.

- b.) {01, 10} ✅ **[CORRECT]**
  > *Rationale:* Correct! [Example 4 Language Identification] The DFA in Example 4 accepts strictly the two binary strings of length 2 with alternating digits: {01, 10}.

- c.) {00, 11} ❌
  > *Rationale:* Incorrect. '{00, 11}' is a distractor. The correct answer is '{01, 10}'.

- d.) {01, 10, 00, 11} ❌
  > *Rationale:* Incorrect. '{01, 10, 00, 11}' is a distractor. The correct answer is '{01, 10}'.

💡 *Hint:* Concept: Example 4 Language Identification

---

### Question 26
**_____ 26. In Activity 1, a DFA is constructed to accept all strings over alphabet Σ = {a, b, c} of length exactly 3. How many total strings are in this language?**

- a.) 81 strings ❌
  > *Rationale:* Incorrect. '81 strings' is a distractor. The correct answer is '27 strings (3^3)'.

- b.) 9 strings ❌
  > *Rationale:* Incorrect. '9 strings' is a distractor. The correct answer is '27 strings (3^3)'.

- c.) 27 strings (3^3) ✅ **[CORRECT]**
  > *Rationale:* Correct! [Ternary Alphabet Length 3] With an alphabet of 3 symbols {a, b, c}, the number of strings of length 3 is 3^3 = 27.

- d.) 8 strings ❌
  > *Rationale:* Incorrect. '8 strings' is a distractor. The correct answer is '27 strings (3^3)'.

💡 *Hint:* Concept: Ternary Alphabet Length 3

---

### Question 27
**_____ 27. In Activity 2, for the language L2 = {strings that start with '0' and end with '1'}, what happens to any string starting with '1'?**

- a.) It loops at the start state ❌
  > *Rationale:* Incorrect. 'It loops at the start state' is a distractor. The correct answer is 'It transitions immediately from the start state to a trap state'.

- b.) It transitions to the final state ❌
  > *Rationale:* Incorrect. 'It transitions to the final state' is a distractor. The correct answer is 'It transitions immediately from the start state to a trap state'.

- c.) It transitions immediately from the start state to a trap state ✅ **[CORRECT]**
  > *Rationale:* Correct! [Start 0 End 1 Rejection] Since the string must start with '0', any string beginning with '1' violates the prefix requirement and is trapped.

- d.) It is accepted ❌
  > *Rationale:* Incorrect. 'It is accepted' is a distractor. The correct answer is 'It transitions immediately from the start state to a trap state'.

💡 *Hint:* Concept: Start 0 End 1 Rejection

---

### Question 28
**_____ 28. In Activity 4, the given transition diagram has start state A looping on {0, 1}, transitioning on '1' to state B, and transitioning from B on {0, 1} to accepting state C. What language does this automaton recognize?**

- a.) All strings that end in '01' ❌
  > *Rationale:* Incorrect. 'All strings that end in '01'' is a distractor. The correct answer is 'All strings where the second symbol from the end is '1''.

- b.) All strings of length 2 ❌
  > *Rationale:* Incorrect. 'All strings of length 2' is a distractor. The correct answer is 'All strings where the second symbol from the end is '1''.

- c.) All strings where the second symbol from the end is '1' ✅ **[CORRECT]**
  > *Rationale:* Correct! [Second from Last Symbol '1'] Transitioning on 1 to B followed by any single symbol {0, 1} to final state C means the string must have '1' as its penultimate (second from end) symbol.

- d.) All strings that start with '1' ❌
  > *Rationale:* Incorrect. 'All strings that start with '1'' is a distractor. The correct answer is 'All strings where the second symbol from the end is '1''.

💡 *Hint:* Concept: Second from Last Symbol '1'

---

### Question 29
**_____ 29. In a DFA with alphabet Σ = {a, b, c} accepting strings containing substring 'abbc' (Activity 3), how many states are required in the forward matching sequence from start to final state?**

- a.) 3 states ❌
  > *Rationale:* Incorrect. '3 states' is a distractor. The correct answer is '5 states'.

- b.) 6 states ❌
  > *Rationale:* Incorrect. '6 states' is a distractor. The correct answer is '5 states'.

- c.) 4 states ❌
  > *Rationale:* Incorrect. '4 states' is a distractor. The correct answer is '5 states'.

- d.) 5 states ✅ **[CORRECT]**
  > *Rationale:* Correct! [Substring 'abbc' State Count] Matching a 4-character substring 'abbc' requires 5 states in sequence: ε, 'a', 'ab', 'abb', 'abbc' (accepting).

💡 *Hint:* Concept: Substring 'abbc' State Count

---

### Question 30
**_____ 30. In a DFA, if the start state q0 is also an accepting state (q0 ∈ F), the automaton accepts the ____ string.**

- a.) dead ❌
  > *Rationale:* Incorrect. 'dead' is a distractor. The correct answer is 'empty (ε)'.

- b.) infinite ❌
  > *Rationale:* Incorrect. 'infinite' is a distractor. The correct answer is 'empty (ε)'.

- c.) empty (ε) ✅ **[CORRECT]**
  > *Rationale:* Correct! [Empty String Acceptance in DFA] If the initial state q0 is a member of F, the machine accepts without reading any input symbols, meaning ε ∈ L(M).

- d.) undefined ❌
  > *Rationale:* Incorrect. 'undefined' is a distractor. The correct answer is 'empty (ε)'.

💡 *Hint:* Concept: Empty String Acceptance in DFA

---

### Question 31
**_____ 31. The property of a DFA that requires EVERY state to have an outgoing transition defined for EVERY symbol in alphabet Σ is known as the ____ condition.**

- a.) completeness (totality) ✅ **[CORRECT]**
  > *Rationale:* Correct! [Completeness Condition of DFA] A DFA's transition function is total: for every state q ∈ Q and symbol a ∈ Σ, δ(q, a) must be explicitly defined.

- b.) non-deterministic ❌
  > *Rationale:* Incorrect. 'non-deterministic' is a distractor. The correct answer is 'completeness (totality)'.

- c.) transductive ❌
  > *Rationale:* Incorrect. 'transductive' is a distractor. The correct answer is 'completeness (totality)'.

- d.) recursive ❌
  > *Rationale:* Incorrect. 'recursive' is a distractor. The correct answer is 'completeness (totality)'.

💡 *Hint:* Concept: Completeness Condition of DFA

---

### Question 32
**_____ 32. In automata theory, the extended transition function that maps a state and an entire string w of symbols to a resulting state is standardly denoted as ____.**

- a.) Σ* (Sigma star) ❌
  > *Rationale:* Incorrect. 'Σ* (Sigma star)' is a distractor. The correct answer is 'δ* (Delta star)'.

- b.) ε* (Epsilon star) ❌
  > *Rationale:* Incorrect. 'ε* (Epsilon star)' is a distractor. The correct answer is 'δ* (Delta star)'.

- c.) δ* (Delta star) ✅ **[CORRECT]**
  > *Rationale:* Correct! [Extended Transition Function] The extended transition function δ*: Q x Σ* -> Q computes the cumulative state transition resulting from processing an entire string.

- d.) Q* (Q star) ❌
  > *Rationale:* Incorrect. 'Q* (Q star)' is a distractor. The correct answer is 'δ* (Delta star)'.

💡 *Hint:* Concept: Extended Transition Function

---

### Question 33
**_____ 33. A formal representation of an automaton that uses a tabular matrix with current states as rows and input symbols as columns is a transition ____.**

- a.) table ✅ **[CORRECT]**
  > *Rationale:* Correct! [Transition Table] A transition table lists current states along the vertical axis and alphabet symbols along the horizontal axis, specifying next states in cell entries.

- b.) stack ❌
  > *Rationale:* Incorrect. 'stack' is a distractor. The correct answer is 'table'.

- c.) tree ❌
  > *Rationale:* Incorrect. 'tree' is a distractor. The correct answer is 'table'.

- d.) tape ❌
  > *Rationale:* Incorrect. 'tape' is a distractor. The correct answer is 'table'.

💡 *Hint:* Concept: Transition Table

---

### Question 34
**_____ 34. In a transition table, the start state is standardly annotated with an arrow (->) and accepting states are annotated with an ____.**

- a.) hashtag (#) ❌
  > *Rationale:* Incorrect. 'hashtag (#)' is a distractor. The correct answer is 'asterisk (*)'.

- b.) asterisk (*) ✅ **[CORRECT]**
  > *Rationale:* Correct! [Transition Table Annotations] In standard textbook notation, '->' marks the start state and '*' marks accepting/final states in a transition table.

- c.) ampersand (&) ❌
  > *Rationale:* Incorrect. 'ampersand (&)' is a distractor. The correct answer is 'asterisk (*)'.

- d.) exclamation mark (!) ❌
  > *Rationale:* Incorrect. 'exclamation mark (!)' is a distractor. The correct answer is 'asterisk (*)'.

💡 *Hint:* Concept: Transition Table Annotations

---

### Question 35
**_____ 35. In the DFA for substring 'aabb' (Example 3), if the machine is in state B (prefix 'a') and receives input 'b', why does it return to state A?**

- a.) Because it enters a dead state ❌
  > *Rationale:* Incorrect. 'Because it enters a dead state' is a distractor. The correct answer is 'Because 'ab' cannot be part of the prefix 'aa', resetting progress'.

- b.) Because state A is an accepting state ❌
  > *Rationale:* Incorrect. 'Because state A is an accepting state' is a distractor. The correct answer is 'Because 'ab' cannot be part of the prefix 'aa', resetting progress'.

- c.) Because 'ab' cannot be part of the prefix 'aa', resetting progress ✅ **[CORRECT]**
  > *Rationale:* Correct! [Prefix Reset Logic] The sequence 'ab' breaks the prefix 'aa'. Since 'b' cannot extend 'aa', the machine must restart matching from state A.

- d.) Because 'b' is not in the alphabet ❌
  > *Rationale:* Incorrect. 'Because 'b' is not in the alphabet' is a distractor. The correct answer is 'Because 'ab' cannot be part of the prefix 'aa', resetting progress'.

💡 *Hint:* Concept: Prefix Reset Logic

---

### Question 36
**_____ 36. In the DFA for substring 'aabb' (Example 3), what is the state trajectory when processing the input string 'baabb'?**

- a.) A -> B -> A -> B -> E ❌
  > *Rationale:* Incorrect. 'A -> B -> A -> B -> E' is a distractor. The correct answer is 'A -> A -> B -> C -> D -> E'.

- b.) A -> A -> B -> C -> D -> E ✅ **[CORRECT]**
  > *Rationale:* Correct! [String Trace 'baabb'] From A, on 'b' it stays at A. Then 'a' moves to B, 'a' to C, 'b' to D, and 'b' to E (accepted).

- c.) A -> B -> C -> D -> E -> E ❌
  > *Rationale:* Incorrect. 'A -> B -> C -> D -> E -> E' is a distractor. The correct answer is 'A -> A -> B -> C -> D -> E'.

- d.) A -> C -> D -> E -> E ❌
  > *Rationale:* Incorrect. 'A -> C -> D -> E -> E' is a distractor. The correct answer is 'A -> A -> B -> C -> D -> E'.

💡 *Hint:* Concept: String Trace 'baabb'

---

### Question 37
**_____ 37. In the DFA for substring 'aabb' (Example 3), does the machine accept the string 'aaabb'?**

- a.) No, because of too many 'a' symbols ❌
  > *Rationale:* Incorrect. 'No, because of too many 'a' symbols' is a distractor. The correct answer is 'Yes, because state C loops on 'a', reaching E on 'bb''.

- b.) Yes, because state C loops on 'a', reaching E on 'bb' ✅ **[CORRECT]**
  > *Rationale:* Correct! [String Trace 'aaabb'] From A: on 'a' -> B, on 'a' -> C, on 'a' -> C (loops), on 'b' -> D, on 'b' -> E (accepts).

- c.) Only if complemented ❌
  > *Rationale:* Incorrect. 'Only if complemented' is a distractor. The correct answer is 'Yes, because state C loops on 'a', reaching E on 'bb''.

- d.) No, it enters a trap state ❌
  > *Rationale:* Incorrect. 'No, it enters a trap state' is a distractor. The correct answer is 'Yes, because state C loops on 'a', reaching E on 'bb''.

💡 *Hint:* Concept: String Trace 'aaabb'

---

### Question 38
**_____ 38. In DFA design, if an automaton with 5 states is complemented by flipping final and non-final states, how many total states does the complement DFA have?**

- a.) 4 states ❌
  > *Rationale:* Incorrect. '4 states' is a distractor. The correct answer is '5 states'.

- b.) 5 states ✅ **[CORRECT]**
  > *Rationale:* Correct! [Complement State Preservation] Complementation changes only the subset of accepting states (F' = Q \ F); the state set Q and transition function δ remain unchanged.

- c.) 6 states ❌
  > *Rationale:* Incorrect. '6 states' is a distractor. The correct answer is '5 states'.

- d.) 10 states ❌
  > *Rationale:* Incorrect. '10 states' is a distractor. The correct answer is '5 states'.

💡 *Hint:* Concept: Complement State Preservation

---

### Question 39
**_____ 39. For a DFA M = (Q, Σ, q0, F, δ), a string w is formally accepted by M if and only if ____.**

- a.) δ*(q0, w) ∉ F ❌
  > *Rationale:* Incorrect. 'δ*(q0, w) ∉ F' is a distractor. The correct answer is 'δ*(q0, w) ∈ F'.

- b.) δ*(q0, w) ∈ F ✅ **[CORRECT]**
  > *Rationale:* Correct! [Formal Language Acceptance Definition] A string w is accepted by DFA M if the state reached after processing w starting from q0 belongs to F.

- c.) δ*(q0, w) = ϕ ❌
  > *Rationale:* Incorrect. 'δ*(q0, w) = ϕ' is a distractor. The correct answer is 'δ*(q0, w) ∈ F'.

- d.) δ*(q0, w) = q0 ❌
  > *Rationale:* Incorrect. 'δ*(q0, w) = q0' is a distractor. The correct answer is 'δ*(q0, w) ∈ F'.

💡 *Hint:* Concept: Formal Language Acceptance Definition

---

### Question 40
**_____ 40. The set of all strings accepted by a DFA M is called the language accepted by M, formally denoted as ____.**

- a.) F(M) ❌
  > *Rationale:* Incorrect. 'F(M)' is a distractor. The correct answer is 'L(M)'.

- b.) Σ(M) ❌
  > *Rationale:* Incorrect. 'Σ(M)' is a distractor. The correct answer is 'L(M)'.

- c.) L(M) ✅ **[CORRECT]**
  > *Rationale:* Correct! [Language of a Machine Notation] L(M) = {w ∈ Σ* | δ*(q0, w) ∈ F} denotes the language recognized by automaton M.

- d.) Q(M) ❌
  > *Rationale:* Incorrect. 'Q(M)' is a distractor. The correct answer is 'L(M)'.

💡 *Hint:* Concept: Language of a Machine Notation

---

### Question 41
**_____ 41. Two DFAs M1 and M2 are defined to be equivalent if and only if they ____.**

- a.) have identical transition tables ❌
  > *Rationale:* Incorrect. 'have identical transition tables' is a distractor. The correct answer is 'accept the exact same language (L(M1) = L(M2))'.

- b.) share the same alphabet ❌
  > *Rationale:* Incorrect. 'share the same alphabet' is a distractor. The correct answer is 'accept the exact same language (L(M1) = L(M2))'.

- c.) have the exact same number of states ❌
  > *Rationale:* Incorrect. 'have the exact same number of states' is a distractor. The correct answer is 'accept the exact same language (L(M1) = L(M2))'.

- d.) accept the exact same language (L(M1) = L(M2)) ✅ **[CORRECT]**
  > *Rationale:* Correct! [DFA Equivalence Definition] Two automata are computationally equivalent if and only if they recognize the identical formal language.

💡 *Hint:* Concept: DFA Equivalence Definition

---
