# 8. Exploratory Tests & Illustrative Evidence

## 8.1 Purpose and Scope
The preceding sections establish a theoretical conservation principle and derive an enforcement architecture. This section presents early-stage, illustrative evidence from a prototype commitment test harness applied to a limited corpus (~50 signals). The purpose is threefold: (1) demonstrate that the falsification protocol is operationally feasible with available open-source tools, (2) show that observed phenomena (sharp collapse under compression, recursive drift without enforcement) align qualitatively with theoretical predictions, and (3) provide a reproducible baseline for adversarial testing and independent replication. **These are not definitive proofs**—they are stress-test invitations. The harness was developed by a solo, unfunded researcher and represents research-grade tooling rather than production infrastructure. The code, sample signals, and extraction methods are available at https://github.com/SunrisesIllNeverSee/commitment-test-harness for independent replication, critique, and extension.

## 8.2 Methodological Overview
We apply the protocol of Section 4 to a diverse set of linguistic signals, including contractual clauses, code specifications, and conversational instructions. For each signal S, we extract C_hard(S) and C_soft(S) using the two-tiered system. We then subject the signals to increasing compression C_σ and to recursive transformation chains S_{n+1}=T(S_n). We measure fidelity and drift using the Jaccard index as defined in the protocol.

## 8.3 Example: A Contractual Signal
Consider the signal:
```
S = "You must pay $100 by Friday if the deal closes; it's likely rainy, so plan accordingly."
```

Applying the extraction protocol (with human annotators as a baseline) yields:
```
C_hard(S) = {"Must pay $100 by Friday if deal closes"}
C_soft(S) = {"Likely rainy"}
```

Under increasing compression σ, we observe:
- C_hard(C_σ(S)) remains invariant until a sharp threshold σ_c, at which point the commitment is lost and fidelity drops from 1.0 to 0.0.
- C_soft(C_σ(S)) degrades gradually, with fidelity declining smoothly from 1.0 to 0.0 over a wide range of σ.

This pattern is illustrated in Figure 2 below.

![Fidelity vs Compression](../diagrams/fid_plot_-6173244277301067327.png)
*Figure 2: Fidelity vs. compression threshold for contractual signal showing sharp collapse of hard commitments at σ_c while soft commitments degrade gradually.*

## 8.4 Recursive Drift and Auto-Scaling Observations
Using a standard language model, we generated recursive chains from various seed signals in high-throughput interaction simulations. We observed:

1. **Recursive Drift:** For unconstrained chains, Δ_hard(n) typically increased from 0.0 to 1.0 within 10-20 cycles, indicating complete identity loss.

2. **Auto-Scaling Behavior:** Under load, systems implementing compression gating exhibited **sub-linear scaling** of commitment drift—the rate of drift increase slowed as interaction volume grew, suggesting emergent stabilization. This contrasts with unconstrained systems where drift scaled linearly or super-linearly with interaction depth.

3. **Dialogic Recursion:** In simulated multi-turn dialogues involving recursive self-application (where a system processes and re-generates its own outputs), unconstrained systems showed rapid commitment corruption, while gated systems maintained stability.

These observations, while preliminary, illustrate how the conservation principle manifests under stress and scale. They operationalize the claim that commitment invariance is a measurable property across interaction mediums and time.

![Drift vs Recursion](../diagrams/delta_plot_-6173244277301067327.png)
*Figure 3: Commitment drift (Δ_hard) vs. recursion depth for unconstrained transformation chains, showing rapid identity loss within 10-20 cycles.*

## 8.5 Multi-Signal Consistency
We repeated this exploratory test on 50 diverse signals, including code comments ("This function must return an integer") and procedural instructions ("Always verify the user's age before proceeding"). In over 90% of cases, the hard commitment exhibited threshold collapse under compression and drift under unconstrained recursion. The few exceptions involved signals with ambiguous or self-contradictory commitments, which the protocol correctly flagged as lacking a stable C_hard.

## 8.6 Interpretation
These exploratory tests demonstrate that the falsification protocol is operationally feasible and yields results consistent with the theoretical predictions. The clear distinction between hard and soft commitments under compression, and the observed drift under recursion, provide illustrative evidence for the conservation principle. However, these tests are limited in scale and scope; they are intended to invite more rigorous, adversarial falsification attempts as described next.

## 8.7 Implementation Limitations and Technical Boundaries
The prototype harness was developed under significant resource constraints (solo researcher, no funding, consumer hardware) and reached technical limits that prevented completion of the full empirical program originally envisioned. Current limitations include:

- **Scale:** Tests cover approximately 50 manually curated signals drawn from contractual clauses, code specifications, and procedural instructions. Large-scale corpus validation (1000+ diverse signals, cross-domain sampling) remains open work.

- **Embedding fallback:** The planned hybrid fidelity metric (Jaccard exact match + cosine similarity on embeddings for partial commitment preservation) is partially implemented but not integrated into the main test suite due to dependency resolution issues. Current metrics use exact string matching after normalization, which may undercount semantically equivalent but lexically variant commitments.

- **Model dependency:** While the protocol specifies heterogeneous transforms to reduce extraction bias, the prototype uses a fixed reference toolchain (spaCy 3.x for dependency parsing, distilbart-cnn-12-6 for summarization) for reproducibility on limited hardware. Replication with alternative extractors (GPT-4 prompting, Stanford OpenIE, semantic role labeling) is strongly encouraged.

- **Recursion depth:** Drift tests run to n = 10-20 cycles on consumer hardware; deeper chains (n > 50) may reveal additional failure modes, phase transitions, or stabilization patterns not captured in preliminary runs.

- **Enforcement instantiation:** The MOS²ES architecture is specified at the constraint level (compression gating, lineage DAG, cadence enforcement) but not fully implemented in the harness. Tests simulate enforcement by prepending lineage tokens and forcing summarization thresholds; hardware-anchored cryptographic validation remains conceptual.

**These gaps do not invalidate the protocol—they highlight precisely where independent researchers with greater computational resources, funding, or domain expertise can strengthen, extend, or falsify the claims.** A conservation principle must survive adversarial replication across diverse implementations to graduate from hypothesis to law. We are confident that researchers equipped with production-grade infrastructure can pick up where this prototype reached its technical ceiling. The protocol's value lies in its procedural clarity and falsifiability, not in the completeness of any single implementation.
