# -*- coding: utf-8 -*-

"""
flask_via.examples.basic
========================

A simple ``Flask-Via`` example Flask application.
"""

from flask import Flask
from flask.ext.via import Via

app = Flask(__name__)
app.config['VIA_ROOT'] = 'flask_via.examples.basic'


def home():
    return 'Hello World!'

routes = [
    ('/', 'home', home)
]

via = Via()
via.init_app(app)

app.run()
