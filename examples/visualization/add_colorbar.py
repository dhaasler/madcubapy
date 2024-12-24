"""
Add colorbar to a MadcubaMap plot
#################################

Example showing how to quickly add a colorbar to a MadcubaMap plot.

.. note::
    Due to how MADCUBA saves some fits header cards, several astropy warnings
    can pop up when reading fits files. Usually these warnings are unexpected
    card names using non-standard conventions.

"""

from madcubapy.io import MadcubaMap
from madcubapy.visualization import append_colorbar
from madcubapy.visualization import add_wcs_axes
import matplotlib.pyplot as plt

# Read fits file
madcuba_map = MadcubaMap.read("../data/IRAS16293_SO_2-1_moment0_madcuba.fits")

fig = plt.figure(figsize=(6,5))
ax, img = add_wcs_axes(fig, 1, 1, 1, fitsmap=madcuba_map, vmin=0, vmax=100)
# Add the colorbar. We can pass kwargs to ax.colorbar() function of matplotlib
append_colorbar(ax, label='Custom label')
plt.show()
