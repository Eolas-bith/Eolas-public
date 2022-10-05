# From the text miner output -gernerate vectors & models.

#file='/Users/jindrich_karasek/data-science/list-of-url'
#url_list_text_to_corpus(file)

#https://radimrehurek.com/gensim/models/doc2vec.html
from gensim.test.utils import common_texts
from gensim.models.doc2vec import Doc2Vec, TaggedDocument
#input: iterable list of taggetd document, input corpus..

#--------------------------------------------
#"""Example: """
##Tagged document = https://stackoverflow.com/questions/45125798/how-to-use-taggeddocument-in-gensim
#s1="the quick brown fox jumps over the lazy dog."
#s1_tag="001"
#s2="I want to burn a zero-day"
#s2_tag="002"
#docs=[]
#docs.append(TaggedDocument(words=s1.split(),tags=[s1_tag]))
#docs.append(TaggedDocument(words=s2.split(),tags=[s2_tag]))
#model=Doc2Vec(documents,vector_size=5,window=2,min_count=1,workers=4)
#model.build_vocab(docs)

documents=[TaggedDocument(doc,[i]) for i, doc in enumerate(common_texts)]
model=Doc2Vec(documents,vector_size=5,window=2,min_count=1,workers=4)

#print("Start training process...")
#model.train(docs,total_examples=model.corpus_count,epochos=model.iter)
##save model:
#model_path='/tmp/model1'
#model.save(model_path)

#-------------------------------------------

from gensim.test.utils import get_tmpfile
fname=get_tmpfile('my_doc2vec_model')
model.save(fname)
model=Doc2Vec.load(fname)

vector=model.infer_vector(["system","response","status"])
print(vector)


def vector_generator(in_corpus,list_of_words):
    from gensim.test.utils import common_texts
    from gensim.models.doc2vec import Doc2Vec, TaggedDocument
    from gensim.test.utils import get_tmpfile
    #documents=[TaggedDocument(doc,[i]) for i, doc in enumerate(common_texts)]
    documents=[TaggedDocument(doc,[i]) for i, doc in enumerate(in_corpus)]
    model=Doc2Vec(documents,vector_size=5,window=2,min_count=1,workers=4)
    from gensim.test.utils import get_tmpfile
    fname=get_tmpfile('my_doc2vec_model')
    model.save(fname)
    model=Doc2Vec.load(fname)
    #list_of_words=["system","response","status"]
    vector=model.infer_vector(list_of_words)
    print(vector)