# -*- coding: utf-8 -*-

"""
flask_via.examples.include.app
==============================

A include ``Flask-Via`` example Flask application.
"""

from flask import Flask
from flask.ext.via import Via

app = Flask(__name__)
app.config['VIA_ROUTES_MODULE'] = 'flask_via.examples.include.routes'

via = Via()
via.init_app(app)

if __name__ == '__main__':
    app.run(debug=True)
