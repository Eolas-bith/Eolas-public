def keyphrase(doc):
    keywords=["wiki",'graph','osint']

    for t in doc:
        #print(doc)
        #print(t.text)
        if t.text in keywords:
            if t.text =="wiki":
                print("wiki entered")
                
                for t in doc: # need to remove value  token.text=='wiki' to work - otherwise it always searches for "wiki is"
                    # working version of the input: "What is wiki pizza? "
                    if t.dep_=='pobj' and (t.pos_=='NOUN' or t.pos_=='PROPN'):
                        return (' '.join([child.text for child in t.lefts]) +" "+t.text).lstrip()
                    for t in reversed(doc):
                        if t.dep_=='nsubj' and (t.pos_=='NOUN' or t.pos_=="PROPN"):
                            return t.text+" "+t.head.text
                    for t in reversed(doc):
                        if t.dep_=='dobj' and (t.pos_=='NOUN' or t.pos_=='PROPN'):
                            return t.head.text + "ing" +" "+t.text
                    return False

            if t.text=="graph":
                print("Graph function entered.")
                return False
                #do something like extract the t.lefts and run grapher on it.