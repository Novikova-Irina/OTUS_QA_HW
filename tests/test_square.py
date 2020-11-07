import pytest

from framework.Square import Square


@pytest.mark.parametrize("a", [
    2,
    10,
    3
])
def test_square_perimeter_positive(a):
    square = Square('Square', 4, a)
    assert square.square_perimeter() > 0


@pytest.mark.parametrize("a", [
    2,
    10,
    3
])
def test_square_area_positive(a):
    square = Square('Square', 4, a)
    assert square.square_area() > 0


def test_add_square_areas():
    square_1 = Square('Square', 4, 8)
    square_2 = Square('Square', 4, 10)
    assert square_1.add_square(square_2) == square_1.square_area() + square_2.square_area()
