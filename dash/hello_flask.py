# in order to this server with a different name other than app.py, you have to
# specify an env variable before run server
# ie. $ export FLASK_APP=hello_flask.py
# run $ python -m flask run 
#
#
from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Flask!"
    