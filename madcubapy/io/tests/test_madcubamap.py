from astropy.table import Table
import astropy.units as u
import pytest
from madcubapy.io.madcubamap import MadcubaMap

@pytest.fixture
def example_madcuba_map():
    # Create and return a Map instance to be used in tests
    return MadcubaMap.read(
        "madcubapy/io/tests/data/IRAS16293_SO_2-1_moment0_madcuba.fits"
    )

@pytest.fixture
def example_carta_map():
    # Create and return a Map instance to be used in tests
    return MadcubaMap.read(
        "madcubapy/io/tests/data/IRAS16293_SO2c_moment0_carta.fits"
    )

def test_read_madcuba_map(example_madcuba_map):
    # Test if the obligatory attributes are correctly initialized
    assert example_madcuba_map.ccddata is not None
    assert example_madcuba_map.data is not None
    assert example_madcuba_map.header is not None
    assert (example_madcuba_map.hist is None or
            isinstance(example_madcuba_map.hist, Table))

def test_invalid_file():
    with pytest.raises(FileNotFoundError):
        MadcubaMap.read("nonexistent_file.fits")

def test_fix_units_correct(example_madcuba_map):
    assert example_madcuba_map.unit == u.Jy * u.m / u.beam / u.s
    example_madcuba_map.fix_units()
    assert example_madcuba_map.unit == u.Jy * u.m / u.beam / u.s

def test_fix_units_incorrect(example_carta_map):
    assert example_carta_map.unit == u.Jy / u.beam / u.km / u.s
    example_carta_map.fix_units()
    assert example_carta_map.unit == u.Jy * u.km / u.beam / u.s
