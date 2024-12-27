"""
SpectraContainer
================ 

Spectra are exported from MADCUBA in a single fits file containing a bintable
with each one of the spectra inside. This fits file is then packaged
alongside the history file inside a *.spec* archive. 

With the SpectraContainer class we can open MADCUBA's *.spec* files.
"""

from astropy.nddata import CCDData
from astropy.table import Table
import astropy.units as u
import matplotlib.axes as maxes
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable
import numpy as np
import os
from pathlib import Path

from madcubapy.io import MadcubaMap
from madcubapy.io import SpectraContainer
from madcubapy.visualization import add_wcs_axes
from madcubapy.visualization import add_manual_wcs_axes
from madcubapy.visualization import append_colorbar

data_folder = Path("data")
spectra_container = SpectraContainer.read(data_folder/"IRAS16293_position_8_TM2_spectra.spec")

###############################################################################
# The spectra are stores in teh ``bintable`` attribute, which is an Astropy
# table contaning the data and header information for every spectra.

# Show the first two spectra inside as an example
spectra_container.bintable[0:2]

###############################################################################
# The spectrum data is contained in the ``DATA`` and ``XAXIS`` columns
# alongside their units if correctly parsed from the header.
# 
# We can quickly plot a spectrum by accesing these values

index = 6

fig, ax = plt.subplots(1, 1, figsize=(7,5))

x = spectra_container.bintable[index]['XAXIS']
x_unit = spectra_container.bintable[index].table['XAXIS'].unit
y = spectra_container.bintable[index]['DATA']
y_unit = spectra_container.bintable[index].table['DATA'].unit

ax.plot(x, y, drawstyle='steps-mid')

ax.set_xlabel(f"Freq [{x_unit}]")
ax.set_ylabel(f"S [{y_unit}]")

plt.show()