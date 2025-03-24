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

Import RoIs
===========

Using :func:`madcubapy.regions.import_roi` the user can import RoIS from
datafiles exported by other astronomical programs. The supported formats are:

- `MADCUBA <https://cab.inta-csic.es/madcuba/>`_ (.mcroi)
- `CASA <https://casa.nrao.edu>`_ and `CARTA <https://cartavis.org>`_ (.crtf)
- `DS9 <https://sites.google.com/cfa.harvard.edu/saoimageds9>`_ (.ds9)
- Custom `madcubapy` format (.pyroi)

The RoIs are imported as `matplotlib.patches` that can be added to an
`~matplotlib.axes.Axes` or `~astropy.visualization.wcsaxes.WCSAxes` object.
The functions accept *kwargs* that are passed for the creation of the
`~matplotlib.patches.Patch`.

The user needs to provide a
`~astropy.nddata.CCDData` or `~madcubapy.io.MadcubaMap` object through the
``fitsmap`` parameter if the RoI has been stored using World coordinates
instead of Image coordinates (pixels).

.. code-block:: python

    >>> ds9_rectangle = import_roi(input_file="rectangle-world.ds9",
                                   fitsmap=example_map,
                                   color='blue', alpha=0.7)

For a complete example on how to import and plot a RoI using `madcubapy` check
the :ref:`Import RoIs <example_import_region>` example.

Export RoIs
===========

The :func:`madcubapy.regions.export_roi` allows users to export
`~matplotlib.patches.Patch` objects as datafiles that can be imported in other
astronomy programs. Supported formats for output of RoIs are:

- PYROI (can be imported into `MADCUBA <https://cab.inta-csic.es/madcuba/>`_
  and `madcubapy`).
- CRTF (can be improted into `MADCUBA <https://cab.inta-csic.es/madcuba/>`_, 
  `CARTA <https://cartavis.org>`_,
  `DS9 <https://sites.google.com/cfa.harvard.edu/saoimageds9>`_, 
  and `madcubapy`)

The user must select the desired file format and coordinate frame through the
``format`` and ``coord_frame`` parameters, respectively.

.. code-block:: python

    >>> export_roi(circle_patch,
                   output="circle-world.crtf",
                   format="crtf",
                   coord_frame="world",
                   fitsmap=example_map)

.. note::
    For world coordinates, only ICRS is currently supported. More will be added
    in the future through the ``coord_system`` parameter.

API Reference
=============

.. toctree::
    :maxdepth: 1
    :includehidden:

    ref_api
