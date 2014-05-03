# -*- coding: utf-8 -*-

"""
flask_via.examples.blueprints.routes
====================================

A blueprint ``Flask-Via`` example Flask application.
"""

from flask.ext.via.routers import default

routes = [
    default.Blueprint(
        'flask_via.examples.blueprints.foo.routes',
        'foo',
        'flask_via.examples.blueprints.foo',
        url_prefix='/foo',
        template_folder='templates'
    )
]
