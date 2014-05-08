# -*- coding: utf-8 -*-

"""
tests.test_routers.test_admin
=============================

Unit tests for the Flask-Admin admin router.
"""

import mock
import unittest

from flask_via.routers import admin


class TestRestfulRouter(unittest.TestCase):

    def setUp(self):
        self.app = mock.MagicMock()

    def test_add_to_app_raises_not_implemented(self):

        resource = admin.AdminRoute(mock.MagicMock())

        with self.assertRaises(NotImplementedError) as e:
            resource.add_to_app(self.app)

        self.assertEqual(
            str(e.exception),
            'flask_admin not passed to add_to_app, did you add it to '
            'via.init_app?')

    def test_add_to_app(self):

        flask_admin = mock.MagicMock()

        class FooAdminView(mock.MagicMock):
            pass

        route = admin.AdminRoute(FooAdminView)
        route.add_to_app(self.app, flask_admin=flask_admin)

        flask_admin.add_view.assert_called_once_with(FooAdminView)
