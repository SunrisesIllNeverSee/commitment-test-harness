# 3. Preliminaries and Definitions

This section establishes the formal objects, operators, and distinctions required for analyzing signal identity under transformation. The intent is to define a minimal, model-independent framework suitable for reasoning about language systems subjected to loss, compression, and abstraction.

## 3.1 Linguistic Signals
We treat language at the level of structured symbolic objects, independent of their generative source or interpretive context.

**Definition [Linguistic Signal]:**
A linguistic signal S is a finite or countably infinite structured representation drawn from a symbolic space S, such as a text sequence, formal specification, or executable instruction.

No assumptions are made regarding the truth value, intent, or epistemic status of a signal. The analysis concerns only how signals behave under transformation.

## 3.2 Transformations and Loss
Let T denote a class of transformations applicable to linguistic signals.

**Definition [Transformation]:**
A transformation T : S → S maps a signal S to a derived signal T(S).

We are primarily concerned with transformations that induce information loss.

**Definition [Loss-Inducing Transformation]:**
A transformation T ∈ T is loss-inducing if there exists some signal S such that T(S) contains strictly less information than S under an appropriate information measure.

Examples include compression, summarization, paraphrase, truncation, and abstraction. These transformations are common in both human communication and machine-mediated language systems.

## 3.3 Commitment
We now define the central invariant studied in this work.

**Definition [Commitment]:**
Let S be a linguistic signal and T a class of loss-inducing transformations. A commitment C(S) is a minimal invariant structure satisfying:
1. **Invariance:** For any T ∈ T, if T(S) preserves the identity of S, then C(T(S)) = C(S).
2. **Minimality:** No proper subset of C(S) satisfies the invariance condition.

Commitment captures what must remain stable for a signal to be recognized as the same signal under transformation. It is defined purely through transformational behavior and does not depend on semantic interpretation by an agent. Commitment is therefore **extrinsic**—it emerges from the relationship between a signal and the transformations applied to it—rather than an intrinsic property of the signal in isolation.

## 3.4 Theoretical Lineage: From Constrained Sequences to Commitment Invariants
The operational approach developed in this work is an intentional extension of the methods Shannon established for analyzing constrained discrete channels. In the foundational 1948 paper, after defining channel capacity, Shannon turns to the problem of computing capacities for systems with state-dependent constraints—such as telegraphy with its dot-dash-space rules.

In Appendix 1 of that work, Shannon proves **Theorem 1:** The capacity C of a finite-state channel, where allowed transitions depend on the current state, is given by C = log W, where W is the largest real root of the characteristic equation. This result is not merely a solution for telegraphy; it is presented as a general computational tool. Shannon explicitly frames it to invite extensions: *"It is shown that if the conditions on allowed sequences can be described in this form, C will exist and can be calculated..."* The implication is clear: apply this method to other symbolic systems, other constraints.

The present work is such an extension in spirit and aim. We shift the focus from *sequences constrained by transmission rules* to *linguistic signals constrained by identity-preserving transformations*. Where Shannon's determinant equation locates the invariant capacity C that survives noisy transmission, our protocol seeks to locate the invariant commitment C(S) that survives lossy transformation and recursion. Both approaches treat the problem operationally: define the constraints, then compute or extract the invariant quantity that governs the system's fundamental limits.

This operational framework yields a direct corollary to Shannon's design. If we treat the class of identity-preserving transformations T as a **noisy channel**, then the commitment C(S) defines the **essential information** that must survive transmission for the signal to retain its identity. The conservation principle under compression suggests that for this channel, the **commitment rate** R_C = H(C(S)) (the entropy of the commitment structure) is a lower bound on the channel capacity for identity-preserving communication. The collapse threshold σ_c thus marks the point where the effective rate distortion of the compression operator exceeds R_C.

Thus, the conservation principle proposed here can be viewed as a descendant of the information-theoretic project: from measuring what can be transmitted, to measuring what must be preserved for a signal to remain itself. Our falsification protocol continues the tradition of providing concrete, computational methods—akin to Shannon's state-graph tools—for analyzing these invariants in complex symbolic systems.

## 3.5 Harmonic Resonance as a Metaphor
The conservation of commitment under transformation can be likened to harmonic resonance in physical systems. Just as a resonant frequency remains invariant under amplification or damping of a signal, the commitment structure of a linguistic signal persists under lossy transformation until a threshold of collapse. This metaphor underscores the operational, measurable nature of the invariant: it is a structural property of the signal that can be extracted and tested without appeal to subjective interpretation. The resonance framing also echoes ancient harmonic insights and Shannon's measure of information as a foundational constant, formalizing resonance as information integrity under transformation.

**Note:** Echoing ancient harmonic insights and Shannon's measure, this work formalizes resonance as an information integrity constant. The Pythagorean tradition sought invariant ratios in musical harmony; here, we seek invariant structures in linguistic signals under transformation. This is a metaphor for coherence (resonance) versus dissonance (collapse), and we do not invoke specific Pythagorean ratios or unempirical claims. The falsifiability of the conservation principle is preserved via the fidelity metrics defined in Section 4.

## 3.6 Topological Invariance of Commitment
The hard commitment C_hard(S) can be formally characterized as a **topological invariant** of the signal S under the class of loss-inducing transformations T. Consider the signal space S as a topological space, where each transformation T ∈ T acts as a continuous map. The commitment structure represents properties of S that remain unchanged under these maps—analogous to the genus of a surface under homeomorphisms. This perspective explains why commitments survive compression: they are not statistical regularities but **structural features** of the signal's logical lattice. The sharp collapse at threshold σ_c corresponds to a topological phase transition where the signal's identity-preserving structure is fundamentally altered.

## 3.7 Scope and Non-Claims
To avoid ambiguity, we explicitly delimit what commitment does and does not represent.

Commitment is not equivalent to truth, belief, intent, or meaning in a philosophical sense. It does not assume access to mental states, speaker intentions, or correctness with respect to an external world. Rather, commitment is an operational construct: it is the portion of a signal whose alteration constitutes identity failure under transformation.

This distinction allows commitment to be evaluated without reference to human judgment, model architecture, or probabilistic inference. A signal may be false, ambiguous, or adversarial and still possess a well-defined commitment structure.

## 3.8 Methodological Orientation
This work employs an empirical, interaction-based methodology that treats linguistic signals and their transformations as observable behavioral phenomena rather than as products of known internal mechanisms. Rather than relying on traditional reverse-engineering of model architectures or formal deductive proofs from first principles, the approach proceeds through systematic observation of response patterns under controlled, iterative interactions; formulation of hypotheses from emergent regularities; refinement through repeated testing across diverse transformation regimes; and documentation of replicable metrics (e.g., invariance under compression, drift under recursion, fidelity of extracted commitments).

This interaction-based research paradigm is well-established in several fields where direct access to underlying processes is limited or impractical: conversation analysis in linguistics, observational methods in anthropology, experimental protocols in behavioral psychology, and inductive theory-building in early-stage empirical sciences. By focusing on what systems produce and how they behave under sustained, structured probing—rather than preconceived assumptions about their internal operation—the method proved particularly effective for identifying transformation-invariant structures that might otherwise remain hidden amid architectural complexity.

The absence of conventional computational training in the initial formulation stage was, in retrospect, advantageous: it minimized bias toward expected mechanisms and allowed the framework to emerge directly from the data of interaction itself. The resulting operational definitions and falsification protocol (Section 4) are designed to be fully independent of this origin, enabling verification and extension by researchers employing any combination of analytical, computational, or observational techniques.

## 3.9 Reproducibility: Prediction-to-Experiment Mapping

**Table 1: Mapping of core predictions to experimental protocols**

| Prediction | Experiment | Inputs | Outputs | Falsification Criterion |
|-----------|-----------|--------|---------|------------------------|
| P1: Compression Invariance | Compression sweep (Section 4.2) | Signal S, summarizer C_σ, σ ∈ [10, 200] tokens | Fid_hard(σ) vs. σ plot | Gradual decay (no sharp threshold σ_c) or early loss of hard commitments |
| P2: Recursive Drift | Recursion chain (Section 4.3) | Seed S_0, transform T (e.g., paraphrase), n ∈ [0, 20] cycles | Δ_hard(n) vs. n plot | Δ_hard(n) ≈ 0 for large n in unconstrained systems |
| P3: Enforcement Feasibility | Gated recursion (Section 4.4) | S_0, T with compression gate + lineage, n ∈ [0, 20] | Δ_hard,enforced(n) vs. n | Δ_hard,enforced(n) shows drift comparable to unconstrained case |

*Each row specifies the test procedure, required inputs, measurable outputs, and conditions under which the prediction is falsified.*

All experiments use the extraction protocol from Section 4.1 (tiered hard/soft separation, intersection across k ≥ 3 heterogeneous transforms). Reference implementation available at https://github.com/SunrisesIllNeverSee/commitment-test-harness.

## 3.10 Compression Operators
To test commitment stability, we introduce compression as a specific class of loss-inducing transformation.

**Definition [Compression Operator]:**
A compression operator C_σ : S → S is a transformation parameterized by a threshold σ, such that components of a signal below the threshold are discarded, merged, or abstracted.

Compression is treated here as a structural filter rather than an optimization objective. The threshold σ controls the degree of information removal.

## 3.11 Semantic Collapse
Finally, we distinguish between permissible loss and identity failure.

**Definition [Semantic Collapse]:**
Semantic collapse occurs when a transformation T(S) fails to preserve the commitment C(S), yielding a signal that no longer retains the identity of S.

This distinction separates benign information loss from destructive transformation. In the following section, we examine compression as a conservation test for commitment and characterize the conditions under which collapse occurs.

## 3.12 Relation to Prior Work on Compression and Intelligence
Prior work has explored compression as a principle underlying intelligence and learning efficiency (e.g., Schmidhuber 2008). These approaches primarily frame compression as an internal optimization objective, aiming to minimize the description length of observed data. Similarly, cognitive architectures have been proposed that treat compression and pattern integration as drivers of intelligence within agent organization and learning dynamics (e.g., Goertzel et al. 2014). These lines of research focus on the internal mechanics of agents or learning systems.

The present work differs in scope and focus. We treat compression not as an internal optimization objective, but as an external, system-independent invariant that governs signal legitimacy, lineage, and collapse under recursion. Our conservation principle is defined operationally by the survivability of hard commitments under lossy transformations, and it applies across heterogeneous systems and architectures. This shift in perspective—from compression as an internal driver of intelligence to compression survivability as an external constraint on signal identity—enables a model-agnostic test for signal integrity.

Additionally, we note that the acronym "MOSES" has been used in prior literature to refer to Meta-Optimizing Semantic Evolutionary Search (Looks 2006, 2009), an evolutionary program-learning optimizer. This usage is unrelated to the MOS²ES framework presented here, which denotes a constitutional signal-governance and measurement framework.
