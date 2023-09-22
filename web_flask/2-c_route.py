#!/usr/bin/python3
"""This script starts a Flask web application and performs some actions."""
from flask import Flask

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
    fmt = ''
    for i in text:
        if i == _:
            fmt += ' '
            continue

        fmt += i
    return fmt


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
