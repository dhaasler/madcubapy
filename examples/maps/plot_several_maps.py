"""
.. _plot_several_maps_example:

Plot several maps
#################

Example showing how to plot several fits map files with MadcubaMap using
:func:`~madcubapy.visualization.wcsaxes_helpers.add_wcs_axes`. We can add as
many subplots as needed following the same convention used for matplotlib's
:meth:`~matplotlib.figure.Figure.add_subplot`: *nrows*, *ncols*, *number* right
after the `~matplotlib.figure.Figure` that we want to use.

.. note::
    Due to how MADCUBA saves some fits header cards, several astropy warnings
    can pop up when reading fits files. Usually these warnings are unexpected
    card names using non-standard conventions.

"""

from madcubapy.io import MadcubaMap
from madcubapy.visualization import add_wcs_axes
import matplotlib.pyplot as plt

# Read fits file
madcuba_map = MadcubaMap.read("../data/IRAS16293_SO_2-1_moment0_madcuba.fits")

# Create empty figure
fig = plt.figure(figsize=(10,5))
# Add as many WCS axes objects as desired.
# We can pass kwargs for matplotlib.pyploy.imshow()
ax1, img1 = add_wcs_axes(fig, 1, 2, 1, fitsmap=madcuba_map, vmin=0, vmax=100)
ax2, img2 = add_wcs_axes(fig, 1, 2, 2, fitsmap=madcuba_map, vmin=0, vmax=100,
                       cmap='jet')
plt.show()
