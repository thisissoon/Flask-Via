# -*- coding: utf-8 -*-

"""
flask_via.examples.small.foo.routes
===================================

A small ``Flask-Via`` example Flask application.
"""

from flask_via.examples.small.foo import views
from flask.ext.via.routers import default, Include

routes = [
    default.Functional('/foo', views.foo),
    Include('flask_via.examples.small.foo.routes',
            routes_name='urls',
            url_prefix='/bar')
]

urls = [
    default.Functional('/bar', views.foo),
]
