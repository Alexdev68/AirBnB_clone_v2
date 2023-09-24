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


@app.route("/states", strict_slashes=False)
@app.route("/states/<id>", strict_slashes=False)
def states_id(id=None):
    '''lists cities in states based on id'''
    ob = storage.all(State)

    if id is None:
        return render_template('9-states.html', states=ob)

    for st in ob.values():
        if st.id == id:
            return render_template('9-states.html', state=st)

        return render_template('9-states.html', state="N")


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
