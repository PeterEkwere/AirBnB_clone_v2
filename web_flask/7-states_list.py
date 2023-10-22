#!/usr/bin/python3
"""
    This is a flask web app
    Author: Peter Ekwere
"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def states():
    """ This function returns the states from html """
    states = storage.all(State)
    return render_template("7-states_list.html", states=states)


@app.teardown_appcontext
def end_session(exc):
    """ This function ends the current session """
    storage.close()


if __name__ == '__main__':
    """ This will trigger when run directly """
    app.run(host='0.0.0.0', port=5000)
