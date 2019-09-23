import pickle
from tensorflow import keras
import os

#To generate a new secret key:
# >>> import random, string
# >>> "".join([random.choice(string.printable) for _ in range(24)])
SECRET_KEY = "#d#JCqTTW\nilK\\7m\x0bp#\tj~#H"
UPLOAD_FOLDER = "App\\static\\new_img\\"
ALLOWED_EXTENSIONS = ['png', 'jpg', 'jpeg']

with open('App\\static\\pickle\\plantesDict.pickle', 'rb') as handle:
    plantesDict = pickle.load(handle)
PLANTES_DICT = plantesDict