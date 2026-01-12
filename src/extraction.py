from spacy import load
import re

def load_spacy_model(model_name='en_core_web_sm'):
    nlp = load(model_name)
    return nlp

def normalize_text(text):
    """Normalize text for comparison: lowercase, strip punctuation."""
    return re.sub(r'[^\w\s]', '', text.lower().strip())

def extract_hard_commitments(text, nlp=None):
    """Extract commitments using expanded modal keyword detection."""
    if nlp is None:
        nlp = load_spacy_model()
    
    doc = nlp(text)
    commitments = set()
    
    # Expanded modal keywords
    hard_modals = {'must', 'shall', 'will', 'have', 'need', 'required', 'ought', 'cannot', 'should'}
    soft_modals = {'might', 'could', 'may', 'perhaps', 'maybe', 'tend'}
    
    # Extract by sentence-level modal presence
    for sent in doc.sents:
        sent_lower = sent.text.lower()
        # Check for hard modals
        if any(modal in sent_lower for modal in hard_modals):
            commitments.add(sent.text.strip())
        # Check for soft modals
        elif any(modal in sent_lower for modal in soft_modals):
            commitments.add(sent.text.strip())
    
    return commitments

def extract_from_texts(texts, model_name='en_core_web_sm'):
    nlp = load_spacy_model(model_name)
    all_commitments = {}
    
    for text in texts:
        commitments = extract_hard_commitments(text, nlp)
        all_commitments[text] = commitments
    
    return all_commitments

def extract_hard(text: str, nlp=None) -> set:
    """Shorthand for extract_hard_commitments."""
    return extract_hard_commitments(text, nlp)