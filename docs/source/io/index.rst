##########
MADCUBA IO
##########

The `madcubapy.io` package allows the user to read MADCUBA products like FITS
and *.spec* files alongside their :ref:`history files <hist_file>`.

MadcubaMap
==========

.. toctree::
    :maxdepth: 1
    :hidden:

    madcubamap

The `~madcubapy.io.madcubamap.MadcubaMap` class stores the data and metadata of
FITS files. This class resembles a `~astropy.nddata.CCDData` class with the
addition of a ``hist`` attribute containing the history information of the FITS
file.

The preferred method of creating a `~madcubapy.io.madcubamap.MadcubaMap`
instance is to read a FITS file through the
:meth:`~madcubapy.io.madcubamap.MadcubaMap.read` method, although it can also be
created by passing any of the following parameters from an astropy
`~astropy.nddata.CCDData` object: ``data``, ``header``, ``wcs``, and ``unit``.
 
Look into the :ref:`MadcubaMap page <info_madcubamap>` for a detailed overview
of the class, its attributes and its methods.

SpectraContainer
================

.. toctree::
    :maxdepth: 1
    :hidden:

    spectracontainer

The purpose of the `~madcubapy.io.spectracontainer.SpectraContainer` class is
storing spectra data exported by MADCUBA in **.spec** format. These **.spec**
archives contain astronomical spectra inside a FITS bintable, alongside the
history file. The `~madcubapy.io.spectracontainer.SpectraContainer` class stores
this data in the ``bintable``, and ``hist`` attributes respectively.

The preferred method of creating a
`~madcubapy.io.spectracontainer.SpectraContainer` instance is to read a
**.spec** file through the
:meth:`~madcubapy.io.spectracontainer.SpectraContainer.read`
method, although it can also be created by passing a ``bintable`` in an astropy
`~astropy.table.Table` format.

Look into the :ref:`SpectraContainer page <info_spectracontainer>` for a
detailed overview of the class, and its attributes and methods.

API Reference
=============

.. toctree::
    :maxdepth: 2

    ref_api
