def url_list_text_summ_to_corpus(file,output):
    import os
    import text_keywords_gen
    import text_summary
    import input_texter
    import bash_commander
    import wiki_searcher
    import input_type
    


    text=''
    with open(file,'r') as f:
        raw_input=[line.strip() for line in f.readlines()]
        a=len(raw_input)
        print("Number of URLS to process: ",a)
        #text=input_texter()
        #if not bool(os.path.isfile(out)):
        #    f=open(out,'x')
        #    f.close()
        #else:
        #    pass
        i=0
        for line in raw_input:
            i+=1
            try:
                print(line)
                out=input_texter(line)
                #print(out[:50])
                text=text+" "+text_summary(out)
                #try:
                #    text=text + text_summary(out)
                #except:
                #    text=text+ " "+out
                print(len(text))
                print(i," out from total: ",a," ","|",a-i," left.")
                f=open(output,'a')
                print("Destionation file opened.")
                print("Length of the text to write: ",len(text))
                f.write(text)
                print("File written.")
                f.close()
                print("Done,closing the file..")
                #text.close()
                print("Data collection finished, file closed.")
            except:
                continue
            #if i>5:
            #    break
    
        
        print("Destination file opened.")
        print("Length of the text to write: ",len(text))
        f.write(text)
        print("File written.")
        f.close()
        print("Done,closing the file..")
        ##text.close()
        print("Data collection finished, file closed.")
        #return text

file='/root/jupyter/TM-Hunting/Eolas/files/urls-4n6strider-it.txt'
output='/root/jupyter/TM-Hunting/Eolas/files/OUT-CORPUS-4n6strider-it-summ.txt'