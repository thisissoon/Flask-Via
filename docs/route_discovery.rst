Route Discovery
===============

Your routes need to live somewhere and they can live anywhere you want them to
but they need to be importable by python so ``Flask-Via`` can load them in at
application start up.

You can tell ``Flask-Via`` where to find routes in a couple of ways:

1. ``VIA_ROUTES_MODULE`` application configuration variable
2. ``routes_module`` argument passed into ``init_app`` in your application
   factory method.

Use which ever you prefer:

Example 1
---------

.. sourcecode:: python

    from flask import Flask
    from flask.ext.via import Via

    app = Flask(__name__)
    app.config['VIA_ROUTES_MODULE'] = 'yourapp.routes'

    via = Via()
    via.init_app(app)

    if __name__ == "__main__":
        app.run(debug=True)

Example 2
---------

.. sourcecode:: python

    from flask import Flask
    from flask.ext.via import Via

    app = Flask(__name__)

    via = Via()
    via.init_app(app, routes_module='yourapp.routes')

    if __name__ == "__main__":
        app.run(debug=True)

Route Module
------------

All the route module needs to do is define a list of routes, by default this
list should be called ``routes`` but as with how the module is discovered you
can change this too by passing the ``routes_name`` keyword argument into
``init_app`` at application start up.

Assume we have the following application structure::

    /path/to/foo
        - __init__.py
        - routes.py
        - views.py
        - app.py

Within ``views.py`` we have::

    def home():
        return 'Hello world!'

    def about():
        return 'The world is big'

Within ``routes.py`` we have::

    from flask.ext.via.routers import default

    urls = [
        default.Basic('/', home),
        default.Basic('/about', about),
    ]

Within ``app.py`` we have::

    from flask import Flask
    from flask.ext.via import Via

    app = Flask(__name__)
    app.config['VIA_ROUTES_MODULE'] = 'foo.routes'

    via = Via()
    via.init_app(app, routes_name='urls')

    if __name__ == "__main__":
        app.run(debug=True)

You will see we used ``routes_name`` when calling ``via.init_app`` to tell
``Via`` what variable to look for within the routes module.
