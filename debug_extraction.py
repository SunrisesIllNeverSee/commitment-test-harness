import spacy

nlp = spacy.load('en_core_web_sm')
text = "You must pay $100 by Friday if the deal closes; it's likely rainy, so plan accordingly."
doc = nlp(text)

print('Sentences detected by spaCy:')
for i, sent in enumerate(doc.sents):
    print(f'{i+1}. [{sent.text}]')
    print(f'   Has "must": {"must" in sent.text.lower()}')

print('\nTesting extract_hard_commitments:')
from src.extraction import extract_hard_commitments
commitments = extract_hard_commitments(text, nlp)
print(f'Commitments found: {commitments}')
