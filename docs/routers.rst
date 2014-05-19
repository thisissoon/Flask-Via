Routers
=======

Here you will find the documentation for each bundled router provided by
``Flask-Via``.

Flask Routers
-------------

These routers are designed to work with standard flask functional and class
based pluggable views.

Functional Router
~~~~~~~~~~~~~~~~~

The :py:class:`flask_via.routers.default.Functional` router handles basic
functional based view routing.

**Arguments**:
    * ``url``: The url for this route, e.g: ``/foo``
    * ``func``: The view function

**Keyword Arguments**:
    * ``endpoint``: (Optional) A custom endpoint name, by default flask uses
      the view function name.

Example
^^^^^^^

.. sourcecode:: python

    from flask.ext.via.routers.default import Functional

    def foo(bar=None):
        return 'foo'

    routes = [
        Functional('/', foo),
        Functional('/<bar>', foo, endpoint='foobar'),
    ]

Pluggable Router
~~~~~~~~~~~~~~~~

The :py:class:`flask_via.routers.default.Pluggable` router handles views created
using Flasks pluggable views.

**Arguments**:
    * ``url``: The url for this route, e.g: ``/foo``
    * ``class``: The Flask Pluggable View Class
    * ``name``: The name of the view, aka: endpoint

**Keyword Arguments**:
    * ``**kwargs``: Arbitrary keyword arguments, for example ``methods``

Example
^^^^^^^

.. sourcecode:: python

    from flask.views import MethodView
    from flask.ext.via.routers.default import Pluggable

    class FooView(MethodView):

        def get(self, bar=None):
            return 'foo'

    routes = [
        Plugganle('/', FooView, 'foo'),
        Plugganle('/<bar>', FooView, 'foobar'),
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
``Flask-Restful`` resources to your application.

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

``Flask-Admin`` Routers
-----------------------

As with the ``Flask-Restful`` router you need to pass an extra argument to
``via.init_app`` called ``flask_admin`` which should hold the ``Flask-Admin``
instance.

.. sourcecode:: python
    :linenos:
    :emphasize-lines: 14

    from flask import Flask
    from flask.ext.admin import Admin
    from flask.ext.via import Via

    app = Flask(__name__)

    admin = Admin(name='Admin')
    admin.init_app(app)

    via = Via()
    via.init_app(
        app,
        routes_module='flask_via.examples.admin',
        flask_admin=admin)

    if __name__ == '__main__':
        app.run(debug=True)

Note that line ``14`` is where the instantiated ``Flask-Admin`` instance gets
passed into ``via.init_app``.

Admin Router
~~~~~~~~~~~~

.. warning::
    Before using this router be sure you have read the section directly above.

The :py:class:`flask_via.routers.admin.AdminRoute` router allows us to register
``Flask-Admin`` views to your application. ``Flask-Admin`` handles defining
urls for its views so a ``url`` argument is not requied, all is required is
the ``Flask-Admin`` view class.

**Arguments**:
    * ``view``: An instantiated ``Flask-Admin`` view

Example
^^^^^^^

.. sourcecode:: python

    class FooAdminView(BaseView):

        @expose('/')
        def index(self):
            return 'foo'

        @expose('/bar')
        def index(self):
            return 'bar'


    routes = [
        AdminRoute(FooAdminView(name='Foo'))
    ]
