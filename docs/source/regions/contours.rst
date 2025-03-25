.. _contours:

#####################
Working with contours
#####################

The `madcubapy.regions` package also helps the user select regions by using
contour levels from maps.

The :func:`~madcubapy.regions.check_contour` function plots a
`~matplotlib.contour.ContourSet` object in a pop-up window and lets the user
select different closed contours in the map via mouse clicks.

When the user selects the 'Save and exit' button
the window closes and the function returns the indexes of the selected regions.
These indexes can be used to import that region as a
`~matplotlib.patches.Patch` or `~matplotlib.contour.ContourSet` object using
the :func:`~madcubapy.regions.import_region_patch` and
:func:`~madcubapy.regions.import_region_contourset` respectively.
Both functions accept ``kwargs`` that are passed to the creation of the
`~matplotlib.patches.Patch` and `~matplotlib.contour.ContourSet` objects.

The function will plot the input contour in a blank space if no other input
parameters are set. To plot the contour on top of a map the user has to provide
a second input parameter:

- A previously plotted `~matplotlib.figure.Figure`, `~matplotlib.axes.Axes`, or
  `~astropy.visualization.wcsaxes.WCSAxes` objects throgh the ``fig`` or ``ax``
  parameters.

- A `~madcubapy.io.MadcubaMap` or `~astropy.nddata.CCDData` objects through the
  ``fitsmap`` parameter.

Example
=======

.. code-block:: python

  # Read map
  >>> madcuba_map = MadcubaMap.read("example_map.fits")

  # Plot the map
  >>> fig = plt.figure(figsize=(6,6))
  >>> ax, img = add_wcs_axes(fig, 1, 1, 1, fitsmap=madcuba_map)

  # Create the contour
  >>> contour_level = 15
  >>> contour = ax.contour(madcuba_map.data[0, 0, :, :], [contour_level],
                           origin=None, colors=['white'], linewidths=1)

  # Possible ways of getting region indexes
  >>> region_index = check_contour(contour_set)
  >>> region_index = check_contour(contour_set, fig=fig)
  >>> region_index = check_contour(contour_set, ax=ax)
  >>> region_index = check_contour(contour_set, fitsmap=madcuba_map)

  # Get a specific region as a a contourset object
  >>> region_contour = import_region_contourset(ax, contour, index=region_index,
                                                colors='black',
                                                linewidths=[1], linestyles='--')

  # Get a specific region as a a patch object
  >>> region_patch = import_region_patch(ax, contour, index=region_index,
                                         color='white', lw=3)
  >>> ax.add_patch(region_patch)
 