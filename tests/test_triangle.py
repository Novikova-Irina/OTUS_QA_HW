import pytest

from framework.Triangle import Triangle


@pytest.mark.parametrize("a, b, c", [
    (2, 2, 3),
    (2, 3, 2),
    (3, 2, 2)
])
def test_triangle_perimeter_positive(a, b, c):
    triangle = Triangle('Triangle', 3, a, b, c)
    assert triangle.perimeter_of_triangle() > 0


@pytest.mark.parametrize("a, b, c", [
    (2, 2, 5),
    (2, 5, 2),
])
def test_triangle_area_positive(a, b, c):
    triangle = Triangle('Triangle', 3, a, b, c)
    assert triangle.triangle_area() > 0


@pytest.mark.parametrize("a, b, c", [
    (-2, -2, -3),
    (-2, -3, -2),
])
def test_triangle_negative_side_values(a, b, c):
    triangle = Triangle('Triangle', 3, a, b, c)
    assert not triangle.perimeter_of_triangle() > 0
