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
