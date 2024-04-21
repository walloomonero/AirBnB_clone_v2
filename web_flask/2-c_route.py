#!/usr/bin/python3
"""The script tha starts a Flask web application.

The application must listen on 0.0.0.0, port 5000.
Routes:
    /: Display 'Hello HBNB!'.
    /hbnb: Display 'HBNB'.
    /c/<text>: Display 'C' followed by the value of <text> variable.
"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """To display 'Hello HBNB!'."""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """To display 'HBNB'."""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """display 'C' followed by the value of <text>."""
    text = text.replace("_", " ")
    return "C {}".format(text)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
