import numpy as np
from numpy.testing import assert_allclose

from geonet.geometry import unit_vector, angle_between

def test_unit_vector():
    v1 = np.array([1, 0, 0])
    assert_allclose(unit_vector(v1), v1)

    v2 = np.array([1, 1, 0])
    u2 = unit_vector(v2)
    assert_allclose(np.linalg.norm(u2), 1.0)

def test_angle_between():
    v1 = np.array([1, 1])
    v2 = np.array([1, 0])
    v3 = np.array([0, 1])

    for v in (v1, v2, v3):
        assert_allclose(angle_between(v, v), 0.0, atol=1e-6)

    assert_allclose(angle_between(v1, v2), np.pi/4, atol=1e-6)
    assert_allclose(angle_between(v2, v1), np.pi/4, atol=1e-6)
    assert_allclose(angle_between(v2, v3), np.pi/2, atol=1e-6)
    assert_allclose(angle_between(v3, v2), np.pi/2, atol=1e-6)
