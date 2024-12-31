.. _philosophy:

###############
Why `madcubapy`
###############

MADCUBA products (Why madcubapy exists)
=======================================

The vision for this package is to facilitate working with MADCUBA exported
files. 

Instead of writing history into header cards when saving a FITS file, MADCUBA
works with an external :ref:`history file <hist_file>` where details for every
operation are stored.
With `madcubapy` we can read FITS files with this external history information
into a single object in python.

Development
===========

Most of madcubapy functionality is acquired through astropy.
madcubapy relies on astropy as its base.

Why use madcubapy
=================
Can use .ccddata attribute if incompatibility with madcubamap.
fixes unit strings.
visualizsation helpers can be used with CCDData objects, no need to use
madcubapy io.

To be continued...
