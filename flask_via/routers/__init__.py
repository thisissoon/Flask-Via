# -*- coding: utf-8 -*-

"""
flask_via.routers
-----------------

Base router classes and utilities.
"""


class BaseRouter(object):
    """ Base router class all routers should inherit from providing common
    router functionality.

    Example
    -------
    .. sourcecode:: python

        from flask.ext.via.routers import BaseRouter

        class MyRouter(BaseRouter):

            def __init__(self, arg):
                ...

            def add_to_app(self, app):
                ...
    """

    def __init__(self):
        """ Constructor should be overridden to accept specific arguments
        for the router.

        Raises
        ------
        NotImplementedError
            If method not implemented
        """

        raise NotImplementedError('__init__ must be overridden')

    def add_to_app(self):
        """ Method all routers require, which handles adding the route to
        the application instance.

        Raises
        ------
        NotImplementedError
            If method not implemented
        """

        raise NotImplementedError('add_to_app must be overridden')
