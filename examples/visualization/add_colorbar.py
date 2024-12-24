"""
Add a colorbar to a map
#######################

Example showing how to quickly add a colorbar to a MadcubaMap plot. 

Even though adding a colorbar using matplotlib syntax directly is very
straightforward, MadcubaMap's functions offer additional functionality and let
the user quickly add the colorbar using only one line of code.

We can add a colorbar by using the ``append_colorbar`` or ``add_colorbar``
functions. Both accept the same number of arguments but create the colorbar
using different approaches.

- ``append_colorbar`` adds a colorbar to one side of the main axes object,
  which is resized to accomodate the colorbar inside the space it was taking
  before. The colorbar axes will always maintain the width that was set in the
  beggining, regardless of a change in the map size later (like resizing the
  window).
- ``add_colorbar`` adds a colorbar at a location relative to the main axes.
  This version does not resize the main axes and adds the cbar axes right
  where it is told, overlapping with anything that could be there before. The
  colorbar maintains the relative width relative to the map if it changes
  size later.

By default this function parses the units from the map object if found, and
sets the label acoordingly.

Both functions accept a number of additional parameters that are passed to
``matplotlib.Figure.colorbar()``. With this we can set custom ticks, a custom
label, etc.

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
# Add the colorbar. We can pass kwargs to matplotlib.Figure.colorbar()
append_colorbar(ax, label='Custom label')
plt.show()
