import math

from framework.Figure import Figure


class Circle(Figure):
    """Класс круг -  наследник класаа Figure"""

    def __init__(self, name, r, angles=None, side_one=None, side_two=None):
        """Инициализация.

        Args:
            name: название фигуры
            r: радиус круга
        """
        super(Circle, self).__init__(name, angles=angles, side_one=side_one, side_two=side_two)
        self.r = r

    def circle_area(self):
        if self.r <= 0:
            raise Exception("Радиус круга не может быть отрицательным значением")
        else:
            return round(math.pi * self.r ** 2, 2)

    def circle_perimeter(self):
        if self.r <= 0:
            raise Exception("Радиус круга не может быть отрицательным значением")
        else:
            return round(2 * math.pi * self.r, 2)
