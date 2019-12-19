import mongo
import pandas as pd
from flask import request
from sklearn import svm
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


def fit(body):

    # Put input file in dataframe
    d = pd.read_csv(upload_file.dataset)

    X_train, X_test, y_train, y_test = train_test_split(d.data, d.target, test_size=0.3, random_state=109)

    clf = svm.SVC(kernel='linear')
    clf.fit(X_train, y_train)
    return clf, X_test, y_test


def predict(body, file=None):

    y_pred = fit.clf.predict(fit.X_test)
    acc = accuracy_score(y_pred, fit.y_test)
    print("The test accuracy for this logistic regression model is", acc)

    return


def upload_file(file=None):
    if 'data_set' in request.files:
        data_set = request.files['data_set']
        mongo.save_file(data_set.filename, data_set)
        mongo.db.users.insert(
            {'username': request.form.get('username'),
             'uploadfile_name': data_set.filename})
        data_set = mongo.db.users.find_one_or_404({'uploadfile_name': data_set.filename})

    return 'File uploaded successfully', data_set
