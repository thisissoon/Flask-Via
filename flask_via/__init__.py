# -*- coding: utf-8 -*-

"""
flask_via
=========
"""

__version__ = '0.1.0-dev'  # pragma: no cover
__author__ = 'SOON_'  # pragma: no cover
__author_email__ = 'dorks@thisissoon.com'  # pragma: no cover

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

    routers = ['flask_via.routers.FlaskRouter']  # pragma: no cover

    def init_app(self, app, **kwargs):
        """ Initialises Flask extension. Bootstraps the automatic route
        registration process.

        Arguments
        ---------
        app : flask.app.Flask
            Flask application instance
        **kwargs
            Arbitrary keyword arguments.
        """

        #: Loads default routers and any extra routers defined in the
        #: application config
        self.load_routers(app, **kwargs)

    def router_class_from_path(self, path):
        """ Returns the router class from a python dotted module path.

        Arguments
        ---------
        path : str
            Python dotted path, for example: ``path.to.MyCustomRouter``

        Returns
        -------
        class
            Un instantiated router class

        Raises
        ------
        ImportError
            If the class or module does not exist
        """

        parts = path.split('.')
        kls_name = parts.pop(len(parts) - 1)
        module_path = '.'.join(parts)

        module = import_module(module_path)
        kls = getattr(module, kls_name, None)

        if not kls:
            raise ImportError('No class named {0} in module {1}'.format(
                kls_name,
                module_path))

        return kls

    def load_routers(self, app, **kwargs):
        """ Loads default routers and extra routers defined in application
        config if they have been defined. These are polymorphic router class
        which read routes from the root router module, instantiating the class
        which in tern should register the routes with the application.

        Arguments
        ---------
        app : flask.app.Flask
            Flask application instance
        **kwargs
            Arbitrary keyword arguments.
        """

        config_routers = app.config.get('VIA_ROUTERS', [])
        routers = self.routers + config_routers

        for path in routers:
            Kls = self.router_class_from_path(path)

            # Instantiate the router class, passing the application instance
            # and key word arguments
            router = Kls()
            router.register(app, **kwargs)
