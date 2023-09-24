#!/usr/bin/python3
'''This script returns an HTML page'''
from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity

app = Flask(__name__)


@app.teardown_appcontext
def teardown(anything):
    '''removes the current SQLAlchemy Session'''
    storage.close()


@app.route("/hbnb_filters", strict_slashes=False)
def filters():
    '''returns template for airbnb site'''
    ob = storage.all(State)
    bo = storage.all(Amenity)

    return render_template('10-hbnb_filters.html', states=ob, amenities=bo)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
