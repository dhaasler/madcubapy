"""
.. _example_read_map:

Read MadcubaMap
###################

Example showing how to read a fits map file as a
`~madcubapy.io.madcubamap.MadcubaMap`.

.. note::
    Due to how MADCUBA saves some fits header cards, several astropy warnings
    can pop up when reading fits files. Usually these warnings are unexpected
    card names using non-standard conventions.

"""

# sphinx_gallery_start_ignore
# Do not show warnings in example page. A note tells the user what to expect
# regarding warnings. 
import warnings
from astropy.utils.exceptions import AstropyWarning
warnings.filterwarnings('ignore', category=AstropyWarning)
# sphinx_gallery_end_ignore

from madcubapy.io import MadcubaMap

# Read fits file
madcuba_map = MadcubaMap.read("../data/IRAS16293_SO_2-1_moment0_madcuba.fits")
