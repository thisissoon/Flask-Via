# -*- coding: utf-8 -*-

"""
tests.test_routers
==================

Unit tests for common router classes and utilities.
"""

import copy
import mock
import unittest

from flask import url_for
from flask_via.routers import BaseRouter, Include
from flask_via.routers.default import Functional
from tests import ViaTestCase


class TestBaseRouter(unittest.TestCase):

    def test_init_must_be_implemented(self):

        class FooRouter(BaseRouter):
            pass

        with self.assertRaises(NotImplementedError) as e:
            FooRouter()

        self.assertTrue(str(e.exception), '__init__ must be overridden')


class TestIncludeRouter(ViaTestCase):

    def setUp(self):
        self.foo_view = mock.MagicMock(
            __name__='foo',
            methods=['GET', ],
            return_value='foo')
        self.bar_view = mock.MagicMock(
            __name__='bar',
            methods=['GET', ],
            return_value='bar')
        self.routes = [
            Functional('/foo', self.foo_view, 'foo'),
            Functional('/bar', self.bar_view, 'bar'),
        ]

    def test_init(self):
        route = Include('foo.bar', routes_name='urls')

        self.assertEqual(route.routes_module, 'foo.bar')
        self.assertEqual(route.routes_name, 'urls')

    @mock.patch('flask_via.import_module')
    def test_add_to_app(self, _import_module):
        _import_module.return_value = mock.MagicMock(urls=self.routes)

        route = Include('foo.bar', routes_name='urls')
        route.add_to_app(self.app)

        self.assertEqual(url_for('foo'), '/foo')
        self.assertEqual(url_for('bar'), '/bar')

    @mock.patch('flask_via.import_module')
    def test_url_prefix(self, _import_module):
        routes1 = copy.deepcopy(self.routes)
        routes1.append(Include(
            'foo.bar',
            url_prefix='/prefix2',
            endpoint='prefix2'))
        routes2 = copy.deepcopy(self.routes)

        _import_module.side_effect = [
            mock.MagicMock(routes=routes1),
            mock.MagicMock(routes=routes2)
        ]

        include = Include('foo.bar', url_prefix='/prefix1')
        include.add_to_app(self.app)

        self.assertEqual(url_for('foo'), '/prefix1/foo')
        self.assertEqual(url_for('bar'), '/prefix1/bar')
        self.assertEqual(url_for('prefix2.foo'), '/prefix1/prefix2/foo')
        self.assertEqual(url_for('prefix2.bar'), '/prefix1/prefix2/bar')

    @mock.patch('flask_via.import_module')
    def test_endpoint_prefix(self, _import_module):
        routes1 = copy.deepcopy(self.routes)
        routes1.append(Include(
            'foo.bar',
            endpoint='endpoint2'))
        routes2 = copy.deepcopy(self.routes)

        _import_module.side_effect = [
            mock.MagicMock(routes=routes1),
            mock.MagicMock(routes=routes2)
        ]

        include = Include('foo.bar', endpoint='endpoint1')
        include.add_to_app(self.app)

        self.assertEqual(url_for('endpoint1.foo'), '/foo')
        self.assertEqual(url_for('endpoint1.bar'), '/bar')
        self.assertEqual(url_for('endpoint1.endpoint2.foo'), '/foo')
        self.assertEqual(url_for('endpoint1.endpoint2.bar'), '/bar')
