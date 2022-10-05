def show_model_topics(model,num_words=4):
        for idx, topic in model.show_topics(num_words, formatted=False):
            print('Topic {} | Words & Probability: {}'.format(idx,topic))