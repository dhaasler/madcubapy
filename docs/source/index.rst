.. madcubapy documentation master file, created by
   sphinx-quickstart on Mon Nov 25 10:03:51 2024.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

MADCUBApy documentation
#######################

``madcubapy`` is a package developed to work with MADCUBA products to quickly
access their data in python. 

`MADCUBA <https://cab.inta-csic.es/madcuba/>`_ is a software developed in the
spanish Center of Astrobiology (CSIC-INTA) to analyze astronomical datacubes,
and is built using the ImageJ infrastructure.

Instead of writing history into new header cards, MADCUBA creates a history file
with the same name as the fits name followed by *_hist.csv*. 
With ``madcubapy`` we can read fits files with this external history information
into a single object in python.


This is the main page of the documentation for the `madcubapy` package.

.. toctree::
   :maxdepth: 1
   :caption: Contents:

   madcubapy
