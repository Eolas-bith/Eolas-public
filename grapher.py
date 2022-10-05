def grapher(user_input):
    import networkx as nx
    import pandas as pd
    import requests
    import bs4
    import spacy
    import matplotlib.pyplot as plt
    import json
    import input_type
    import input_texter
    import language_detection
    import translator
    import deepl_usage
    import wiki_searcher
    import string_cleaner
    import text_summary
    import bash_commander
    import url_list_text_to_corpus
    import VAR_working_directory
    from VAR_working_directory import g_path
    import spacy_udpipe

    input_tp=input_type(user_input)
    #Loading defaults:
    df_id=pd.DataFrame()
    #Input:
    text_raw=input_texter(user_input)
    text_raw=string_cleaner(text_raw)
    print("User input type: ",input_tp)
    print("User input sample: ","\n",text_raw[:166])
    #Language detection and translation:
    if language_detection(text_raw)!='EN':
        print('Translating to English, first...')
        print("Text to translate: ",len(text_raw))
        text=translator(string_cleaner(text_raw),target_lang='EN')
        print(text[:66],"\n")
        #deepl_usage()
    else:
        nlp=spacy.load('en_core_web_md')
        text=text_raw
        #deepl_usage()
        #print(type(text))
    #Text summary for checking:
    summary=text_summary(user_input,81)
    print("\n","Summary for input validation: ","\n",summary)    
    #Creation of the dataframe:
    nlp=spacy.load('en_core_web_md')
    nlp.max_length = 4030000
    doc=nlp(text)
    for i,sent in enumerate(doc.sents):
        #print(sent,'\n')
        if i in range(0,len(text)-2):
            for token in sent:
                if token.dep_=="dobj" or token.pos_=='PROPN' or token.pos_=='NOUN':
                    dobj=[token.text]
                    conj=[t.text for t in token.conjuncts]
                    vrb=[t.text for t in sent if t.pos_=='VERB']
                    objj=[t.text for t in sent if t.pos_=='VPROPN']
                    #compose the list of elements:
                    vrbd=vrb+objj
                    dobj_conj=dobj+conj
                    if len(dobj_conj)>1:
                        #print(dobj_conj)
                        line=r"{"+"\""+"source"+"\""+":"+"\""+str(dobj).replace(u'\xa0', u'').replace('\\xa0', '').replace(':', '').replace(' ', '').replace('\'','').replace('[', '').replace(']', '').replace('\"', '').strip()+"\""+","+"\""+"target"+"\""+":"+"\""+str(conj).replace(u'\xa0', u'').replace('\\xa0', '').replace(':', '').replace(' ', '').replace('\'','').replace('[', '').replace(']', '').replace('\"', '').strip()+"\""+"}"
                        df_id=df_id.append(json.loads(line),ignore_index=True)
                    if len(vrbd)>1:
                        line=r"{"+"\""+"source"+"\""+":"+"\""+str(vrb).replace(u'\xa0', u'').replace('\\xa0', '').replace(':', '').replace(' ', '').replace('\'','').replace('[', '').replace(']', '').replace('\"', '').strip()+"\""+","+"\""+"target"+"\""+":"+"\""+str(objj).replace(u'\xa0', u'').replace('\\xa0', '').replace(':', '').replace(' ', '').replace('\'','').replace('[', '').replace(']', '').replace('\"', '').strip()+"\""+"}"
                        df_id=df_id.append(json.loads(line),ignore_index=True)

    
    for entity in doc.ents:
        entl=entity.label_
        entt=entity.text
        data={"source":entt,"target":entl}
        ser=pd.Series(data=data,index=['source','target'])
        df_id=df_id.append(ser,ignore_index=True)
        #if entity.label_=='PERSON':
            #print(entity.label_,"|",entity.text)
            
    #for col in df_id:
    #    print("Columns name: ",col,"\n")
    print("[+] Columns to dataframe loaded")
    
    #Graphing:
    df1=df_id[['source','target']].fillna("X")
    #print(df1)

    df1.columns=['source','target']
    edgelist=df1
    #deduplicate the edgelist
    edgelist.drop_duplicates(keep='first')

    #save the edgelists to a csv files
    #edgelist.to_csv("/root/.jupyter/files/Dust.csv", sep=',', encoding='utf-8')
    #print("Edgelist csv saved")

    print("G9 graph generation:")
    #G9=nx.from_pandas_dataframe(df,source='source',target='target',create_using=nx.MultiDiGraph())
    G9=nx.from_pandas_edgelist(edgelist,source='source',target='target',create_using=nx.MultiGraph())

    print("Whole Graph size: ", G9.size(),"number of nodes:",G9.number_of_nodes())
    print(nx.info(G9))
    print("\n [*] All data loaded successfully, Graph generated!")
    nx.draw(G9,with_labels=True, node_size=150, node_color="skyblue", node_shape="s", alpha=0.5, linewidths=40)
    filename=str(user_input).replace(":","").replace(".","").replace("/","")
    path=g_path+filename
    pathp=path+".png"
    paths=path+".svg"
    pathg=path+".gexf"
    plt.savefig(pathp,format="png")
    plt.savefig(paths,format="svg")
    print(path," saved!")
    #print("Graph picture saved")
    

    #Gephi export:
    #print("Exporting to GFX file:")
    nx.write_gexf(G9, pathg)
    print("[*]GFX file saved.")

