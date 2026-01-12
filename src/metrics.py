from typing import Set

def jaccard_index(set_a, set_b):
    intersection = len(set_a.intersection(set_b))
    union = len(set_a.union(set_b))
    if union == 0:
        return 0.0
    return intersection / union

def fidelity_metric(commitments_a, commitments_b):
    return jaccard_index(set(commitments_a), set(commitments_b))

def jaccard(a: Set[str], b: Set[str]) -> float:
    if not a and not b:
        return 1.0
    if not a or not b:
        return 0.0
    inter = len(a & b)
    uni = len(a | b)
    return inter / uni

def fid_hard(base: Set[str], comp: Set[str]):
    return jaccard(base, comp)

def delta_hard(base: Set[str], cyc: Set[str]):
    return 1.0 - jaccard(base, cyc)