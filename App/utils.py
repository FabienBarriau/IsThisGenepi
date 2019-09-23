from PIL import Image
import numpy as np
import keras as ks
from keras import backend as K

def searchBestPlantes(plantesDict, img_send_path):
    model = ks.applications.vgg19.VGG19(include_top=False, weights='imagenet', input_tensor=None,
                                           input_shape=(224, 224, 3), pooling="max", classes=1000)
    model._make_predict_function()
    im = Image.open(img_send_path)
    tensor = np.stack([np.asarray(im.resize([224, 224], Image.NEAREST))], axis=0)
    img_send_encoding = model.predict(tensor, batch_size=1, verbose=1)
    K.clear_session()
    dist = []
    for key, value in plantesDict.items():
        dist.append((np.linalg.norm(img_send_encoding - value["encoding"]), key))

    return plantesDict[min(dist)[1]]
