import mongo
import numpy as np
from flask import request, json
import requests
from keras.applications.resnet50 import ResNet50
from keras.preprocessing import image
from keras.applications.resnet50 import preprocess_input, decode_predictions
from werkzeug.utils import secure_filename

# UPLOAD_FOLDER = 'C:Users/Work/uploads'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


def upload_file(file=None):
    profileImage = request.files['file']
    if profileImage and allowed_file(profileImage.filename):
        img = secure_filename(profileImage.filename)
        numpy_image = image.img_to_array(img)
        image_batch = np.expand_dims(numpy_image, axis=0)
        processed_image = preprocess_input(image_batch, mode='caffe')
        mongo.save_file(processed_image.filename, processed_image)
        mongo.db.data.insert({'image': processed_image.filename})

        return 'Processed image saved in database'


def classify(filename):
    r = mongo.db.data.send_file(filename)
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
