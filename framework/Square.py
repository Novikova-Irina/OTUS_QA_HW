from framework.Figure import Figure


class Square(Figure):
    """Класс Квадрат - наследник класаа Figure"""

    def __init__(self, name, angles, side_one, side_two=None):
        """Инициализация.

        Args:
            name: название фигуры
            angle: количество углов фигуры
            side_one: одна сторона квадрата
        """
        super(Square, self).__init__(name, angles, side_one, side_two=side_two)
        self.side_one = side_one

    def square_area(self):
        square_area = self.side_one ** 2
        return square_area

    def square_perimeter(self):
        return 4 * self.side_one
