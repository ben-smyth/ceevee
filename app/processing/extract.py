import re
from processing.nltk import getTokensBySentance, getTokensByWord

def extractName(sentanceTokens):
    names = []

    name_regex = r"([A-Z][a-z]+)(\s[A-Z][a-z]+)+"

    for sentance in sentanceTokens:
        names.extend(re.findall(name_regex, sentance))

    return names


def extract(text):
    wordTokens = getTokensByWord(text)
    sentanceTokens = getTokensBySentance(text)

    names = extractName(sentanceTokens)

    return names
        