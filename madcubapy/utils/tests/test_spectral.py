import astropy.constants as const
import astropy.units as u
from astropy.constants import c
from astropy.units import Quantity
import numpy as np
import pytest
from madcubapy.utils.spectral import (
    create_spectral_array,
    convert_spectral_resolution,
    obs_to_rest,
    rest_to_obs,
    obs_to_vel,
    vel_to_obs,
    rest_to_vel,
    vel_to_rest,
    measure_snr_peak,
    measure_snr_profile_fit,
    measure_snr_profile_observed,
    estimate_rms_profile_fit,
    estimate_rms_peak
)


def test_create_spectral_array_without_units():
    """Test a specific array without units"""
    assert (create_spectral_array(8, 0.5, -3, 10).all()
         == np.array([11.5, 12, 12.5, 13, 13.5, 14, 14.5, 15]).all())

def test_create_spectral_array_with_units():
    """Test a specific array with units"""
    a = create_spectral_array(8, 0.5 * u.s, -3, 10)
    b = np.array([11.5, 12, 12.5, 13, 13.5, 14, 14.5, 15]) * u.s
    assert a.value.all() == b.value.all()
    assert a.unit == b.unit

@pytest.mark.parametrize("bad_input", [None, [10, 20], "50GHz"])
def test_various_invalid_types(bad_input):
    """Parametrized test for multiple non-Quantity types."""
    rest_freq = 100 * u.GHz
    with pytest.raises(TypeError):
        convert_spectral_resolution(bad_input, rest_freq)

def test_convert_spectral_resolution_incompatible_unit():
    """Test that UnitConversionError is raised for wrong physical dimensions."""
    rest_freq = 100 * u.GHz
    spectral_res = 5 * u.m
    with pytest.raises(u.UnitConversionError, 
                       match="is not a valid spectral resolution unit"):
        convert_spectral_resolution(spectral_res, rest_freq)

def test_correct_output_unit_frequency_to_velocity():
    """If input is Hz, output must be equivalent to km/s."""
    rest_freq = 100 * u.GHz
    spectral_res = 1 * u.MHz
    result = convert_spectral_resolution(spectral_res, rest_freq)
    assert result.unit.is_equivalent(u.km / u.s)

def test_correct_output_value_frequency_to_velocity():
    """If input is Hz, output must be equivalent to km/s."""
    rest_freq = 100 * u.GHz
    spectral_res = 1 * u.MHz
    result = convert_spectral_resolution(spectral_res, rest_freq)
    expected = (c * (1 * u.MHz / (100 * u.GHz))).to(u.km / u.s)
    assert pytest.approx(result.value) == expected.value

def test_correct_output_unit_velocity_to_frequency():
    """If input is km/s, output must be equivalent to Hz."""
    rest_freq = 100 * u.GHz
    spectral_res = 10 * u.km / u.s
    result = convert_spectral_resolution(spectral_res, rest_freq)
    assert result.unit.is_equivalent(u.Hz)

def test_correct_output_value_velocity_to_frequency():
    """If input is km/s, output must be equivalent to Hz."""
    rest_freq = 100 * u.GHz
    spectral_res = 10 * u.km / u.s
    result = convert_spectral_resolution(spectral_res, rest_freq)
    expected = (rest_freq * (10 * u.km / u.s / c)).to(u.Hz)
    assert pytest.approx(result.value) == expected.value

# Global precalculated values
rest_array = (266, 267) * u. GHz
rest_single = 266 * u. GHz
obs_array_rad = (263.33815852, 264.3281516) * u.GHz
obs_array_rel = (263.35134466, 264.3413873) * u.GHz
vel_array_rad = (2999.99999999999, 1884.23887969924) * u.km / u.s
vel_array_rel = (2999.99999999999, 1875.14957479892) * u.km / u.s
vel_single = 3000 * u.km / u.s

def test_rest_to_obs_result():
    """Test rest_to_obs results"""
    assert np.allclose(
        rest_to_obs(rest_array, vel_single, "radio").value,
        obs_array_rad.value,
        atol=1e-5, rtol=0
    )
    assert np.allclose(
        rest_to_obs(rest_array, vel_single, "relativistic").value,
        obs_array_rel.value,
        atol=1e-5, rtol=0
    )
    assert not np.allclose(
        rest_to_obs(rest_array, vel_single, "radio").value,
        obs_array_rel.value,
        atol=1e-5, rtol=0
    )
    assert not np.allclose(
        rest_to_obs(rest_array, vel_single, "relativistic").value,
        obs_array_rad.value,
        atol=1e-5, rtol=0
    )

def test_obs_to_rest_result():
    """Test obs_to_rest results"""
    assert np.allclose(
        obs_to_rest(obs_array_rad, vel_single, "radio").value,
        rest_array.value,
        atol=1e-5, rtol=0
    )
    assert np.allclose(
        obs_to_rest(obs_array_rel, vel_single, "relativistic").value,
        rest_array.value,
        atol=1e-5, rtol=0
    )
    assert not np.allclose(
        obs_to_rest(obs_array_rel, vel_single, "radio").value,
        rest_array.value,
        atol=1e-5, rtol=0
    )
    assert not np.allclose(
        obs_to_rest(obs_array_rad, vel_single, "relativistic").value,
        rest_array.value,
        atol=1e-5, rtol=0
    )

def test_obs_to_vel_result():
    """Test obs_to_vel results"""
    assert np.allclose(
        obs_to_vel(obs_array_rad, rest_single, "radio").to(u.km / u.s).value,
        vel_array_rad.to(u.km / u.s).value,
        atol=1e-5, rtol=0
    )
    assert np.allclose(
        obs_to_vel(obs_array_rel, rest_single, "relativistic").to(u.km / u.s).value,
        vel_array_rel.to(u.km / u.s).value,
        atol=1e-5, rtol=0
    )
    assert not np.allclose(
        obs_to_vel(obs_array_rel, rest_single, "radio").to(u.km / u.s).value,
        vel_array_rad.to(u.km / u.s).value,
        atol=1e-5, rtol=0
    )
    assert not np.allclose(
        obs_to_vel(obs_array_rad, rest_single, "relativistic").to(u.km / u.s).value,
        vel_array_rel.to(u.km / u.s).value,
        atol=1e-5, rtol=0
    )

def test_vel_to_obs_result():
    """Test vel_to_obs results"""
    assert np.allclose(
        vel_to_obs(vel_array_rad, rest_single, "radio").to(u.GHz).value,
        obs_array_rad.to(u.GHz).value,
        atol=1e-5, rtol=0
    )
    assert np.allclose(
        vel_to_obs(vel_array_rel, rest_single, "relativistic").to(u.GHz).value,
        obs_array_rel.to(u.GHz).value,
        atol=1e-5, rtol=0
    )
    assert not np.allclose(
        vel_to_obs(vel_array_rel, rest_single, "radio").to(u.GHz).value,
        obs_array_rel.to(u.GHz).value,
        atol=1e-5, rtol=0
    )
    assert not np.allclose(
        vel_to_obs(vel_array_rad, rest_single, "relativistic").to(u.GHz).value,
        obs_array_rad.to(u.GHz).value,
        atol=1e-5, rtol=0
    )

def test_rest_to_vel_result():
    """Test rest_to_vel results"""
    assert np.allclose(
        rest_to_vel(rest_array, vel_single, rest_single, "radio").to(u.km / u.s).value,
        vel_array_rad.to(u.km / u.s).value,
        atol=1e-5, rtol=0
    )
    assert np.allclose(
        rest_to_vel(rest_array, vel_single, rest_single, "relativistic").to(u.km / u.s).value,
        vel_array_rel.to(u.km / u.s).value,
        atol=1e-5, rtol=0
    )
    assert not np.allclose(
        rest_to_vel(rest_array, vel_single, rest_single, "radio").to(u.km / u.s).value,
        vel_array_rel.to(u.km / u.s).value,
        atol=1e-5, rtol=0
    )
    assert not np.allclose(
        rest_to_vel(rest_array, vel_single, rest_single, "relativistic").to(u.km / u.s).value,
        vel_array_rad.to(u.km / u.s).value,
        atol=1e-5, rtol=0
    )

def test_vel_to_rest_result():
    """Test vel_to_rest results"""
    assert np.allclose(
        vel_to_rest(vel_array_rad, vel_single, rest_single, "radio").to(u.GHz).value,
        rest_array.to(u.GHz).value,
        atol=1e-5, rtol=0
    )
    assert np.allclose(
        vel_to_rest(vel_array_rel, vel_single, rest_single, "relativistic").to(u.GHz).value,
        rest_array.to(u.GHz).value,
        atol=1e-5, rtol=0
    )
    assert not np.allclose(
        vel_to_rest(vel_array_rel, vel_single, rest_single, "radio").to(u.GHz).value,
        rest_array.to(u.GHz).value,
        atol=1e-5, rtol=0
    )
    assert not np.allclose(
        vel_to_rest(vel_array_rad, vel_single, rest_single, "relativistic").to(u.GHz).value,
        rest_array.to(u.GHz).value,
        atol=1e-5, rtol=0
    )

def test_measure_snr_peak_basic():
    # Simple float test
    assert measure_snr_peak(10.0, 2.0) == 5.0
    # Quantity test
    peak = 10.0 * u.Jy
    rms = 2.0 * u.Jy
    assert measure_snr_peak(peak, rms).value == 5.0
    assert measure_snr_peak(peak, rms).unit.is_unity()

def test_measure_snr_peak_type_error():
    with pytest.raises(TypeError, match="must be a float or astropy Quantity"):
        measure_snr_peak("10", 2.0)

def test_measure_snr_profile_fit_consistency_float():
    area = 10.0
    fwhm = 2.0
    dv = 0.5
    rms = 0.1
    snr = measure_snr_profile_fit(area, fwhm, dv, rms)
    assert np.isclose(snr, 100.0)

def test_measure_snr_profile_fit_consistency_quantity():
    area = 10.0 * u.K * u.km / u.s
    fwhm = 2.0 * u.km / u.s
    dv = 0.5 * u.km / u.s
    rms = 0.1 * u.K
    snr = measure_snr_profile_fit(area, fwhm, dv, rms)
    assert np.isclose(snr, 100.0)

@pytest.mark.parametrize(
    "parameter, value",
    [
        ("area", "3"),
        ("area", u.km),

        ("fwhm", "3"),
        ("fwhm", u.km),

        ("dv", "3"),
        ("dv", u.km),

        ("rms", "3"),
        ("rms", u.km),        
    ],
)
def test_invalid_init_types(parameter, value):
    with pytest.raises(TypeError):
        measure_snr_profile_fit(**{parameter: value})

@pytest.fixture
def sample_spectrum():
    """Creates a simple box 'line' for testing integration."""
    dv = 1.0
    x = np.arange(-10, 11, dv) * u.km/u.s
    y = np.zeros_like(x.value) * u.K
    # Put a flat signal of 1.0 Jy from -2 to 2
    y[(x.value >= -2) & (x.value <= 2)] = 1.0 * u.K
    return x, y, dv * u.km/u.s

def test_measure_snr_observed_binary(sample_spectrum):
    """Test simple known snr value in binary mask."""
    x, y, dv = sample_spectrum
    v0 = 0.0 * u.km / u.s
    fwhm = 2.355 * u.km / u.s  # sigma = 1
    rms = 0.1 * u.K
    # sigma window = 3 accounts for 7 channels: (-3, -2, -1, 0, 1, 2, 3)
    nchan = 7
    snr = measure_snr_profile_observed(x, y, v0, fwhm, dv, rms, 
                                       window_sigma_factor=3, 
                                       window_selection_method="binary")
    expected_area = 5.0  # (y=1 for -2, -1, 0, 1, 2) * dv=1
    expected_sigma_area = 0.1 * 1.0 * np.sqrt(nchan)
    assert np.isclose(snr.value, expected_area / expected_sigma_area)

def test_measure_snr_observed_fractional_edges():
    """Test simple known snr value in fractional mask."""
    # Test that fractional logic handles sub-channel windows
    x = np.array([0.0]) * u.km/u.s
    y = np.array([1.0]) * u.Jy
    dv = 1.0 * u.km/u.s
    v0 = 0.0 * u.km/u.s
    fwhm = 2.355 * u.km/u.s # sigma = 1
    rms = 0.1 * u.Jy
    # Force a window that only covers half the center channel
    # (factor=0.5, so window is +/- 0.5)
    # The channel spans -0.5 to 0.5. Window is -0.5 to 0.5. Overlap should be 1.0.
    snr = measure_snr_profile_observed(x, y, v0, fwhm, dv, rms, 
                                       window_sigma_factor=0.5, 
                                       window_selection_method="fractional")
    assert snr > 0

def test_measure_snr_observed_invalid_method(sample_spectrum):
    x, y, dv = sample_spectrum
    with pytest.raises(TypeError, match="must be 'fractional' or 'binary'"):
        measure_snr_profile_observed(x, y, 0, 1, dv, 0.1,
                                     window_selection_method="invalid")

def test_rms_estimation_roundtrip():
    """Verify that estimating RMS and then measuring SNR returns the original SNR."""
    area = 50.0 * (u.Jy * u.km/u.s)
    fwhm = 10.0 * u.km/u.s
    dv = 1.0 * u.km/u.s
    target_snr = 25.0
    estimated_rms = estimate_rms_profile_fit(area, fwhm, dv, target_snr)
    calculated_snr = measure_snr_profile_fit(area, fwhm, dv, estimated_rms)
    assert np.isclose(calculated_snr, target_snr)

def test_estimate_rms_peak():
    assert estimate_rms_peak(10.0, 5.0) == 2.0
