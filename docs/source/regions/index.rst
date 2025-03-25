#######
Regions
#######

The `madcubapy.regions` package contains functions to import and export Regions
of Interest (RoIs) using `matplotlib.patches`.

.. note::
    The astropy `regions <https://astropy-regions.readthedocs.io/en/stable/>`_
    package is a great tool to work with RoIs (except
    `MADCUBA <https://cab.inta-csic.es/madcuba/>`_ and `madcubapy` rois).
    
    However, to code the RoI Tools into MADCUBA, I had to write parser
    functions from scratch in ImageJ, and converting those functions to python
    was easy and straightforward.
    I leave the `madcubapy.regions` package as is. In a future release I will
    very likely change the code to use the astropy 
    `regions <https://astropy-regions.readthedocs.io/en/stable/>`_ package.


:ref:`Import & Export RoIs <import_and_export_rois>`
====================================================


:ref:`Working with contours <contours>`
=======================================


.. toctree::
    :maxdepth: 1
    :includehidden:
    :hidden:

    import_export_rois
    contours

API Reference
=============

.. toctree::
    :maxdepth: 1
    :includehidden:

    ref_api
