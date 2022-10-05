def url_list_text_to_df(file):
    import os
    import pandas as pd
    import spacy
    import json
    import demoji
    #import spacy_udpipe
    from tqdm import tqdm
    import input_texter
    import text_keywords_gen
    import text_summary
    import svo_tripple_extract
    import translator
    import sentiment_detector
    import VAR_working_directory
    from VAR_working_directory import t_o_p_path

    text=''
    colls=["url","summary","keywords","sentiment","svotr"]
    df=pd.DataFrame(columns=colls)
    with open(file,'r') as f:
        raw_input=[line.strip() for line in f.readlines()]
        a=len(raw_input)
        print("Number of URLS to process: ",a)
        i=0
            
        for line in tqdm(raw_input):
            i+=1
            #print("Remaining number of ULRS: ",a-i,"|",a)
            #print("Line: ",line)
            if len(line)<1:
                line="empty-url"
            else:
                line=line
            try:
                out=input_texter(line)
                keywords=text_keywords_gen(out)
                if len(keywords)<1:
                    keywords="empty-keywords"
                else: keywords=keywords
                summary=text_summary(out)
                if len(summary)<3:
                    summary="Too-short-to-summarize"
                    svotr="SVO-tripple-undetected"
                    sentiment="Sentiment-undetected"
                else:
                    summary=summary
                    svotr=svo_tripple_extract(translator(summary))
                    sentiment=sentiment_detector(translator(summary))
                    
                #print("Keywords: ","\n",keywords)
                #print("\nSummary of the text from url: ","\n",summary)
                dta={"url":str(line).strip(),"summary":str(summary).strip(),"keywords":str(keywords).strip(),"svotr":str(svotr).strip(),"sentiment":str(sentiment).strip()}
                ser=pd.Series(data=dta)
                df=df.append(ser,ignore_index=True)
            except:
                continue
    #return df 
    #pickle_path="/root/jupyter/TM-Hunting/Eolas/files/df_pickle"+projectname
    df.to_pickle(t_o_p_path,compression="infer",protocol=4)
    #print(df.head())
    #print(df.info())
    print(df.describe())
    #for col in df.columns:
    #    print(col)