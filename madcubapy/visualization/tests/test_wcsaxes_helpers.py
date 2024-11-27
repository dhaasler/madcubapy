import astropy
from astropy.nddata import CCDData
from madcubapy.io import MadcubaMap
from madcubapy.visualization import add_wcs_axes
from madcubapy.visualization import add_manual_wcs_axes
from madcubapy.visualization import append_colorbar
from madcubapy.visualization import add_colorbar
from madcubapy.visualization import parse_clabel
import matplotlib
import matplotlib.pyplot as plt
from pathlib import Path
import pytest

@pytest.fixture
def example_madcuba_map():
    # Create and return a Map instance to be used in tests
    return MadcubaMap.read(
        "madcubapy/io/tests/data/IRAS16293_SO_2-1_moment0_madcuba.fits"
    )

def test_create_wcs_axes(example_madcuba_map):
    fig = plt.figure(figsize=(10,5))
    ax, img = add_wcs_axes(fig, 1, 2, 1, fitsmap=example_madcuba_map)
    assert isinstance(ax, astropy.visualization.wcsaxes.WCSAxes)
    assert isinstance(img, matplotlib.image.AxesImage)

def test_add_colorbar(example_madcuba_map):
    fig = plt.figure(figsize=(10,5))
    ax, img = add_wcs_axes(fig, 1, 2, 1, fitsmap=example_madcuba_map)
    cbar = add_colorbar(ax=ax, location='top', label='custom units')
    assert isinstance(cbar, matplotlib.colorbar.Colorbar)

def test_parse_clabel(example_madcuba_map):
    label = parse_clabel(example_madcuba_map)
    assert label == r'$I \ {\rm (Jy \ beam^{-1} \ m \ s^{-1})}$'
