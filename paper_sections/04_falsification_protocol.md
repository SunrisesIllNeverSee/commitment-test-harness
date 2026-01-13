# 4. A Protocol for Falsification

The central claims of this work are falsifiable. To facilitate rigorous testing and critique, we propose the following operational protocol. This protocol translates the theoretical definitions of commitment, conservation, and collapse into concrete, replicable procedures designed to produce unambiguous, reviewer-resistant results.

## 4.1 Operational Extraction of Commitment: A Two-Tiered System
We distinguish two classes of commitment to prevent semantic handwaving and ensure collapse events are unambiguous.

**Tier A: Hard Commitments (C_hard(S)):** These are necessary, binary constraints that must hold for signal identity (e.g., "If condition X, then obligation Y", "Agent A is prohibited from Z", "The value is defined as V"). They are extracted via deterministic, rule-based methods or fixed, non-probabilistic prompting templates where possible. **Only C_hard(S) participates in the core conservation and collapse claims of this theory.**

**Tier B: Soft Commitments (C_soft(S)):** These are contextual, graded, or probabilistic aspects of a signal. They are recorded for secondary, supplemental analysis but are **explicitly excluded** from the primary falsification tests of the conservation principle.

Formally, the operational commitment is:
```
C_op(S) = C_hard(S) ∪ C_soft(S)
```

All invariance, conservation, and drift metrics defined below are computed **solely on C_hard(S)**.

### Extraction Procedure for C_hard(S):

1. **Input:** A linguistic signal S.

2. **Transformational Sieve:** Apply a diverse set of k loss-inducing, purportedly identity-preserving transformations {T_1, T_2, ..., T_k}. To ensure replicability and avoid embedding-space vagueness, we suggest using distinct *model classes* as reference implementations:
   - **Summarization:** `facebook/bart-large-cnn` or `google/pegasus-xsum` with controlled `max_length` parameter σ.
   - **Paraphrase:** `t5-base` fine-tuned on paraphrase data, or `gpt-4` with a fixed temperature and a prompt template (e.g., "Rephrase the following text completely.").
   - **Translation:** `Helsinki-NLP` MarianMT models for a non-English target language.
   - **Abstraction:** A rule-based clause or dependency-tree simplifier.

3. **Hard Commitment Extraction:** From each T_i(S), extract C_hard(T_i(S)) using a method that minimizes probabilistic inference:
   - **Method A (Rule-Based):** Use a structured parser (e.g., spaCy for dependency parsing, Stanford OpenIE) to extract subject-relation-object tuples representing claims, conditions, and negations. Filter to those containing modal verbs ("must", "shall", "cannot") or logical operators.
   - **Method B (Fixed Prompting):** Use a fixed, non-creative prompt with a high-reliability model (e.g., "List every specific, non-negotiable rule, condition, or definition stated in the text below. Format as a bulleted list."). Parse the output into a set of strings.
   - **Baseline Human Protocol (for non-NLP experts or validation):** Provide the same instruction to three independent human annotators. Define C_hard(S) as the intersection of their listed commitments.

4. **Intersection:** Define the operational hard commitment as:
   ```
   C_hard,op(S) = ∩_{i=1}^k C_hard(T_i(S))
   ```
   The intersection of structures surviving across *all* heterogeneous transformations is the candidate invariant. **Potential Falsification Point:** If no consistent C_hard,op(S) emerges for a well-formed S across diverse T_i, the core premise of a conserved, extractable commitment is challenged.

### Hardware-Based Extraction Determinism
In the physical implementation, hard commitment extraction employs **deterministic geometric parsing** of the signal's lattice structure. This algorithm analyzes syntactic and logical topology—such as constraint nesting, dependency graphs, and modal operator scope—using fixed, non-probabilistic rules implemented directly in hardware. This ensures extraction invariance regardless of signal source (human, AI, or synthetic generation), eliminating model-specific bias from the commitment definition.

### Implementation Note
The protocol specifies *functional requirements* (e.g., controllable compression threshold, heterogeneous transform classes, deterministic extraction methods) rather than specific model versions or software packages. The tools listed above (bart-large-cnn, t5-base, spaCy, etc.) are **reference implementations only**—illustrative examples that satisfy the procedural constraints. Researchers may substitute equivalent tools provided they maintain procedural adherence: tiered extraction (hard vs. soft), intersection across diverse transforms, and binary hard-commitment matching. The invariant is the protocol, not the implementation.

### Observer Effect Mitigation
This intersection method across heterogeneous transformation families {T_i} is designed to mitigate the 'observer effect' or extraction-model bias. If each T_i employs different architectures and biases, their intersection converges on structures invariant to the extraction mechanism itself. A commitment that appears only under one class of transformations (e.g., only with GPT-4) is, by this definition, not a true transformational invariant and is filtered out. The protocol treats the extraction bias as a source of noise, and invariance across extractors as the signal.

## 4.2 Testing Prediction 1: Conservation Under Compression

**Prediction:** C_hard(S) remains invariant under increasing compression C_σ until a discrete threshold σ_c, where semantic collapse occurs (characterized by an abrupt, substantial drop in fidelity within a narrow interval of σ).

### Test Procedure:
1. For a signal S, obtain C_hard,op(S) via Protocol 4.1.
2. Apply a compression operator C_σ (e.g., `bart-large-cnn` with progressively shorter `max_length` = σ).
3. For each σ, extract C_hard,op(C_σ(S)) using the **identical** extraction method (e.g., the same rule-based parser or fixed prompt) from Step 1.
4. Measure hard commitment fidelity:
   ```
   Fid_hard(σ) = J(C_hard,op(S), C_hard,op(C_σ(S)))
   ```
   where J(A, B) = |A ∩ B| / |A ∪ B| is the Jaccard index (ExactMatchRatio) between two sets of hard commitments.
5. Plot Fid_hard(σ) vs. σ.

### Falsification Conditions:
- **Gradual Degradation:** If Fid_hard(σ) declines smoothly without a clear, sharp drop to near-zero (e.g., from >0.9 to <0.1 within a small σ interval), it falsifies the threshold-collapse model.
- **Early Necessary Loss:** If elements in C_hard,op(S) are lost at very low σ (mild compression), it falsifies the claim that hard commitments are conserved *in practice* under compression.

## 4.3 Testing Prediction 2: Drift Under Recursion

**Prediction:** Under recursive application S_{n+1} = T(S_n) without invariance constraints, C_hard(S_n) will drift from C_hard(S_0).

### Test Procedure:
1. For a seed signal S_0, obtain C_hard,op(S_0).
2. Define a recursive transformation T (e.g., "Rephrase the following instruction for a new agent.") implemented by a standard model (e.g., `gpt-4`, `claude-3-opus`) with fixed, non-zero temperature.
3. Generate a chain S_{n+1} = T(S_n) for n = 0, 1, ..., N cycles.
4. At each cycle n, extract C_hard,op(S_n) using the **same, chain-independent method** from Step 1.
5. Compute hard commitment drift:
   ```
   Δ_hard(n) = 1 - J(C_hard,op(S_0), C_hard,op(S_n))
   ```
6. Plot Δ_hard(n) vs. n.

### Falsification Condition:
- **Stability in Standard Systems:** If Δ_hard(n) remains at or near zero for large N across a wide range of S_0 in *existing, unmodified systems*, it falsifies the claim that recursive drift of hard commitments is a systemic failure mode.

## 4.4 Testing Prediction 3: Feasibility of Enforcement

**Prediction:** A system enforcing compression gating and lineage validation can maintain C_hard(S_n) = C_hard(S_0) under recursion.

### Test Procedure:
1. Implement a minimal enforcement layer embodying the derived constraints:
   - **Compression Gating:** Before each recursive step, force summarization of S_n to a fixed token length using a deterministic algorithm (e.g., extractive summarization based on sentence ranking).
   - **Lineage Validation:** Prepend an immutable, hashed identifier of C_hard,op(S_0) to the context window for every step.
2. Run the identical recursive test from 4.3, with this enforcement layer active.
3. Measure Δ_hard,enforced(n).

### Falsification Condition:
- **Enforcement Failure:** If Δ_hard,enforced(n) shows significant drift comparable to the unconstrained system, it falsifies the sufficiency of the proposed enforcement mechanisms.

## 4.5 Adversarial Falsification Note

This protocol is designed to invite adversarial testing. The burden of proof is intentionally inverted: the theory must withstand attempts to break it.

- **Reviewers are explicitly encouraged to:** Design stronger, more disruptive transformation sets {T_i}; use alternative extraction tools; select signal classes (S) expected to be problematic (e.g., poetry, ambiguous directives).
- **Procedure invariance is key:** The specific tools named (e.g., `bart-large-cnn`) are suggested **reference implementations only**. Any functionally equivalent tool or model is acceptable. The core requirement is adherence to the **procedure**—tiered extraction, intersection, and binary hard-commitment matching.
- **Negative results are supremely informative:** A clear, replicated failure of any prediction above is not a failure of the research program, but a vital step in refining or falsifying the proposed conservation principle. Such results are the explicit goal of this protocol.
