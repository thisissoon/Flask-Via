# -*- coding: utf-8 -*-

"""
flask_via.examples.small.routes
===============================

A small ``Flask-Via`` example Flask application.
"""

from flask_via.examples.small import views
from flask.ext.via.routers import flask

routes = [
    flask.Basic('/', views.home),
    flask.Basic('/about', views.about),
    flask.Basic('/contact', views.contact)
]