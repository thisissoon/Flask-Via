# -*- coding: utf-8 -*-

"""
flask_via.examples.blueprints.routes
====================================

A blueprint ``Flask-Via`` example Flask application.
"""

from flask_via.examples.blueprints.baz import blueprint
from flask.ext.via.routers import default, Include

routes = [
    # Create the blueprint instance
    default.Blueprint(
        'foo',
        'flask_via.examples.blueprints.foo',
        url_prefix='/foo',
        template_folder='templates'
    ),
    # Use a blueprint instance
    default.Blueprint(blueprint),
    # Include blueprints
    Include(
        'flask_via.examples.blueprints.routes',
        routes_name='urls',
        url_prefix='/bar',
        endpoint='bar'
    )
]

urls = [
    default.Blueprint(
        'foo',
        'flask_via.examples.blueprints.foo',
        url_prefix='/foo',
        template_folder='templates'
    )
]
