from processing.nltk.email import getEmailFromString
from processing.nltk.phone import getPhoneFromString
from processing.spacy.name import getNameFromString

def extract(text: str):
    return {
        "emails": getEmailFromString(text),
        "phoneNumbers": getPhoneFromString(text),
        "names": getNameFromString(text)
    }