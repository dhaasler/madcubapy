.. _interaction:

#################################
Interacting with Maps and Figures
#################################

The `madcubapy.visualization` package offers various functions to let the user
interact with plotted figures and maps. 

Get pixel coordinates from mouse clicks
=======================================

The :func:`~madcubapy.visualization.get_input` function opens a previously
plotted :class:`~matplotlib.figure.Figure`, or a map object
(`~madcubapy.io.MadcubaMap` or `~astropy.nddata.CCDData`), and lets the user
select points with mouse clicks:

* **Left click**: Adds a point to the image.
* **Middle click**: Deletes the last selected point.
* **Right click**: Ends the function and **returns the selected points**.

**Example Usage**

>>> selected_points = get_input(fig)
>>> selected_points
array([[30, 30],
       [56, 90]])

>>> selected_points = get_input(madcuba_map)
>>> selected_points
array([[13, 65],
       [23, 60],
       [70, 11]])

**Returns**

This function returns a :class:`numpy.ndarray` containing the pixel coordinates
of the selected points.

**Additional Parameters**

This function accepts optional keyword arguments that are passed to
:func:`~madcubapy.visualization.add_wcs_axes` if the input object is a 
`~madcubapy.io.MadcubaMap` or `~astropy.nddata.CCDData`.

>>> get_input(madcuba_map, vmin=0, vmax=100)
