#--------------------------------
# Iterating around the local tree:
#print("Iterating around the local tree:",'\n')
#import spacy

#nlp = spacy.load("en_core_web_sm")
#doc = nlp("for the bright red apples")
#print([token.text for token in doc[2].lefts])  # ['bright', 'red']
#print([token.text for token in doc[2].rights])  # ['on']
#print(doc[2].n_lefts)  # 2
#print(doc[2].n_rights)  # 1

#Getting subtree:
#print("Getting subtree:",'\n')
#import spacy

#nlp = spacy.load("en_core_web_sm")
#doc = nlp("Credit and mortgage account holders must submit their requests")

#root = [token for token in doc if token.head == token][0]
#subject = list(root.lefts)[0]
#for descendant in subject.subtree:
#    assert subject is descendant or subject.is_ancestor(descendant)
#    print(descendant.text, descendant.dep_, descendant.n_lefts,
#            descendant.n_rights,
#            [ancestor.text for ancestor in descendant.ancestors])

sentence="Credit and mortgage account holders must submit their requests"
def subtree_extract(text):
    #Getting subtree for complex senteces like this: "Credit and mortgage account holders must submit their requests."
    import spacy
    nlp=spacy.load("en_core_web_sm")
    doc=nlp(text)
    root=[token for token in doc if token.head==token][0]
    subject=list(root.lefts)[0]
    subtree_list=[]
    for descendant in subject.subtree:
        assert subject is descendant or subject.is_ancestor(descendant)
        #print(descendant.text, descendant.dep_, descendant.n_lefts,
        #    descendant.n_rights,
        #    [ancestor.text for ancestor in descendant.ancestors])
        subtree_list.append([descendant.text, descendant.dep_, descendant.n_lefts,descendant.n_rights,[ancestor.text for ancestor in descendant.ancestors]])
    return subtree_list