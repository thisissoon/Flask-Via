# -*- coding: utf-8 -*-

"""
flask_via.examples.include.foo.routes
=====================================

A include ``Flask-Via`` example Flask application.
"""

from flask_via.examples.include.foo.views import BarView, BazView
from flask.ext.via.routers import Include
from flask.ext.via.routers.default import Pluggable

routes = [
    Pluggable('/bar', BarView, 'bar'),
    Pluggable('/baz', BazView, 'baz'),
    Include(
        'flask_via.examples.include.bar.routes',
        url_prefix='/bar',
        endpoint='bar')
]
