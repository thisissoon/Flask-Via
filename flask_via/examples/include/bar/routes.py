# -*- coding: utf-8 -*-

"""
flask_via.examples.include.foo.routes
=====================================

A include ``Flask-Via`` example Flask application.
"""

from flask_via.examples.include.bar.views import FooView, FazView, flop
from flask.ext.via.routers.default import Functional, Pluggable

routes = [
    Pluggable('/foo', FooView, 'foo'),
    Pluggable('/faz', FazView, 'faz'),
    Functional('/flop', flop),
]
