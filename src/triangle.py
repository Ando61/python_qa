from figure import Figure
import math


class Triangle(Figure):
    def __init__(self, a, b, c):
        if a <= 0 or b <= 0 or c <= 0:
            raise ValueError("Длины сторон треугольника должны быть положительными числами.")
        if a + b <= c or a + c <= b or b + c <= a:
            raise ValueError("Стороны не могут образовать треугольник.")
        self.a = a
        self.b = b
        self.c = c
        if self.a + self.b <= self.c or self.a + self.c <= self.b or self.b + self.c <= self.a:
            raise ValueError("raise ValueError")

    def get_area(self):
        s = self.get_perimeter() / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def get_perimeter(self):
        return self.a + self.b + self.c
