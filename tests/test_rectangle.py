import pytest

from framework.Rectangle import Rectangle


@pytest.mark.parametrize("a, b", [
    (2, 6),
    (10, 15),
    (3, 8)
])
def test_rectangle_perimeter_positive(a, b):
    rectangle = Rectangle('Rectangle', 4, a, b)
    assert rectangle.perimeter() > 0


@pytest.mark.parametrize("a, b", [
    (2, 6),
    (10, 15),
    (3, 8)
])
def test_rectangle_area_positive(a, b):
    rectangle = Rectangle('Rectangle', 4, a, b)
    assert rectangle._area() > 0


def test_add_rectangle_areas():
    rectangle_1 = Rectangle('Rectangle', 4, 8, 16)
    rectangle_2 = Rectangle('Rectangle', 4, 10, 5)
    assert rectangle_1.add_square(rectangle_2) == rectangle_1._area() + rectangle_2._area()
