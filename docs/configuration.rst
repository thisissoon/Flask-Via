Configuration
-------------

The following configuration variables can be set in your flask application
config.

.. tabularcolumns:: |p{6.5cm}|p{8.5cm}|

================================= =========================================
``VIA_ROUTES_MODULE``             This should be a string with the value
                                  of a python dotted path to your root module
                                  which contains routes, e.g::

                                      VIA_ROUTES_MODULE = 'yourapp.routes'

``VIA_ROUTES_NAME``               By default Via will look for a variable
                                  called ``routes`` within the routes module,
                                  if you want to call it something different
                                  then use this config variable, e.g::

                                      VIA_ROUTES_NAME = 'urls'
================================= =========================================
