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
    * ``url_prefix``: (optional) Add a url prefix to all routes included
    * ``endpoint``: (optional) Add a endpoint prefix to all routes included

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
        default.Functional('/bar', some_view)
    ]

You can see this in action with the
`Small Application Example <https://github.com/thisissoon/Flask-Via/tree/master/flask_via/examples/small>`_.

URL Prefixes
~~~~~~~~~~~~

The :py:class:`flask_via.routers.Include` class also allows you to add a
``url_prefix`` similar to blueprints.

The following routers support the ``url_prefix`` being passed to their
``add_to_app`` methods:

* :py:class:`flask_via.routers.default.Functional`
* :py:class:`flask_via.routers.default.Pluggable`
* :py:class:`flask_via.routers.default.Blueprint`

Example
^^^^^^^

Assume the same application structure as in the above examples except the
top level ``routes.py`` now looks like this::

    from flask.ext.via.routers import Include

    routes = [
        Include('foo.bar.routes', url_prefix='/foo')
    ]

This will result in the url to the view becoming ``/foo/bar`` instead of
``/bar``.

Endpoints
~~~~~~~~~

The :py:class:`flask_via.routers.Include` router also allows you to add
endpoint prefixes to your included routes, much like blueprints. This is
supported by:

* :py:class:`flask_via.routers.default.Functional`
* :py:class:`flask_via.routers.default.Pluggable`
* :py:class:`flask_via.routers.default.Blueprint`

Example
^^^^^^^

We will assume the same application structure as we have in the previous
example applications. The top level ``routes.py`` can be altered as followes::

    from flask.ext.via.routers import Include

    routes = [
        Include('foo.bar.routes', url_prefix='/foo', endpoint='foo')
    ]

We can now call ``url_for`` with ``foo.bar`` which would generate ``/foo/bar``.

Blueprint Router
----------------

Flask Blueprints are also supported allowing ``Flask-Via``.

You can either let ``Flask-Via`` automatically create and register your
blueprint or create an instance of your blueprint and pass that to the
Blueprint router.

.. seealso::

    * :py:class:`flask_via.routers.default.Blueprint`.

.. note::

    All routes will be added to the blueprint rather than the flask
    application, this applies to any routes included using the ``Include``
    router.

**Arguments**:
    * ``name_or_instance``: A Blueprint name or a Blueprint instance

**Keyword Arguments**:
    * ``module``: Python module path to blueprint module, defaults to ``None``
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

Automatic Example
~~~~~~~~~~~~~~~~~

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
        default.Functional('/bar', some_view)
    ]

Instance Example
~~~~~~~~~~~~~~~~

If you do not wish ``Flask-Via`` to automatically create the Blueprint instance
you can pass a Blueprint instance as the first and only argument into the.

In the above example we would alter the contents of
``/path/to/foo/bar/routes.py`` as follows::

    from flask import Blueprint
    from flask.ext.via.routes import default
    from foo.bar.views import some_view

    blueprint = Blueprint('bar', 'foo.bar', template_folder='templates')

    routes = [
        default.Functional('/bar', some_view)
    ]

And now in our ``/path/to/foo/routes.py`` we would import the blueprint and
pass it into the router::

    from foo.bar.routes import blueprint
    from flask.ext.via.routers.default import Blueprint

    routes = [
        Blueprint(blueprint)
    ]

Of course you can crate your Blueprint instance where ever you wish.

Including Blueprints
~~~~~~~~~~~~~~~~~~~~

You can use the :py:class:`flask_via.routers.Include` router to also include
blueprints, you can even add ``url_prefix`` to prefix the blueprints
``url_prefix``, crazy eh?

Example
^^^^^^^

Let us assume we have the same application structure as in the earlier
blueprint examples, except our top level ``routes.py`` now looks like this::

    from flask.ext.via.routers import default, Include

    routes = [
        Include(
            'foo.routes',
            routes_name='api',
            url_prefix='/api/v1',
            endpoint='api.v1')
    ]

    api = [
        default.Blueprint('bar', 'foo.bar', url_prefix='/bar')
        # These don't exist but just for illustraion purposes
        default.Blueprint('baz', 'foo.baz', url_prefix'/baz')
        default.Blueprint('fap', 'foo.fap', url_prefix'/fap')
    ]

Here we will include all the routes defined in the ``api`` list which are all
blueprints, each blueprint will be registered with a ``url_prefix`` of
``/api/v1`` as well their url prefixes for the blueprint, so the above
blueprints will be accessible on the followibg urls:

* ``/api/v1/bar``
* ``/api/v1/baz``
* ``/api/v1/fap``

If each of these blueprints had a route defined with a url of ``/bar`` these
would be accessed on the following urls:

* ``/api/v1/bar/bar``
* ``/api/v1/baz/bar``
* ``/api/v1/fap/bar``

Hopefully you can see from this that :py:class:`flask_via.routers.Include`
coupled with :py:class:`flask_via.routers.default.Blueprint` can offer some
potentially powerful routing options for your application.

You will also notice we used the ``endpoint`` keyword agument in the Include.
This means our urls can also be reversed using ``url_for``, for example::

* ``url_for('api.v1.bar.bar')`` would return: ``/api/v1/bar/bar``
* ``url_for('api.v1.baz.bar')`` would return: ``/api/v1/baz/bar``
* ``url_for('api.v1.fap.bar')`` would return: ``/api/v1/fap/bar``
