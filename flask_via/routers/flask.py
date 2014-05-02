# -*- coding: utf-8 -*-

"""
flask_via.routers.flask
=======================

A set of flask specific router classes to be used when defining routes.

Example
-------

from flask.ext.via.routes.flask import Basic, Pluggable
from yourapp.views import BarView, foo_view

routes = [
    Basic('/foo', 'foo', foo_view),
    Pluggable('/bar', view_func=BarView.as_view('bar')),
]

"""

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

        app.add_url_rule(self.url, **self.kwargs)
