Including
=========

Sometimes you don't want to define all your routes in one place, you want to be
modular right!? You can do that too with ``Flask-Via``.

Include Router
--------------

The most basic way of including other routes is to use the
:py:class:`flask_via.routers.Include` router. This is not a intended replacement
or implementation of Flask blueprints, just a simple way of putting routes
somewhere else in your application.

**Arguments**:
    * ``routes_module``: Python dotted path to the route module as a string.

**Keyword Arguments**:
    * ``routes_name``: (Optional) If you have not called the list of routes in
      the moduke ``routes`` you can set that here, for example ``urls``.

Example
~~~~~~~

Assume the following application structure::

    /path/to/foo
        - bar/
            - __init__.py
            - routes.py
            - views.py
        - __int__.py
        - routes.py

In the top level ``routes.py`` we would have::

    from flask.ext.via.routers import Include

    routes = [
        Include('foo.bar.routes')
    ]

In the ``foo.routes`` we would have::

    from flask.ext.via.routes import default
    from foo.bar.views import some_view

    routes = [
        default.Basic('/bar', some_view)
    ]

You can see this in action with the
`Small Application Example <https://github.com/thisissoon/Flask-Via/tree/master/flask_via/examples/small>`_.

Blueprint Router
----------------

Flask Blueprints are also supported allowing ``Flask-Via`` to automatically
register blueprints on the application and routes on the blueprint, this is
provided by the :py:class:`flask_via.routers.default.Blueprint` router.

**Arguments**:
    * ``name`` : Blueprint name
    * ``module``: Python module path to blueprint module

**Keyword Arguments**:
    * ``routes_module_name``: The module ``Flask-Via`` will look for within
      the blueprint module which contains the routes, defaults to ``routes``
    * ``routes_name``: If you have not called the list of routes in
      the module ``routes`` you can set that here, for example ``urls``.
    * ``static_folder``: Path to static files for blueprint, defaults to ``None``
    * ``static_url_path``: URL path for blueprint static files,
      defaults to ``None``
    * ``template_folder``: Templates folder name, defaults to ``None``
    * ``url_prefix``: URL prefix for routes served within the blueprint,
      defaults to ``None``
    * ``subdomain`` : Sub domain for blueprint, defaults to ``None``
    * ``url_defaults``: Callback function for URL defaults for this blueprint.
      It's called with the endpoint and values and should update
      the values passed in place, defaults to ``None``.

Example
~~~~~~~

Let us assume we have the following application structure::

    /path/to/foo
        - bar/
            - templates/
                - foo.html
            - __init__.py
            - routes.py
            - views.py
        - __int__.py
        - routes.py

In the above structure ``bar`` is a Flask blueprint which we wish to add to our
flask application, so our top level routes would look like this::

    from flask.ext.via.routers.default import Blueprint

    routes = [
        Blueprint('bar', 'foo.bar', template_folder='templates')
    ]

You will note we give the blueprint a name and pass the top level module path
to the blueprint rather than a path to the routes file.

In our blueprints views we can define routes as normal::

    from flask.ext.via.routes import default
    from foo.bar.views import some_view

    routes = [
        default.Basic('/bar', some_view)
    ]

.. note::
    All routes will be added to the blueprint rather than the flask
    application, this applies to any routes included using the ``Include``
    router.
