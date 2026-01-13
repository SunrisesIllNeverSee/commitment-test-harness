# Commitment Test Harness

**Research-grade prototype for testing commitment conservation under compression and recursion.**

This repository contains a prototype implementation of the falsification protocol described in *"A Conservation Law for Commitment in Language Under Transformative Compression and Recursive Application"* (McHenry, 2026). It tests the hypothesis that linguistic signals contain a conserved structure—**hard commitments**—that remains invariant under lossy compression until a sharp collapse threshold, and that degrades under recursive application without enforcement constraints.

**Status**: Early-stage, illustrative tooling developed by a solo, unfunded researcher. The harness demonstrates operational feasibility of the protocol on ~50 signals but hit technical limits (scale, embedding integration, recursion depth). It is provided as a **starting point for adversarial replication and extension**, not as a production system.

**What it does**:
- Extracts hard commitments (modal obligations, negations, constraints) via spaCy dependency parsing + pattern matching
- Runs compression sweeps (progressive summarization) to measure fidelity vs. threshold σ
- Tests recursive drift (iterative transformation chains) with lineage tracking
- Computes Jaccard-based fidelity and drift metrics
- Generates plots (where PNG outputs were produced)

**What it doesn't do** (yet):
- Scale beyond ~50 signals (needs parallelization, larger corpus)
- Hybrid fidelity (embedding-based partial match for semantic equivalence)
- Deep recursion (n>20 cycles constrained by compute/time)
- Full MOS²ES enforcement (compression gating and cryptographic lineage are conceptual; simulated via prepending tokens)

**Invitation**: If you have production-grade infrastructure, extend this. If you find gradual collapse (no sharp threshold), inherent recursive conservation (no drift), or signals with no stable hard commitments—publish it. Negative results are supremely valuable.

## Project Structure

```bash
commitment-test-harness/
├── .github/workflows/ci.yaml       # CI/CD
├── Dockerfile                      # Containerization
├── README.md                       # Docs with Quickstart
├── appendix_a_extractor.md         # Extractor spec
├── data/canonical_corpus.json      # 20 test signals
├── environment.yml                 # Conda env
├── notebooks/                      # Jupyter
├── pyproject.toml                  # Poetry config
├── requirements.txt                # Pip deps
├── src/
│   ├── advanced_extractor.py       # Robust spaCy parser
│   ├── config.py                   # Settings
│   ├── deterministic_pipeline.py   # Full pipeline
│   ├── extraction.py               # Basic extractor
│   ├── harness.py                  # Original harness
│   ├── metrics.py                  # Jaccard + extras
│   ├── plotting.py                 # Plot functions
│   ├── samples.py                  # Sample signals
│   └── test_harness.py             # New end-to-end harness
├── tests/
│   ├── test_full_harness.py        # 10+ unit tests
│   └── test_harness.py             # Original tests
```

## Quickstart (Mac)

1. `python3 -m venv .venv && source .venv/bin/activate`
2. `pip install -r requirements.txt`
3. `python -m spacy download en_core_web_sm`
4. `cd src && python test_harness.py`

**Expected output**: Console logs showing hard commitment extraction, compression sweep results, and (if complete) PNG plots of fidelity vs. σ and drift vs. n.

**Known issues**:
- Embedding model download may hang on slow connections (large BART model ~1.2GB)
- Recursion tests may be slow (disabled by default to avoid CI timeouts)
- Plots may fail if matplotlib backend is misconfigured

## Reproducibility Checklist

To enable independent replication and falsification:

### Dataset
- **Corpus**: `data/canonical_corpus.json` contains ~20 curated signals (contracts, code specs, instructions)
- **Licensing**: Signals are synthetic/public-domain examples or author-created; no privacy/copyright restrictions
- **Annotation**: Ground-truth hard commitments manually verified; no inter-annotator agreement scores (solo researcher)
- **Limitations**: Small sample size; no adversarial or edge-case signals (poetry, metaphor, self-contradiction)

### Toolchain & Versions
- **spaCy**: 3.7.x (`en_core_web_sm` model for dependency parsing)
- **Transformers**: 4.x (HuggingFace pipelines for summarization)
- **Summarizer**: `facebook/bart-large-cnn` or `sshleifer/distilbart-cnn-12-6` (smaller, faster)
- **Python**: 3.10+ (tested on macOS; Linux/Windows may differ)
- **Determinism**: Fixed random seeds in `test_harness.py` (line 23: `random.seed(42)`); note that transformer models may still show minor variability across runs due to GPU/CPU differences

### Collapse Detection (σ_c)
- **Method**: Manual inspection of fidelity plots for visual threshold (sharp drop from >0.8 to <0.2 within Δσ ≤ 20 tokens)
- **Not implemented**: Automated change-point detection (Bayesian, CUSUM) or statistical significance tests
- **Limitation**: Threshold identification is subjective without quantitative criteria

### Statistical Rigor
- **Sample size**: n=20-50 signals per test (underpowered for formal hypothesis testing)
- **No confidence intervals** or effect-size calculations
- **Falsification criterion**: Qualitative pattern match (sharp vs. gradual collapse); future work should add quantitative thresholds (e.g., "collapse = fidelity drop >0.6 within Δσ ≤ 10, p < 0.05 via permutation test")

## Implementation Status

### Implemented (Prototype-Level)
- Hard commitment extraction via spaCy (modal verbs, negations, dependency patterns)
- Compression sweep with controllable σ (max_length in summarizer)
- Recursion drift tracking (fidelity measurement across n cycles)
- Jaccard fidelity metric (exact string match after normalization)
- Basic plotting utilities (matplotlib-based)

### Partially Implemented
- Hybrid fidelity (Jaccard + cosine similarity on embeddings): code exists in `metrics.py` but not integrated into main pipeline due to dependency issues
- Enforcement simulation: lineage tokens prepended manually; no cryptographic hashing or cadence enforcement

### Not Implemented (Conceptual/Future Work)
- Hardware-based extraction (deterministic geometric parsing via custom silicon)
- Full MOS²ES architecture (compression gates, cryptographic lineage DAG, physical cadence constraints)
- Large-scale corpus (1000+ signals)
- Cross-domain validation (code, speech, formal logic)
- Automated collapse detection (change-point algorithms)

### Docker/Conda Notes
- `Dockerfile` provided for containerization (not fully tested on all platforms)
- `environment.yml` for conda users (Mac-specific; may need adjustments for Linux/Windows)
- CI pipeline (`.github/workflows/ci.yaml`) runs basic tests on push

## Usage

### Running the Protocol

1. **Compression Sweep** (Test Prediction 1: invariance until sharp collapse):
   ```bash
   python src/test_harness.py --mode compression --signals data/canonical_corpus.json
   ```
   Outputs: Console logs of fidelity vs. σ; look for sharp drops indicating σ_c

2. **Recursion Drift** (Test Prediction 2: drift without enforcement):
   ```bash
   python src/test_harness.py --mode recursion --cycles 20
   ```
   Outputs: Drift Δ(n) vs. cycle n; observe whether hard commitments diverge from seed

3. **Extract Commitments** (standalone):
   ```python
   from src.extraction import extract_hard_commitments
   commitments = extract_hard_commitments("You must pay $100 by Friday if the deal closes.")
   # Expected: {"Must pay $100 by Friday if deal closes"}
   ```

4. **Calculate Fidelity**:
   ```python
   from src.metrics import jaccard_index
   original = {"Must pay $100", "Cannot exceed limit"}
   compressed = {"Must pay $100"}
   fidelity = jaccard_index(original, compressed)  # 0.5
   ```

5. **Visualize** (if plots generated):
   ```python
   from src.plotting import plot_fidelity
   plot_fidelity(fidelity_data, output="fidelity_vs_sigma.png")
   ```

### Limitations & Known Issues

**Extractor Sensitivity**:
- Modal verb heuristics may miss implicit commitments ("The deadline is Friday" → not flagged as hard commitment)
- Negation scope detection is imperfect (nested negations, distant modals)
- No semantic understanding (paraphrased commitments may not match exactly)

**Domain Limitations**:
- Designed for procedural/contractual language; likely fails on poetry, metaphor, ambiguous directives
- Cross-lingual support untested (spaCy models language-specific)

**Hardware Claims**:
- "Deterministic geometric parsing" and "hardware-anchored enforcement" are architectural proposals, not implemented systems
- Current extractor is software-based (spaCy + regex); no custom silicon or FPGA prototypes exist

**Scalability**:
- Single-threaded; large corpora will be slow
- Transformer models memory-intensive (may OOM on machines with <8GB RAM)

**Replication Challenges**:
- No Docker image published (Dockerfile exists but not containerized/pushed)
- Random seed fixation incomplete (transformers may vary across GPU/CPU)
- Plots may not generate if recursion/compression tests hit errors mid-run

## Falsification Criteria

This harness is designed to be **broken**. Key ways to falsify the conservation principle:

1. **No stable hard commitments**: Find signals where `extract_hard_commitments` produces inconsistent results across heterogeneous transforms
2. **Gradual collapse**: Show fidelity decays smoothly (no sharp threshold) across compression sweep
3. **Inherent recursive conservation**: Demonstrate models that maintain hard commitment fidelity under recursion *without* enforcement (lineage, compression gates)
4. **Extractor bias**: Prove extracted commitments are artifacts of spaCy/pattern-matching, not transformation-invariant properties

**Report negative results**: Open issues or PRs with counterexamples. The protocol is only valuable if it survives adversarial testing.

## Contributing

Contributions are **strongly encouraged**, especially:

- **Scaling**: Parallelize extraction/compression for 1000+ signal corpora
- **Embedding integration**: Complete hybrid fidelity (Jaccard + semantic similarity)
- **Change-point detection**: Add Bayesian or CUSUM algorithms for automated σ_c identification
- **Cross-domain tests**: Validate on code, speech transcripts, formal specifications
- **Adversarial signals**: Construct edge cases (self-contradictory, poetic, ambiguous) to probe extractor limits
- **Statistical rigor**: Add confidence intervals, power analyses, effect-size thresholds
- **Alternative extractors**: Implement GPT-4 prompting or Stanford OpenIE for extractor-independence tests

**Process**: Submit PRs with test coverage; open issues for falsification attempts. Negative results (e.g., "I found gradual collapse on 100 signals") are as valuable as improvements.

## Citation

If you use this harness or extend the protocol, please cite:

```bibtex
@misc{mchenry2026commitment,
  author = {McHenry, Deric J.},
  title = {A Conservation Law for Commitment in Language Under Transformative Compression and Recursive Application},
  year = {2026},
  note = {Preprint, arXiv:XXXX.XXXXX [cs.IT]},
  url = {https://github.com/YOUR_USERNAME/commitment-test-harness}
}
```

## Related Work & Context

This harness implements the falsification protocol for a broader hypothesis: that **commitment conservation** extends Shannon's information theory from transmission fidelity to identity preservation under transformation. Key claim: language has a measurable, conserved kernel that survives compression until sharp collapse (σ_c) but drifts under recursion without enforcement.

**Gap from current AI research**: Existing work (SimpleMem, recursive LMs, constitutional AI) optimizes *internal model performance*. This protocol tests *external invariance*—what must be preserved for a signal to remain itself, independent of the processing system. It's a physics question, not an engineering one.

See the paper for full context on MOS²ES (enforcement architecture), the constitutional vacuum, and the Shannon lineage.

## License

MIT License. Code is freely available for research, commercial use, and modification. The **MOS²ES architecture and enforcement mechanisms** described in the paper are subject to provisional patent protection (Ello Cello LLC); this harness is a research tool demonstrating the falsification protocol only.
