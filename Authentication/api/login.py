from flask import Flask, Response, request
app = Flask(__name__)

@app.route("/<path>")
def index(path):
    
    return request.json()
