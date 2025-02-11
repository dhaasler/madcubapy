from madcubapy.visualization import measure_noise
from madcubapy.visualization import get_input
import pytest

def test_invalid_object_type_measure_noise():
    with pytest.raises(TypeError):
        measure_noise("string")
    with pytest.raises(TypeError):
        measure_noise(999)

def test_invalid_object_type_get_input():
    with pytest.raises(TypeError):
        get_input("string")
    with pytest.raises(TypeError):
        get_input(999)