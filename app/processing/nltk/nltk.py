import nltk

# nltk.download('punkt')

def getTokensByWord(text: str):
    return nltk.word_tokenize(text)

def getTokensBySentance(text: str):
    return nltk.sent_tokenize(text)