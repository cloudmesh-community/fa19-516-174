from flask import Flask, jsonify, request
from flask_restful import Api, Resource
from pymongo import MongoClient
import numpy
import requests
import subprocess
import json
import jsonify

app = Flask(__name__)
api = Api(app)

client = MongoClient("mongodb://db:27017")
db = client.IRG
users = db["Users"]

class Classify(Resource):
    def get(self):

        retJson = {}
        proc = subprocess.Popen('python meanshift.py', stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
        with open("text.txt") as f:
            retJson = json.load(f)
        return retJson

api.add_resource(Classify, '/classify')

if __name__=="__main__":
    app.run(host='0.0.0.0')
