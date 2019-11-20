from flask import Flask, Response, request
app = Flask(__name__)

@app.route("/<path>", methods=["GET","POST"])
def loginRoute(path):
    
    return "hello"
