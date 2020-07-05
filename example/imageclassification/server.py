from flask import jsonify
import connexion
from cloudmesh.mongo.CmDatabase import CmDatabase

cmdb = CmDatabase()
db = cmdb.client["Images"]

data = db["image_files"]
data.insert_one({"AI Services": "Image Classification"})

# Create the application instance
app = connexion.App(__name__, specification_dir="/")
app.add_api("api.yaml")

# create a URL route in our application for "/"
@app.route("/")
def home():
    msg = {"msg": "It's working!"}
    return jsonify(msg),

if __name__ == "__main__":
    app.run(port=8080, debug=True)