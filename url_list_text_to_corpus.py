def url_list_text_to_corpus(file,output):
    import os
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
            
        for i,line in enumerate(raw_input):
            try:
                print(line)
                out=input_texter(line)
                text=text+" "+out
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
    
        
        #print("Destionation file opened.")
        #print("Length of the text to write: ",len(text))
        #f.write(text)
        #print("File written.")
        #f.close()
        #print("Done,closing the file..")
        ##text.close()
        #print("Data collection finished, file closed.")
        #return text