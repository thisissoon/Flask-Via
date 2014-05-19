Change Log
==========

2014.05.19
----------
* Feature: ``Include`` now supports ``endpoint`` prefixing
* Feature: Blueprint router can now take a blueprint instance
* Feature: Added support for ``VIA_ROUTES_NAME`` to set a common routes name
* Deprecated: ``Basic`` Router in favour of the ``Functional`` router
* Improved: ``Pluggable`` Router API is now cleaner
* Improved: Test Suite now uses PyTest
* Improved: ``ImproperlyConfigured`` now raised if routes module is not defined
  in either ``init_app`` or in application configuration via
  ``VIA_ROUTES_MODULE``

2014.05.08
----------
* Feature: Flask Admin Router
* Feature: Include ``url_prefix`` option

2014.05.06
----------
* Feature: Flask extension initialisation
* Feature: Basic and Pluggable Flask Routers
* Feature: Flask-Restful Router
* Feature: Ability to include other routes
* Feature: Ability to register blueprints
