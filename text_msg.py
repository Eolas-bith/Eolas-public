def text_msg(update,context): # this function needs to repair so that if grapher is called, it wont do the wiki search.
    msg=update.message.text
    #nlp=spacy.load('en_core_web_sm')
    #doc=nlp(msg)
    concept=input_texter(msg)
    print(keyphrase)
    print(concept)
    if input_type(msg)=="STRING":
        update.message.reply_text(wiki_searcher(msg))
    elif input_type(msg)=="URL":
        update.message.reply_text(grapher(msg))
    elif input_type(msg)=='FILE':
        update.message.reply_text(grapher(msg))
    elif input_type(msg)=='IP':
            print('OSINT YET TO BE IMPLEMENTED')
    else:
        update.message.reply_text('Please rephrase your question.')
        
