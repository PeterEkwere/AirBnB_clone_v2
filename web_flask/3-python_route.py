#!/usr/bin/python3
"""
    This is a flask web app
    Author: Peter Ekwere
"""
from flask import Flask
from markupsafe import escape

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def Hello():
    """ This function displays Hello HBNB! """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def holberton():
    """ This function displays HBNB """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def path_text(text):
    """ this function concatenates and prints the path """
    return f"C {escape(text.replace('_', ' '))}"


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def newpath(text="is cool"):
    """ This function is the same as its predecessor """
    return f"Python {escape(text.replace('_', ' '))}"


if __name__ == '__main__':
    """ This will trigger when run directly """
    app.run(host='0.0.0.0', port=5000)
