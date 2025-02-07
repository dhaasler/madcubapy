.. _info_madcubamap:

##########
MadcubaMap
##########

The `~madcubapy.io.MadcubaMap` class is a specialized container for FITS file
data and metadata, aimed for MADCUBA workflows. While it closely resembles
Astropy's `~astropy.nddata.CCDData` class, it includes additional functionality
that makes it tailored for working with MADCUBA products, but also versatile for
many other FITS workflows.

Overview
========

The `~madcubapy.io.MadcubaMap` class is designed to:

- Integrate FITS file data with metadata, including history from MADCUBA's
  external :ref:`history files<hist_file>`.
- Provide seamless compatibility with Astropy-based workflows by mimicking the
  behavior of `~astropy.nddata.CCDData`.

.. _madcubamap_attributes:

Core Attributes
---------------

The `~madcubapy.io.MadcubaMap` class stores FITS information in
several attributes, some of which are identical to those contained in a 
`~astropy.nddata.CCDData` object:

- ``data``: The array containing the FITS image data.
- ``header``: The FITS header object, storing metadata about the observation.
- ``wcs``: The World Coordinate System (WCS) information for the FITS file.
- ``unit``: The physical unit of the data, derived from the FITS header's
  `BUNIT` keyword.

alongisde additional attributes:

- ``hist``: Stores information from MADCUBA's :ref:`history file<hist_file>`.
- ``filename``: Filename of the FITS file. Used for tracking several operations
  performed on the file.
- ``ccddata``: A `~astropy.nddata.CCDData` object representing the same FITS
  data. Used as a failsafe for incompatibilities with
  `~madcubapy.io.MadcubaMap`.

Examples
^^^^^^^^
    
Create an instance by reading a FITS file through
`MadcubaMap.read() <madcubapy.io.MadcubaMap.read>` (recommended method):

    >>> from madcubapy.io import MadcubaMap
    >>> madcubamap = MadcubaMap.read("example_cube.fits")

.. note::
    Due to how MADCUBA saves some fits header cards, several astropy warnings
    can pop up when reading fits files. Usually these warnings are unexpected
    card names using non-standard conventions.

We can also create an instance manually by providing any attribute stated
:ref:`before <madcubamap_attributes>`, for example:

    >>> import numpy as np
    >>> madcubamap = MadcubaMap(data=np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]]))

To access attributes, the data for example, we can call them directly:

    >>> madcubamap.data

The history information is present in the ``hist`` attribute:

    >>> madcubamap.hist

For a fully fledged example on how to work with a MadcubaMap object, check the
begginer's :ref:`tutorial<tutorial_read_plot_maps>` on how to read and plot FITS
files using `~madcubapy.io.MadcubaMap`.

Compatibility with `~astropy.nddata.CCDData`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The ``ccddata`` attribute provides a failsafe for scenarios where functions are
incompatible with the `~madcubapy.io.MadcubaMap` class.
By accessing this attribute, users can work with a standard
`~astropy.nddata.CCDData` object while retaining access to the original FITS
data:

We can directly use this attribute or set a variable to point to its content:

    >>> ccd = madcubamap.ccddata

Quality-of-Life Features
------------------------

The `~madcubapy.io.MadcubaMap` class also introduces methods and
functions that improve usability and accuracy when working with FITS files
(even non-MADCUBA products):

* **Correction of data unit**

  Fixes improperly formatted units in the `BUNIT` header card, ensuring
  compatibility with Astropy.
  We can tell the program to try to fix the units with the
  :meth:`~madcubapy.io.MadcubaMap.fix_units` method:
 
      >>> madcubamap.fix_units()

* **Noise Level Estimation**

  (**Soon to be implemented**) Automatically calculates and stores the noise
  level of the image, simplifying further analysis.

* **Quick map visualization**
  
  The user can quickly take a look at a map in a pop-up window using:

      >>> madcubamap.show()

* **Extensibility**

  New features will continue to be added, enhancing its capabilities for FITS
  file workflows.

Why Use MadcubaMap?
===================

Advantages Over CCDData
-----------------------

The `~madcubapy.io.MadcubaMap` class provides the following benefits:

- **Integrated History**: Combines FITS data with history files for a unified
  representation.

- **Improved Compatibility**: Fixes common issues in FITS files, such as
  improperly formatted `BUNIT` keywords.

- **Added Functionality**: Built-in features like noise level calculation
  simplify data processing.

Beyond MADCUBA
--------------

While designed for MADCUBA workflows, the `~madcubapy.io.MadcubaMap`
class is suitable for general-purpose FITS file processing. Its features make it
a powerful tool even for FITS files unrelated to MADCUBA.
