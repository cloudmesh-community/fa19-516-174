import pandas as pd
from cloudmesh import mongo
from flask import request
from flask_pymongo import PyMongo
from sklearn.feature_selection import SelectKBest, chi2
from sklearn import svm
from sklearn.metrics import accuracy_score


def fit(body):
    # Put input file in dataframe
    train = pd.read_csv(upload_file.trainset, index_col=0)
    test = pd.read_csv(upload_file.testset, index_col=0)

    ytrain = train['labels']
    ytest = test['labels']
    xtrain = train.drop(['labels'], axis=1, )
    xtest = test.drop(['labels'], axis=1)

    #    fe = SelectKBest(chi2, k=15)
    #    xnew = fe.fit_transform(xtrain, ytrain.values.reshape(-1, ))
    #    xnew = pd.DataFrame(xnew)
    #    cols = xtrain.columns.values[fe.get_support()]

    xtrain_final = xtrain[['feat_48', 'feat_64', 'feat_105', 'feat_136', 'feat_153',
                           'feat_241', 'feat_336', 'feat_338', 'feat_378', 'feat_411',
                           'feat_442', 'feat_453', 'feat_472', 'feat_475', 'feat_493']]

    xtest_final = xtest[['feat_48', 'feat_64', 'feat_105', 'feat_136', 'feat_153',
                         'feat_241', 'feat_336', 'feat_338', 'feat_378', 'feat_411',
                         'feat_442', 'feat_453', 'feat_472', 'feat_475', 'feat_493']]

    clf = svm.SVC(kernel='linear')
    clf.fit(xtrain_final, ytrain.values.reshape(-1, ))
    return clf, xtest_final, ytest


def predict(body, file=None):
    ypred = fit.clf.predict(fit.xtest_final)
    acc = accuracy_score(ypred, fit.ytest)
    print("The test accuracy for this logistic regression model is", acc)

    return


def upload_file(file=None):
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
