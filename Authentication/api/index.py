from flask import Flask, Response
app = Flask(__name__)

@app.route('/')
def index():
    return {
        "login":{"path":"/login", "method":"post"},
        "issue":{"path":"/request", "method":"post"}
    }
