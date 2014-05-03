# -*- coding: utf-8 -*-

"""
tests.test_routers.test_default
===============================

Unit tests for Flask specific router classes.
"""

import mock
import unittest

from flask_via.routers import default


class TestFlaskBasicRouter(unittest.TestCase):

    def setUp(self):
        self.app = mock.MagicMock()

    def test_add_to_app(self):
        view = mock.MagicMock()
        route = default.Basic('/', view, endpoint='foo')
        route.add_to_app(self.app)

        self.app.add_url_rule.assert_called_once_with('/', 'foo', view)


class TestFlaskPluggableRouter(unittest.TestCase):

    def setUp(self):
        self.app = mock.MagicMock()

    def test_add_to_app(self):
        view = mock.MagicMock()
        route = default.Pluggable('/', view_func=view, endpoint='foo')
        route.add_to_app(self.app)

        self.app.add_url_rule.assert_called_once_with(
            '/',
            view_func=view,
            endpoint='foo')
