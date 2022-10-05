def pytextrank_top_phrases(text):
    #textrank: https://spacy.io/universe/project/spacy-pytextrank
    """
    Implementation of spacy's textrank

    e.g. for mining entities, keywords, preliminar analysis if the input text
    """
    import spacy
    import pytextrank
    nlp=spacy.load('en_core_web_sm')
    tr=pytextrank.TextRank()
    nlp.add_pipe(tr.PipeLineComponent,name='textrank',last=True)
    doc=nlp(text)
    phrases=[]
    for p in doc._.phrases:
        #print('{:.4f} {:5d} {}'.format(p.rank,p.count.p.text))
        phrases.append([p.rank,p.count,p.text])
        #print(p.chunks)
    return phrases
