=====
Usage
=====

To use PharmCRM2 Sales in a project, add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'sales.apps.SalesConfig',
        ...
    )

Add PharmCRM2 Sales's URL patterns:

.. code-block:: python

    from sales import urls as sales_urls


    urlpatterns = [
        ...
        url(r'^', include(sales_urls)),
        ...
    ]
