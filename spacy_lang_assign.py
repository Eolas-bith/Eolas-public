def spacy_lang_assign(lang,model_size):
    #lang -> df_ac["lang"]
    #model size values: "sm" "md" "lg"
    #python -m spacy download "model"
    #model_size="sm"
    if lang=='cn':
        model="zh_core_web"+"_"+model_size
    elif lang=='hr':
        model="hr_core_news"+"_"+model_size
    elif lang=='da':
        model=="da_core_news"+"_"+model_size
    elif lang=='nl':
        model="nl_core_news"+"_"+model_size
    elif lang=="en":
        model="en_core_web"+"_"+model_size
    elif lang=="fi":
        model="fi_core_news"+"_"+model_size
    elif lang=="fr":
        model="fr_core_news"+"_"+model_size
    elif lang=="de":
        model="de_core_news_sm"+"_"+model_size
    elif lang=="el":
        model="el_core_news"+"_"+model_size
    elif lang=="it":
        model="it_core_news"+"_"+model_size
    elif lang=="ja":
        model="ja_core_news"+"_"+model_size
    elif lang=="ko":
        model="ko_core_news"+"_"+model_size
    elif lang=="lt":
        model="lt_core_news"+"_"+model_size
    elif lang=="mk": #Makedonia
        model="mk_core_news"+"_"+model_size
    elif lang=="nb": #Norvegian Bokmal
        model="nb_core_news"+"_"+model_size
    elif lang =="pl": #polish
        model="pl_core_news"+"_"+model_size
    elif lang=="pt":#portuguese
        model="pt_core_news"+"_"+model_size
    elif lang=="ro": #Romanian
        model="ro_core_news"+"_"+model_size
    elif lang=="ru":
        model="ru_core_news"+"_"+model_size
    elif lang=="es":
        model="es_core_news"+"_"+model_size
    elif lang=="sv":
        model="sv_core_news"+"_"+model_size
    else:
        #model="spacy_udpipe" - >this wont work because it has to preinstall particular language package, anyways.
        model="UNSUPORTED_LANGUAGE"
    return model