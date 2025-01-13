from figure import Figure


class Rectangle(Figure):
    def __init__(self, width, height):
        if width <= 0:
            raise ValueError("Ширина должна быть положительным числом.")
        if height <= 0:
            raise ValueError("Высота должна быть положительным числом.")
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * (self.width + self.height)
