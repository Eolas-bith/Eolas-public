#Named entity recognitions:
#sentence="Apple is looking at buying U.K. startup for $1 billion"

def ner_extract(sentence):
    #Named entity recognition in a span / sentence.
    import spacy
    nlp=spacy.load("en_core_web_sm")
    doc=nlp(sentence)
    entities=[]
    for ent in doc.ents:
        #print(ent.text, ent.start_char, ent.end_char, ent.label_)
        entities.append([ent.text, ent.start_char, ent.end_char, ent.label_])
    return entities