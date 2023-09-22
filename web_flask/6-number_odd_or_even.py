#!/usr/bin/python3
"""This script starts a Flask web application and performs some actions."""
from flask import Flask, render_template

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/")
def hello():
    """This function returns `Hello HBNB`"""
    return "Hello HBNB!"


@app.route("/hbnb")
def hbnb():
    """This function returns `HBNB`"""
    return "HBNB"


@app.route("/c/<text>")
def C_text(text):
    """This function returns C with the text and changes all the underscores
    to spaces.
    """
    space = text.replace("_", " ")
    fmt = 'C ' + space

    return fmt


@app.route("/python/")
@app.route("/python/<text>")
def py_text(text="is cool"):
    """This function returns Python with whatever the text is and changes
    all the underscores to spaces.
    """
    space = text.replace("_", " ")
    fmt = "Python " + space

    return fmt


@app.route("/number/<int:n>")
def num(n):
    """This function returns a number only if it is an integer."""
    return f"{n} is a number"


@app.route("/number_template/<int:n>")
def num_temp(n):
    """This function returns an HTML page."""
    text = f"Number: {n}"
    return render_template('5-number.html', text=text)


@app.route("/number_odd_or_even/<int:n>")
def odd_even(n):
    """This function returns an HTML page."""
    if n % 2 == 0:
        text = f"Number: {n} is even"
    else:
        text = f"Number: {n} is odd"

    return render_template('6-number_odd_or_even.html', text=text)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
