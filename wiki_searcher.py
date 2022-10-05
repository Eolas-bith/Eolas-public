def wiki_searcher(user_input):
    import spacy
    import wikipedia
    nlp=spacy.load('en_core_web_sm')
    doc=nlp(user_input)
    #The NLP part needs improvement. Currently, it answers only to question like this:
    # "I want to know about flint stone"
    for t in doc:
        if t.dep_=='pobj' and (t.pos_=='NOUN' or t.pos_=='PROPN'):
            phrase=(''.join([child.text for child in t.lefts]) +" "+t.text).lstrip()
            print("Searching Wiki for: ",phrase,'\n')
            wiki_resp=wikipedia.page(phrase)
            art_title=wiki_resp.title
            art_url=wiki_resp.url
            art_summ=wikipedia.summary(phrase,sentences=9)
            answer=art_title+"\n"+art_url+"\n"+art_summ+"\n"
            return answer
        elif t.pos_=='NOUN':
            phrase=t.text
            print("Searching wiki for: ",phrase,'\n')
            wiki_resp=wikipedia.page(phrase)
            art_title=wiki_resp.title
            art_url=wiki_resp.url
            art_summ=wikipedia.summary(phrase,sentences=9)
            answer=art_title+"\n"+art_url+"\n"+art_summ+"\n"
            return answer
        else:
            try:
                phrase=t.text
                print("Searching wiki for: ",phrase,'\n')
                wiki_resp=wikipedia.page(phrase)
                art_title=wiki_resp.title
                art_url=wiki_resp.url
                art_summ=wikipedia.summary(phrase,sentences=9)
                answer=art_title+"\n"+art_url+"\n"+art_summ+"\n"
                return answer
            except:
                return "Wrong_input"