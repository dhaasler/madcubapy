.. _operations_maps_arithmetic:

Arithmetic
##########

The :ref:`madcubapy.operations.maps.arithmetic<operations_maps_arithmetic>`
module contains functions to perform arithmetic operations on the FITS files. 

Addition
========

So far, the only available utility function is
:func:`~madcubapy.operations.maps.stack_maps`, which adds the emission of
any number of maps. The function accepts `~madcubapy.io.MadcubaMap` and
`~astropy.nddata.CCDData` objects, but all of them must be from the same object
type. The returned object will be a `~madcubapy.io.MadcubaMap` or
`~astropy.nddata.CCDData` with the metadata of the first input map.

    >>> from madcubapy.operations import stack_maps
    >>> sum_map = stack_maps(madcuba_map_1, madcuba_map_2, madcuba_map_3)
