# -*- coding: utf-8 -*-

"""
flask_via.examples.admin
========================

A simple ``Flask-Admin`` example Flask application.
"""

from flask import Flask
from flask.ext.admin import Admin
from flask.ext.via import Via
from flask_admin import BaseView, expose
from flask.ext.via.routers.admin import AdminRoute


app = Flask(__name__)

admin = Admin(name='Admin')
admin.init_app(app)


class FooAdminView(BaseView):

    @expose('/')
    def index(self):
        return 'foo'

routes = [
    AdminRoute(FooAdminView(name='Foo'))
]

via = Via()
via.init_app(
    app,
    routes_module='flask_via.examples.admin',
    flask_admin=admin)

if __name__ == '__main__':
    app.run(debug=True)
