# -*- coding: utf-8 -*-

"""
flask_via.routers.default
-------------------------

A set of flask specific router classes to be used when defining routes.

Example
-------

.. sourcecode:: python

    from flask.ext.via.routes.flask import Basic, Pluggable
    from yourapp.views import BarView, foo_view

    routes = [
        Basic('/foo', 'foo', foo_view),
        Pluggable('/bar', BarView, 'bar'),
    ]

"""

from flask import Blueprint as FlaskBlueprint
from flask_via import RoutesImporter
from flask_via.routers import BaseRouter


class Functional(BaseRouter):
    """ A basic Flask router, used for the most basic form of flask routes,
    namely functionally based views which would normally use the ``@route``
    decorator.

    .. versionadded:: 2014.05.19

    Example
    -------
    .. sourcecode:: python

        from flask.ext.via.routes import default
        from yourapp.views import foo_view, bar_view

        routes = [
            default.Functional('/foo', 'foo', foo_view),
            default.Functional('/bar', 'bar', bar_view),
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

        .. versionchanged:: 2014.05.08

            * ``url_prefix`` can now be prefixed if present in kwargs

        .. versionchanged:: 2014.05.19

            * ``endpoint`` can now be prefixed if present in kwargs

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

        #: If this route was included a endpoint prefix may have been passed
        #: to the route
        if 'endpoint' in kwargs:
            if self.endpoint is None:
                self.endpoint = self.func.__name__
            self.endpoint = kwargs['endpoint'] + self.endpoint

        app.add_url_rule(self.url, self.endpoint, self.func)


class Basic(Functional):
    """ This is deprecated and will be removed in the next release. Please use
    :class:`.Functional`.

    .. versionadded:: 2014.05.06
    .. deprecated:: 2014.05.19
    """


class Pluggable(BaseRouter):
    """ Pluggable View router class, allows Flask pluggable view routes to be
    added to the flask application.

    .. versionadded:: 2014.05.06

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
            flask.Pluggable('/', FooView, 'foo')
            flask.Pluggable('/', BarView, 'bar')
        ]
    """

    def __init__(self, url, view, endpoint, **kwargs):
        """ Pluggable router constructor, stores passed arguments on instance.

        .. versionchanged:: 2014.05.19

            * Added ``view`` argument
            * Added ``endpoint`` argument

        Arguments
        ---------
        url : str
            The url to use for the route
        view : class
            The Flask pluggable view class, for example:
            * :class:`flask.views.View`
            * :class:`flask.views.MethodView`
        endpoint : str
            The Flask endpoint name for the view, this is required for Flask
            pluggable views.
        \*\*kwargs :
            Arbitrary keyword arguments for ``add_url_rule``
        """

        self.url = url
        self.view = view
        self.endpoint = endpoint
        self.kwargs = kwargs

    def add_to_app(self, app, **kwargs):
        """ Adds the url route to the flask application object.

        .. versionchanged:: 2014.05.19

            Updated ``add_url_rule`` to support endpoint prefixing and support
            new way of defining Pluggable views

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

        #: If this route was included a endpoint prefix may have been passed
        #: to the route
        if 'endpoint' in kwargs:
            self.endpoint = kwargs['endpoint'] + self.endpoint

        app.add_url_rule(
            self.url,
            view_func=self.view.as_view(self.endpoint),
            **self.kwargs)


class Blueprint(BaseRouter, RoutesImporter):
    """ Registers a flask blueprint and registers routes to that blueprint,
    similar to :py:class:`flask_via.routers.Include`.

    .. versionadded:: 2014.05.06

    Example
    -------

    **Auto creates Blueprint instance***

    .. sourcecode:: python

        from flask.ext.via.routers import default

        routes = [
            default.Blueprint('foo', 'flask_via.examples.blueprints.foo')
        ]

    **Pass existing Blueprint instance***

    .. sourcecode:: python

        from flask import Blueprint
        from flask.ext.via.routers import default

        blueprint = Blueprint('foo', __name__)

        routes = [
            default.Blueprint(blueprint)
        ]

    """

    def __init__(
            self,
            name_or_instance,
            module=None,
            routes_module_name='routes',
            routes_name=None,
            static_folder=None,
            static_url_path=None,
            template_folder=None,
            url_prefix=None,
            subdomain=None,
            url_defaults=None):
        """ Constructor for blueprint router.

        .. versionchanged:: 2014.05.19

            * Replaced ``name`` with ``name_or_instance`` argument which allows
              the router to take an already instantiated blueprint instance.
            * ``module`` argument optional when instance is passed as the
              first argument
            * ``routes_name`` keyword argument default value set to ``None``

        Arguments
        ---------
        name : str, flask.blueprints.Blueprint
            Blueprint name or a Blueprint class instance

        Keyword Arguments
        -----------------
        module : str
            Python dotted path to the blueprint module
        routes_module_name : str, optional
            The module ``Flask-Via`` will look for within the blueprint module
            which contains the routes, defaults to ``routes``
        routes_name : str, optional
            Name of the variable holding the routes in the module, defaults to
            ``None``
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

        if isinstance(name_or_instance, FlaskBlueprint):
            self.instance = name_or_instance
            self.endpoint = self.instance.name
            self.module = self.instance.import_name
        else:
            self.endpoint = name_or_instance
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

    def blueprint(self, **kwargs):
        """ Returns a Flask Blueprint instance, either one provided or created
        here.

        .. versionchanged:: 2014.05.19

            * Renamed method from ``create_blueprint`` to ``blueprint``
            * If ``instance`` attribute exists, use this is as the blueprint
              else create the blueprint.
            * Support for endpoint prefixing

        Returns
        -------
        flask.blueprints.Blueprint
            An instantiated Flask Blueprint instance
        """

        try:
            blueprint = self.instance
        except AttributeError:

            #: If this route was included a url preifx may have been passed
            #: to the route
            if 'url_prefix' in kwargs:
                url_prefix = self.url_prefix or ''
                self.url_prefix = kwargs['url_prefix'] + url_prefix

            #: If this route was included a endpoint prefix may have been
            #: passed to the route
            if 'endpoint' in kwargs:
                endpoint = self.endpoint or ''
                self.endpoint = kwargs['endpoint'] + endpoint

            blueprint = FlaskBlueprint(
                self.endpoint,
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
        blueprint = self.blueprint(**kwargs)

        # Routes name can be configured by setting VIA_ROUTES_NAME
        if not self.routes_name:
            self.routes_name = app.config.get('VIA_ROUTES_NAME', 'routes')

        # Get the routes
        routes = self.include(self.routes_module, self.routes_name)

        # Load the routes
        self.load(blueprint, routes)

        # Register the blueprint with the application
        app.register_blueprint(blueprint)
