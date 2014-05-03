# -*- coding: utf-8 -*-

"""
flask_via.examples.blueprints.foo.views
=======================================

A blueprint ``Flask-Via`` example Flask application.
"""

from flask import render_template


def foo():
    return render_template('foo.html')
