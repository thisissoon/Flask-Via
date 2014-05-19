# -*- coding: utf-8 -*-

"""
tests
=====

Base Test Case / Utilities for the Test Suite
"""

from flask import Flask
from flask.ext.testing import TestCase


class ViaTestCase(TestCase):
    """ Sets up a Do-It Flask application for testing using the testing
    config.
    """

    def create_app(self):
        app = Flask(__name__, static_folder=None)
        app.config['TESTING'] = True
        return app
