# -*- coding: utf-8 -*-

"""
flask_via.examples.include.routes
=================================

A include ``Flask-Via`` example Flask application.
"""

from flask.ext.via.routers import Include

routes = [
    Include(
        'flask_via.examples.include.foo.routes',
        url_prefix='/foo',
        endpoint='foo')
]
