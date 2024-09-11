# minimal Flask app

from flask import Flask

app = Flask(__name__)
# do any app specific setupu here
# for instance, loading a database

@app.route("/")
def index():
    # three quotes from multiline strings
    return """
    <h3>Hello CTS285!!!!!! :)</h3>
    <p>This is a paragraph</p>
    <a href="action">Click here</a>

"""

@app.route("/action")
def action():
    return "Hello from the action route!"