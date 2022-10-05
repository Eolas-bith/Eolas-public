#{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}
#--------------------------------------------------
#part of the code block for topic modeling
###Stopwords from kaggle for czech: https://www.kaggle.com/mpwolke/czech-stop-words-w2v

def get_stopwords_list(stop_file_path):
    #This loads the stop words list
    with open(stop_file_path,'r',encoding='utf-8') as f:
        stopwords=f.readlines()
        stop_set=set(m.strip() for m in stopwords)
        return list(frozenset(stop_set))

