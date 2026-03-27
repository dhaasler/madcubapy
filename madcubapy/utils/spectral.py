import astropy.constants as const
import astropy.units as u
from astropy.units import Quantity
import numpy as np

__all__ = [
    'create_spectral_array',
    'convert_spectral_resolution',
    'obs_to_rest',
    'rest_to_obs',
    'obs_to_vel',
    'vel_to_obs',
    'rest_to_vel',
    'vel_to_rest',
    'measure_snr_peak',
    'measure_snr_profile_fit',
    'measure_snr_profile_observed',
    'estimate_rms_profile_fit',
    'estimate_rms_peak',
]

def create_spectral_array(nchan, cdelt, crpix, crval):
    """
    Create a spectral axis array.

    Parameters
    ----------
    nchan : `~int`
        Number of channels in the spectrum.
    cdelt : `~float` or `~astropy.units.Quantity`
        Width of a channel.
    crpix : `~float`
        Reference channel of the spectrum.
    crval : `~float`
        Value of the reference channel.
    
    Returns
    -------
    spectral_array : `~numpy.ndarray` or `~astropy.units.Quantity`
        Returned spectral axis array with units if cdelt is a quantity.

    """

    # if cdelt has units
    if isinstance(cdelt, Quantity):
        first_chan = crval - (cdelt.value * crpix)
        last_chan = crval + (cdelt.value * (nchan-1 - crpix))
        spectral_array = np.linspace(first_chan, last_chan, nchan) * cdelt.unit
    # if cdelt is adimensional
    else:
        first_chan = crval - (cdelt * crpix)
        last_chan = crval + (cdelt * (nchan-1 - crpix))
        spectral_array = np.linspace(first_chan, last_chan, nchan)

    return spectral_array


def convert_spectral_resolution(spectral_res, rest_freq):
    """
    Convert a channel width between velocity and frequency.

    Parameters
    ----------
    spectral_res : `~astropy.units.Quantity`
        Width of channel in velocity or frequency units.
    rest_freq : `~astropy.units.Quantity`
        Rest frequency of the spectrum.

    Returns
    -------
    `~astropy.units.Quantity`
        Spectral rest converted to the other units.

    """

    if not isinstance(spectral_res, u.Quantity):
        raise TypeError("spectral_res must be an astropy Quantity,"
                        + f"not {type(spectral_res)}")
    if spectral_res.unit.is_equivalent(u.Hz):
        spectral_res_vel = const.c * (spectral_res / rest_freq.to(spectral_res.unit))
        return spectral_res_vel.to(u.km / u.s)
    elif spectral_res.unit.is_equivalent(u.m / u.s):
        spectral_res_freq = rest_freq * (spectral_res / const.c)
        return spectral_res_freq.to(u.Hz)
    else:
        raise u.UnitConversionError(
            f"Unit '{spectral_res.unit}' is not a valid spectral resolution unit. "
            "Must be equivalent to Hz or km/s."
        )



def obs_to_rest(obs_freq, radial_velocity, doppler_convention="radio"):
    """
    Convert observed frequency to rest frequency.

    Parameters
    ----------
    obs_freq : `~astropy.units.Quantity`
        Observed frequency.
    radial_velocity : `~astropy.units.Quantity`
        Radial velocity of the source relative to the observer.
    doppler_convention : {"radio", "relativistic"}, default: "radio"
        The Doppler convention to use.

    Returns
    -------
    rest_freq : `~astropy.units.Quantity`
        Rest frequency.

    """

    if not isinstance(obs_freq, u.Quantity):
        raise TypeError("obs_freq must be an astropy Quantity.")
    if not isinstance(radial_velocity, u.Quantity):
        raise TypeError("vel must be an astropy Quantity.")
    
    if doppler_convention == "radio":
        rest_freq = _obs_to_rest_radio(obs_freq, radial_velocity)
    elif doppler_convention == "relativistic":
        rest_freq = _obs_to_rest_rel(obs_freq, radial_velocity)
    else:
        raise ValueError(
            "Doppler convention can only be radio or relativistic.")

    return rest_freq


def rest_to_obs(rest_freq, radial_velocity, doppler_convention="radio"):
    """
    Convert rest frequency to observed frequency.

    Parameters
    ----------
    rest_freq : `~astropy.units.Quantity`
        Rest frequency.
    radial_velocity : `~astropy.units.Quantity`
        Radial velocity of the source relative to the observer.
    doppler_convention : {"radio", "relativistic"}, default: "radio"
        The Doppler convention to use.

    Returns
    -------
    obs_freq : `~astropy.units.Quantity`
        Observed frequency.

    """

    if not isinstance(rest_freq, u.Quantity):
        raise TypeError("rest_freq must be an astropy Quantity.")
    if not isinstance(radial_velocity, u.Quantity):
        raise TypeError("vel must be an astropy Quantity.")
    
    if doppler_convention == "radio":
        obs_freq = _rest_to_obs_radio(rest_freq, radial_velocity)
    elif doppler_convention == "relativistic":
        obs_freq = _rest_to_obs_rel(rest_freq, radial_velocity)
    else:
        raise ValueError(
            "Doppler convention can only be radio or relativistic.")

    return obs_freq


def obs_to_vel(obs_freq, doppler_rest, doppler_convention="radio"):
    """
    Convert observed frequency to velocity.

    Parameters
    ----------
    obs_freq : `~astropy.units.Quantity`
        Observed frequency.
    doppler_rest : `~astropy.units.Quantity`
        Rest frequency of the line.
    doppler_convention : {"radio", "relativistic"}, default: "radio"
        The Doppler convention to use.

    Returns
    -------
    vel : `~astropy.units.Quantity`
        Velocity.

    """

    if not isinstance(obs_freq, u.Quantity):
        raise TypeError("obs_freq must be an astropy Quantity.")
    if not isinstance(doppler_rest, u.Quantity):
        raise TypeError("doppler_rest must be an astropy Quantity.")
    
    if doppler_convention == "radio":
        vel = _obs_to_vel_radio(obs_freq, doppler_rest)
    elif doppler_convention == "relativistic":
        vel = _obs_to_vel_rel(obs_freq, doppler_rest)
    else:
        raise ValueError(
            "Doppler convention can only be radio or relativistic.")

    return vel


def vel_to_obs(vel, doppler_rest, doppler_convention="radio"):
    """
    Convert velocity to observed frequency.

    Parameters
    ----------
    vel : `~astropy.units.Quantity`
        Velocity.
    doppler_rest : `~astropy.units.Quantity`
        Rest frequency of the line.
    doppler_convention : {"radio", "relativistic"}, default: "radio"
        The Doppler convention to use.

    Returns
    -------
    obs_freq : `~astropy.units.Quantity`
        Observed frequency.

    """

    if not isinstance(vel, u.Quantity):
        raise TypeError("vel must be an astropy Quantity.")
    if not isinstance(doppler_rest, u.Quantity):
        raise TypeError("doppler_rest must be an astropy Quantity.")
    
    if doppler_convention == "radio":
        obs_freq = _vel_to_obs_radio(vel, doppler_rest)
    elif doppler_convention == "relativistic":
        obs_freq = _vel_to_obs_rel(vel, doppler_rest)
    else:
        raise ValueError(
            "Doppler convention can only be radio or relativistic.")

    return obs_freq


def rest_to_vel(rest_freq, radial_velocity, doppler_rest, doppler_convention="radio"):
    """
    Convert rest frequency to velocity.

    Parameters
    ----------
    rest_freq : `~astropy.units.Quantity`
        Observed frequency.
    radial_velocity : `~astropy.units.Quantity`
        Radial velocity of the source relative to the observer.
    doppler_rest : `~astropy.units.Quantity`
        Rest frequency of the line.
    doppler_convention : {"radio", "relativistic"}, default: "radio"
        The Doppler convention to use.

    Returns
    -------
    vel : `~astropy.units.Quantity`
        Velocity.

    """

    if not isinstance(rest_freq, u.Quantity):
        raise TypeError("rest_freq must be an astropy Quantity.")
    if not isinstance(radial_velocity, u.Quantity):
        raise TypeError("radial_velocity must be an astropy Quantity.")
    if not isinstance(doppler_rest, u.Quantity):
        raise TypeError("doppler_rest must be an astropy Quantity.")
    
    if doppler_convention not in ["radio", "relativistic"]:
        raise ValueError(
            "Doppler convention can only be radio or relativistic.")
    
    obs_freq = rest_to_obs(rest_freq, radial_velocity, doppler_convention)
    vel = obs_to_vel(obs_freq, doppler_rest, doppler_convention)

    return vel


def vel_to_rest(vel, radial_velocity, doppler_rest, doppler_convention="radio"):
    """
    Convert velocty to rest frequency.

    Parameters
    ----------
    vel : `~astropy.units.Quantity`
        Velocity.
    radial_velocity : `~astropy.units.Quantity`
        Radial velocity of the source relative to the observer.
    doppler_rest : `~astropy.units.Quantity`
        Rest frequency of the line.
    doppler_convention : {"radio", "relativistic"}, default: "radio"
        The Doppler convention to use.

    Returns
    -------
    rest_freq : `~astropy.units.Quantity`
        Rest frequency.

    """

    if not isinstance(vel, u.Quantity):
        raise TypeError("vel must be an astropy Quantity.")
    if not isinstance(radial_velocity, u.Quantity):
        raise TypeError("radial_velocity must be an astropy Quantity.")
    if not isinstance(doppler_rest, u.Quantity):
        raise TypeError("doppler_rest must be an astropy Quantity.")
    
    if doppler_convention not in ["radio", "relativistic"]:
        raise ValueError(
            "Doppler convention can only be radio or relativistic.")
    
    obs_freq = vel_to_obs(vel, doppler_rest, doppler_convention)
    rest_freq = obs_to_rest(obs_freq, radial_velocity, doppler_convention)

    return rest_freq


def _obs_to_rest_radio(obs_freq, vel):
    return obs_freq / (1 - vel / const.c)

def _obs_to_rest_rel(obs_freq, vel):
    beta = vel / const.c
    return obs_freq * np.sqrt((1 + beta) / (1 - beta))

def _rest_to_obs_radio(rest_freq, vel):
    return rest_freq * (1 - vel / const.c)

def _rest_to_obs_rel(rest_freq, vel):
    beta = vel / const.c
    return rest_freq * ((1 - beta) / (1 + beta))**0.5

def _obs_to_vel_radio(obs_freq, rest_freq):
    return const.c * ((rest_freq - obs_freq) / rest_freq)

def _obs_to_vel_rel(obs_freq, rest_freq):
    R = obs_freq / rest_freq
    beta = (1 - R**2) / (1 + R**2)
    return beta * const.c

def _vel_to_obs_radio(vel, rest_freq):
    return rest_freq * (1 - vel / const.c)

def _vel_to_obs_rel(vel, rest_freq):
    beta = (vel / const.c)
    return rest_freq * ((1 - beta) / (1 + beta))**0.5

def measure_snr_peak(peak_int, rms):
    """Measure the peak SNR of a line by providing peak intensity and rms"""
    if (not isinstance(peak_int, u.Quantity)
        and not isinstance (peak_int, int)
        and not isinstance (peak_int, float)):
        raise TypeError("'peak_int' must be a float or astropy Quantity.")
    if (not isinstance(rms, u.Quantity)
        and not isinstance (rms, int)
        and not isinstance (rms, float)):
        raise TypeError("'rms' must be a float or astropy Quantity.")
    return peak_int / rms

def measure_snr_profile_fit(area, fwhm, dv, rms):
    """
    Measure the SNR of a line by integrating the emission on the fitted
    gaussian profile

    Parameters
    ----------
    area : `float` or `~astropy.units.Quantity`
        Area of the fitted gaussian line.
    fwhm : `float` or `~astropy.units.Quantity`
        FWHM of the fitted gaussian line.
    dv : `float` or `~astropy.units.Quantity`
        Channel width.
    rms : `float` or `~astropy.units.Quantity`
        Measured rms on the spectral data.

    Returns
    -------
    snr : `float`
        Measured integrated SNR.

    """
    if (not isinstance(area, u.Quantity)
        and not isinstance (area, int)
        and not isinstance (area, float)):
        raise TypeError("'area' must be a float or astropy Quantity.")
    if (not isinstance(dv, u.Quantity)
        and not isinstance (dv, int)
        and not isinstance (dv, float)):
        raise TypeError("'dv' must be a float or astropy Quantity.")
    if (not isinstance(fwhm, u.Quantity)
        and not isinstance (fwhm, int)
        and not isinstance (fwhm, float)):
        raise TypeError("'fwhm' must be a float or astropy Quantity.")
    if (not isinstance(rms, u.Quantity)
        and not isinstance (rms, int)
        and not isinstance (rms, float)):
        raise TypeError("'rms' must be a float or astropy Quantity.")
    
    sigma_area = rms * dv * np.sqrt(fwhm/dv)
    snr = area / sigma_area

    return snr

def measure_snr_profile_observed(x_array, y_array, v0, fwhm, dv, rms,
                                 window_sigma_factor=3,
                                 window_selection_method="fractional"):
    """
    Measure the SNR of a line by integrating the emission on the observed
    channels.
    
    Note: Needs the velocity and width of a fitted gaussian line on the
    observed line profile to select the channels.

    Parameters
    ----------
    x_array : `~np.array` or `~astropy.units.Quantity`
        X axis array of the observed spectrum in velocity units.
    y_array : `~np.array` or `~astropy.units.Quantity`
        Y axis array of the observed spectrum.
    v0 : `float` or `~astropy.units.Quantity`
        Central velocity of the fitted gaussian line.
    fwhm : `float` or `~astropy.units.Quantity`
        FWHM of the fitted gaussian line.
    dv : `float` or `~astropy.units.Quantity`
        Channel width.
    rms : `float` or `~astropy.units.Quantity`
        Measured rms on the spectral data.
    window_sigma_factor : `float`, default: 3
        Number of sigma deviation to be used for each side of the gaussian
        center as the selected window.
    window_selection_method : {"fractional", "binary"}, default: "fractional"
        Method for handling channels at the edge of the integration window:

        - 'fractional' (Recommended): Weights boundary channels by the fraction
          of their width that falls inside the selected window.
        - 'binary': Boolean masking; includes the full flux of any channel 
          whose center is within the window boundaries.

    Returns
    -------
    snr : `float`
        Measured integrated SNR.

    """

    if (not isinstance(x_array, u.Quantity)
        and not isinstance (x_array, np.ndarray)):
        raise TypeError("'x_array' must be a numpy array or astropy Quantity.")
    if (not isinstance(y_array, u.Quantity)
        and not isinstance (y_array, np.ndarray)):
        raise TypeError("'y_array' must be a numpy array or astropy Quantity.")
    if (not isinstance(v0, u.Quantity)
        and not isinstance (v0, int)
        and not isinstance (v0, float)):
        raise TypeError("'area' must be a float or astropy Quantity.")
    if (not isinstance(fwhm, u.Quantity)
        and not isinstance (fwhm, int)
        and not isinstance (fwhm, float)):
        raise TypeError("'fwhm' must be a float or astropy Quantity.")
    if (not isinstance(dv, u.Quantity)
        and not isinstance (dv, int)
        and not isinstance (dv, float)):
        raise TypeError("'dv' must be a float or astropy Quantity.")
    if (not isinstance(rms, u.Quantity)
        and not isinstance (rms, int)
        and not isinstance (rms, float)):
        raise TypeError("'rms' must be a float or astropy Quantity.")

    sigma_v = fwhm / (2 * np.sqrt(2 * np.log(2)))

    if window_selection_method == "binary":
        mask_hard = ((x_array >= v0 - window_sigma_factor*sigma_v) &
                     (x_array <= v0 + window_sigma_factor*sigma_v))
        # sum of the flux in each channel multiplied by the channel width 
        area_obs_hard = np.sum(y_array[mask_hard]) * dv
        N_eff_hard = mask_hard.sum()
        sigma_area_hard = rms * dv * np.sqrt(N_eff_hard)
        snr = area_obs_hard / sigma_area_hard
        return snr
    elif window_selection_method == "fractional":
        vmin = v0 - window_sigma_factor*sigma_v
        vmax = v0 + window_sigma_factor*sigma_v
        v_left = x_array - dv/2
        v_right = x_array + dv/2
        # Create a mask with overlapping channels with contributions on each
        # channel. 0 to 1. Channels that are only partially on the window have
        # a number between 0 and 1. The ones entirely in the window are 1, the
        # ones outside are 0.
        f_overlap = np.clip((np.minimum(v_right, vmax)
                             - np.maximum(v_left, vmin))/dv, 0, 1)
        area_obs_frac = np.sum(y_array * f_overlap * dv)
        N_eff_frac = np.sum(f_overlap)
        sigma_area_frac = rms * dv * np.sqrt(N_eff_frac)
        snr = area_obs_frac / sigma_area_frac
        return snr
    else:
        raise TypeError("'window_selection_method' must be 'fractional' or 'binary'.")

def estimate_rms_profile_fit(area, fwhm, dv, snr):
    """
    Measure the SNR of a line by integrating the emission on the fitted
    gaussian profile

    Parameters
    ----------
    area : `float` or `~astropy.units.Quantity`
        Area of the fitted gaussian line.
    fwhm : `float` or `~astropy.units.Quantity`
        FWHM of the fitted gaussian line.
    dv : `float` or `~astropy.units.Quantity`
        Channel width.
    snr : `float` or `~astropy.units.Quantity`
        Target SNR.

    Returns
    -------
    rms : `float` or `~astropy.units.Quantity`
        Estimated rms for the target SNR.

    """
    sigma_area = area / snr
    rms = sigma_area / (dv * np.sqrt(fwhm/dv))
    return rms

def estimate_rms_peak(peak_int, snr):
    """Estimate the rms for a given peak intensity and desired SNR of a line"""
    rms = peak_int / snr
    return rms
