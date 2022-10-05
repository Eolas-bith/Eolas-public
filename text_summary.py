def text_summary(user_input,ratio):
    import requests
    import bs4
    import input_texter
    from nltk.tokenize import sent_tokenize
    from gensim.summarization import summarize
    text= input_texter(user_input)
    print("\nSummary: ")
    if len(text)>100000:
        print("Sample of text: ",text[:250])
        print("Text too long for a brief summary...skipping!")
    else:
        summary=summarize(text,ratio=ratio) #instead of word_count its possible to use "ratio=0.01" to get summary in length of 1% of the document 
        sentences=sent_tokenize(summary)
        sents=set(sentences) #set is unordered, deduplicated, so output might vary.
        #print(' '.join(sents))
        return ' '.join(sents)