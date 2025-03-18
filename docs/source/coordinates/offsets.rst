#######
Offsets
#######

The `madcubapy.coordinates` package offers a set of utility functions to work
with coordinates and perform coordinates transformations.

Convert points to offsets
=========================

The :func:`~madcubapy.coordinates.get_angular_offset_points` and
:func:`~madcubapy.coordinates.get_physical_offset_points` functions let the user
get the coordinates of a point or set of points as angular or physical
(providing a distance) offset with respect to a reference point.

.. code-block:: python

    >>> from madcubapy.io import MadcubaMap
    >>> from madcubapy.coordinates import get_angular_offset_points

.. code-block:: python
    
    # Read map
    >>> madcubamap = MadcubaMap.read("example_cube.fits")

.. code-block:: python

    # Convert points to angular offsets
    >>> points = np.array([[120, 250], [140, 250], [160,250], [180,250]])
    >>> ref_point = np.array([370, 300])
    >>> new_points = get_angular_offset_points(points, ref_point, madcubamap)
    
    >>> new_points
    [[0.00430556 -0.00086111]
     [0.00396111 -0.00086111]
     [0.00361667 -0.00086111]
     [0.00327222 -0.00086111]] deg

.. code-block:: python

    # Convert points to physical offsets
    >>> import astropy.units as u
    >>> distance = 141 * u.pc
    >>> new_points = get_physical_offset_points(points, ref_point, madcubamap, distance)
    
    >>> new_points
    [[2185.5  -437.1 ]
     [2010.66 -437.1 ]
     [1835.82 -437.1 ]
     [1660.98 -437.1 ]] AU




Calculate separations
=====================

The :func:`~madcubapy.coordinates.get_angular_separation` and
:func:`~madcubapy.coordinates.get_physical_separation` functions let the user
get the separation between a point or set of points and a reference point in
angular or physical (providing a distance) units.

.. code-block:: python

    >>> from madcubapy.io import MadcubaMap
    >>> from madcubapy.coordinates import get_angular_offset_points

.. code-block:: python

    # Read map
    >>> madcubamap = MadcubaMap.read("example_cube.fits")

.. code-block:: python
    
    # Calculate angular separation between points
    >>> points = np.array([[120, 250], [140, 250], [160,250], [180,250]])
    >>> ref_point = np.array([370, 300])
    >>> separation = get_angular_separation(points, ref_point, madcubamap)
    
    >>> separation
    [0.00439082 0.00405363 0.00371777 0.00338363] deg

.. code-block:: python

    # Calculate physical separation between points
    >>> import astropy.units as u
    >>> distance = 141 * u.pc
    >>> separation = get_physical_separation(points, ref_point, madcubamap, distance)
    
    >>> separation
    [2228.78142939 2057.62242542 1887.13843753 1717.53048602] AU
