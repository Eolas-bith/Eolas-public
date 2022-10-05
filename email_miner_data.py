def email_miner_data(email_file):
    import datetime
    import json
    import eml_parser
    import numpy as np
    import pandas as pd
    import os
    import mailparser
    #https://pypi.org/project/mail-parser/
    """Dataframe design"""
    lcolumns=["Filename","messageID","from","subject","mailto","mailtod","received","attachments","text-html","text"]
    ledf=pd.DataFrame(columns=lcolumns)
    try:
        with open(email_file,'rb') as fhdl:
            raw_email=fhdl.read()
            #print(filename)
            #all the code for edf filling comes here
            mail = mailparser.parse_from_bytes(raw_email)
            #data=np.array([str(file),str(mail.message_id),str(mail.from_),str(mail.subject),str(mail.to),str(mail.to_domains),str(mail.received),str(mail.attachments),str(mail.text_html),str(mail.text)])
            data={"Filename":str(file),"messageID":str(mail.message_id),"from":str(mail.from_),"subject":str(mail.subject),"mailto":str(mail.to),"mailtod":str(mail.to_domains),"received":str(mail.received),"attachments":str(mail.attachments),"text-html":str(mail.text_html),"text":str(mail.text)}
            #dct=dict(enumerate(data.flatten(),1))
            row=pd.Series(data,index=lcolumns)
            ledf=ledf.append(pd.Series(row),ignore_index=True)
    except:
        pass
    #print(ledf)
    #print(ledf.describe())
    #print(ledf["subject"],ledf["Filename"])
    #deduplicate the edgelist
    #ledf.drop_duplicates(keep='first')
    #save the edgelists to a csv files
    #ledf.to_csv("ledf.csv", sep=',', encoding='utf-8')
    #print(data)
    return data