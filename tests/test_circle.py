import pytest

from framework.Circle import Circle


@pytest.mark.parametrize("r", [
    2,
    10,
    3
])
def test_circle_perimeter_positive(r):
    circle = Circle('Circle', r)
    assert circle.circle_perimeter() > 0


@pytest.mark.parametrize("r", [
    2,
    10,
    3
])
def test_circle_area_positive(r):
    circle = Circle('Circle', r)
    assert circle.circle_area() > 0
