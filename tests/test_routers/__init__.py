# -*- coding: utf-8 -*-

"""
tests.test_routers
==================

Unit tests for common router classes and utilities.
"""

import unittest

from flask_via.routers import BaseRouter


class TestBaseRouter(unittest.TestCase):

    def test_init_must_be_implemented(self):

        class FooRouter(BaseRouter):
            pass

        with self.assertRaises(NotImplementedError) as e:
            FooRouter()

        self.assertTrue(str(e.exception), '__init__ must be overridden')
