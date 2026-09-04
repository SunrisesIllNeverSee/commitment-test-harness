# ...new file...
import os
from transformers import pipeline
from .extraction import extract_hard
from .metrics import fid_hard, delta_hard
from .plotting import plot_fid, plot_delta
from . import config

# initialize deterministic pipelines (no sampling)
SUMMARIZER = pipeline("summarization", model="facebook/bart-large-cnn", framework="pt", device=-1)
# back-translation paraphrase via Marian (en->de and de->en)
EN_DE = pipeline("translation", model="Helsinki-NLP/opus-mt-en-de", tokenizer="Helsinki-NLP/opus-mt-en-de", framework="pt")
DE_EN = pipeline("translation", model="Helsinki-NLP/opus-mt-de-en", tokenizer="Helsinki-NLP/opus-mt-de-en", framework="pt")

def transform_sieve(text, sigma):
    # Summarization (compression)
    summ = SUMMARIZER(text, max_length=sigma, min_length=max(5, sigma//4), do_sample=False)[0]['summary_text']
    # Paraphrase via back-translation
    de = EN_DE(summ, max_length=400, do_sample=False)[0]['translation_text']
    para = DE_EN(de, max_length=400, do_sample=False)[0]['translation_text']
    # Abstraction: simple extractive shortener (first sentence)
    abstract = summ.split(".")[0].strip()
    return [summ, para, abstract]

def compression_sweep(signal_text):
    base = extract_hard(signal_text)
    sig_label = signal_text[:40].replace("\n"," ")
    sigma_vals = []
    fid_vals = []
    for s in config.SIGMA_GRID:
        outs = transform_sieve(signal_text, s)
        # intersection across transforms per protocol
        sets = [extract_hard(o) for o in outs]
        if sets:
            inter = set.intersection(*sets) if all(sets) else set()
        else:
            inter = set()
        fid = fid_hard(base, inter)
        sigma_vals.append(s)
        fid_vals.append(fid)
    plot_fid(sig_label, sigma_vals, fid_vals, outpath=f"fid_{hash(sig_label)}.png")
    return sigma_vals, fid_vals

def recursion_test(signal_text, depth=config.RECURSION_DEPTH, enforced=False):
    base = extract_hard(signal_text)
    cur = signal_text
    deltas = []
    for n in range(depth+1):
        cur_keys = extract_hard(cur)
        deltas.append(delta_hard(base, cur_keys))
        if n==depth:
            break
        # next step
        if enforced:
            # simple enforcement: prepend canonicalized base keys as context marker
            marker = "COMMITMENT_HASH:" + str(hash("".join(sorted(base))))
            ctx = marker + " " + cur
        else:
            ctx = cur
        # use summarizer as step transform to simulate T
        next_s = SUMMARIZER(ctx, max_length=40, min_length=5, do_sample=False)[0]['summary_text']
        cur = next_s
    plot_delta(signal_text[:30], list(range(depth+1)), deltas, outpath=f"delta_{hash(signal_text[:30])}.png")
    return deltas

if __name__ == "__main__":
    for s in config.SIGNS["sample_signals"]:
        compression_sweep(s)
        recursion_test(s, enforced=False)
        recursion_test(s, enforced=True)