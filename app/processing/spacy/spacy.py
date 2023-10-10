import en_core_web_sm

def spacyTest(text: str):
    nlp = en_core_web_sm.load()
    doc = nlp(text)

    return([(w.text, w.pos_) for w in doc])


