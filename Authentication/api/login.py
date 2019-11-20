from flask import Flask, Response, request
from db.graph import Neo4jDatabase
app = Flask(__name__)

db = Neo4jDatabase.getInstance()

@app.route("/<path>", methods=["GET","POST"])
def loginRoute(path):
    print(request.args)
    name = request.args.get("name")
    
    result = db.query("CREATE (a:Person {name:$name})", name=name)
    print(result)
    return {"success":True}
