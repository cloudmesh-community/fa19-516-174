import csv

import pandas as pd
import mongo
from sklearn.feature_selection import SelectKBest, chi2
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from cloudmesh.mongo.CmDatabase import CmDatabase
from sklearn.model_selection import train_test_split

cmdb = CmDatabase()
db = cmdb.client["cloudmesh_ai"]
data = db["files"]


def fit(file):
    # Put input file in dataframe

    f = data.find_one(file))
    # f2 = data.find(file2)

    #dat = pd.read_csv(f)
    f.head(5)

    return
    # df2 = pd.to_csv(f2)
    #
    # dataset = pd.read_csv(df, index_col=0)
    # x = dataset.iloc[:, :-1].values
    # y = dataset.iloc[:,1].values
    # test = pd.read_csv(df2, index_col=0)
    # x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=0)
    #
    # lg = LogisticRegression()
    # lg.fit(x_train, y_train)
    # y_pred = lg.predict(x_test)
    # acc = accuracy_score(y_pred, y_test)
    # print("The test accuracy for this logistic regression model is", acc)

    # return lg, x_train, x_test, y_train, y_test


# def predict():
#
#     y_pred = fit.lg.predict(fit.x_test)
#     acc = accuracy_score(y_pred, fit.y_test)
#     print("The test accuracy for this logistic regression model is", acc)
#
#     return
#
#
fit('a4-train.csv')
# predict()
