import re

def getPhoneFromString(text: str) -> [int]:
    phoneNumbers = [int]

    phone_regex = r'\b\d{3}[-.]?\d{3}[-.]?\d{4}\b'
    phoneNumbers = re.findall(phone_regex, text)

    return phoneNumbers