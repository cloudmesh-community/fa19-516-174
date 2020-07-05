import os
#import pymongo
from flask import jsonify, request, render_template, url_for, Flask
#from flask_restplus import Api, Resource
import connexion
#from flask_pymongo import PyMongo
#from pymongo import MongoClient
from werkzeug.utils import secure_filename, redirect

# http://0.0.0.0:8080/cloudmesh_ai/ui

from cloudmesh.mongo.CmDatabase import CmDatabase

cmdb = CmDatabase()
db = cmdb.client["cloudmesh_ai"]

data = db["files"]
data.insert_one({"gregor": "hallo"})



# Create the application instance
app = connexion.FlaskApp(__name__, specification_dir="../logreg/")
app.add_api("api.yaml")


# create a URL route in our application for "/"
@app.route("/")
def home():
    msg = {"msg": "It's working!"}
    return jsonify(msg)

#
# this is actually being configures in the yaml file and not here in tha app.
# the app has only starting the server based on the app configuration. other
# than the home route this should not have any other routes
#
@app.route("/upload_file", methods=['POST'])
def file_upload():
    return render_template("upload.html");

if __name__ == "__main__":
    app.run(port=8080, debug=True)
