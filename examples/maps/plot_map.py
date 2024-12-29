"""
.. _example_plot_map:

Plot a map
##########

Example showing how to plot a fits map file with MadcubaMap using
:func:`~madcubapy.visualization.wcsaxes_helpers.add_wcs_axes`.

"""

# sphinx_gallery_start_ignore
# Do not show warnings in example page. A note tells the user what to expect
# regarding warnings. 
import warnings
from astropy.utils.exceptions import AstropyWarning
warnings.filterwarnings('ignore', category=AstropyWarning)
# sphinx_gallery_end_ignore

from madcubapy.io import MadcubaMap
from madcubapy.visualization import add_wcs_axes
import matplotlib.pyplot as plt

# Read fits file
madcuba_map = MadcubaMap.read("../data/IRAS16293_SO_2-1_moment0_madcuba.fits")

# Create empty figure
fig = plt.figure(figsize=(6,6))
# We can set kwargs that are passed to matplotlib.pyplot.imshow()
ax, img = add_wcs_axes(fig, fitsmap=madcuba_map, vmin=0, vmax=100)
plt.show()
