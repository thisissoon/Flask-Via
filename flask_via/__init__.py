# -*- coding: utf-8 -*-

"""
flask_via
---------
"""

from flask_via.exceptions import ImproperlyConfigured
from importlib import import_module


class RoutesImporter(object):
    """ Handles the import of routes module and obtaining a list of routes
    from that module as well as loading each route onto the application

    .. versionadded:: 2014.05.06
    """

    def include(self, routes_module, routes_name):
        """ Imports a routes module and gets the routes from within that
        module and returns them.

        Arguments
        ---------
        routes_module : str
            Python dotted path to routes module
        routes_name : str
            Module attribute name to use when attempted to get the routes

        Returns
        -------
        list
            List of routes in the module

        Raises
        ------
        ImportError
            If the route module cannot be imported
        AttributeError
            If routes do not exist in the moduke
        """

        # Import the moduke
        module = import_module(routes_module)

        # Get the routes from the module
        routes = getattr(module, routes_name)

        return routes

    def load(self, app, routes, **kwargs):
        """ Loads passed routes onto the application by calling each routes
        ``add_to_app`` method which must be implemented by the route class.
        """

        for route in routes:
            route.add_to_app(app, **kwargs)


class Via(RoutesImporter):
    """ The core class which kicks off the whole registration processes.

    .. versionadded:: 2014.05.06

    Example
    -------
    .. sourcecode:: python

        from flask import Flask
        from flask.ext.via import Via
        from flask.ext.via.routers.flask import Basic

        app = Flask(__name__)

        def foo(bar=None):
            return 'Foo View!'

        routes = [
            Basic('/foo', foo),
            Basic('/foo/<bar>', foo, endpoint='foo2'),
        ]

        via = Via()
        via.init_app(app, routes_module='path.to.here')

        if __name__ == "__main__":
            app.run(debug=True)
    """

    def init_app(
            self,
            app,
            routes_module=None,
            routes_name=None,
            **kwargs):
        """ Initialises Flask extension. Bootstraps the automatic route
        registration process.

        .. versionchanged:: 2014.05.19

            * Replace ``NotImplementedError`` with ``ImproperlyConfigured``
            * ``routes_name`` keyword argument default value set to ``None``
            * ``routes_name`` can now be configured using ``VIA_ROUTES_NAME``
              app configuration variable. If ``routes_name`` keyword argument
              and ``VIA_ROUTES_NAME`` are not configured the default will be
              routes.

        Arguments
        ---------
        app : flask.app.Flask
            Flask application instance

        Keyword Arguments
        -----------------
        route_module : str, optional
            Python dotted path to where routes are defined, defaults
            to ``None``
        routes_name : str, optional
            Within the routes module look for a variable of this name,
            defaults to ``None``
        \*\*kwargs
            Arbitrary keyword arguments passed to ``add_url_rule``

        Raises
        ------
        ImproperlyConfigured
            If ``VIA_ROUTES_MODULE`` is not configured in appluication config
            and ``route_module`` keyword argument has not been provided.
        """

        if not routes_module:
            routes_module = app.config.get('VIA_ROUTES_MODULE')

        if not routes_module:
            raise ImproperlyConfigured(
                'VIA_ROUTES_MODULE is not defined in application '
                'configuration.')

        # Routes name can be configured by setting VIA_ROUTES_NAME
        if not routes_name:
            routes_name = app.config.get('VIA_ROUTES_NAME', 'routes')

        # Get the routes
        routes = self.include(routes_module, routes_name)

        # Load the routes
        self.load(app, routes, **kwargs)
