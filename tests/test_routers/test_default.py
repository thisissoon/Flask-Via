# -*- coding: utf-8 -*-

"""
tests.test_routers.test_default
===============================

Unit tests for Flask specific router classes.
"""

import mock

from flask import Blueprint, url_for
from flask.views import MethodView
from flask_via.routers import default
from tests import ViaTestCase


class TestFlaskFunctionalRouter(ViaTestCase):

    def setUp(self):
        self.view = mock.MagicMock(
            __name__='foo',
            methods=['GET', ],
            return_value='foo')

    def test_add_to_app(self):
        route = default.Functional('/', self.view, endpoint='foo')
        route.add_to_app(self.app)

        self.assertEqual(url_for('foo'), '/')
        self.assertEqual(self.client.get('/').data, b'foo')

    def test_url_prefix(self):
        route = default.Functional('/', self.view, endpoint='foo')
        route.add_to_app(self.app, url_prefix='/foo')

        self.assertEqual(url_for('foo'), '/foo/')
        self.assertEqual(self.client.get('/foo/').data, b'foo')

    def test_endpoint_prefix(self):
        route = default.Functional('/', self.view, endpoint='foo')
        route.add_to_app(self.app, endpoint='bar.')

        self.assertEqual(url_for('bar.foo'), '/')
        self.assertEqual(self.client.get('/').data, b'foo')

    def test_default_endpoint_name(self):
        route = default.Functional('/', self.view)
        route.add_to_app(self.app, endpoint='bar.')

        self.assertEqual(url_for('bar.foo'), '/')
        self.assertEqual(self.client.get('/').data, b'foo')


class TestFlaskPluggableRouter(ViaTestCase):

    def setUp(self):
        class View(MethodView):

            def get(self):
                return 'foo'

        self.View = View

    def test_add_to_app(self):
        route = default.Pluggable('/', self.View, 'foo')
        route.add_to_app(self.app)

        self.assertEqual(url_for('foo'), '/')
        self.assertEqual(self.client.get('/').data, b'foo')

    def test_url_prefix(self):
        route = default.Pluggable('/', self.View, 'foo')
        route.add_to_app(self.app, url_prefix='/foo')

        self.assertEqual(url_for('foo'), '/foo/')
        self.assertEqual(self.client.get('/foo/').data, b'foo')

    def test_endpoint_prefix(self):
        route = default.Pluggable('/', self.View, endpoint='foo')
        route.add_to_app(self.app, endpoint='bar.')

        self.assertEqual(url_for('bar.foo'), '/')
        self.assertEqual(self.client.get('/').data, b'foo')


class TestBlueprintRouter(ViaTestCase):

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

    @mock.patch('flask.helpers.get_root_path')
    def test_endpoint_prefix(self, _get_root_path):
        route = default.Blueprint('bar', 'foo.bar')
        blueprint = route.blueprint(endpoint='foo.')

        self.assertEqual(blueprint.name, 'foo.bar')

    @mock.patch('flask_via.import_module')
    def test_add_to_app(self, _import_module):
        foo = mock.MagicMock(
            __name__='foo',
            methods=['GET', ],
            return_value='foo')
        bar = mock.MagicMock(
            __name__='bar',
            methods=['GET', ],
            return_value='bar')

        routes = [
            default.Functional('/foo', foo, 'foo'),
            default.Functional('/bar', bar, 'bar'),
        ]

        _import_module.side_effect = [
            mock.MagicMock(routes=routes),
        ]

        route = default.Blueprint('foo', 'foo.bar')

        with mock.patch('flask.helpers.pkgutil.get_loader'):
            route.add_to_app(self.app)

        self.assertEqual(url_for('foo.foo'), '/foo')
        self.assertEqual(url_for('foo.bar'), '/bar')
