``Flask-Via``
=============

Inspired by the Django URL configuration system, ``Flask-Via`` is designed to
add similar functionality to Flask applications which have grown beyond a
simple single file application.

|travis_master| |coveralls_master| |health| |PyPi_version| |PyPi_downloads|
|license|

Example
-------

.. sourcecode:: python

    from flask import Flask
    from flask.ext.via import Via
    from flask.ext.via.routers.default import Functional

    app = Flask(__name__)

    def foo(bar=None):
        return 'Foo View!'

    routes = [
        Functional('/foo', foo),
        Functional('/foo/<bar>', foo, endpoint='foo2'),
    ]

    via = Via()
    via.init_app(app, route_module='flask_via.examples.basic')

    if __name__ == "__main__":
        app.run(debug=True)

Why?
----

Growing your application can be quite difficult when it's not always clear
where and how your routes are discovered. This can lead to a cluttered
application factory method when all your routes are defined at application
creation - resulting in code which is difficult to maintain, not to mention
messy.

A better solution is to define your routes in a ``routes.py`` and automatically
load them at application start up. This is what ``Flask-Via`` helps to do.

Third party Flask extensions don't always follow the same conventions for
adding routes to an application, so ``Flask-Via`` has been designed to be easy
for developers to write their own custom routers. For an example of this, take
a look at the bundled ``Flask-Restful`` Resource_ router.

If you do write a custom router that is useful to you, it will probably be
useful to someone else so please do contribute back :)

Links
-----

* Documentation: http://flask-via.thisissoon.com
* CI: https://travis-ci.org/thisissoon/Flask-Via
* Coverage: https://coveralls.io/r/thisissoon/Flask-Via?branch=master

.. |PyPi_version| image:: https://pypip.in/version/Flask-Via/badge.svg
    :target: https://pypi.python.org/pypi/Flask-Via
    :alt: Latest PyPI version

.. |PyPi_downloads| image:: https://pypip.in/download/Flask-Via/badge.svg?period=month
    :target: https://pypi.python.org/pypi/Flask-Via
    :alt: Number of PyPI downloads

.. |license| image:: https://pypip.in/license/Flask-Via/badge.svg
    :target: https://pypi.python.org/pypi/Flask-Via
    :alt: MIT License

.. |coveralls_master| image:: https://coveralls.io/repos/thisissoon/Flask-Via/badge.png?branch=master
    :target: https://coveralls.io/r/thisissoon/Flask-Via?branch=master
    :alt: Test Coverage

.. |travis_master| image:: https://travis-ci.org/thisissoon/Flask-Via.svg?branch=master
    :target: https://travis-ci.org/thisissoon/Flask-Via
    :alt: Travis build status on Master Branch

.. |health| image:: https://landscape.io/github/thisissoon/Flask-Via/master/landscape.png
   :target: https://landscape.io/github/thisissoon/Flask-Via/master
   :alt: Code Health

.. _Resource: http://flask-via.thisissoon.com/en/latest/api.html#flask_via.routers.restful.Resource
