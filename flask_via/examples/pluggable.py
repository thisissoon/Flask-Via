# -*- coding: utf-8 -*-

"""
flask_via.examples.pluggable
============================

A simple ``Flask-Via`` example Flask application.
"""

from flask import Flask
from flask.views import MethodView
from flask.ext.via import Via
from flask.ext.via.routers.default import Pluggable


class FooView(MethodView):

    def get(self, bar=None):
        if bar:
            return 'Pluggable - Foo View with Bar = {0}'.format(bar)
        return 'Pluggable - Foo View'

app = Flask(__name__)

routes = [
    Pluggable('/foo', FooView, 'foo'),
    Pluggable('/foo/<bar>', FooView, 'foo2'),
]

via = Via()
via.init_app(app, routes_module='flask_via.examples.pluggable')

if __name__ == "__main__":
    app.run(debug=True)
