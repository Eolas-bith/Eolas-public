def rule_based_pattern_matcher(text,pattern):
    """
    important for sentiment analysis and intent recognition:

    Using spacy matcher to find word sequence patterns
    https://spacy.io/usage/rule-based-matching
    """

    import spacy
    from spacy.matcher import Matcher
    nlp=spacy.load('en_core_web_md')
    matcher=Matcher(nlp.vocab)
    #example:
    # pattern=[{"POS":"NOUN"},{"POS":"PRON"},{"POS":"AUX"},{"POS":"VERB"},{"POS":"ADP"},{"POS":"PROPN"}]
    matcher.add('NsubjAuxRoot',[pattern])


    nlp=spacy.load('en_core_web_sm')
    #this will read the document to the list of lines.
    with open(file,'r') as f:
        text_raw=[line.strip() for line in f.readlines()]
    

    for i,t in enumerate(text_raw):
        if i in range(0,len(text_raw)-2):
            doc=nlp(t)
            matches=matcher(doc)
            for match_id,start,end in matches:
                span=doc[start:end]
                print("Span: ",span.text)
                print("The positions in the doc are: ",start,"-",end)