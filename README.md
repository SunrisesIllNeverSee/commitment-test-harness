# Commitment Test Harness

This project implements a test harness for evaluating the conservation of commitments in linguistic signals under various transformations. It integrates HuggingFace pipelines for processing text and utilizes spaCy for extracting hard commitments. The project also includes metrics for measuring fidelity and visualization tools for analyzing results.

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

Outputs: PNG plots (Fid_hard and Δ_hard) and example commitments printed.

## Usage

1. **Run the Test Harness**: Execute the main test harness to evaluate commitments in linguistic signals.

   ```bash
   python src/harness.py
   ```

2. **Extract Commitments**: Use the extraction module to process text and extract hard commitments.

   ```python
   from src.extraction import extract_hard_commitments
   commitments = extract_hard_commitments("Your linguistic signal here.")
   ```

3. **Calculate Fidelity**: Measure the fidelity of extracted commitments using the Jaccard index.

   ```python
   from src.metrics import jaccard_index
   fidelity = jaccard_index(set1, set2)
   ```

4. **Visualize Results**: Plot the results of the tests using the plotting module.

   ```python
   from src.plotting import plot_fidelity
   plot_fidelity(fidelity_data)
   ```

## Contributing

Contributions are welcome! Please submit a pull request or open an issue for discussion.

## License

This project is licensed under the MIT License. See the LICENSE file for details.
