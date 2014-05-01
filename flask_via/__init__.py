# -*- coding: utf-8 -*-

"""
flask_via
=========
"""

from importlib import import_module


class Via(object):
    """ The core class which kicks off the whole registration processes.

    Attributes
    ----------
    routers : list
        A list of python dotted string paths to a single router class. This
        is the default list of routers applied, these are:

        * :py:class:`.routers.FlaskRouter`

        Override this before you init_app to change the default routers
        applied, an empty list is acceptable to avoid any default routers
        being run.

    Example
    ------
    .. sourcecode:: python

        from flask import Flask
        from flask.ext.via import Via

        app = Flask(__name__)
        via = Via()

        via.routers = []  # No default routers run
        via.init_app(app)

        app.run()
    """

    def init_app(self, app, route_module=None, routes_variable='routes'):
        """ Initialises Flask extension. Bootstraps the automatic route
        registration process.

        Arguments
        ---------
        app : flask.app.Flask
            Flask application instance

        Keyword Arguments
        -----------------
        route_module : str
            Python dotted path to where routes are defined, defaults
            to ``None``
        routes_variable : str
            Within the routes module look for a variable of this name,
            defaults to ``routes``

        Raises
        ------
        ImportError
            If the route module cannot be imported
        AttributeError
            If routes do not exist in the moduke
        NotImplementedError
            If VIA_ROUTE_MODULE is not configured in appluication config and
            ``route_module`` keyword argument has not been provided.
        """

        if not route_module:
            route_module = app.config.get('VIA_ROUTE_MODULE')

        if not route_module:
            raise NotImplementedError(
                'VIA_ROUTE_MODULE is not defined in application '
                'configuration.')

        # Import the moduke
        module = import_module(route_module)

        # Get the routes from the module
        routes = getattr(module, routes_variable)

        # Process Routes
        for route in routes:
            route.add_to_app(app)
