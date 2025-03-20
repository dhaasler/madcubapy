###########
Conversions
###########

The `madcubapy.coordinates` package offers a set of utility functions to
convert between several coordinate systems.

Convert pixels between FITS and Python standards
================================================

The :func:`~madcubapy.coordinates.python_to_fits` and
:func:`~madcubapy.coordinates.fits_to_python` functions let the
user convert one or several points between FITS and python standards.

.. code-block:: python

    >>> from madcubapy.coordinates import python_to_fits
    >>> points = np.array([[20, 35], [30, 40]])
    >>> python_to_fits(points)
    [[21 36]
     [31 41]]

Convert points between world coordinates and pixels in an map
=============================================================

The :func:`~madcubapy.coordinates.world_to_pixel` and
:func:`~madcubapy.coordinates.pixel_to_world` functions let the user convert
points between world coordinates and pixel coordinates of a certain map object
(`~madcubapy.io.MadcubaMap` or `~astropy.nddata.CCDData`).

.. code-block:: python

    >>> from madcubapy.io import MadcubaMap
    >>> from madcubapy.coordinates import pixel_to_world, world_to_pixel
    >>> madcubamap = MadcubaMap.read("example_cube.fits")
    >>> points = np.array([[20, 35], [30, 40]])
    >>> world_points = pixel_to_world(points, madcubamap, origin=0)
    >>> world_points
    [[248.09917019 -24.47990265]
     [248.09898095 -24.47981654]] deg
    >>> pixel_points = world_to_pixel(world_points, madcubamap, origin=0)
    >>> pixel_points
    [[20, 35],
     [30, 40]])

Convert arcs in the sky between angular units and pixels
========================================================

The :func:`~madcubapy.coordinates.angle_to_pixels` and
:func:`~madcubapy.coordinates.pixels_to_angle` functions let the user convert
angles in the sky to pixel lengths of a certain map object
(`~madcubapy.io.MadcubaMap` or `~astropy.nddata.CCDData`), and vice versa.

    >>> from madcubapy.io import MadcubaMap
    >>> from madcubapy.coordinates import angle_to_pixels, pixels_to_angle
    >>> madcubamap = MadcubaMap.read("example_cube.fits")
    >>> length = (2 * u.arcsec, 1 * u.arcsec)
    >>> pixel_lengths = angle_to_pixels(length, madcubamap, origin=0)
    >>> pixel_lengths
    [-32.25806455, -16.12903227]
    >>> angles = pixels_to_angle(pixel_lengths, madcubamap, origin=0)
    >>> angles
    [0.00055556 0.00027778] deg
