def pyldavis_topic_modeling(lda_model,bow_corpus,dictionary):
    import pyLDAvis
    import pyLDAvis.gensim_models as gensimvis
    pyLDAvis.enable_notebook()
    import show_model_topics
    import VAR_working_directory
    from VAR_working_directory import t_o_p_path

    lda_display=gensimvis.prepare(lda_model,bow_corpus,dictionary)
    pyLDAvis.display(lda_display)
    print("Saving the picture:")
    pyLDAvis.save_html(lda_display,"/Users/jindrich_karasek/data-science/lda_display1.html")
    print("Visualization saved!")


    print("LDA Using the TF-IDF:","\n")
    ####
    #LDA using TF-IDF -due to the better filtering acapabilities, it works a bit better than BoW only
    from gensim import corpora,models
    #create corpus
    tfidf=models.TfidfModel(bow_corpus)
    corpus_tfidf=tfidf[bow_corpus]

    #Train LDA using the TF-IDF:
    lda_model_tfidf=gensim.models.LdaMulticore(corpus_tfidf,num_topics=4,id2word=dictionary,passes=2,workers=4)
    print("Model lda_model_tfidf:",'\n')
    show_model_topics(lda_model_tfidf)

    import pyLDAvis
    import pyLDAvis.gensim_models as gensimvis
    pyLDAvis.enable_notebook()

    lda_display=gensimvis.prepare(lda_model_tfidf,bow_corpus,dictionary)
    pyLDAvis.display(lda_display)
    print("Saving the picture:")
    ldaf_tfidf_filename=t_o_p_path + "/"+"lda_tdfidfdisplay2.html"
    pyLDAvis.save_html(lda_display,ldaf_tfidf_filename)
    print("Visualization saved!")