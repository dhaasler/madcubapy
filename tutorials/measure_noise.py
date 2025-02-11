"""
.. _tutorial_measure_noise:

Measure noise of a FITS file
############################

Beginner's tutorial showing how to measure the noise of a
`~madcubapy.io.MadcubaMap` object. For a detailed overview go to the
:ref:`documentation page<measure_noise>`.

First we read the FITS file as a MadcubaMap object.

"""

# sphinx_gallery_start_ignore
# Do not show warnings in tutorial page. A note tells the user what to expect
# regarding warnings. 
import warnings
from astropy.utils.exceptions import AstropyWarning
warnings.filterwarnings('ignore', category=AstropyWarning)
# sphinx_gallery_end_ignore

from madcubapy.io import MadcubaMap

# Read fits file
madcuba_map = MadcubaMap.read("data/IRAS16293_SO_2-1_moment0_madcuba.fits")

###############################################################################
# To measure the noise level of the map we have two options:
# 
# * We can use the :func:`~madcubapy.operations.maps.measure_noise` function on
#   the `~madcubapy.io.MadcubaMap` object to obtain the sigma value in a
#   variable (this also works for `~astropy.nddata.CCDData` objects):
# 
#   .. code-block:: python
# 
#       sigma = measure_noise(madcuba_map)
#
# * Or we can use the
#   :meth:`MadcubaMap.update_sigma() <madcubapy.io.MadcubaMap.update_sigma>`
#   method to automatically store the measured sigma value in the FITS header,
#   on the ``SIGMA`` card, and have it available for future analysis:
#
#   .. code-block:: python
# 
#       madcuba_map.update_sigma()
#
#   .. note::
#
#       Remember that changes applied to a `~madcubapy.io.MadcubaMap` object
#       during a python run are not stored into the FITS file until the file is
#       explicitly saved:
#
#       .. code-block:: python
# 
#           madcuba_map.write("output_file.fits", overwrite=True)
# 
# How it works
# ------------
# 
# Both options behave in the same way. A window will appear where the user can
# select polygons using the mouse:
# 
# - Left clicks create polygon vertices.
# - Right click closes the current polygon, and a subsequent left click
#   starts a new polygon.
#
# This window also offers buttons to change the statistic used to calculate
# the noise.
#
# Once we have the desired polygons, we can press the **Finish** button to
# close the window and return the noise value in a variable (the case of
# :func:`~madcubapy.operations.maps.measure_noise`) or stored in the FITS
# header (the case of
# :meth:`MadcubaMap.update_sigma() <madcubapy.io.MadcubaMap.update_sigma>`).
#
# .. figure:: ../_static/figures/measure_noise.png
#     :alt: Image with pcolor
#     :figclass: align-center
