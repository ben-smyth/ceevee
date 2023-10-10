import re

def getEmailFromString(text: str) -> [str]:
    email = [str]

    email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    email = re.findall(email_regex, text)

    return email