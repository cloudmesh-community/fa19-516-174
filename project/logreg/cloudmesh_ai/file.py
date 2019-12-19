import pandas as pd
from cloudmesh import mongo # ???
from flask import request
from flask_pymongo import PyMongo
from sklearn.feature_selection import SelectKBest, chi2
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score


def upload(file=None):
    if 'trainfile' in request.files:
        trainfile = request.files['trainfile']
        mongo.save_file(trainfile.filename, trainfile)
        mongo.db.users.insert(
            {'username': request.form.get('username'),
             'uploadfile_name': trainfile.filename})
        trainset = mongo.db.users.find_one_or_404({'uploadfile_name': trainfile.filename})

    if 'testfile' in request.files:
        testfile = request.files['testfile']
        mongo.save_file(testfile.filename, testfile)
        mongo.db.users.insert({'username': request.form.get('username'), 'uploadfile_name': testfile.filename})
        testset = mongo.db.users.find_one_or_404({'uploadfile_name': testfile.filename})

    return 'File uploaded successfully', trainset, testset
