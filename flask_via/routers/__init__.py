# -*- coding: utf-8 -*-

"""
flask_via.routers
-----------------

Base router classes and utilities.
"""

from flask_via import RoutesImporter


class BaseRouter(object):
    """ Base router class all routers should inherit from providing common
    router functionality.

    .. versionadded:: 2014.05.06

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

    def add_to_app(self, app, **kwargs):
        """ Method all routers require, which handles adding the route to
        the application instance.

        Raises
        ------
        NotImplementedError
            If method not implemented
        """

        raise NotImplementedError('add_to_app must be overridden')


class Include(BaseRouter, RoutesImporter):
    """ Adds the ability to include routes from other modules, this can be
    handy when you want to break out your routes into separate files for
    sanity.

    .. versionadded:: 2014.05.06

    Note
    ----
    This is not a implementation of Flask blueprints
    """

    def __init__(self, routes_module, routes_name='routes', url_prefix=None):
        """ Constructor for Include router, taking the passed arguments
        and storing them on the instance.

        .. versionchanged:: 2014.05.08

            * ``url_prefix`` argument added

        Arguments
        ---------
        routes_module : str
            Python dotted path to the routes module

        Keyword Arguments
        -----------------
        routes_name : str (optional)
            Name of the variable holding the routes in the module, defaults to
            ``routes``
        url_prefix : str (optional)
            Adds a url prefix to all routes included by the router, defaults
            to ``None``
        """

        self.routes_module = routes_module
        self.routes_name = routes_name
        self.url_prefix = url_prefix

    def add_to_app(self, app, **kwargs):
        """ Instead of adding a route to the flask application this will
        include and load routes similar, same as in the
        :py:class:`flask_via.Via` class.abs

        Arguments
        ---------
        app : flask.app.Flask
            Flask application instance
        \*\*kwargs
            Arbitrary keyword arguments passed in to ``init_app``
        """

        # Inject url_prefix into kwargs
        if self.url_prefix is not None:
            # This allows us to chain url prefix's when multiple includes
            # are called
            try:
                url_prefix = kwargs['url_prefix']
            except KeyError:
                url_prefix = ''
            kwargs['url_prefix'] = url_prefix + self.url_prefix

        # Get the routes
        routes = self.include(self.routes_module, self.routes_name)

        # Load the routes
        self.load(app, routes, **kwargs)
