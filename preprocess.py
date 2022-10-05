def preprocess(text):
    import lemmatize_stemming
    from gensim.utils import simple_preprocess
    result=[]
    for token in gensim.utils.simple_preprocess(text):
        #remove stopword token and tokens of lenght smaller than 3   
        #if token not in gensim.parsing.preprocessing.STOPWORDS and len(token) >2:
        if token not in stopwords and len(token) >2:
            result.append(lemmatize_stemming(token))
    return result