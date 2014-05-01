# -*- coding: utf-8 -*-

"""
tests.test_via
==============

Unit tests for flask_via.Via class.
"""

import mock
import unittest

from flask_via import Via


class TestVia(unittest.TestCase):
    """ flask_via.Via """

    def setUp(self):
        self.app = mock.MagicMock()
        self.app.config = {}

    def tearDown(self):
        del self.app

    @mock.patch('flask_via.routers.FlaskRouter', create=True)
    def test_init_app(self, FlaskRouter):
        """ init_app passes app and kwargs to load_routers """

        instance = mock.MagicMock()
        FlaskRouter.return_value = instance

        via = Via()

        via.init_app(self.app, foo='bar')

        self.assertTrue(FlaskRouter.called)
        instance.register.assert_called_with(self.app, foo='bar')

    def test_raises_import_error(self):
        """ router_class_from_path raises import error """

        via = Via()
        path = 'foo.bar.Kls'

        with self.assertRaises(ImportError) as e:
            via.router_class_from_path(path)

        self.assertEqual(e.exception.message, 'No module named foo.bar')

    def test_missing_class_raises_import_error(self):
        """ router_class_from_path raises imort error on missing class """

        via = Via()
        path = 'flask_via.Foo'

        with self.assertRaises(ImportError) as e:
            via.router_class_from_path(path)

        self.assertEqual(
            e.exception.message,
            'No class named Foo in module flask_via')

    def test_uninstantiated_class_returned(self):
        """ router_class_from_path returns uninstantiated class """

        via = Via()
        path = 'flask_via.Via'

        kls = via.router_class_from_path(path)

        self.assertNotIsInstance(Via, kls)

    @mock.patch('flask_via.routers.FooRouter', create=True)
    @mock.patch('flask_via.routers.BarRouter', create=True)
    def test_load_routers(
            self,
            FooRouter,
            BarRouter):
        """ load_routers instantiates router classes """

        self.app.config = {'VIA_ROUTERS': ['flask_via.routers.BarRouter']}

        via = Via()
        via.routers = ['flask_via.routers.FooRouter']
        via.load_routers(self.app)

        self.assertTrue(FooRouter.called)
        self.assertTrue(BarRouter.called)
