# Identify possible subjects and verbs related to the subject:
#print("Identifying the possible subjects and verbs:",'\n')
#import spacy
#from spacy.symbols import nsubj, VERB

#nlp = spacy.load("en_core_web_sm")
#doc = nlp("Credit and mortgage account holders must submit their requests.")

# Finding a verb with a subject from below — good
#verbs = set()
#for possible_subject in doc:
#    if possible_subject.dep == nsubj and possible_subject.head.pos == VERB:
#        verbs.add(possible_subject.head)
#print(verbs)

text="Credit and mortgage account holders must submit their requests."
def subj_verb_extract(text):
    #identifying possible subject and the verb, related to it.
    import spacy
    from spacy.symbols import nsubj, VERB
    nlp=spacy.load("en_core_web_sm")
    doc=nlp(text)
    subj_verbs=[]
    verbs=set()
    for possible_subject in doc:
        if possible_subject.dep==nsubj and possible_subject.head.pos==VERB:
            verbs.add(possible_subject.head)
            subj_verbs.append([possible_subject,possible_subject.head])
    #print(verbs)
    #print(subj_verbs)
    return subj_verbs