# -*- coding: utf-8 -*-

"""
flask_via.examples.blueprints.baz.routes
========================================

A blueprint ``Flask-Via`` example Flask application.
"""

from flask_via.examples.blueprints.baz import views
from flask.ext.via.routers import default


routes = [
    default.Functional('/', views.baz),
]
