=============================
PharmCRM2 Sales
=============================

.. image:: https://badge.fury.io/py/pharmcrm2-sales.svg
    :target: https://badge.fury.io/py/pharmcrm2-sales

.. image:: https://travis-ci.org/dcopm999/pharmcrm2-sales.svg?branch=master
    :target: https://travis-ci.org/dcopm999/pharmcrm2-sales

.. image:: https://codecov.io/gh/dcopm999/pharmcrm2-sales/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/dcopm999/pharmcrm2-sales

PharmCRM2 Sales

Documentation
-------------

The full documentation is at https://pharmcrm2-sales.readthedocs.io.

Quickstart
----------

Install PharmCRM2 Sales::

    pip install pharmcrm2-sales

Add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'sales',
        ...
    )

Add PharmCRM2 Sales's URL patterns:

.. code-block:: python

    urlpatterns = [
        ...
        path('sales/', include('sales.urls')),
        ...
    ]

Features
--------

* TODO

Running Tests
-------------

Does the code actually work?

::

    source <YOURVIRTUALENV>/bin/activate
    (myenv) $ pip install tox
    (myenv) $ tox


Development commands
---------------------

::

    pip install -r requirements_dev.txt
    invoke -l


Credits
-------

Tools used in rendering this package:

*  Cookiecutter_
*  `cookiecutter-djangopackage`_

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cookiecutter-djangopackage`: https://github.com/pydanny/cookiecutter-djangopackage
