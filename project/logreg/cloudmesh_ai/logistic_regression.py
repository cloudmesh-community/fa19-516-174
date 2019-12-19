import pandas as pd
from cloudmesh import mongo
from flask import request
from flask_pymongo import PyMongo
from sklearn.feature_selection import SelectKBest, chi2
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from .file import upload

def fit(body):
    # Put input file in dataframe
    train = pd.read_csv(upload.trainset, index_col=0)
    test = pd.read_csv(upload.testset, index_col=0)

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

    lg = LogisticRegression()
    lg.fit(xtrain_final, ytrain.values.reshape(-1, ))
    return lg, xtest_final, ytest


def predict(body, file=None):
    ypred = fit.lg.predict(fit.xtest_final)
    acc = accuracy_score(ypred, fit.ytest)
    print("The test accuracy for this logistic regression model is", acc)

    return
