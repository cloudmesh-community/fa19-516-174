import mongo
#from cloudmesh import mongo # ???
from flask import request


def upload(file=None):

    if 'trainfile' in request.files:
        trainfile = request.files['trainfile']
        mongo.db.data.insert({"file": "trainfile"})
        #mongo.save_file(trainfile.filename, trainfile)
        #mongo.db.users.insert({'username': request.form.get('username'),'uploadfile_name': trainfile.filename})
        trainset = mongo.db.data.find_one_or_404({'uploadfile_name': trainfile.filename})

    if 'testfile' in request.files:
        testfile = request.files['testfile']
        mongo.db.data.insert({"file": "testfile"})
        #mongo.save_file(testfile.filename, testfile)
        #mongo.db.users.insert({'username': request.form.get('username'), 'uploadfile_name': testfile.filename})
        testset = mongo.db.data.find_one_or_404({'uploadfile_name': testfile.filename})

    return 'File uploaded successfully'
