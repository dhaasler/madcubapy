.. _operations_maps_noise:

#####
Noise
#####

The :ref:`madcubapy.operations.maps.noise<operations_maps_noise>` module
contains functions to help the user estimate and work with the noise of the data
in FITS files. 

.. _measure_noise:

Measure noise
=============

The :func:`~madcubapy.operations.maps.measure_noise` function helps the user
measure the noise level of a `~madcubapy.io.MadcubaMap` or `~astropy.nddata.CCDData` object.

The function plots the map in a pop-up window and lets the user select several
polygons in which the noise will be calculated. The polygons are selected using
the mouse:

* **Left clicks** create polygon vertices.
* **Right click** closes the current polygon, and a subsequent left click
  starts a new polygon.

**Parameters**

Once the window with the plotted map is opened the user can select the polygons,
and also the statistic to be used for calculating the noise via GUI buttons.
The user can also select the desired statistic with the
``statistic`` parameter:

* 'std' for standard deviation.
* 'rms' for root mean square.

**Example Usage**

>>> sigma = measure_sigma(madcuba_map, statistic='rms')
>>> sigma
42.34567

**Returns**

This function returns a :class:`float` number: the noise calculated as the
specified statistic.

**Additional Parameters**

This function accepts optional keyword arguments that are passed to
:func:`~madcubapy.visualization.add_wcs_axes` for visualization purposes.

>>> measure_sigma(madcuba_map, vmin=0, vmax=100)
