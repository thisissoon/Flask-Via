Routers
=======

Here you will find the documentation for each bundled router provided by
``Flask-Via``.

Flask Routers
-------------

These routers are designed to work with standard flask functional and class
based pluggable views.

Basic Router
~~~~~~~~~~~~

The :py:class:`flask_via.routers.flask.Basic` router handles basic functional
based view routing.

**Arguments**:
    * ``url``: The url for this route, e.g: ``/foo``
    * ``func``: The view function

**Keyword Arguments**:
    * ``endpoint``: (Optional) A custom endpoint name, by default flask uses
      the view function name.

Example
^^^^^^^

.. sourcecode:: python

    from flask.ext.via.routers.flask import Basic

    def foo(bar=None):
        return 'foo'

    routes = [
        Basic('/', foo),
        Basic('/<bar>', foo, endpoint='foobar'),
    ]

Pluggable Router
~~~~~~~~~~~~~~~~

The :py:class:`flask_via.routers.flask.Pluggable` router handles views created
using Flasks pluggable views.

**Arguments**:
    * ``url``: The url for this route, e.g: ``/foo``

**Keyword Arguments**:
    * ``view_func``: View function

Example
^^^^^^^

.. sourcecode:: python

    from flask.views import MethodView
    from flask.ext.via.routers.flask import Pluggable

    class FooView(MethodView):

        def get(self, bar=None):
            return 'foo'

    routes = [
        Plugganle('/', view_func=FooView.as_view('foo')),
        Plugganle('/<bar>', view_func=FooView.as_view('foobar')),
    ]

``Flask-Restful`` Routers
-------------------------

``Flask-Restful`` is an awesome framework for building REST API's in Flask but
has it's own way of adding routes to the Flask application, so tere is a little
bit of extra work required when bootstrapping your application:

.. sourcecode:: python
    :linenos:
    :emphasize-lines: 12

    from flask import Flask
    from flask.ext import restful
    from flask.ext.via import Via

    app = Flask(__name__)
    api = restful.Api(app)

    via = Via()
    via.init_app(
        app,
        routes_module='yourapp.routes',
        restful_api=api)

    if __name__ == '__main__':
        app.run(debug=True)

Note that on line ``12`` we passed a keyword argument called ``restful_api``
with the value being the ``Flask-Restful`` api object into ``via.init_app``.
This will allow the :py:class:`flask_via.routers.restful.Resource` router to
add resouce routes to the api.

Resouce Router
~~~~~~~~~~~~~~

.. warning::
    Before using this router be sure you have read the section directly above.

The :py:class:`flask_via.routers.restful.Resource` router allows us to register
``Flask-Restful`` resources to our application.

**Arguments**:
    * ``url``: The url for this route, e.g: ``/foo``
    * ``resource``: A ``Flask-Restful`` ``Resource`` class

**Keyword Arguments**:
    * ``endpoint``: (Optional) A custom endpoint name

Example
^^^^^^^

.. sourcecode:: python

    class FooResource(restful.Resource):

        def get(self, bar=None):
            return {'hello': 'world'}

    routes = [
        Resource('/', FooResource)
        Resource('/<bar>', FooResource, endpoint='foobar')
    ]
