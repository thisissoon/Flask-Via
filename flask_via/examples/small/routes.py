# -*- coding: utf-8 -*-

"""
flask_via.examples.small.routes
===============================

A small ``Flask-Via`` example Flask application.
"""

from flask_via.examples.small import views
from flask.ext.via.routers import default, Include

routes = [
    default.Basic('/', views.home),
    default.Basic('/about', views.about),
    default.Basic('/contact', views.contact),
    # Include other routes from other modules
    Include('flask_via.examples.small.foo.routes')
]
