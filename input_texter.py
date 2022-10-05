def input_texter(user_input):
    import input_type
    if input_type(user_input)=='URL':
        import requests
        import bs4
        from nltk.tokenize import sent_tokenize
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
        page=requests.get(user_input,headers=headers)
        page.raise_for_status()
        soup=bs4.BeautifulSoup(page.text,'html.parser')
        p_elems=[element.text for element in soup.find_all('p')]
        text_raw=''.join(p_elems)
        return text_raw
    elif input_type(user_input)=='IP':
        cmd='host'+' '+user_input
        return bash_commander(cmd)
    elif input_type(user_input)=='FILE':
        file=user_input
        with open(file,'r') as f:
            text_raw=[line.strip() for line in f.readlines()]
            return str(text_raw)
    elif input_type(user_input)=="URL_LIST":
            text_raw=url_list_text_to_corpus(user_input)
            return str(text_raw)
    else:
        wiki_searcher(user_input)