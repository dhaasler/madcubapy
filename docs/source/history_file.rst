.. _hist_file:

################
The History file
################

The key difference between MADCUBA exported cubes and spectra, and those exported
by other programs is how history is written into the files. Instead of writing
the new history into new header cards, MADCUBA opts for an external
history file that contains every operation performed on the
data since first imported into MADCUBA.

This file has the same name as the FITS name followed by *_hist.csv*. 
With `madcubapy` we can read FITS files with this external history information
into a single object in python.

.. Instead of writing history into new header cards, MADCUBA creates a history file
.. with the same name as the FITS name followed by *_hist.csv*. 
.. With `madcubapy` we can read FITS files with this external history information
.. into a single object in python.

To be continued...
