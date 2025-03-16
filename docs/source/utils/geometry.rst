##############
Geometry utils
##############

The `madcubapy.utils` package offers a set of utils to perform operations on
spectra data.

Convert points to offsets
=========================

The :func:`~madcubapy.utils.get_angular_offset_points` and
:func:`~madcubapy.utils.get_physical_offset_points` functions let the user
get the coordinates of a point or set of points as angular or physical offset
with respect to a reference point.

>>> from madcubapy.io import MadcubaMap
>>> from madcubapy.utils import get_angular_offset_points
>>> madcubamap = MadcubaMap.read("example_cube.fits")

>>> points = np.array([[120, 250], [140, 250], [160,250], [180,250]])
>>> ref_point = np.array([370, 300])
>>> get_angular_offset_points(points, ref_point, madcubamap)
[[ 0.00430556 -0.00086111]
 [ 0.00396111 -0.00086111]
 [ 0.00361667 -0.00086111]
 [ 0.00327222 -0.00086111]] deg

>>> import astropy.units as u
>>> distance = 141 * u.pc
>>> get_physical_offset_points(points, ref_point, madcubamap, distance)
[[2185.5  -437.1 ]
 [2010.66 -437.1 ]
 [1835.82 -437.1 ]
 [1660.98 -437.1 ]] AU




Calculate separations
=====================

The :func:`~madcubapy.utils.get_angular_separation` and
:func:`~madcubapy.utils.get_physical_separation` functions let the user
get the separation between a point or set of points and a reference point in
angular or physical units.

>>> from madcubapy.io import MadcubaMap
>>> from madcubapy.utils import get_angular_offset_points
>>> madcubamap = MadcubaMap.read("example_cube.fits")

>>> points = np.array([[120, 250], [140, 250], [160,250], [180,250]])
>>> ref_point = np.array([370, 300])
>>> get_angular_separation(points, ref_point, madcubamap)
[0.00439082 0.00405363 0.00371777 0.00338363] deg

>>> import astropy.units as u
>>> distance = 141 * u.pc
>>> get_phisical_separation(points, ref_point, madcubamap, distance)
[2228.78142939 2057.62242542 1887.13843753 1717.53048602] AU
