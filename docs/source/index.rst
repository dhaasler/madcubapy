.. madcubapy documentation master file, created by
   sphinx-quickstart on Mon Nov 25 10:03:51 2024.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

madcubapy documentation
#######################

``madcubapy`` is a package developed to work with ``MADCUBA`` products to
quickly access their data in python. 

Instead of writing history into new fits
cards in the header of the file, MADCUBA creates a history file named
`_hist.csv`. With ``madcubapy`` we can read fits files with this external
history information into a single object in python.


.. toctree::
   :maxdepth: 1
   :caption: Contents:

   modules
