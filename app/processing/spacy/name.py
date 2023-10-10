import spacy
from spacy.matcher import Matcher

nlp = spacy.load('en_core_web_sm')

def getNameFromString(text):
    # Initialize the Matcher with the shared vocabulary
    matcher = Matcher(nlp.vocab)

    # Define the pattern for matching names

    pattern = [{'POS': 'PROPN'}, {'ENT_TYPE': 'PERSON'}]
    matcher.add('NAME', [pattern])

    doc = nlp(text)
    matches = matcher(doc)

    names = [doc[start:end].text for _, start, end in matches]

    return names