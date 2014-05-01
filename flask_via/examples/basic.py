# -*- coding: utf-8 -*-

"""
flask_via.examples.basic
========================

A simple ``Flask-Via`` example Flask application.
"""

from flask import Flask
from flask.ext.via import Via
from flask.ext.via.routers.flask import Basic


app = Flask(__name__)


def foo(bar=None):
    return 'Foo View!'


routes = [
    Basic('/foo', foo),
    Basic('/foo/<bar>', foo, endpoint='foo2'),
]

via = Via()
via.init_app(app, route_module='flask_via.examples.basic')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
