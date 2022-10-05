def email_dir_miner(path):
    import VAR_working_directory
    from VAR_working_directory import eml_dirminer_output
    """Read ALL directory,TOP DOWN from starting point, select all the *.eml files and parse metadata into the dataframe"""
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
    ledf=pd.DataFrame(columns=columns)
    """iterate over the files and add pd series generated from each into the final datatframe"""
    #https://www.bogotobogo.com/python/python_traversing_directory_tree_recursively_os_walk.php
    for filename in os.listdir(path):
        file=filename
        #print(file)
        filename=str(str(path)+(os.fsdecode(filename)))
        #print(filename)
        if filename.endswith(".eml"):
            with open(filename,'rb') as fhdl:
                raw_email=fhdl.read()
                #print(filename)
                #all the code for edf filling comes here
                mail = mailparser.parse_from_bytes(raw_email)
                #data=np.array([str(file),str(mail.message_id),str(mail.from_),str(mail.subject),str(mail.to),str(mail.to_domains),str(mail.received),str(mail.attachments),str(mail.text_html)])
                data={"Filename":str(file),"messageID":str(mail.message_id),"from":str(mail.from_),"subject":str(mail.subject),"mailto":str(mail.to),"mailtod":str(mail.to_domains),"received":str(mail.received),"attachments":str(mail.attachments),"text-html":str(mail.text_html),"text":str(mail.text)}
                row=pd.Series(data,index=lcolumns)
                ledf=ledf.append(pd.Series(row),ignore_index=True)
                continue
        else:
            continue              
    #deduplicate the edgelist
    ledf.drop_duplicates(keep='first')
    print("[*]Duplicates dropped.")
    #print(edf)
    print(ledf.describe())
    print(ledf["subject"],ledf["from"])
    #save the edgelists to a csv files
    ledf.to_csv(eml_dirminer_output, sep=',', encoding='utf-8')
    print("[*] CSV file saved, done!")