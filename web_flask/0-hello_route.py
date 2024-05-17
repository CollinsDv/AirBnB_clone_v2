#!/usr/bin/python3
"""
module: 0-hello_route
"""
from flask import Flask

# instanciate a Flask instance with module name
app = Flask(__name__)


# decorator to register view function to URL rulw
@app.route('/', strict_slashes=False)
def hello():
    """return a string on route invoke
    """
    return 'Hello HBNB!'


if __name__ == '__main__':
    app.run(host='0.0.0.0')
