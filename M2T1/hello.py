# minimal Flask app

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello CTS285!</p>"