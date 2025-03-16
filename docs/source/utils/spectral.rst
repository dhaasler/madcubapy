##############
Spectral utils
##############

The `madcubapy.utils` package offers a set of utils to perform operations on
spectra data.

Create spectral arrays
======================

So far, the only available utility function is
:func:`~madcubapy.utils.create_spectral_array`, which creates an spectral array
by providing the following parameters:

* ``nchan`` : Number of channels in the spectrum.
* ``cdelt`` : Width of a channel.
* ``crpix`` : Reference channel of the spectrum.
* ``crval`` : Value of the reference channel.

    >>> from madcubapy.utils import create_spectral_array
    >>> x_axis = create_spectral_array(nchan=5, cdelt=2, crpix=2, crval=10)
    >>> x_axis
    array([8, 10, 12, 14, 16])