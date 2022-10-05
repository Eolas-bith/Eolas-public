def text_topic_modeling(pickled_df,column):
    #Input has to be in a form f a dataframe (from function url_list_text_to_df()), 
    # or text to dataframe modification has to be implemented to this function
    #column = column of interest, the best choice is either summary or better - the keywords/
    """
    Topic modeling experiment: Extract topics with nltk and gensim
    This method requires preprocessing od the data to form a dataframe, which is then loaded as data input.
    reference: 
    https://app.pluralsight.com/course-player?clipId=89c38875-0a3f-4636-8d81-86d15e0d94ce
    """
    import gensim
    from gensim.utils import simple_preprocess
    from gensim.parsing.preprocessing import STOPWORDS
    from nltk.stem import WordNetLemmatizer, SnowballStemmer
    from gensim.corpora import Dictionary
    import pandas as pd
    import matplotlib.pyplot as plt
    import preprocess
    import pyldavis_topic_modeling

    #from ntlk.stem.porter import *
    import numpy as np
    np.random.seed(1234)
    import nltk
    #nltk.download('wordnet')  # this has to eb run just once
    #corpus= list of words, stopwords has to be removed.
    #corpus=remove_stop_words(text)
    #corpus=text
    stemmer=SnowballStemmer('english')
    # item in data- in form of pd dataframe, filtered out:

    #Example:
    #preprocessing the data:
    #movie_plots_selection=movie_plots_data[[movie_plots_df['Release year']>=2015 & movie_plots_df['Genre']=='Comedy']]
    #movie_plots=movie_plots_selection.plot  #
    #preprocessed_docs=movie_plots.map(preprocess)

    #in case the source of the text is dataframe-pickled with the text in summary column:
    df=pd.read_pickle(pickled_df)
    text_summarized=df[column]
    print("text_summarized loaded:",len(text_summarized))

    #generate list of uniqe words to feed the stopwords generator function disinfo_stopwords_cz()
    words=[]
    for text in text_summarized:
        for word in text.split(' '):
            words.append(word)
    words=set(words)
    #print(words)
    print("Number of uniqe words in corpus: ",len(words))

    #preprocessed_docs=text_summarized.map(preprocess)
    preprocessed_docs=text_summarized.apply(preprocess)
    print("Preprocessed docs created :",len(preprocessed_docs))

    #BoW dictionaru on the dataset:
    dictionary=gensim.corpora.Dictionary(preprocessed_docs)
    print("Dictionary created: ",len(dictionary))
    #filter out exreme values:
    dictionary.filter_extremes(no_below=2,no_above=0.5,keep_n=100000)
    #create a corpus using the BoW transformation:
    bow_corpus=[dictionary.doc2bow(doc) for doc in preprocessed_docs]
    # count he word occurence:
    word_dict_count={}
    for doc in bow_corpus:
        for i,word_info in enumerate(doc):
            word=dictionary[word_info[0]]
            word_count=word_info[1]
            if word in word_dict_count:
                word_dict_count[word]+=word_count
            else:
                word_dict_count[word]=0

    #create word dictionary:
    word_dict={'words':list(word_dict_count.keys()),'count':list(word_dict_count.values())}
    print("Size of the word dict: ",len(word_dict),"\n")
    print("Size of word_dict_count: ",len(word_dict_count),"\n")

    #train LDA model using BoW:
    lda_model=gensim.models.LdaMulticore(bow_corpus,num_topics=4,id2word=dictionary,passes=2,workers=4)
    print("lda_model trained!", lda_model.show_topics())

    def show_model_topics(model,num_words=4):
        for idx, topic in model.show_topics(num_words, formatted=False):
            print('Topic {} | Words & Probability: {}'.format(idx,topic))

    show_model_topics(lda_model,4)
    pyldavis_topic_modeling(lda_model,bow_corpus,dictionary)