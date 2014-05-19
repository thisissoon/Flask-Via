# -*- coding: utf-8 -*-

"""
flask_via.examples.include.foo.views
====================================

A include ``Flask-Via`` example Flask application.
"""

from flask import request
from flask.views import MethodView


class BarView(MethodView):

    def get(self):
        return '{0.path} - {0.endpoint}'.format(request)


class BazView(MethodView):

    def get(self):
        return '{0.path} - {0.endpoint}'.format(request)
