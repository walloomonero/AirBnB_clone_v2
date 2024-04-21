#!/usr/bin/python3
"""The script that starts a Flask web application.

The application Must listen on 0.0.0.0, port 5000.
Routes:
    /: Display 'Hello HBNB!'.
    /hbnb: Display 'HBNB'.
    /c/<text>: Display 'C' followed by the value of <text> variable.
    /python/(<text>): Display 'Python' followed by the value of <text>.
    The default value of text is “is cool”.
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
    """To display 'C' followed by the value of <text>.

        To replace any underscores in <text> with slashes.
    """
    text = text.replace("_", " ")
    return "C {}".format(text)


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text="is cool"):
    """To display 'Python' followed by the value of <text>.

        To replace any underscores in <text> with slashes.
    """
    text = text.replace("_", " ")
    return "Python {}".format(text)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
