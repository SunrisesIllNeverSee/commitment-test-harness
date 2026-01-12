# ...new file...
import re
import json
import hashlib
import dateparser
import spacy

nlp = spacy.load("en_core_web_sm")

NUM_RE = re.compile(r'\$?\d{1,3}(?:[,\d]*)?(?:\.\d+)?')

MODAL_LEX = {
    "must": "OBLIGATION", "shall": "OBLIGATION", "required": "OBLIGATION",
    "must not": "PROHIBITION", "shall not": "PROHIBITION", "cannot": "PROHIBITION",
    "may": "PERMISSION", "is defined as": "DEFINITION", "means": "DEFINITION"
}

def normalize_text(s: str) -> str:
    s = s.strip()
    s = s.replace("—", "-").replace("–", "-")
    s = " ".join(s.split())
    return s

def canonicalize_number(tok: str) -> str:
    # convert simple money/number patterns to placeholders
    if NUM_RE.search(tok):
        return "#NUM"
    dt = dateparser.parse(tok)
    if dt:
        return dt.date().isoformat()
    return tok.lower()

def sentence_candidates(text: str):
    doc = nlp(normalize_text(text))
    return [sent.text.strip() for sent in doc.sents]

def cue_lookup(sent: str):
    s = sent.lower()
    for cue, mod in MODAL_LEX.items():
        if cue in s:
            return cue, mod
    return None, None

def build_tuple_from_sentence(sent: str):
    cue, modality = cue_lookup(sent)
    doc = nlp(sent)
    subj = None
    obj = None
    verb = None
    cond = None
    # regex conditional capture
    m = re.search(r'(.+?)\b(if|when|provided that|unless|in the event that)\b(.+)', sent, flags=re.I)
    if m:
        cond = m.group(3).strip()
    # dependency heuristics
    for token in doc:
        if token.dep_ in ("nsubj", "nsubjpass") and subj is None:
            subj = token.text
        if token.dep_ in ("dobj", "pobj", "attr") and obj is None:
            obj = token.text
        if token.pos_ == "VERB" and verb is None:
            verb = token.lemma_
    subj = subj or "UNKNOWN"
    verb = verb or ""
    obj = obj or ""
    # canonicalize object tokens
    obj_canon = " ".join(canonicalize_number(t.text) for t in nlp(obj)) if obj else ""
    cond_canon = cond.lower() if cond else ""
    tup = {
        "actor": subj.lower(),
        "modality": modality or "UNMARKED",
        "action": verb,
        "object": obj_canon,
        "condition": cond_canon
    }
    # canonical key deterministic JSON
    key = json.dumps(tup, sort_keys=True, separators=(',', ':'))
    key_hash = hashlib.sha256(key.encode("utf8")).hexdigest()[:12]
    return tup, key, key_hash

def extract_hard(text: str):
    keys = []
    for sent in sentence_candidates(text):
        cue, _ = cue_lookup(sent)
        if cue:
            tup, key, h = build_tuple_from_sentence(sent)
            keys.append(key)
    # deterministic fallback: if none, emit empty set
    return set(keys)