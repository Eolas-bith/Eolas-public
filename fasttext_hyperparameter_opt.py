
{}{}{}{}{}
This code has to be finished and tested, first

def fasttext_hyperparameter_opt():
    #tb coded based on the lines below:

    """
    Fast text's automatic hyperparameter optimisation:
    https://fasttext.cc/docs/en/autotune.html
    """
    import fasttext
    model = fasttext.train_supervised(input='cooking.train', autotuneValidationFile='cooking.valid')
    model.test("cooking.valid")
    #autotune with lmit=10 minutes
    model = fasttext.train_supervised(input='cooking.train', autotuneValidationFile='cooking.valid', autotuneDuration=600)

    #constraint model size:
    import fasttext
    model = fasttext.train_supervised(input='cooking.train', autotuneValidationFile='cooking.valid', autotuneModelSize="2M")
    model.save_model("model_cooking.ftz")
    import os
    os.stat("model_cooking.ftz").st_size
    model.test("cooking.valid")

    #how to set optimizastion metric:
    import fasttext
    model = fasttext.train_supervised(input='cooking.train', autotuneValidationFile='cooking.valid', autotuneMetric="f1:__label__baking")

