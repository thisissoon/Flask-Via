# -*- coding: utf-8 -*-

"""
flask_via.routers.flask
-----------------------

A set of flask specific router classes to be used when defining routes.

Example
-------

.. sourcecode:: python

    from flask.ext.via.routes.flask import Basic, Pluggable
    from yourapp.views import BarView, foo_view

    routes = [
        Basic('/foo', 'foo', foo_view),
        Pluggable('/bar', view_func=BarView.as_view('bar')),
    ]

"""

from flask import Blueprint as FlaskBlueprint
from flask_via import RoutesImporter
from flask_via.routers import BaseRouter


class Basic(BaseRouter):
    """ A basic Flask router, used for the most basic form of flask routes,
    namely functionally based views which would normally use the ``@route``
    decorator.

    Example
    -------
    .. sourcecode:: python

        from flask.ext.via.routes import flask
        from yourapp.views import foo_view, bar_view

        routes = [
            Basic('/foo', 'foo', foo_view),
            Basic('/bar', 'bar', bar_view),
        ]
    """

    def __init__(self, url, func, endpoint=None):
        """ Basic router constructor, stores passed arguments on the
        instance.

        Arguments
        ---------
        url : str
            The url to use for the route
        func : function
            The view function to connect the route with

        Keyword Arguments
        -----------------
        endpoint : str, optional
            Optional endpoint string, by default flask will use the
            view function name as the endpoint name, use this argument
            to change the endpoint name.
        """

        self.url = url
        self.func = func
        self.endpoint = endpoint

    def add_to_app(self, app, **kwargs):
        """ Adds the url route to the flask application object.mro

        Arguments
        ---------
        app : flask.app.Flask
            Flask application instance
        \*\*kwargs
            Arbitrary keyword arguments passed in to ``init_app``
        """

        #: If this route was included a url preifx may have been passed
        #: to the route
        if 'url_prefix' in kwargs:
            self.url = kwargs['url_prefix'] + self.url

        app.add_url_rule(self.url, self.endpoint, self.func)


class Pluggable(BaseRouter):
    """ Pluggable View router class, allows Flask pluggable view routes to be
    added to the flask application.

    Example
    -------
    .. sourcecode:: python

        from flask.ext.via.routers import flask
        from flask.views import MethodView

        class FooView(MethodView):
            def get(self):
                return 'foo view'

        class BarView(MethodView):
            def get(self):
                return 'bar view'

        routes = [
            flask.Pluggable('/', view_func=FooView.as_view('foo'))
            flask.Pluggable('/', view_func=BarView.as_view('bar'))
        ]
    """

    def __init__(self, url, **kwargs):
        """ Pluggable router constructor, stores passed arguments on instance.

        Arguments
        ---------
        url : str
            The url to use for the route
        \*\*kwargs
            Arbitrary keyword arguments passed to ``add_url_rule``
        """

        self.url = url
        self.kwargs = kwargs

    def add_to_app(self, app, **kwargs):
        """ Adds the url route to the flask application object.

        Arguments
        ---------
        app : flask.app.Flask
            Flask application instance
        \*\*kwargs
            Arbitrary keyword arguments passed in to ``init_app``
        """

        #: If this route was included a url preifx may have been passed
        #: to the route
        if 'url_prefix' in kwargs:
            self.url = kwargs['url_prefix'] + self.url

        app.add_url_rule(self.url, **self.kwargs)


class Blueprint(BaseRouter, RoutesImporter):
    """ Registers a flask blueprint and registers routes to that blueprint,
    similar to :py:class:`flask_via.routes.Include`.

    Example
    -------
    .. sourcecode:: python

        from flask.ext.via.routers import default

        routes = [
            default.blueprint('foo', 'flask_via.examples.blueprints.foo')
        ]
    """

    def __init__(
            self,
            name,
            module,
            routes_module_name='routes',
            routes_name='routes',
            static_folder=None,
            static_url_path=None,
            template_folder=None,
            url_prefix=None,
            subdomain=None,
            url_defaults=None):
        """ Constructor for blueprint router.

        Arguments
        ---------
        name : str
            Blueprint name
        module : str
            Python dotted path to the blueprint module, not the routes module

        Keyword Arguments
        -----------------
        routes_module_name : str, optional
            The module ``Flask-Via`` will look for within the blueprint module
            which contains the routes, defaults to ``routes``
        routes_name : str, optional
            Name of the variable holding the routes in the module, defaults to
            ``routes``
        static_folder : str, optional
            Path to static files for blueprint, defaults to ``None``
        static_url_path : str, optional
            URL path for blueprint static files, defaults to ``None``
        template_folder : str, optional
            Templates folder name, defaults to ``None``
        url_prefix : str, optional
            URL prefix for routes served within the blueprint, defaults
            to ``None``
        subdomain : str, optional
            Sub domain for blueprint, defaults to ``None``
        url_defaults : function, optional
            Callback function for URL defaults for this blueprint.
            It's called with the endpoint and values and should update
            the values passed in place, defaults to ``None``.
        """

        self.name = name
        self.module = module
        self.routes_module_name = routes_module_name
        self.routes_name = routes_name
        self.static_folder = static_folder
        self.static_url_path = static_url_path
        self.template_folder = template_folder
        self.url_prefix = url_prefix
        self.subdomain = subdomain
        self.url_defaults = url_defaults

    @property
    def routes_module(self):
        """ Generates the routes module path, this is built from
        ``self.module`` and ``self.routes_module_name``.

        Returns
        -------
        str
            Python dotted path to the routes module containing routes.
        """

        return '{0}.{1}'.format(self.module, self.routes_module_name)

    def create_blueprint(self, **kwargs):
        """ Creates a flask blueprint instance.
        """

        #: If this route was included a url preifx may have been passed
        #: to the route
        if 'url_prefix' in kwargs:
            url_prefix = self.url_prefix or ''
            self.url_prefix = kwargs['url_prefix'] + url_prefix

        blueprint = FlaskBlueprint(
            self.name,
            self.module,
            static_folder=self.static_folder,
            static_url_path=self.static_url_path,
            template_folder=self.template_folder,
            url_prefix=self.url_prefix,
            subdomain=self.subdomain,
            url_defaults=self.url_defaults)

        return blueprint

    def add_to_app(self, app, **kwargs):
        """ Creates a Flask blueprint and registers routes with that blueprint,
        this means any routes defined will be added to the blueprint rather
        than the application.

        Arguments
        ---------
        app : flask.app.Flask
            Flask application instance
        \*\*kwargs
            Arbitrary keyword arguments passed in to ``init_app``
        """

        # Register blueproiint
        blueprint = self.create_blueprint(**kwargs)

        # Get the routes
        routes = self.include(self.routes_module, self.routes_name)

        # Load the routes
        self.load(blueprint, routes)

        # Register the blueprint with the application
        app.register_blueprint(blueprint)
