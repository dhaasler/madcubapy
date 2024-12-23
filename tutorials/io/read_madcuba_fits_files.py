"""
Read maps with MadcubaMap
#################################

MADCUBA exports a history file with the same name of the fits file ended with
*_hist.csv*.

With the ``MadcubaMap`` class we can open these fits files alongside their
history tables.

We start by importing the necessary libraries
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
from madcubapy.io import SpectraContainer

###############################################################################
# Set Path of example files

data_folder = Path("../data")

###############################################################################
# Read the fits file with the ``MadcubaMap.read()`` method

madcuba_map = MadcubaMap.read(
    data_folder/"IRAS16293_SO_2-1_moment0_madcuba.fits")

###############################################################################
# The MadcubaMap class resembles the ``CCDData`` class from astropy with
# ``data``, ``header``, ``wcs``, and ``unit`` attributes, with the addition of
# a ``hist`` attribute, the history table.

madcuba_map.hist

###############################################################################
# As a failsafe, a ``CCDDdata`` object is also present inside the
# ``MadcubaMap`` object in the ``ccddata`` attribute.

madcuba_map.ccddata

###############################################################################
# We can plot the data array of the fits file from the ``data`` attribute.
# Keep in mind that usually we need to do some slicing to get rid of the
# spectral and polarization axes if present.

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

###############################################################################
# We can get a lot of information from the header and wcs parameters like the
# units for the axes, but that will be shown in a future example using utility
# functions.

###############################################################################
# Fix units
# =========
# Some programs export the BUNIT fits card incorrectly with more than one slash
# and astropy has problems parsing units in those strings. With this method
# the user can try to fix this problem and correctly parse the units.
# 
# For example, CARTA exports units like this. When we read a CARTA map, astropy
# gives us a warning:

carta_map = MadcubaMap.read(data_folder/"IRAS16293_SO2c_moment0_carta.fits")

###############################################################################
# The warning is telling us that we have a string with multiple slashes:
# 'Jy/beam.km/s', and the 'km' are placed on the denominator:

carta_map.unit
###############################################################################
# We can run the ``fix_units`` method of MadcubaMap to fix this.

carta_map.fix_units()
carta_map.unit

###############################################################################
# It is important to note that the ccddata object inside MadcubaMap also gets
# the correct units when they are fixed.

carta_map.ccddata.unit

###############################################################################
# Even though a CARTA exported map does not have a *_hist.csv* file, it is
# encouraged to read it as a MadcubaMap, even when the user wants to work with
# a CCDData object. That's why we have the failsafe CCDData object in the
# ``MadcubaMap.ccddata`` atribute.

carta_ccddata = carta_map.ccddata
carta_ccddata

###############################################################################
# We can work with carta_ccddata just as if it was directly read with the
# ``CCDData.read()`` method from astropy.

###############################################################################
# SpectraContainer
# ================ 
# 
# Spectra are exported from MADCUBA in a single fits file containing a bintable
# with each one of the spectra inside. This fits file is then packaged
# alongside the history file inside a *.spec* archive. 
# 
# With the SpectraContainer class we can open MADCUBA's *.spec* files.

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
