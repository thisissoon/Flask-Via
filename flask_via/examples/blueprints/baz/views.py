# -*- coding: utf-8 -*-

"""
flask_via.examples.blueprints.baz.views
=======================================

A blueprint ``Flask-Via`` example Flask application.
"""

from flask import render_template


def baz():
    return render_template('baz.html')
