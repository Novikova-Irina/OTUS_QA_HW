from framework.Figure import Figure


class Rectangle(Figure):
    """Класс Прямоугольник - абсолютный наследник класаа Figure"""

    def __init__(self, name, angles, side_one, side_two):
        """Инициализация.

        Args:
            name: название фигуры
            angle: количество углов фигуры
            side_one: одна сторона прямоугольника
            side_two: вторая сторона прямоугорьника
        """
        super(Rectangle, self).__init__(name, angles, side_one, side_two)
        self.side_one = side_one

    def rectangle_area(self):
        return self._area()
