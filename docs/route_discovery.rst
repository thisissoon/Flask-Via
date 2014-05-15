Route Discovery
===============

Routes can live anywhere you want them too, as long as they are importable.

You can tell ``Flask-Via`` where to find routes in a couple of ways:

1. ``VIA_ROUTES_MODULE`` application configuration variable
2. ``routes_module`` argument passed into ``init_app`` in your application
   factory method.

You can use which ever you prefer.

Using Application Config
------------------------

.. sourcecode:: python

    from flask import Flask
    from flask.ext.via import Via

    app = Flask(__name__)
    app.config['VIA_ROUTES_MODULE'] = 'yourapp.routes'

    via = Via()
    via.init_app(app)

    if __name__ == "__main__":
        app.run(debug=True)

Using ``init_app`` setting ``routes_module``
--------------------------------------------

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

The routes module should define a ``list`` of routes, by default this list
is called ``routes``::

    routes = [
        Basic('/', home),
        Basic('/about', about),
    ]

You can configure ``Flask-Via`` to look for any variable name of your choosing,
this is done by passing an argument named ``routes_name`` into ``init_app``,
for example::

    via = Via()
    via.init_app(app, routes_name='urls')

You can also make this setting permanent by using the ``VIA_ROUTES_NAME``
configuration variable::

    app = Flask(__name__)
    app.config['VIA_ROUTES_MODULE'] = 'yourapp.routes'
    app.config['VIA_ROUTES_NAME'] = 'urls'

    via = Via()
    via.init_app(app)

.. note::

    If you set ``VIA_ROUTES_NAME`` overriding this using ``routes_name`` is
    still possible however this does not propagate over any routes which are
    included.

Application Example
-------------------

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
