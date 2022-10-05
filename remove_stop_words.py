
def remove_stop_words(corpus,stop_file_path):
    import get_stopwords_list
    stop_set=get_stopwords_list(stop_file_path)
    results=[]
    for text in corpus:
        tmp=text.split(' ')
        for stop_word in stop_set:
            if stop_word in tmp:
               tmp.remove(stop_word)
        results.append(" ".join(tmp))
    return results