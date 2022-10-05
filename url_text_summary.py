#text summary code:
#Whole code as a function:
def url_text_summary(url,word_count):
    import requests
    import bs4
    from nltk.tokenize import sent_tokenize
    from gensim.summarization import summarize
    page=requests.get(url)
    page.raise_for_status()
    soup=bs4.BeautifulSoup(page.text,'html.parser')
    p_elems=[element.text for element in soup.find_all('p')]
    speech=''.join(p_elems)
    summary=summarize(speech,word_count=word_count)
    sentences=sent_tokenize(summary)
    sents=set(sentences)
    out=' '.join(sents)
    print("\nSummary: ")
    print(out)
    return out