# -*- coding: utf-8 -*-

"""
flask_via.examples.blueprints.routes
====================================

A blueprint ``Flask-Via`` example Flask application.
"""

from flask.ext.via.routers import default, Include

routes = [
    default.Blueprint(
        'foo',
        'flask_via.examples.blueprints.foo',
        url_prefix='/foo',
        template_folder='templates'
    ),
    Include(
        'flask_via.examples.blueprints.routes',
        routes_name='urls',
        url_prefix='/bar'
    )
]

urls = [
    default.Blueprint(
        'foo.bar',
        'flask_via.examples.blueprints.foo',
        url_prefix='/foo',
        template_folder='templates'
    )
]
