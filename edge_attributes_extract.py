# Edge attributes of the token can be useful:
#print('\n',"Edge attribute tokens:",'\n')
#import spacy

#nlp = spacy.load("en_core_web_sm")
#doc = nlp("Credit and mortgage account holders must submit their requests")
#span = doc[doc[4].left_edge.i : doc[4].right_edge.i+1]
#with doc.retokenize() as retokenizer:
#    retokenizer.merge(span)
#for token in doc:
    #print(token.text, token.pos_, token.dep_, token.head.text)

sentence="Credit and mortgage account holders must submit their requests"
def edge_attributes_extract(sentence):
    #extracts edge attributes tokens:
    import spacy
    nlp=spacy.load("en_core_web_sm")
    doc=nlp(sentence)
    span = doc[doc[4].left_edge.i : doc[4].right_edge.i+1]
    with doc.retokenize() as retokenizer:
        retokenizer.merge(span)
    edge_attrs=[]
    for token in doc:
        #print(token.text, token.pos_, token.dep_, token.head.text)
        edge_attrs.append([token.text, token.pos_, token.dep_, token.head.text])
    return edge_attrs