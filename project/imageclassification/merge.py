import os
import numpy as np
from flask import Flask, request, url_for, app, json
from flask_restful import Api, Resource
from pymongo import MongoClient
import requests
from keras.applications.resnet50 import ResNet50
from keras.preprocessing import image
from keras.applications.resnet50 import preprocess_input, decode_predictions
from werkzeug.utils import secure_filename

# use cloudmesh shell

UPLOAD_FOLDER = 'C:Users/Work/uploads'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

def upload_file():
    file = request.files['file']
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        url = url_for('uploaded_file', filename=filename)
        return url

def classify():

    r = requests.get(upload_file.url)
    retJson = {}

    model = ResNet50(weights='imagenet')
    img = image.load_img(r)
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)
    pred = model.predict(x)

    retJson[decode_predictions(pred, top=3)]
    print('Predicted:', decode_predictions(pred, top=3)[0])
    with open("text.txt") as f:
        json.dump(retJson)
    retJson = json.load(f)

    return retJson
