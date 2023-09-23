#!/usr/bin/python3
'''This script an HTML page that lists the states in it's body.'''
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def teardown(anything):
    '''removes the current SQLAlchemy Session'''
    storage.close()


@app.route("/cities_by_states", strict_slashes=False)
def sc_list():
    '''lists states'''
    ob = storage.all(State)
    return render_template('8-cities_by_states.html', states=ob)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
