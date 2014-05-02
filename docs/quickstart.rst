Quickstart
==========

Installation
------------

``Flask-Via`` is simple to install, just use your favourite python package
manage, for example ``pip``::

    $ pip install Flask-Via

Basic Application
-----------------

Once we have installed ``Flask-Via`` we need to perform the following steps:

1. Create some view functions
2. Create a list of routes
3. Initialise :py:class:`flask_via.Via` and call
   :py:meth:`flask_via.Via.init_app`

The following example code performs the above steps with key lines emphasised.

.. sourcecode:: python
    :linenos:
    :emphasize-lines: 10-13, 16

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
    via.init_app(app, route_module='path.to.here')

    if __name__ == "__main__":
        app.run(debug=True)

Lines ``10-13`` show how routes are defined in a list using the basic flask
router class (:py:class:`flask_via.routers.flask.Basic`).

Line ``16`` shows how we ``Flask-Via`` looks for where routes are defined, this
can be set as we have done above or using the ``VIA_ROUTES_MODULE`` application
configuration variable.
