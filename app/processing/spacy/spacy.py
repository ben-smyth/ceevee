import en_core_web_sm

def spacyTest(text: str):
    nlp = en_core_web_sm.load()
    doc = nlp(text)

    return([(w.text, w.pos_) for w in doc])


def getSpacyNames(text: str):
    nlp = en_core_web_sm.load()
    doc = nlp(text)

    return([(w.text, w.label_) for w in doc.ents if w.label_ == "PERSON"])