import pandas as pd
from cloudmesh.mongo.CmDatabase import CmDatabase
from flask import request
from werkzeug.datastructures import FileStorage

cmdb = CmDatabase()
#db = cmdb.client["cloudmesh"]
#data = db["local-file"]
db = cmdb.client["cloudmesh_ai"]
data = db["files"]

def upload(file=None):

    data.insert_one({"filename": file})
    return 'File uploaded successfully'

upload("abc")