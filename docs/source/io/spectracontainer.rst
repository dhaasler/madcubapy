.. _info_spectracontainer:

################
SpectraContainer
################

The `~madcubapy.io.SpectraContainer` class is a specialized python container for
MADCUBA exported spectra. MADCUBA exports spectra as a **.spec** archive,
containing FITS files alongside their :ref:`history files<hist_file>`. With this
class, the user can easily read spectra data from MADCUBA, perform a series
of operations on them, or quickly plot them.

Overview
========

Core Attributes
---------------

The `~madcubapy.io.SpectraContainer` class stores FITS information in several
attributes:

- ``bintable``: Table containing the spectra data.
- ``hist``: Stores information from MADCUBA's :ref:`history file<hist_file>`.
- ``filename``: Filename of the **.spec** file. Used for tracking several
  operations performed on the file.

Examples
^^^^^^^^
    
Create an instance:

    >>> from madcubapy.io import SpectraContainer
    >>> spectracontainer = SpectraContainer.read("example_file.spec")

To access the spectra data we can call the ``bintable`` attribute:

    >>> spectracontainer.bintable

The history information is present in the ``hist`` attribute:

    >>> spectracontainer.hist

.. For a fully fledged example on how to work with a SpectraContainer object, check
.. the begginer's tutorial on how to read and plot **.spec** files using
.. `~madcubapy.io.SpectraContainer`.

Quality-of-Life Features
------------------------

The `~madcubapy.io.SpectraContainer` class introduces methods and functions to
facilitate working with the data.

* **Creation of spectral axis**

  * The headers of the spectra usually contain arrays for the Y axis of the data
    with the corresponding units, but not for the X axis. 
    When reading a **.spec** file, the program automatically creates this axis.

* **Extensibility**

  * New features will continue to be added, enhancing its capabilities for
    **.spec** file workflows.
