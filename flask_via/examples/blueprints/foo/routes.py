# -*- coding: utf-8 -*-

"""
flask_via.examples.blueprints.foo.routes
========================================

A blueprint ``Flask-Via`` example Flask application.
"""

from flask_via.examples.blueprints.foo import views
from flask.ext.via.routers import default

routes = [
    default.Functional('/baz', views.baz),
]
