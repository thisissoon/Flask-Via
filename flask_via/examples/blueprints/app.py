# -*- coding: utf-8 -*-

"""
flask_via.examples.blueprints.app
=================================

A blueprint ``Flask-Via`` example Flask application.
"""

from flask import Flask
from flask.ext.via import Via

app = Flask(__name__)
app.config['VIA_ROUTES_MODULE'] = 'flask_via.examples.blueprints.routes'

via = Via()
via.init_app(app)

if __name__ == '__main__':
    app.run(debug=True)
