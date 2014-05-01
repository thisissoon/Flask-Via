``Flask-Via``
=============

Inspired by Django's URL configuration ``Flask-Via`` is designed to add similar
functionality for Flask applications that are goriwng beyind that simple single
file application.

|PyPi_version| |PyPi_downloads| |travis_master| |coveralls_master|

Example
-------

.. sourcecode:: python

    from flask import Flask
    from flask.ext.via import Via

    app = Flask(__name__)
    app.config['VIA_ROOT'] = 'flask_via.examples.basic'


    def home():
        return 'Hello World!'

    routes = [
        ('/', 'home', home)
    ]

    via = Via()
    via.init_app(app)

    app.run()

.. |PyPi_version| image:: https://pypip.in/version/Flask-Via/badge.png
    :alt: Latest PyPI version

.. |PyPi_downloads| image:: https://pypip.in/download/Flask-Via/badge.png
    :alt: Number of PyPI downloads

.. |coveralls_master| image:: https://coveralls.io/repos/SOON-Dorks/Flask-Via/badge.png?branch=master
    :alt: Test Coverage

.. |travis_master| image:: https://travis-ci.org/thisissoon/Flask-Via.svg?branch=master
    :alt: Travis build status on Master Branch
