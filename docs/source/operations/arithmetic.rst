Arithmetic
##########

The :mod:`madcubapy.operations.maps.arithmetic` module contains functions to perform
arithmetic operations on the FITS files. 

Addition
========

So far, the only available utility function is
:func:`~madcubapy.operations.maps.stack_emission`, which adds the emission of
any number of maps. The function accepts `~madcubapy.io.MadcubaMap` and
`~astropy.nddata.CCDData` objects, but all of them must be from the same object
type. The returned object will be a `~madcubapy.io.MadcubaMap` or
`~astropy.nddata.CCDData` with the metadata of the first input map.

    >>> from madcubapy.operations import stack_emission
    >>> sum_map = stack_emission(madcuba_map_1, madcuba_map_2, madcuba_map_3)
