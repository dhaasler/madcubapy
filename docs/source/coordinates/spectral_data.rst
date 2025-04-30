.. _use_spectral_data:

############
SpectralData
############

The `madcubapy.coordinates` package offers a set of utility functions to work
with spectral data.

Using the SpectralData class
============================

`~madcubapy.coordinates.SpectralData` is a wrapper for Astropy's
`~astropy.coordinates.SpectralCoord` that lets the user specify the input data
as the rest frequency instead of observed frequency.

We can initialize a `~madcubapy.coordinates.SpectralData` instance using a
value and a unit, or a `~astropy.units.Quantity` object:

.. code-block:: python

    >>> from madcubapy.coordinates import SpectralData
    >>> sd = SpectralData((266, 267) * u.GHz,
                        frame_type="rest",
                        radial_velocity=50 * u.km / u.s,)
    >>> sd
    [265.95564, 266.95547] GHz

Note that the representation of `~madcubapy.coordinates.SpectralData` and
`~astropy.coordinates.SpectralCoord` is the observed frequency corresponding
to the input rest frequency and radial velocity.

We can obtain the rest frequency again with:

.. code-block:: python

    >>> sd.to_rest()
    [266, 267] GHz

We can obtain the array in velocity by providing the rest frequency and doppler
convention (the ``doppler_rest`` and ``doppler_convention`` parameters can also
be set when initializing the `~madcubapy.coordinates.SpectralData` object).

.. code-block:: python

    >>> sd.to(u.km / u.s, doppler_rest=267.01 * u.GHz, doppler_convention="radio")
    [1183.8106, 61.22172] km / s

Extra functionality
===================

Since this class is based on `~astropy.coordinates.SpectralCoord`, it retains
all of its functionality. Check the
`Using SpectralCoord page <https://docs.astropy.org/en/stable/coordinates/spectralcoord.html>`_
for an overview on all of its functionality.
