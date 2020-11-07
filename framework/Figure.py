class Figure:
    """Родительский класс Figure"""

    def __init__(self, name, angles, side_one, side_two):
        """Инициализация.

        Args:
            name: название фигуры
            angle: количество углов фигуры
            side_one: одна сторона прямоугольника
            side_two: вторая сторона прямоугорьника
            _area: площадь прямоульника
            perimeter: периметр прямоугольника

        """
        self.name = name
        self.angles = angles
        self.side_one = side_one
        self.side_two = side_two

    def _area(self):
        """Расчет площади"""
        if self.side_one and self.side_two is not None:
            area_fig = self.side_one * self.side_two
            return area_fig
        elif self.side_one is None:
            raise Exception("Здачение стороны - 1 должно быть задано")
        elif self.side_two is None:
            area_fig = self.side_one ** 2
            return area_fig  # возвращает площадь квадрата

    def perimeter(self):
        """Периметр прямоугольника"""
        perimeter_fig = (self.side_one + self.side_two) * 2
        return perimeter_fig

    def add_square(self, name_of_figure):
        if not isinstance(name_of_figure, Figure):
            raise Exception("Аргумент не является объектом класса Figure")
        else:
            return name_of_figure._area() + self._area()
