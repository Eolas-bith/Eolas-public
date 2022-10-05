def fasttext_supervised(path_to_training_data,path_to_validation_data,path_to_predict_data,path_to_save_model):
    import VAR_fasttext
    #from VAR_fasttext import path_to_training_data
    #from VAR_fasttext import path_to_validation_data
    #from VAR_fasttext import path_to_predict_data

    #tb coded based on the below code:

# Fast text: Text classification

#https://fasttext.cc/docs/en/supervised-tutorial.html
#Text classification for e.g sentiment analysis

#1) get the sample data and extract them: 
#wget https://dl.fbaipublicfiles.com/fasttext/data/cooking.stackexchange.tar.gz && tar xvzf cooking.stackexchange.tar.gz
#head cooking.stackexchange.txt
#2) wc cooking.stackexchange.txt
#head -n 12404 cooking.stackexchange.txt > cooking.train
#tail -n 3000 cooking.stackexchange.txt > cooking.valid

    import fasttext
    model=fasttext.train_supervised(input=path_to_training_data)

    model.save_model(path_to_save_model)
    #model.predict(path_to_predict_data)
    model.test(path_to_validation_data)
    #model.test(path_to_validation_data,k=5)
    #model.predict("Why not put knives in the dishwasher?", k=5)

#Improving the model:

#preprocessing:
#cat cooking.stackexchange.txt | sed -e "s/\([.\!?,'/()]\)/ \1 /g" | tr "[:upper:]" "[:lower:]" > cooking.preprocessed.txt
#head -n 12404 cooking.preprocessed.txt > cooking.train
#tail -n 3000 cooking.preprocessed.txt > cooking.valid
    model=fasttext.train_supervised(input=path_to_training_data)
    model.test(path_to_validation_data)

#More epochs and larger learning rate:
    #import fasttext
    #model=fasttext.train_supervised(input=path_to_training_data,epoch=25)
    #model.test(path_to_validation_data)

    #model=fasttext.train_supervised(input=path_to_training_data,lr=1.0)
    #model.test(path_to_validation_data)
    #model=fasttext.train_supervised(input=path_to_training_data,lr=1.0,epoch=25)
    #model.test(path_to_validation_data)

#Using the word n-grams to improve the performance:
    #model=fasttext.train_supervised(input=path_to_training_data,lr=1.0,epoch=25,wordNgrams=2)
    #model.test(path_to_validation_data)

#
    #model=fasttext.train_supervised(input=path_to_training_data, lr=1.0, epoch=25, wordNgrams=2, bucket=200000, dim=50, loss='hs')
    #model.test(path_to_validation_data)

#multilabel classification
    #model=fasttext.train_supervised(input=path_to_training_data, lr=0.5, epoch=25, wordNgrams=2, bucket=200000, dim=50, loss='ova')
    #model.test(path_to_validation_data)

    #model.predict("Which baking dish is best to bake a banana bread ?", k=-1, threshold=0.5)
    #model.test(path_to_validation_data,k=-1)

    prediction=model.predict(path_to_predict_data)
    return(prediction)