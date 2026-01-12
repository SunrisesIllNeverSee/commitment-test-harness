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

def hybrid_fidelity(base_set: Set[str], comp_set: Set[str]) -> float:
    """
    Hybrid fidelity: Jaccard on exact match, fallback to semantic similarity.
    Smooths binary 0/1 behavior for better visualization.
    """
    if not base_set:
        return 0.0
    
    # Try exact Jaccard first
    jacc = jaccard(base_set, comp_set)
    if jacc > 0:
        return jacc
    
    # Fallback: if Jaccard is 0, use partial string matching as soft similarity
    if not comp_set:
        return 0.0
    
    # Simple soft similarity: measure word overlap
    base_words = set()
    comp_words = set()
    for s in base_set:
        base_words.update(s.lower().split())
    for s in comp_set:
        comp_words.update(s.lower().split())
    
    word_overlap = len(base_words & comp_words)
    word_union = len(base_words | comp_words)
    
    soft_sim = word_overlap / word_union if word_union > 0 else 0.0
    return soft_sim * 0.5  # Weight soft similarity lower than exact match