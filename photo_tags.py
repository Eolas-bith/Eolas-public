#Uses clariafi API - not working well - tb improved

def photo_tags(filename):
    app=ClarifaiApp(api_key=a879693e2a02434a816d9d3433fd2066)
    model=app.public_models.general_model
    image=Image(file_obj=open(filename,'rb'))
    response=model.predict([image])
    concepts=response['outputs'][0]['data']['concepts']
    for concept in concepts:
        if concept['name']=='food':
            food_model=app.public_models.food_model
            result=food_model.predict([image])
            first_concept=result['outputs'][0]['data']['concepts'][0]['name']
            return first_concept
    return response['outputs'][0]['data']['concepts'][1]['name']