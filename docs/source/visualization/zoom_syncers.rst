###############################
Copy or synchronize plot limits
###############################

The `madcubapy.visualization` package also offers a set of functions to copy
the X and Y limits (zoom) between map objects (CCDData or MadcubaMap), or
`~astropy.visualization.wcsaxes.WCSAxes` objects.

Copy limits from one map to another
===================================

The :func:`~madcubapy.visualization.copy_zoom_fitsmap` function lets the user
transform the limits from one map to another by using the WCS data from the
FITS files.

The user needs to provide the y_lim and y_lim values and the function returns
the transformed limits.

.. code-block:: python

    # Read maps
    >>> madcubamap_1 = MadcubaMap.read("high_res_cube.fits")
    >>> madcubamap_2 = MadcubaMap.read("low_res_cube.fits")

.. code-block:: python

    # Transform limits
    >>> xlim1 = (200, 350)
    >>> ylim1 = (200, 350)
    
    >>> xlim2, ylim2 = copy_zoom_fitsmap(
            ref_fitsmap=madcubamap_1,
            target_fitsmap=madcubamap_2,
            x_lim=xlim1, 
            y_lim=ylim1
        )

    >>> xlim2, ylim2
    ([68.446, 120.113]
     [68.443, 120.110])


Copy limits from one WCSAxes to another
=======================================

The :func:`~madcubapy.visualization.copy_zoom_axes` function lets the user
transform the limits from one WCSAxes to another and set them automatically.

With this function the user does not have to provide the y_lim and y_lim\
values, because they are directly read from the axes.

.. code-block:: python

    # Plot maps
    >>> fig = plt.figure(figsize=(10,6))
    >>> ax1, img1 = add_wcs_axes(fig, 1, 2, 1, fitsmap=madcubamap_1)
    >>> ax2, img2 = add_wcs_axes(fig, 1, 2, 2, fitsmap=madcubamap_2)

    # Set limits in ax1
    >>> xlim1 = (200, 350)
    >>> ylim1 = (200, 350)
    >>> ax1.set_xlim(xlim1)
    >>> ax1.set_ylim(ylim1)

    # Transform limits and automatically set them in ax2
    >>> copy_zoom_axes(ref_ax=ax1, target_ax=ax2)


Synchronize zoom in several WCSAxes
===================================

The :func:`~madcubapy.visualization.sync_zoom` function automatically links the
zoom level of any number of WCSAxes objects by calculating the new X and Y
limits of each WCSAxes everytime a plot changes them.

This function should be used before setting any limits on the WCSAxes, after
that the user can change the limits of one WCSAxes object, and the rest will
automatically be set to the corresponding limits.

.. code-block:: python

    # Read maps
    >>> madcubamap_1 = MadcubaMap.read("high_res_cube.fits")
    >>> madcubamap_2 = MadcubaMap.read("low_res_cube.fits")
    >>> madcubamap_3 = MadcubaMap.read("extra_cube.fits")

.. code-block:: python

    # Plot maps
    >>> fig = plt.figure(figsize=(10,6))
    >>> ax1, img1 = add_wcs_axes(fig, 1, 3, 1, fitsmap=madcubamap_1)
    >>> ax2, img2 = add_wcs_axes(fig, 1, 3, 2, fitsmap=madcubamap_2)
    >>> ax3, img3 = add_wcs_axes(fig, 1, 3, 3, fitsmap=madcubamap_3)

    # Synchronize every WCSAxes
    >>> sync_zoom(ax1, ax2, ax3)

    # Set limits in any WCSAxes
    >>> xlim1 = (200, 350)
    >>> ylim1 = (200, 350)
    >>> ax1.set_xlim(xlim1)
    >>> ax1.set_ylim(ylim1)
