#!/usr/bin/python3
"""module: 7-states_list
queries the storage engine and uses a template
to print out results"""
from models import storage
from flask import Flask, render_template
from models.state import State

app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def states_list():
    """accesses a template that formats state output in <UL>"""
    states = storage.all(State)
    return render_template('8-cities_by_states.html',states=states)


@app.teardown_appcontext
def teardown_db(exception):
    """stops current SQLAlchemy Session"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0')
