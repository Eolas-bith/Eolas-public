def punctuation_heatmap(text,punct_char):
    import math
    from string import punctuation
    import nltk
    import numpy as np
    import matplotlib.pyplot as plt
    from matplotlib.colors import ListedColormap
    import seaborn as sns
    PUNCT_SET = set(punctuation)
    
    def text_to_string(filename):
        """Read a text file and return a string."""
        with open(filename) as infile:
            return infile.read()

    def make_punct_dict(strings_by_author):
        """Return dictionary of tokenized punctuation by corpus by author."""
        punct_by_author = dict()
        for author in strings_by_author:
            tokens = nltk.word_tokenize(strings_by_author[author])
            punct_by_author[author] = ([token for token in tokens if token in PUNCT_SET])
            print("Number punctuation marks in {} = {}"
                  .format(author, len(punct_by_author[author])))
        return punct_by_author  

    def convert_punct_to_number(punct_by_author, author):
        """Return list of punctuation marks converted to numerical values."""
        heat_vals = []
        for char in punct_by_author[author]:
            if char == punct_char:
                value = 1
            else:
                value = 2
            heat_vals.append(value)
        return heat_vals
    
        # Load text files into dictionary by author.
    strings_by_author = dict()
    strings_by_author["1"]=text
    #strings_by_author['Tolkien'] = text_to_string('/root/jupyter/TM-Hunting/Eolas/files/CTF-silmarillion.txt')
    #strings_by_author['wells'] = text_to_string('war.txt')
    #strings_by_author['unknown'] = text_to_string('lost.txt')

    # Tokenize text strings preserving only punctuation marks.
    punct_by_author = make_punct_dict(strings_by_author)

    # Convert punctuation marks to numerical values and plot heatmaps.
    plt.ion()
    for author in punct_by_author:
        heat = convert_punct_to_number(punct_by_author, author)
        arr = np.array((heat[:6561])) # trim to largest size for square array
        arr_reshaped = arr.reshape(int(math.sqrt(len(arr))),
                                   int(math.sqrt(len(arr))))
        fig, ax = plt.subplots(figsize=(7, 7))
        sns.heatmap(arr_reshaped,
                    cmap=ListedColormap(['blue', 'yellow']),
                    square=True,
                    ax=ax)
        ax.set_title('Heatmap {}'.format(author))
    #plt.show()
    plt.savefig("char-heatmap.png")
    return plt 