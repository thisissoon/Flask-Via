# -*- coding: utf-8 -*-

"""
tests.test_routers
==================

Unit tests for common router classes and utilities.
"""

import mock
import unittest

from flask_via.routers import BaseRouter, Include


class TestBaseRouter(unittest.TestCase):

    def test_init_must_be_implemented(self):

        class FooRouter(BaseRouter):
            pass

        with self.assertRaises(NotImplementedError) as e:
            FooRouter()

        self.assertTrue(str(e.exception), '__init__ must be overridden')


class TestIncludeRouter(unittest.TestCase):

    def setUp(self):
        self.app = mock.MagicMock()

    def test_init(self):
        route = Include('foo.bar', routes_name='urls')

        self.assertEqual(route.routes_module, 'foo.bar')
        self.assertEqual(route.routes_name, 'urls')

    @mock.patch('flask_via.import_module')
    def test_add_to_app(self, import_module):
        routes = [
            mock.MagicMock(),
            mock.MagicMock()
        ]
        import_module.return_value = mock.MagicMock(urls=routes)

        route = Include('foo.bar', routes_name='urls')
        route.add_to_app(self.app)

        for instance in routes:
            instance.add_to_app.assert_called_once_with(self.app)
