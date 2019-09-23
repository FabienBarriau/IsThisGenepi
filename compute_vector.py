import os
import pandas as pd
from tensorflow import keras
from PIL import Image
import numpy as np
import pickle

REP_IMG = "C:/Users/fabien/PycharmProjects/genepi_webApp/App/"

model = keras.applications.vgg19.VGG19(include_top=False, weights='imagenet', input_tensor=None,
                                               input_shape=(224, 224, 3), pooling="max", classes=1000)

df = pd.read_csv(REP_IMG + "static/csv/info.csv", sep='\t', encoding="latin_1")

plantesDict = dict()
for index, row in df.iterrows():
    im = Image.open(REP_IMG + "static/pictures/" + row.imgName)
    tensor = np.stack([np.asarray(im.resize([224, 224], Image.NEAREST))], axis=0)
    encoding = model.predict(tensor, batch_size=1, verbose=1)
    plantesDict[row.id] = {"encoding": encoding, "description": row.description, "imgName": row.imgName, "latinName": row.id}

with open(REP_IMG + "static/pickle/plantesDict.pickle", 'wb') as handle:
    pickle.dump(plantesDict, handle, protocol=pickle.HIGHEST_PROTOCOL)





