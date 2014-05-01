# -*- coding: utf-8 -*-

"""
tests.test_routers
==================

Unit tests for flask_via.router module and classes.
"""

import mock
import unittest

from flask_via.routers import BaseRouter


class TestBaseRouter(unittest.TestCase):
    """ flask_via.routers.BaseRouter """

    def setUp(self):
        self.app = mock.MagicMock(config={})

    def test_kwargs_private_instance_vars(self):
        """ __init__ sets app and kwargs as instance variables """

        instance = BaseRouter(self.app, foo='bar')

        self.assertEqual(self.app, instance.app)
        self.assertEqual('bar', instance._foo)

    def test_root_module_must_be_defined(self):
        """ VIA_ROOT must be defined in app config """

        instance = BaseRouter(self.app)

        with self.assertRaises(NotImplementedError) as e:
            instance.root_module()

        self.assertTrue(
            e.exception.message,
            'VIA_ROOT is not defined in application configuration.')

    @mock.patch('flask_via.routers.import_module')
    def test_root_module_loaded(self, import_module):
        """ loads VIA_ROOT module """

        self.app.config = {'VIA_ROOT': 'foo.bar'}

        instance = BaseRouter(self.app)
        import_module.side_effect = mock.MagicMock()

        instance.root_module()

        import_module.assert_called_with('foo.bar')

    def test_not_implemented_raised_if_name_not_defined(self):
        """ name attribute must be defined on child class """

        class FooRouter(BaseRouter):
            pass

        instance = FooRouter(self.app)

        with self.assertRaises(NotImplementedError) as e:
            instance.name

        self.assertTrue(
            e.exception.message,
            'name attribute must be defined on FooRouter')

    def test_register_method_must_be_implemented(self):
        """ register method must be implemented in child class """

        class FooRouter(BaseRouter):
            pass

        instance = FooRouter(self.app)

        with self.assertRaises(NotImplementedError) as e:
            instance.register()

        self.assertTrue(
            e.exception.message,
            'register method not defined on FooRouter')
