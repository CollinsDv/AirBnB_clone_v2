#!/usr/bin/python3
"""
module: 2-c_route
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


if __name__ == '__main__':
    app.run(host='0.0.0.0')
