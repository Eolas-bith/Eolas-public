def text_keywords_gen(user_input): 
    import requests
    import bs4
    from nltk.tokenize import sent_tokenize
    from gensim.summarization import summarize
    from gensim.summarization import keywords
    #text= input_texter(user_input)
    text=user_input
    #print("\nKeywords: ")
    #print(keywords(user_input).split("\n"))
    kwrds=keywords(user_input).split("\n")
    return kwrds