# -*- coding: utf-8 -*-

"""
tests.test_routers.test_restful
================================

Unit tests for the Flask-Restful resource router.
"""

import mock
import unittest

from flask_via.routers import restful


class TestRestfulRouter(unittest.TestCase):

    def setUp(self):
        self.app = mock.MagicMock()

    def test_add_to_app_raises_not_implemented(self):

        resource = restful.Resource('/', mock.MagicMock())

        with self.assertRaises(NotImplementedError) as e:
            resource.add_to_app(self.app)

        self.assertEqual(
            str(e.exception),
            'restful_api not passed to add_to_app, did you add it to '
            'via.init_app?')

    def test_add_to_app(self):

        api = mock.MagicMock()

        class Resource(mock.MagicMock):
            pass

        resource = restful.Resource('/', Resource)
        resource.add_to_app(self.app, restful_api=api)

        api.add_resource.assert_called_once_with(Resource, '/', endpoint=None)
