import pytest
from src.extraction import extract_hard_commitments
from src.metrics import jaccard_index
from src.plotting import plot_fidelity

def test_run_tests():
    from src.test_harness import compression_sweep
    sigs, fids = compression_sweep("You must pay $100.")
    assert len(sigs) == len(fids)

def test_extract_hard_commitments():
    signal = "You must pay $100 by Friday."
    commitments = extract_hard_commitments(signal)
    assert isinstance(commitments, set)
    assert len(commitments) > 0

def test_jaccard_index():
    set_a = {"If condition X, then obligation Y."}
    set_b = {"If condition X, then obligation Y.", "Agent A is prohibited from Z."}
    similarity = jaccard_index(set_a, set_b)
    assert similarity == 0.5

def test_plot_fidelity():
    compression_thresholds = [0.1, 0.2, 0.3]
    fidelity_scores = [0.9, 0.7, 0.5]
    plot_fidelity(compression_thresholds, fidelity_scores)  # No assertion, just check for errors

if __name__ == "__main__":
    pytest.main()
