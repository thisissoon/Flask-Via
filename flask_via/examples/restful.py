# -*- coding: utf-8 -*-

"""
flask_via.examples.restful
==========================

A simple ``Flask-Via`` example Flask application.
"""

from flask import Flask
from flask.ext import restful
from flask.ext.via import Via
from flask.ext.via.routers.restful import Resource


app = Flask(__name__)
api = restful.Api(app)


class FooResource(restful.Resource):

    def get(self):
        return {'hello': 'world'}


routes = [
    Resource('/foo', FooResource)
]

via = Via()
via.init_app(
    app,
    routes_module='flask_via.examples.restful',
    restful_api=api)


if __name__ == '__main__':
    app.run(debug=True)
