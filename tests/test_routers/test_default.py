# -*- coding: utf-8 -*-

"""
tests.test_routers.test_default
===============================

Unit tests for Flask specific router classes.
"""

import mock
import unittest

from flask import Blueprint
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


class TestBlueprintRouter(unittest.TestCase):

    def setUp(self):
        self.app = mock.MagicMock()

    def test_routes_module_path(self):
        route = default.Blueprint('foo', 'foo.bar')

        self.assertEqual(route.routes_module, 'foo.bar.routes')

    @mock.patch('flask.helpers.get_root_path')
    def test_create_bluepint_returns_blurprint(self, _get_root_path):
        route = default.Blueprint('foo', 'foo.bar')

        self.assertIsInstance(route.create_blueprint(), Blueprint)

    @mock.patch('flask_via.routers.default.Blueprint.include')
    @mock.patch('flask_via.routers.default.Blueprint.create_blueprint')
    def test_add_to_app(self, _create_blueprint, _include):
        blueprint = mock.MagicMock()
        routes = [
            mock.MagicMock(),
            mock.MagicMock()
        ]
        _include.return_value = routes
        _create_blueprint.return_value = blueprint

        route = default.Blueprint('foo', 'foo.bar')
        route.add_to_app(self.app)

        for instance in routes:
            instance.add_to_app.assert_called_once_with(blueprint)

        self.app.register_blueprint.assert_called_once_with(blueprint)
