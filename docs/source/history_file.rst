.. _hist_file:

################
The History file
################

MADCUBA handles data differently compared to other programs by separating the
history of operations from the FITS file headers. Instead of writing new history
records as header cards in the FITS file, MADCUBA creates a dedicated
**history file** to store all operations performed on the data.

`madcubapy` was created to help the user read FITS files alongside this external
history information with ease in Python.

Key Characteristics of the History File
=======================================

- **Name**: The history file shares the same base name as the FITS file, with
  the suffix `_hist.csv`.  
  Example: For `data_cube.fits`, the history file is `data_cube_hist.csv`.
- **Content**: It contains a chronological record of every operation applied to
  the data since its import into MADCUBA.

How madcubapy Integrates the History File
=========================================

`madcubapy` simplifies the workflow by merging the FITS file and its
corresponding history file into a unified Python object. This integration
ensures:

- Easy access to both data and its processing history.
- Seamless compatibility with Astropy-based workflows.
- Improved efficiency in managing and analyzing MADCUBA-exported files.

For more details on madcubapy's functionality, check the
:ref:`Examples Gallery <examples>` or explore the :ref:`Tutorials <tutorials>`.
