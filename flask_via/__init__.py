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
    """ Flask-VIa integration into Flask applications. Flask-Via can
    be integrated in two different ways depending on how you have setup your
    Flask application.

    .. versionadded:: 2014.05.06

    You can bind to a specific flask application::

        from flask import Flask
        from flask.ext.via import Via
        from flask.ext.via.routers.flask import Functional

        app = Flask(__name__)

        def foo(bar=None):
            return 'Foo View!'

        routes = [
            Functional('/foo', foo),
            Functional('/foo/<bar>', foo, endpoint='foo2'),
        ]

        via = Via(app, routes_module='path.to.here')

        if __name__ == "__main__":
            app.run(debug=True)

    Or if you use an application factory you can use
    :meth:`flask_via.Via.init_app`::

        from flask import Flask
        from flask.ext.via import Via
        from flask.ext.via.routers.flask import Functional

        via = Via()

        def foo(bar=None):
            return 'Foo View!'

        routes = [
            Functional('/foo', foo),
            Functional('/foo/<bar>', foo, endpoint='foo2'),
        ]

        def create_app():
            app = Flask(__name__)
            via.init_app(app)
            return app

        app = create_app()

        if __name__ == "__main__":
            app.run(debug=True)
    """

    def __init__(self, app=None, *args, **kwargs):
        """ Constructor. Functionalally acts as a proxy to
        :meth:`flask_store.Store.init_app`.

        .. versionadded:: 2014.05.19.2

        Key Arguments
        -------------
        app : flask.app.Flask, optional
            Optional Flask application instance, default None
        """

        if app:
            self.init_app(app, *args, **kwargs)

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

        .. versionchanged:: 2014.05.19.2

            * Improved ``init_app`` method

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

        app.config.setdefault('VIA_ROUTES_MODULE', routes_module)
        app.config.setdefault('VIA_ROUTES_NAME', routes_name or 'routes')

        if not app.config['VIA_ROUTES_MODULE']:
            raise ImproperlyConfigured(
                'VIA_ROUTES_MODULE is not defined in application '
                'configuration.')

        routes_module = app.config['VIA_ROUTES_MODULE']
        routes_name = app.config['VIA_ROUTES_NAME']

        # Get the routes
        routes = self.include(routes_module, routes_name)

        # Load the routes
        self.load(app, routes, **kwargs)
