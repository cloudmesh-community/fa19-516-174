from cloudmesh.mongo.CmDatabase import CmDatabase

cmdb = CmDatabase()
db = cmdb.client["cloudmesh_ai"]

data = db["files"]
data.insert_one({"gregor": "hallo"})


