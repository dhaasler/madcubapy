"""
.. _tutorial_read_plot_spec:

Read and plot spectra with SpectraContainer
===========================================

.. note::
    This tutorial is not final. It will be finished once all the core
    functionalities of `~madcubapy.io.SpectraContainer` are implemented. 

Introduction to using `madcubapy` to read and plot MADCUBA spectra.

We start by importing the necessary libraries for this tutorial.
"""

from madcubapy.io import SpectraContainer
import matplotlib.pyplot as plt

# sphinx_gallery_start_ignore
# Do not show warnings in tutorial page. A note tells the user what to expect
# regarding warnings. 
import warnings
from astropy.utils.exceptions import AstropyWarning
warnings.filterwarnings('ignore', category=AstropyWarning)
# sphinx_gallery_end_ignore

###############################################################################
# Reading the spectra file
# ========================
# 
# Spectra are exported from MADCUBA in a single FITS file containing a bintable
# with each one of the spectra inside. This FITS file is then packaged
# alongside the :ref:`history file <hist_file>` inside a *.spec* archive. With
# the `~madcubapy.io.SpectraContainer` class we can open MADCUBA's **.spec**
# files alongside their history tables.
# 
# We can read the **.spec** file with the
# `SpectraContainer.read() <madcubapy.io.SpectraContainer.read>` method, and
# the corresponding :ref:`history file <hist_file>` will be loaded as well if
# present.

spectra_container = SpectraContainer.read(
    "../examples/data/IRAS16293_position_8_TM2_spectra.spec")

###############################################################################
# .. note:: 
#     Due to how MADCUBA saves some FITS header cards, several `astropy`
#     warnings can pop up when reading spectra. Usually these warnings are
#     incorrectly written units, or units using non-standard conventions.
# 
# The spectra are stored in the ``bintable`` attribute, which is an Astropy
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
