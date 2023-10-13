import spacy
from spacy.matcher import Matcher

nlp = spacy.load('en_core_web_lg')

def getPhoneFromString(text):
    # Initialize the Matcher with the shared vocabulary
    matcher = Matcher(nlp.vocab)

    pattern = [{
        'TEXT':{
            'REGEX': "^[+]*[(]{0,1}[0-9]{1,4}[)]{0,1}[-\s\./0-9]*$",
        }
        }]
    matcher.add('PHONE_NUM', [pattern])

    doc = nlp(text)
    matches = matcher(doc)

    numbers = [doc[start:end].text for _, start, end in matches]

    return numbers