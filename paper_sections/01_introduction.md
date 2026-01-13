# 1. Introduction

Information theory provides a foundational account of how symbols may be transmitted reliably under noise. In particular, Shannon's formulation characterizes limits on channel capacity and error correction without regard to semantic content. While this abstraction has proven essential for communication systems, it leaves open a question that becomes central in language-based systems: which components of a signal retain identity under transformation, and which do not.

Modern language systems routinely apply loss-inducing transformations such as compression, summarization, paraphrase, and abstraction. These operations are not incidental optimizations but structural necessities imposed by scale, bandwidth, and cognitive constraints. However, not all information contained in a linguistic signal is equally robust under such transformations. Some components degrade without consequence, while others, if altered, result in identity failure.

Existing approaches typically address this problem implicitly. Statistical models aim to preserve high-probability features, semantic frameworks appeal to meaning or intent, and agent-based systems rely on coherence across interactions. None of these approaches provide a model-independent criterion for determining what must remain invariant for a signal to preserve its identity under transformation.

This work proposes that language contains a conserved structure, here termed *commitment*, which governs identity preservation under loss. Commitment is defined operationally as the minimal invariant structure shared by all identity-preserving transformations of a signal. Unlike semantic or pragmatic notions, commitment is not tied to truth, belief, or intent, but to transformational stability.

Beyond written text, the conservation principle applies to any structured symbolic form—including speech, code, and formal specifications—where identity must be preserved under transformation. This universality allows for cross-domain verification and falsification, grounding the principle in Shannon's semantic-agnostic measure of information. We frame commitment conservation as a form of harmonic resonance in information systems: just as a harmonic frequency remains invariant under amplification or damping, the commitment structure of a signal persists under lossy transformation until a threshold of collapse. This resonance metaphor underscores the operational, measurable nature of the invariant, which we formalize without appeal to mystical ratios or unempirical claims.

We investigate commitment conservation under two regimes. First, we treat compression as a diagnostic test, examining whether commitments persist as non-essential information is removed. Second, we consider recursive application as a stress regime in which transformations are applied repeatedly, a setting in which many existing systems exhibit drift and identity loss. The latter regime is particularly relevant to modern language systems that operate through iterative generation, feedback, and self-application.

The contributions of this paper are as follows:
- We introduce a formal definition of commitment as a transformation-invariant structure in linguistic signals.
- We show that commitment is conserved under compression while non-commitment content collapses.
- We demonstrate that commitment conservation is not guaranteed under recursive application without additional constraints.
- We outline an enforcement architecture consistent with these findings.

Together, these results suggest that commitment conservation provides a measurable criterion for signal integrity in language systems, extending information-theoretic analysis beyond transmission to identity preservation under transformation.

## 1.1 Falsifiable Core Predictions
This work makes three specific, falsifiable predictions:

1. **Compression Invariance:** For any well-formed linguistic signal S, there exists a conserved structure C_hard(S) (hard commitments) that remains invariant under increasing lossy compression C_σ until a discrete threshold σ_c, at which point semantic collapse occurs (characterized by an abrupt, substantial drop in fidelity within a narrow interval of σ).

2. **Recursive Drift:** In the absence of explicit invariance-preserving constraints, recursively applying lossy transformations T to S will cause C_hard(S_n) to drift from C_hard(S_0), leading to identity loss.

3. **Enforcement Feasibility:** A system enforcing compression gating and lineage validation (as derived in Section 6) will maintain C_hard(S_n) = C_hard(S_0) under recursion, where equivalent unconstrained systems fail.

In Section 3, we provide a detailed operational protocol for testing these predictions. The remainder of the paper formalizes the concepts, presents illustrative evidence, and invites adversarial falsification.
