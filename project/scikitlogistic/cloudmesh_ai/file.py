from cloudmesh.mongo.CmDatabase import CmDatabase
from flask import request

cmdb = CmDatabase()
db = cmdb.client["ai_services"]
data = db["Dataset"]

def upload(file=None):

    filename = file.filename
    data.insert_one(filename)

#    if 'file' in request.files:
#        file = request.files['file']
#        data.save_file(file.filename, file)
#        data.insert({'uploadfile_name': file.filename})
        #f = data.find_one_or_404({'uploadfile_name': file.filename})

    return 'File uploaded successfully'

