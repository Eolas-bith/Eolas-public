from unittest import FunctionTestCase


{}{}{}{}{}
THIs has to be finished and tested first prior to finialisation of the FunctionTestCase

def fasttext_unsupervised(input_data):
    import VAR_fasttext
    from VAR_fasttext import path_to_u_data

    #tb codede based on the lines of code below:

    # Fast text: Word representation
    """
    https://fasttext.cc/docs/en/unsupervised-tutorial.html
    Word representations for eg word analogies, semantics..
    """

    #1) Getting the data: raw dump of wikipedia
    #wget https://dumps.wikimedia.org/enwiki/latest/enwiki-latest-pages-articles.xml.bz2
    #2) As it may be too large, intsead lets use the first billion bytes of English Wikipedia
    #mkdir data
    #wget wget -c http://mattmahoney.net/dc/enwik9.zip -P data
    # unzip data/enwik9.zip -d data
    #text has a lot of html/xml data. preprocess it with wikifil.pl script bundled with fasttext:
    #perl wikifil.pl data/enwik9 > data/fil9
    #check the file:
    #head -c 80 data/fil9

    #Trainign the vectors:
    import fasttext
    model = fasttext.train_unsupervised('data/fil9')
    model.words
    model.get_word_vector("the")
    model.save_model("result/fil9.bin")

    #reload the model again:
    model = fasttext.load_model("result/fil9.bin")

    #skipgrams vs cbow - continuous bag of words:
    model = fasttext.train_unsupervised('data/fil9', "cbow")

    #playing with parameters:
    model = fasttext.train_unsupervised('data/fil9', minn=2, maxn=5, dim=300)

    model = fasttext.train_unsupervised('data/fil9', epoch=1, lr=0.5)

    model = fasttext.train_unsupervised('data/fil9', thread=4)

    [model.get_word_vector(x) for x in ["asparagus", "pidgey", "yellow"]]

    model.get_word_vector("enviroment")

    #nearest neighbor queries:
    model.get_nearest_neighbors('asparagus')

    #measure of similarity:
    model.get_analogies("berlin", "germany", "france")

    #subwords - the example word is not in wiki, but thanks to n-grams it will be still processed:
    model.get_nearest_neighbors('gearshift')

    #model without subwords: so that substrings in n-grams are not considered.
    model_without_subwords = fasttext.train_unsupervised('data/fil9', maxn=0)

    model_without_subwords.get_nearest_neighbors('accomodation')
    model.get_nearest_neighbors('accomodation')