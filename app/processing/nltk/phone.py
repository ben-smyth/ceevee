import re

def getPhoneFromString(text: str) -> [str]:
    phoneNumbers = []

    patterns = [
        r'(?:\+?\d{2}\s?)?\d{4}\s?\d{4,5}',
        r'(?:\(?\d{3}\)?[\s.-]?)?\d{3}[\s.-]?\d{4}',  # matches (123) 456-7890
        r'\d{3}-\d{3}-\d{4}',  # matches 123-456-7890 or 123-456-7890 ext. 1234
        r'\d{3}-\d{3}-\d{4}(?: ext\. \d{1,4})?'
    ]

    combined_pattern = "|".join(patterns)
    phoneNumbers = re.findall(combined_pattern, text)

    # Remove duplicates from the list while preserving order
    phoneNumbers = list(dict.fromkeys(phoneNumbers))

    return phoneNumbers