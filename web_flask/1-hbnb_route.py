#!/usr/bin/python3
"""
    This is a flask web app
    Author: Peter Ekwere
"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def Hello():
    """ This function displays Hello HBNB! """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def holberton():
    """ This function displays HBNB """
    return "HBNB"


if __name__ == '__main__':
    """ This will trigger when run directly """
    app.run(host='0.0.0.0', port=5000)
