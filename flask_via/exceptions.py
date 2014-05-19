# -*- coding: utf-8 -*-

"""
flask_via.exceptions
--------------------

Custom exceptions which can be thrown by ``Flask-Via``.
"""


class ImproperlyConfigured(Exception):
    """ Raised in the event ``Flask-Via`` has not been properly configured

    .. versionadded: 2014.05.19
    """

    pass
