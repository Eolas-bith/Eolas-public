def noun_chunks_extract(text):
    nchunks=[]
    import spacy
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)
    for chunk in doc.noun_chunks:
        #print(chunk.text, chunk.root.text, chunk.root.dep_,chunk.root.head.text)
        nchunks.append([chunk.text, chunk.root.text, chunk.root.dep_,chunk.root.head.text])
    return nchunks