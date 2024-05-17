#!/usr/bin/python3
"""
module: 4-number_route
"""
from flask import Flask
from markupsafe import escape

# instanciate a Flask instance with module name
app = Flask(__name__)


# decorator to register view function/controller to URL rule
@app.route('/', strict_slashes=False)
def hello():
    """return a string on route path "/hbnb" invoke
    """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hello_hnb():
    """return a string on route path "/hbnb" invoke
    """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_is_fun(text):
    """return string in "/c/is-fun"
       replace "_" with space
    """
    # replace '_'
    text = text.replace('_', ' ')
    return f'C {escape(text)}'


@app.route('/python/<text>', strict_slashes=False)
@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python', defaults={'text': 'is cool'}, strict_slashes=False)
def python_route(text):
    """implement a default variable entry
    """
    text = text.replace('_', ' ')
    return f'Python {escape(text)}'


@app.route('/number/<int:n>', strict_slashes=False)
def integer(n):
    """process number variables"""
    return f'{escape(n)} is a number'


if __name__ == '__main__':
    app.run(host='0.0.0.0')
