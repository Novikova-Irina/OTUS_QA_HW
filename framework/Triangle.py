import math

from framework.Figure import Figure


class Triangle(Figure):
    """Класс Треугольник - наследник класcа Figure"""

    def __init__(self, name, angles, side_one, side_two, side_three):
        """Инициализация.

        Args:
            name: название фигуры
            angle: количество углов фигуры
            side_one: одна сторона треугольника
            side_two: вторая сторона треугольника
            side_three: третья сторона треугольника

        """
        super(Triangle, self).__init__(name, angles, side_one, side_two)
        self.side_one = side_one
        self.side_two = side_two
        self.side_three = side_three
        self._perimeter = self.side_one + self.side_two + self.side_three

    def perimeter_of_triangle(self):
        return self._perimeter

    def triangle_area(self):
        p = self._perimeter
        area = math.sqrt(p * (p - self.side_one) * (p - self.side_two) * (p - self.side_three))
        return round(area, 2)
