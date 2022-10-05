def disinfo_stopwords_cz(words):
    import pandas as pd
    import spacy
    import translator
    import VAR_working_directory
    from VAR_working_directory import t_o_p_path
    
    nlp=spacy.load("en_core_web_lg")
    df_stopwords=pd.DataFrame()
    for wrd in words:
        try:
            tr_wrd=translator(wrd)
        except:
            tr_wrd="not_translated"
        #nlp code placeholder
        doc=nlp(wrd)
        try:
            for entity in doc.ents:
                entl=entity.label_
                entt=entity.text
                data={"word":wrd,"en_translation":tr_wrd,"is_ner":"yes","entity_label":entl,"entity_text":entt}
                ser=pd.Series(data=data,index=["word","en_translation","is_ner","entity_label","entity_text"])
                df_stopwords=df_stopwords.append(ser,ignore_index=True)
        except:
            data={"word":wrd,"en_translation":tr_wrd,"is_ner":"no","entity_label":"NA","entity_text":"NA"}
            ser=pd.Series(data=data,index=["word","en_translation","is_ner","entity_label","entity_text"])
            df_stopwords=df_stopwords.append(ser,ignore_index=True)
            continue
    stopwords_df_filename="df_stopwords_pickle"
    dfstopwordssavepath=t_o_p_path+"/"+stopwords_df_filename
    df_stopwords.to_pickle(dfstopwordssavepath,compression="infer",protocol=5)
    print(df_stopwords.info())
    return df_stopwords