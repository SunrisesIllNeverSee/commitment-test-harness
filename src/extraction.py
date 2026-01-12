from spacy import load

def load_spacy_model(model_name='en_core_web_sm'):
    nlp = load(model_name)
    return nlp

def extract_hard_commitments(text, nlp):
    doc = nlp(text)
    commitments = set()
    
    for sent in doc.sents:
        for token in sent:
            if token.dep_ in ('nsubj', 'dobj', 'pobj') and token.head.lemma_ in ('must', 'shall', 'cannot'):
                commitments.add(sent.text)
    
    return commitments

def extract_from_texts(texts, model_name='en_core_web_sm'):
    nlp = load_spacy_model(model_name)
    all_commitments = {}
    
    for text in texts:
        commitments = extract_hard_commitments(text, nlp)
        all_commitments[text] = commitments
    
    return all_commitments