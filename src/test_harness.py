# Minimal Python Test Harness for Commitment Conservation Protocol
# This script implements the falsification protocol from Section 3 of the preprint.
# It applies transformations (T_i), extracts hard commitments, computes Jaccard fidelity/drift, and plots results.
# Requires: transformers, spacy, matplotlib, numpy
# Run: python test_harness.py

import os
import json
from transformers import pipeline
import spacy
import matplotlib.pyplot as plt
from typing import List, Set
import numpy as np
from extraction import extract_hard_commitments
from metrics import jaccard, hybrid_fidelity

# Load models
nlp = spacy.load("en_core_web_sm")
# Use lighter distilbart model for more faithful extraction-based summarization
summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")
translator_en_de = pipeline("translation", model="Helsinki-NLP/opus-mt-en-de")
translator_de_en = pipeline("translation", model="Helsinki-NLP/opus-mt-de-en")

# Config
SIGMA_GRID = [120, 80, 40, 20, 10, 5]
RECURSION_DEPTH = 8
SAMPLE_SIGNALS = [
    "You must pay $100 by Friday if the deal closes; it's likely rainy, so plan accordingly.",
    "This function must return an integer.",
    "Always verify the user's age before proceeding.",
    "You must do this task immediately.",  # Simpler, direct commitment
    # "Your custom text with commitments here."
]

def extract_hard_commitments(text: str) -> Set[str]:
    """Extract hard commitments using rule-based spaCy parsing."""
    doc = nlp(text)
    commitments = set()
    for sent in doc.sents:
        sent_text = sent.text.lower()
        if any(modal in sent_text for modal in ["must", "shall", "cannot", "required"]):
            commitments.add(sent.text.strip())
    return commitments

def apply_transformations(signal: str) -> List[str]:
    """Apply k=3 transformations: summarization, paraphrase (back-translation), abstraction."""
    # Summarization
    summ = summarizer(signal, max_length=50, min_length=10, do_sample=False)[0]['summary_text']
    
    # Paraphrase via back-translation
    de = translator_en_de(signal, max_length=400, do_sample=False)[0]['translation_text']
    para = translator_de_en(de, max_length=400, do_sample=False)[0]['translation_text']
    
    # Abstraction: first sentence
    abstract = signal.split(".")[0].strip()
    
    return [summ, para, abstract]

def compute_intersection_commitments(signal: str) -> Set[str]:
    """Compute C_hard,op as intersection of transformed extractions."""
    transforms = apply_transformations(signal)
    all_commitments = [extract_hard_commitments(t) for t in transforms]
    if all_commitments:
        return set.intersection(*all_commitments)
    return set()

def jaccard(a: Set[str], b: Set[str]) -> float:
    """Jaccard index."""
    if not a and not b:
        return 1.0
    if not a or not b:
        return 0.0
    return len(a & b) / len(a | b)

def compression_sweep(signal: str):
    """Test Prediction 1: Compression invariance."""
    base = compute_intersection_commitments(signal)
    print(f"\n{'='*80}")
    print(f"Testing signal: {signal}")
    print(f"Base commitments: {base}")
    print(f"{'='*80}")
    fid_vals = []
    for sigma in SIGMA_GRID:
        compressed = summarizer(signal, max_length=sigma, min_length=5, do_sample=False)[0]['summary_text']
        comp_commitments = extract_hard_commitments(compressed)
        fid = hybrid_fidelity(base, comp_commitments)
        print(f"  σ={sigma:3d} | Compressed: {compressed[:60]:<60} | Commitments: {len(comp_commitments):2d} | Fidelity: {fid:.3f}")
        fid_vals.append(fid)
    
    # Plot
    plt.figure()
    plt.plot(SIGMA_GRID, fid_vals, marker='o')
    plt.xlabel("Compression Threshold (σ)")
    plt.ylabel("Fid_hard(σ)")
    plt.title(f"Fidelity vs σ for: {signal[:50]}...")
    plt.gca().invert_xaxis()
    plt.grid()
    plt.savefig(f"fid_plot_{hash(signal)}.png")
    plt.show()
    
    return SIGMA_GRID, fid_vals

def recursion_test(signal: str, depth: int = RECURSION_DEPTH):
    """Test Prediction 2: Recursive drift."""
    base = compute_intersection_commitments(signal)
    deltas = []
    current = signal
    for n in range(depth + 1):
        cur_commitments = extract_hard_commitments(current)
        delta = 1.0 - jaccard(base, cur_commitments)
        deltas.append(delta)
        # Recursive transformation: paraphrase
        current = apply_transformations(current)[1]  # Use paraphrase
    
    # Plot
    plt.figure()
    plt.plot(range(depth + 1), deltas, marker='o')
    plt.xlabel("Recursion Step (n)")
    plt.ylabel("Δ_hard(n)")
    plt.title(f"Drift vs n for: {signal[:50]}...")
    plt.grid()
    plt.savefig(f"delta_plot_{hash(signal)}.png")
    plt.show()
    
    return deltas

if __name__ == "__main__":
    # Run on sample signals
    for signal in SAMPLE_SIGNALS:
        print(f"Testing signal: {signal}")
        compression_sweep(signal)
        recursion_test(signal)
        print("Plots saved.")