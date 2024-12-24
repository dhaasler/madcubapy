"""
Read MadcubaMap
###################

Example showing how to read a fits map file as a
`~madcubapy.io.madcubamap.MadcubaMap`.

.. note::
    Due to how MADCUBA saves some fits header cards, several astropy warnings
    can pop up when reading fits files. Usually these warnings are unexpected
    card names using non-standard conventions.

"""

from madcubapy.io import MadcubaMap

# Read fits file
madcuba_map = MadcubaMap.read("../data/IRAS16293_SO_2-1_moment0_madcuba.fits")
