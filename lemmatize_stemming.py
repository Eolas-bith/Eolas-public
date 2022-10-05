def lemmatize_stemming(text):
    from nltk.stem import WordNetLemmatizer, SnowballStemmer
    #lemmatize + stemm a text
    return stemmer.stem(WordNetLemmatizer().lemmatize(text,pos='v'))