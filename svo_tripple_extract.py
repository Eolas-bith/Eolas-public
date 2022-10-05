def svo_triple_extract(span):
    #requires the EN version of span - line or sentence
    from textacy.extract import subject_verb_object_triples
    import spacy
    nlp=spacy.load('en_core_web_sm')
    doc=nlp(span)
    iterator=subject_verb_object_triples(doc)
    svotr=[]
    for i in iterator:
        svotr.append(i)
    return svotr #list of SVO triple found in the span.s