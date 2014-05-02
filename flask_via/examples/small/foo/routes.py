# -*- coding: utf-8 -*-

"""
flask_via.examples.small.foo.routes
===================================

A small ``Flask-Via`` example Flask application.
"""

from flask_via.examples.small.foo import views
from flask.ext.via.routers import flask

routes = [
    flask.Basic('/foo', views.foo),
]
