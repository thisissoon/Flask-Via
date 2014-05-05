# -*- coding: utf-8 -*-

"""
flask_via.examples.small.foo.routes
===================================

A small ``Flask-Via`` example Flask application.
"""

from flask_via.examples.small.foo import views
from flask.ext.via.routers import default

routes = [
    default.Basic('/foo', views.foo),
]
