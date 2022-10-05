def sentiment_detector(span):
    import spacy
    from spacytextblob.spacytextblob import SpacyTextBlob
    nlp=spacy.load('en_core_web_sm')
    nlp.add_pipe('spacytextblob')
    doc=nlp(span)
    sentiment={"polarity":doc._.polarity,"subjectivity":doc._.subjectivity,"assessments":doc._.assessments}
    print(str(sentiment))
    return sentiment