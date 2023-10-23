#!/usr/bin/python3
"""
    This is a flask web app
    Author: Peter Ekwere
"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route("/states", strict_slashes=False)
def state_cities():
    """ This function returns the states from html """
    print("entered /states or /states/ function")
    states = storage.all(State)
    return render_template("9-states.html", state=states, id=id)


@app.route("/states/<id>", strict_slashes=False)
def state_city(id):
    """ This function returns the states from html """
    print("entered states/id function")
    states = storage.all(State).values()
    for state in states:
        if state.id == id:
            return render_template("9-states.html", state=state)
    return render_template("9-states.html")


@app.teardown_appcontext
def end_session(exc):
    """ This function ends the current session """
    storage.close()


if __name__ == '__main__':
    """ This will trigger when run directly """
    app.run(host='0.0.0.0', port=5000)
