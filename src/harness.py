from transformers import pipeline
import spacy
from metrics import jaccard_index
import matplotlib.pyplot as plt

def run_tests(signal, compression_thresholds):
    summarizer = pipeline("summarization")
    nlp = spacy.load("en_core_web_sm")

    original_commitments = extract_hard_commitments(signal, nlp)
    fidelity_results = []

    for threshold in compression_thresholds:
        compressed_signal = compress_signal(signal, threshold, summarizer)
        compressed_commitments = extract_hard_commitments(compressed_signal, nlp)
        fidelity = jaccard_index(original_commitments, compressed_commitments)
        fidelity_results.append(fidelity)

    plot_results(compression_thresholds, fidelity_results)

def extract_hard_commitments(signal, nlp):
    doc = nlp(signal)
    commitments = set()
    for sent in doc.sents:
        # Example extraction logic; customize as needed
        commitments.add(sent.text)
    return commitments

def compress_signal(signal, threshold, summarizer):
    # Example compression logic; customize as needed
    summary = summarizer(signal, max_length=threshold, min_length=5, do_sample=False)
    return summary[0]['summary_text']

def plot_results(thresholds, fidelity):
    plt.plot(thresholds, fidelity, marker='o')
    plt.title('Fidelity of Hard Commitments vs Compression Threshold')
    plt.xlabel('Compression Threshold')
    plt.ylabel('Jaccard Fidelity')
    plt.grid()
    plt.show()