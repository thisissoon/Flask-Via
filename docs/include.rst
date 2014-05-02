Including
=========

Sometimes you don't want to define all your routes in one place, you want to be
modular right!? You can do that too with ``Flask-Via``.

Basic Include Router
--------------------

The most basic way of including other routes is to use the
:py:class:`flask_via.routes.Include` router. This is not a intended replacement
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

    from flask.ext.via.routes import flask
    from foo.bar.views import some_view

    routes = [
        flask.Basic('/bar', some_view)
    ]

You can see this in action with the
`Small Application Example <https://github.com/thisissoon/Flask-Via/tree/master/flask_via/examples/small>`_.
