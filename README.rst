``Flask-Via``
=============

Inspired by Django's URL configuration ``Flask-Via`` is designed to add similar
functionality for Flask applications that are goriwng beyind that simple single
file application.

|travis_master| |coveralls_master| |PyPi_version| |PyPi_downloads|

Example
-------

.. sourcecode:: python

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
    via.init_app(app, route_module='flask_via.examples.basic')

    if __name__ == "__main__":
        app.run(debug=True)

Why?
----

Growing your application can be quite hard and not always clear where and how
your routes are discovered. It can lead to a cluttered application factory
method where you define all your routes at application creation and this is
hard to maintain and not to mention messy.

A better way would be to define your routes on a ``routes.py`` and
automatically load them at application start up, this is what ``Flask-Via``
helps to do.

Third party Flask extensions don't always follow the same conventions for
adding routes to an application so ``Flask-Via`` has been designed to be easy
for developers to write their own custom routers, for example take a look at
the bundled ``Flask-Restful`` resource router: http://flask-via.thisissoon.com/en/latest/api.html#flask_via.routers.restful.Resource

If you do write a custom router that is useful to you it is probably be useful
to someone else so please do contribute back :)

Links
-----

* Documentation: http://flask-via.thisissoon.com
* CI: https://travis-ci.org/thisissoon/Flask-Via
* Coverage: https://coveralls.io/r/thisissoon/Flask-Via?branch=master

.. |PyPi_version| image:: https://badge.fury.io/py/Flask-Via.svg
    :target: https://pypi.python.org/pypi/Flask-Via
    :alt: Latest PyPI version

.. |PyPi_downloads| image:: https://pypip.in/download/Flask-Via/badge.png
    :target: https://pypi.python.org/pypi/Flask-Via
    :alt: Number of PyPI downloads

.. |coveralls_master| image:: https://coveralls.io/repos/thisissoon/Flask-Via/badge.png?branch=master
    :target: https://coveralls.io/r/thisissoon/Flask-Via?branch=master
    :alt: Test Coverage

.. |travis_master| image:: https://travis-ci.org/thisissoon/Flask-Via.svg?branch=master
    :target: https://travis-ci.org/thisissoon/Flask-Via
    :alt: Travis build status on Master Branch
