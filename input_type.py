def input_type(user_input):
    #recognizes: URL, IP and if any of these, considers as a string.
    import os,sys,re
    URL_regex='(https?|ftp|file)://[-A-Za-z0-9\+&@#/%?=~_|!:,.;]*[-A-Za-z0-9\+&@#/%=~_|]'
    IP_regex=re.compile("^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$")
    URL_LIST_regex='(https?|ftp|file)://[-A-Za-z0-9\+&@#/%?=~_|!:,.;]*[-A-Za-z0-9\+&@#/%=~_|]'
    #FILE_regex=
    cwd=os.getcwd()
    path=cwd
    dirs=os.listdir(path)
    #OS walk:
    #for root,dirs,files in os.walk(path,topdown=True):
        #do sth
    if len(re.findall(URL_regex,user_input))> 1:
        return "URL_LIST"
    elif bool(re.search(URL_regex,user_input)):
        return "URL"
    
    elif bool(re.search(IP_regex,user_input)):
        return "IP"
    elif bool(os.path.isfile(user_input)):
        return "FILE"
    else:
        #String if nothing else recognized:
        return "STRING"