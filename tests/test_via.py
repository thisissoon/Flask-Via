# -*- coding: utf-8 -*-

"""
tests.test_via
==============

Unit tests for flask_via.Via class.
"""

import mock
import unittest

from flask_via.via import Via


class TestVia(unittest.TestCase):
    """ flask_via.Via """

    def setUp(self):
        self.app = mock.MagicMock()
        self.app.config = {}

    @mock.patch('flask_via.via.import_module')
    def test_init_app_args(self, import_module):
        """ init_app passes app and kwargs to load_routers """

        FlaskRouter = mock.MagicMock()
        import_module.side_effect = [
            mock.MagicMock(FlaskRouter=FlaskRouter)
        ]

        via = Via()
        via.init_app(self.app, foo='bar')

        FlaskRouter.assert_called_with(self.app, foo='bar')

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

    @mock.patch('flask_via.via.import_module')
    def test_uninstantiated_class_returned(self, import_module):
        """ router_class_from_path returns uninstantiated class """

        class BarRouter(object):
            pass

        import_module.side_effect = mock.MagicMock(BarRouter=BarRouter)

        via = Via()
        path = 'foo.BarRouter'

        kls = via.router_class_from_path(path)

        self.assertNotIsInstance(kls, BarRouter)

    @mock.patch('flask_via.via.import_module')
    def test_load_routers(self, import_module):
        """ load_routers instantiates router classes """

        FooRouter = mock.MagicMock()
        BarRouter = mock.MagicMock()

        import_module.side_effect = [
            mock.MagicMock(FooRouter=FooRouter),
            mock.MagicMock(BarRouter=BarRouter)]

        self.app.config = {'VIA_ROUTERS': ['flask_via.routers.BarRouter']}

        via = Via()
        via.routers = ['flask_via.routers.FooRouter']
        via.load_routers(self.app)

        self.assertTrue(FooRouter.called)
        self.assertTrue(BarRouter.called)
