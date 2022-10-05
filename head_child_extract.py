# Head and child: Iterationg around the tree.
"""
spaCy uses the terms head and child to describe the words connected 
by a single arc in the dependency tree. The term dep is used for the 
arc label, which describes the type of syntactic relation that connects 
the child to the head. As with other attributes, the value of .dep is a 
hash value. You can get the string value with .dep_.
"""
#print("Iterating around the tree:",'\n')
#import spacy

#nlp = spacy.load("en_core_web_sm")
#doc = nlp("Autonomous cars shift insurance liability toward manufacturers")
#for token in doc:
#    print(token.text, token.dep_, token.pos_,token.head.text, token.head.pos_,[child for child in token.children])


def head_child_extract(text):
    #if there is no child, function returns empty list item.
    import spacy
    nlp=spacy.load("en_core_web_sm")
    doc=nlp(text)
    head_child=[]
    for token in doc:
        #print(token.text, token.dep_, token.pos_,token.head.text, token.head.pos_,[child for child in token.children])
        head_child.append([token.text, token.dep_, token.pos_,token.head.text, token.head.pos_,[child for child in token.children]])
    return head_child