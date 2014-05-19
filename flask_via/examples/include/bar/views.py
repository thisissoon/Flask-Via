# -*- coding: utf-8 -*-

"""
flask_via.examples.include.bar.views
====================================

A include ``Flask-Via`` example Flask application.
"""

from flask import request
from flask.views import MethodView


class FooView(MethodView):

    def get(self):
        return '{0.path} - {0.endpoint}'.format(request)


class FazView(MethodView):

    def get(self):
        return '{0.path} - {0.endpoint}'.format(request)


def flop():
    return '{0.path} - {0.endpoint}'.format(request)
