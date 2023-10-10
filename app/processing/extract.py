from processing.nltk.email import getEmailFromString
from processing.nltk.phone import getPhoneFromString

def extract(text: str):
    return {
        "emails": getEmailFromString(text),
        "phoneNumbers": getPhoneFromString(text)
    }