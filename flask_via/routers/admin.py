# -*- coding: utf-8 -*-

"""
flask_via.routers.admin
-----------------------

Routers for the Flask-Admin framework.
"""

from flask_via.routers import BaseRouter


class AdminRoute(BaseRouter):
    """ The Admin router allows you to define Flask-Admin routes and have
    those views added to the application automatically. For this to
    work you must at ``init_app`` time pass a optional keyword argument
    ``flask_admin`` to ``init_app`` with its value being the Flask-Aadmin
    extension instance.

    .. versionadded:: 2014.05.08

    Note
    ----
    ``Flask-Admin`` has its own way of handling defining urls so this router
    literally only requires the ``Flask-Admin`` view class.

    Example
    -------
    .. sourcecode:: python

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
    """

    def __init__(self, view):
        """ Admin route constructor, this router handles adding ``Flask-admin``
        views to the application.

        Arguments
        ---------
        view : flask_admin.base.AdminViewMeta
            The Flask Admin View Class
        """

        self.view = view

    def add_to_app(self, app, **kwargs):
        """ Adds the ``Flask-Admin`` View to the Flask the application.

        Arguments
        ---------
        app : flask.app.Flask
            Flask application instance, this is ignored.
        \*\*kwargs
            Arbitrary keyword arguments

        Raises
        ------
        NotImplementedError
            If ``flask_admin`` is not provided
        """

        try:
            admin = kwargs['flask_admin']
        except KeyError:
            raise NotImplementedError(
                'flask_admin not passed to add_to_app, did you add it to '
                'via.init_app?')

        admin.add_view(self.view)
