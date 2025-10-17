##############
Geometry utils
##############

The `madcubapy.utils` package offers a set of utils to perform geometry
operations.

Measure area and centroid of polygons
=====================================

The :func:`~madcubapy.utils.polygon_area` and
:func:`~madcubapy.utils.polygon_signed_area` functions measure the area and
signed area of a polygon.
The signed area of a polygon encodes its orientation, negative area if its
vertices are ordered clockwise and positive area if counterclockwise.

The :func:`~madcubapy.utils.calculate_polygon_centroid` calculates the centroid
of a polygon.
