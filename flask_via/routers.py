# -*- coding: utf-8 -*-

"""
flask_via.routers
=================

This module contains the bundled router classed with Flask-Via. Simply define
these classed in your application config using the ``VIA_ROUTES`` config
variable, this should be a list of Python dotted paths to a class, for
example::

    VIA_ROUTES = [
        'flask.ext.via.routers.RestfulRouter',
        'my.custom.Router',
    ]
"""

from importlib import import_module


class BaseRouter(object):
    """ This class provides the base router class all routers should inherit
    from, it provides basic functionality and also defines methods which need
    to implemented by inheriting classes, raising ``NotImplementedError``
    exceptions where appropriate.

    Example
    -------
    .. sourcecode:: python

        form flask.ext.via.routers import BaseRouter

        class MyRouter(BaseRouter):
            ...
    """

    def __init__(self, app, **kwargs):
        """ Constructor. Adds Flask application instance and arbitrary keyword
        arguments as instance variables.

        Example
        -------
        If ``Via`` was instantiated with keyword arguments these will become
        private instance variables on the router instance:

        .. soucecode:: python

            from flask import Flask
            from flask.ext.restful import Api
            from flask.ext.via import Via

            app = Flask(__name__)

            api = Api(app)
            via = Via()

            via.init_app(app, restful_api=api)

            # self._restful_api can now be access in the router class

        """

        self.app = app

        for attr, value in kwargs.iteritems():
            setattr(self, '_{0}'.format(attr), value)

    @property
    def root_module(self):
        """ Attempts to get the root routes module which contains the routes
        to be added to the application instance. This is obtained from the
        ``VIA_ROOT`` config setting which should be a python dotted path to a
        python module, for example::

            VIA_ROOT = 'yourapp.routes'

        Returns
        -------
        module
            Root routes module

        Raises
        ------
        NotImplementedError
            If ``VIA_ROOT`` is not defined
        ImportError
            If the module does not exist
        """

        path = self.app.config.get('VIA_ROOT')
        if not path:
            raise NotImplementedError('VIA_ROOT is not defined in '
                                      'application configuration.')

        module = import_module(path)

        return module

    @property
    def name(self):
        """ Each class inheriting from ``BaseRouter`` must also define a
        ``name`` class variable which defines the variable name within
        the root routes module to use when iterating over routes to register
        them with the Flask application, for example::

            # path/to/my/router.py
            class MyFoo(BaseRouter):
                name = 'foos'

            # path/to/root/routes.pt
            foos = [
                ('/', 'thing')
            ]

        Raises
        ------
        NotImplementedError
            If ``name`` is not defined
        """

        raise NotImplementedError('name attribute must be defined on '
                                  '{0}'.format(self.__class__.__name__))

    def register(self):
        """ Method must be implemented by sub class which handles registering
        the routes with the Flask application.

        Raises
        ------
        NotImplementedError
            If this method has not been implemented
        """

        raise NotImplementedError('register method not defined on {0}'.format(
            self.__class__.__name__))
