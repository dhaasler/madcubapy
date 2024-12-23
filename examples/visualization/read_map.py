"""
Reading MadcubaMap
##################

Example showing how to read a fits map file with MadcubaMap.
"""

from astropy.nddata import CCDData
from astropy.table import Table
import astropy.units as u
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable
import numpy as np
import os
from pathlib import Path

from madcubapy.io import MadcubaMap

madcuba_map = MadcubaMap.read("../data/IRAS16293_SO_2-1_moment0_madcuba.fits")

fig, ax = plt.subplots(1, 1, figsize=(6, 6))
map_data = madcuba_map.data[0, 0, :, :]  # apply slicing
img = ax.imshow(map_data, cmap='viridis', origin='lower')
divider = make_axes_locatable(ax)
cax = divider.append_axes("right", size="5%", pad=0.05)
fig.colorbar(img, cax=cax, label='Intensity')

ax.set_title('Madcuba Map')
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')

plt.show()
