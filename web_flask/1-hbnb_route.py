#!/usr/bin/python3
"""
module: 1-hbnb_route
"""
from flask import Flask

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


if __name__ == '__main__':
    app.run(host='0.0.0.0')
