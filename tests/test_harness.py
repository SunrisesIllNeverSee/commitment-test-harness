import pytest
from src.harness import run_tests
from src.extraction import extract_hard_commitments
from src.metrics import jaccard_index
from src.plotting import plot_fidelity

def test_run_tests():
    results = run_tests()
    assert isinstance(results, dict)
    assert 'compression_results' in results
    assert 'recursion_results' in results

def test_extract_hard_commitments():
    signal = "If condition X, then obligation Y."
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