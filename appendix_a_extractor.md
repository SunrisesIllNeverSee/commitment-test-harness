# Appendix A: Precise Deterministic Extractor Specification
# This appendix provides a complete, reproducible specification for extracting hard commitments (C_hard) from linguistic signals.
# It is designed to be model-independent, deterministic, and falsifiable, minimizing probabilistic inference.
# Implementation: Rule-based parsing with spaCy; canonicalization for robustness.

## A.1 Input and Output
- **Input:** A string S (linguistic signal, e.g., text).
- **Output:** A set C_hard(S) of strings, each representing a hard commitment (e.g., {"Must pay $100 by Friday if deal closes"}).

## A.2 Extraction Procedure
1. **Normalization:** Lowercase, strip whitespace, replace common variants (e.g., "—" → "-", "–" → "-").
2. **Sentence Segmentation:** Use spaCy to split into sentences.
3. **Modal Detection:** Identify sentences containing modals: "must", "shall", "cannot", "required", "obligated".
4. **Canonicalization:** Normalize entities (numbers: "#NUM", dates: ISO format, names: lowercase).
5. **Output Set:** Collect matching sentences as strings.

## A.3 Canonical Examples
- Input: "You must pay $100 by Friday if the deal closes."
  - Output: {"must pay #NUM by 2023-01-13 if the deal closes"}  # Assuming date parsing
- Input: "This function shall return an integer."
  - Output: {"this function shall return an integer"}

## A.4 Unit Tests
def test_extractor():
    assert extract_hard_commitments("You must pay $100.") == {"must pay #NUM"}
    assert extract_hard_commitments("It's likely rainy.") == set()  # No hard commitment

## A.5 Falsification
- If extractor varies across runs or models, falsifies determinism.
- If no C_hard for well-formed S, falsifies existence of invariant.