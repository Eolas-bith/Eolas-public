def cz_mff_parser(text):
    import bash_commander
    #raw result:
    cmd="curl --data "+"\""+"tokenizer=&tagger=&parser=&data="+str(text)+"\""+" "+"http://lindat.mff.cuni.cz/services/udpipe/api/process"
    #with json parsing:
    #cmd="curl --data "+"\""+"tokenizer=&tagger=&parser=&data="+str(text)+"\""+" "+"http://lindat.mff.cuni.cz/services/udpipe/api/process"+"| PYTHONIOENCODING=utf-8 python -c "+"\""+"import sys,json; sys.stdout.write(json.load(sys.stdin)['result'])"+"\""    
    print(bash_commander(cmd))