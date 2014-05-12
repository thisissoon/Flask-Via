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

    def test_url_prefix(self):
        view = mock.MagicMock()
        route = default.Basic('/', view, endpoint='foo')
        route.add_to_app(self.app, url_prefix='/foo')

        self.app.add_url_rule.assert_called_once_with('/foo/', 'foo', view)


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

    def test_url_prefix(self):
        view = mock.MagicMock()
        route = default.Pluggable('/', view_func=view, endpoint='foo')
        route.add_to_app(self.app, url_prefix='/foo')

        self.app.add_url_rule.assert_called_once_with(
            '/foo/',
            view_func=view,
            endpoint='foo')


class TestBlueprintRouter(unittest.TestCase):

    def setUp(self):
        self.app = mock.MagicMock()

    def test_routes_module_path(self):
        route = default.Blueprint('foo', 'foo.bar')

        self.assertEqual(route.routes_module, 'foo.bar.routes')

    @mock.patch('flask.helpers.get_root_path')
    def test_bluepint_creates_blurprint(self, _get_root_path):
        route = default.Blueprint('foo', 'foo.bar')

        self.assertIsInstance(route.blueprint(), Blueprint)

    @mock.patch('flask.helpers.get_root_path')
    def test_bluepint_returns_blurprint(self, _get_root_path):
        blueprint = Blueprint('foo', __name__)
        route = default.Blueprint(blueprint)

        self.assertIsInstance(route.blueprint(), Blueprint)
        self.assertEqual(route.blueprint(), blueprint)

    @mock.patch('flask.helpers.get_root_path')
    def test_url_prefix(self, _get_root_path):
        route = default.Blueprint('foo', 'foo.bar')
        blueprint = route.blueprint(url_prefix='/foo')

        self.assertEqual(blueprint.url_prefix, '/foo')

    @mock.patch('flask_via.routers.default.Blueprint.include')
    @mock.patch('flask_via.routers.default.Blueprint.blueprint')
    def test_add_to_app(self, _blueprint, _include):
        blueprint = mock.MagicMock()
        routes = [
            mock.MagicMock(),
            mock.MagicMock()
        ]
        _include.return_value = routes
        _blueprint.return_value = blueprint

        route = default.Blueprint('foo', 'foo.bar')
        route.add_to_app(self.app)

        for instance in routes:
            instance.add_to_app.assert_called_once_with(blueprint)

        self.app.register_blueprint.assert_called_once_with(blueprint)
