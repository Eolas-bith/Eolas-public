def wc_from_url(url,jpg):

    """
    Wordclouds - text scraped from URL
    """
    """Combined: Scrape text from URL, parse, tokenize, dedup with set,
    turn to string and send to wordloud!"""

    #gensim wiki link https://en.wikipedia.org/wiki/Gensim

    import requests
    import bs4
    from nltk.tokenize import sent_tokenize
    from gensim.summarization import summarize

    import numpy as np
    from PIL import Image
    import matplotlib.pyplot as plt
    from wordcloud import WordCloud, STOPWORDS


    #url='https://en.wikipedia.org/wiki/Meditation'
    #url='https://www.ac24.cz/'
    page=requests.get(str(url))
    page.raise_for_status()
    soup=bs4.BeautifulSoup(page.text,'html.parser')
    p_elems=[element.text for element in soup.find_all('p')]

    speech=''.join(p_elems)

    print("\nSummary of the Text from URL: ")
    """procedure below removes duplicate sentences, ocassionally left by gensim"""
    summary=summarize(speech,word_count=100) #instead of word_count its possible to use "ratio=0.01" to get summary in length of 1% of the document 
    sentences=sent_tokenize(summary)
    sents=set(sentences) #set is unordered, deduplicated, so output might vary.
    print(' '.join(sents))
    print(type(sents))




    text = str(sents)

    # Load an image as a NumPy array.
    mask = np.array(Image.open(str(jpg)))


    # Get stop words as a set and add extra words.
    stopwords = STOPWORDS
    stopwords.update(['us', 'one', 'will', 'said', 'now', 'well', 'man', 'may',
                      'little', 'say', 'must', 'way', 'long', 'yet', 'mean',
                      'put', 'seem', 'asked', 'made', 'half', 'much',
                      'certainly', 'might', 'came','upon'])

    # Generate word cloud.
    wc = WordCloud(max_words=50,
                   relative_scaling=0.5,
                   mask=mask,
                   background_color='white',
                   stopwords=stopwords,
                   margin=2,
                   random_state=7,
                   contour_width=2,
                   contour_color='brown',
                   colormap='YlGnBu_r').generate(text)

    # Turn wc object into an array.
    colors = wc.to_array()

    # Plot and save word cloud.
    plt.figure(figsize=(25,30))
    plt.title("What wiki thinks about meditation:\n",
          fontsize=15, color='brown')
    plt.text(-10, 0, "Meditation!",fontsize=20, fontweight='bold', color='turquoise')
    plt.suptitle("Hell yes!",
                 x=0.52, y=0.095, fontsize=15, color='brown')
    plt.imshow(colors, interpolation="bilinear")
    plt.axis('off')
    plt.show()
    ##plt.savefig('hound_wordcloud.png')