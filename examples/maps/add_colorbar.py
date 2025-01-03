"""
.. _example_colorbar:

Add a colorbar to a map
#######################

Example showing how to quickly add a colorbar to a map plot. 

Even though adding a colorbar using `~matplotlib` syntax directly is very
straightforward, `~madcubapy` functions offer additional functionality and let
the user quickly add the colorbar using only one line of code.

We can add a colorbar by using
:func:`~madcubapy.visualization.append_colorbar` or
:func:`~madcubapy.visualization.add_colorbar`.
Both functions accept a number of additional parameters that are passed to
:func:`matplotlib.pyplot.colorbar`. With this we can set custom ticks, a custom
label, etc.

Check the :ref:`Colorbar page <colorbar>` to know more about how these two
functions work.

"""

# sphinx_gallery_start_ignore
# Do not show warnings in example page. A note tells the user what to expect
# regarding warnings. 
import warnings
from astropy.utils.exceptions import AstropyWarning
warnings.filterwarnings('ignore', category=AstropyWarning)
# sphinx_gallery_end_ignore

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
