from fileinput import filename

import pandas as pd
import requests
from cloudmesh.mongo.CmDatabase import CmDatabase
import os
import io
import flask
from flask import request, url_for
from flask_restful.inputs import url

from werkzeug.utils import secure_filename

cmdb = CmDatabase()
#db = cmdb.client["cloudmesh"]
#data = db["local-file"]
db = cmdb.client["cloudmesh_ai"]
data = db["files"]

#INPUT_DIR = '/tmp/aiservice/input'
#os.makedirs(INPUT_DIR, exist_ok=True)

def upload(file=None):

    #if request.method == 'POST':
    #file = request.files['file']
    # file.save(os.path.join(flask.app.config['UPLOAD_FOLDER'], file.filename))
        # for browser, add 'redirect' function on top of 'url_for'
    # r = url_for('uploaded_file',filename=file.filename)

    df = pd.read_csv(file)
    dat = df.to_dict(orient = 'records')
    result = data.insert_many(dat)

    return result, 'File uploaded successfully'

upload("predict.csv")