# -*- coding: utf-8 -*-

"""
flask_via.examples.blueprints.baz
=================================

A blueprint ``Flask-Via`` example Flask application.
"""

from flask import Blueprint


blueprint = Blueprint(
    'baz', __name__, template_folder='templates', url_prefix='/baz')
