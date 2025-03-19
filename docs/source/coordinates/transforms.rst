##########
Transforms
##########

The `madcubapy.coordinates` package offers a set of utility functions to work
with coordinates and perform coordinates transformations.

Transform coordinates between two map objects
=============================================

The :func:`~madcubapy.coordinates.transform_coords_fitsmap` function lets the
user transform one or several points FITS or image coordinates from one map
to another. This function uses the WCS data stored in the FITS file.

.. code-block:: python

    >>> from madcubapy.io import MadcubaMap
    >>> from madcubapy.coordinates import transform_coords_fitsmap

.. code-block:: python

    # Read maps
    >>> madcubamap_1 = MadcubaMap.read("example_cube.fits")
    >>> madcubamap_2 = MadcubaMap.read("other_cube.fits")

    # Transform points
    >>> points = np.array([[300, 350], [300, 400], [300, 450]])
    >>> new_points = transform_coords_fitsmap(
            ref_fitsmap=madcubamap_1,
            target_fitsmap=madcubamap_2,
            points=points,
        )
        
    >>> new_points
    [[102.89121886 120.1101461 ]
     [102.89121888 137.33236833]
     [102.89121889 154.55459055]]


Transform coordinates between two Axes objects
==============================================

The :func:`~madcubapy.coordinates.transform_coords_axes` function lets the
user transform one or several points FITS or image coordinates from one
`~astropy.visualization.wcsaxes.WCSAxes` to another.

If we plot the map objects from the prior example we can also use the Axes to
transform the coordinates of points

.. code-block:: python

    >>> from madcubapy.coordinates import transform_coords_axes
    >>> from madcubapy.visualization import add_wcs_axes

.. code-block:: python
    
    # Plot maps
    >>> fig = plt.figure(figsize=(6,6))
    >>> ax1, img1 = add_wcs_axes(fig, 1, 2, 1, fitsmap=m0_madcubamap_1)
    >>> ax2, img2 = add_wcs_axes(fig, 1, 2, 2, fitsmap=m0_madcubamap_2)
    
    # Transform points
    >>> points = np.array([[300, 350], [300, 400], [300, 450]])
    >>> new_points = transform_coords_axes(
            ref_ax=ax1,
            target_ax=ax2,
            points=points,
        )
    
    >>> new_points
    [[102.89121886 120.1101461 ]
     [102.89121888 137.33236833]
     [102.89121889 154.55459055]]
