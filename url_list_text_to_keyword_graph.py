def url_list_text_to_keyword_graph(filename):
    import os
    #For the graphing:
    import networkx as nx
    import pandas as pd
    import spacy
    import json
    import demoji
    import edgelist_to_graph
    import text_keywords_gen
    import input_texter
    import bash_commander
    import wiki_searcher
    import input_type


    #import spacy_udpipe
    text=''
    colls=['source','target']
    df=pd.DataFrame(columns=colls)
    
    with open(filename,'r') as f:
        raw_input=[line.strip() for line in f.readlines()]
        a=len(raw_input)
        print("Number of URLS to process: ",a)
        i=0    
        for line in raw_input:
            i+=1
            print("Remaining number of urls: ", a-i,"|",a)
            print("line: ",line)
            if len(line)<1:
                line="empty-url"
            else: 
                line=line
                
            try:
                out=input_texter(line)
                #print("Output length: ",len(out))
                keywords=text_keywords_gen(out)
                print("Keywords: ","\n",keywords)
                #print(type(keywords))
                #Block of code to generate df from line=urls and keyword.
                for r in keywords:
                    #print(r)
                    #print(line)
                    dta={"source":str(line).strip(),"target":str(r).strip()}
                    #print("Data: ","\n",dta)
                    ser=pd.Series(data=dta)
                    #print("Series: ","\n",ser)
                    df=df.append(ser,ignore_index=True)
            except:
                continue
                    
                
        edgelist_to_graph(df)