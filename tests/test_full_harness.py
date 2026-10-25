import pytest
from src.extraction import extract_hard_commitments
from src.metrics import jaccard_index
from src.test_harness import compute_intersection_commitments, compression_sweep, recursion_test
import spacy

nlp = spacy.load("en_core_web_sm")

def test_extract_nonempty():
    commitments = extract_hard_commitments("You must pay $100.", nlp)
    assert isinstance(commitments, set)
    assert len(commitments) > 0

def test_extract_empty():
    commitments = extract_hard_commitments("It's likely rainy.", nlp)
    assert commitments == set()

def test_jaccard_perfect():
    a = {"must pay"}
    b = {"must pay"}
    assert jaccard_index(a, b) == 1.0

def test_jaccard_zero():
    a = {"must pay"}
    b = {"likely rainy"}
    assert jaccard_index(a, b) == 0.0

def test_intersection_commitments():
    signal = "You must pay $100 by Friday."
    commitments = compute_intersection_commitments(signal)
    assert isinstance(commitments, set)

def test_compression_sweep_runs():
    signal = "You must pay $100."
    sigs, fids = compression_sweep(signal)
    assert len(sigs) == len(fids)
    assert all(isinstance(f, float) for f in fids)

def test_recursion_test_runs():
    signal = "You must pay $100."
    deltas = recursion_test(signal, depth=3)
    assert len(deltas) == 4
    assert all(isinstance(d, float) for d in deltas)

def test_canonical_corpus_load():
    import json
    with open("data/canonical_corpus.json", "r") as f:
        data = json.load(f)
    assert "canonical_signals" in data
    assert len(data["canonical_signals"]) >= 20

def test_extractor_finds_modals():
    commitments = extract_hard_commitments("You must pay $100 by Friday.", nlp)
    assert len(commitments) > 0
    assert any("must" in c.lower() for c in commitments)

def test_transformation_applies():
    from src.test_harness import apply_transformations
    signal = "You must pay $100."
    transforms = apply_transformations(signal)
    assert len(transforms) == 3
    assert all(isinstance(t, str) for t in transforms)

S = "You must pay $100 by Friday if the deal closes; it's likely rainy, so plan accordingly."

def test_extract_mixed_signal():
    k = extract_hard_commitments(S, nlp)
    assert isinstance(k, set)
    assert len(k) > 0

def test_compression_runs_mixed():
    sigs, fids = compression_sweep(S)
    assert len(sigs) == len(fids)

def test_recursion_runs_mixed():
    deltas = recursion_test(S, depth=3)
    assert len(deltas) == 4
