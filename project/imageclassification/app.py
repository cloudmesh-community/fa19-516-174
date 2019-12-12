from flask import Flask, jsonify, request
from flask_restful import Api, Resource
from pymongo import MongoClient
import numpy
import keras
import requests 
import subprocess
import json
# use cloudmesh shell

app = Flask(__name__)
api = Api(app)

client = MongoClient("mongodb://db:27017")
db = client.IRG
users = db["Users"]

class Classify(Resource):
    def post(self):
        postedData = request.get_json()

        url = postedData["url"]

        r = requests.get(url)
        retJson = {}
        with open('temp.jpg', 'wb') as f:
            f.write(r.content)
            proc = subprocess.Popen('python classify.py --model_dir=. --image_file=./temp.jpg',
                                    stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
#            ret = proc.communicate()[0]
#            proc.wait()
            with open("text.txt") as f:
                retJson = json.load(f)

        return retJson

api.add_resource(Classify, '/classify')

if __name__=="__main__":
    app.run(host='0.0.0.0')
