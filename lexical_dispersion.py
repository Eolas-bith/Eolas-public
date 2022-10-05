#list_of_names=['Morgoth','Sauron','Melian','Elves','Galadriel','Men','Hobbits','Earendil','Numenor']

def lexical_dispersion(text,list_of_names):
    import nltk
    corpus=text
    tokens = nltk.word_tokenize(corpus)
    tokens = nltk.Text(tokens)  # NLTK wrapper for automatic text analysis.
    dispersion = tokens.dispersion_plot(list_of_names)
    return dispersion