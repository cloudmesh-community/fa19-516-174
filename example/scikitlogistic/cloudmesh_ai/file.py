import pandas as pd
from cloudmesh.mongo.CmDatabase import CmDatabase
from flask import jsonify

cmdb = CmDatabase()
#db = cmdb.client["cloudmesh"]
#data = db["local-file"]
db = cmdb.client["cloudmesh_ai"]
data = db["files"]

#INPUT_DIR = '/tmp/aiservice/input'
#os.makedirs(INPUT_DIR, exist_ok=True)

def upload(file=None):

    #if request.method == 'POST':
    #file = request.files['file']
    # file.save(os.path.join(flask.app.config['UPLOAD_FOLDER'], file.filename))
        # for browser, add 'redirect' function on top of 'url_for'
    # r = url_for('uploaded_file',filename=file.filename)

    #df = pd.read_csv(file)
    #dat = df.to_dict(orient = 'records')
    #result = data.insert_many(dat)

    #return result, 'File uploaded successfully'

    r = {"name": file}

    return jsonify(**r)

if __name__ == "__main__":
    upload("a4-test.csv")