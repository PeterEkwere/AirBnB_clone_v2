#!/usr/bin/python3
"""
    This is a flask web app
    Author: Peter Ekwere
"""
from flask import Flask, render_template
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


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """ this function returns n """
    return f"{escape(n)} is a number"


@app.route("/number_template/<int:n>", strict_slashes=False)
def num_template(n):
    """ This function renders a html page """
    return render_template("5-number.html", n=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def odd_or_even(n):
    """ This function renders a html page """
    return render_template("6-number_odd_or_even.html", n=n)


if __name__ == '__main__':
    """ This will trigger when run directly """
    app.run(host='0.0.0.0', port=5000)
