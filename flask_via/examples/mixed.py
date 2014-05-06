# -*- coding: utf-8 -*-

"""
flask_via.examples.mixed
========================

Mixed router example.
"""

from flask import Flask
from flask.views import MethodView
from flask.ext import restful
from flask.ext.via import Via
from flask.ext.via.routers.default import Basic, Pluggable
from flask.ext.via.routers.restful import Resource


class FooView(MethodView):

    def get(self, bar=None):
        rtn = 'Pluggable Foo View'
        if bar:
            rtn += ' bar = {0}'.format(bar)

        return rtn


class FooResource(restful.Resource):

    def get(self, bar=None):
        rtn = {'resource': 'foo'}
        if bar:
            rtn['bar'] = bar

        return rtn


def foo(bar=None):
    rtn = 'Basic Foo View'
    if bar:
        rtn += ' bar = {0}'.format(bar)

    return rtn


app = Flask(__name__)
api = restful.Api(app)

routes = [
    Basic('/basic', foo),
    Basic('/basic/<bar>', foo, endpoint='foo.basic'),
    Pluggable('/pluggable', view_func=FooView.as_view('foo.pluggable')),
    Pluggable(
        '/pluggable/<bar>',
        view_func=FooView.as_view('foobar.pluggable')),
    Resource('/resource', FooResource, 'foo.resource'),
    Resource('/resource/<bar>', FooResource, endpoint='foobar.resource')
]

via = Via()
via.init_app(
    app,
    routes_module='flask_via.examples.mixed',
    restful_api=api)

if __name__ == '__main__':
    app.run(debug=True)
