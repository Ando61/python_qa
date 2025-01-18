import pytest
import math
from rectangle import Rectangle
from square import Square
from triangle import Triangle
from circle import Circle


@pytest.mark.parametrize("width, height, expected_area, expected_perimeter", [
    (3, 4, 12, 14),  # Тест для прямоугольника 3x4
    (5, 5, 25, 20),  # Тест для квадрата 5x5
    (2, 2, 4, 8)  # Тест для квадрата 2x2
])
def test_rectangle_and_square(width, height, expected_area, expected_perimeter):
    if width == height:  # Если это квадрат
        square = Square(width)
        assert square.get_area() == expected_area
        assert square.get_perimeter() == expected_perimeter
    else:  # Если это прямоугольник
        rectangle = Rectangle(width, height)
        assert rectangle.get_area() == expected_area
        assert rectangle.get_perimeter() == expected_perimeter


@pytest.mark.parametrize("a, b, c, expected_area, expected_perimeter", [
    (3, 4, 5, 6, 12),  # Тест для треугольника с длинами сторон 3, 4, 5
    (5, 5, 5, 10.8253, 15),  # Тест для равностороннего треугольника
])
def test_triangle(a, b, c, expected_area, expected_perimeter):
    triangle = Triangle(a, b, c)
    assert math.isclose(triangle.get_area(), expected_area, rel_tol=1e-4)  # Сравнение с точностью
    assert triangle.get_perimeter() == expected_perimeter


@pytest.mark.parametrize("radius, expected_area, expected_perimeter", [
    (1, math.pi, 2 * math.pi),  # Тест для круга с радиусом 1
    (2, 4 * math.pi, 4 * math.pi),  # Тест для круга с радиусом 2
])
def test_circle(radius, expected_area, expected_perimeter):
    circle = Circle(radius)
    assert math.isclose(circle.get_area(), expected_area, rel_tol=1e-4)  # Сравнение с точностью
    assert math.isclose(circle.get_perimeter(), expected_perimeter, rel_tol=1e-4)


@pytest.mark.parametrize("figure_a, figure_b, expected_area_sum", [
    (Rectangle(3, 4), Rectangle(2, 5), 26),  # Сложение площадей прямоугольников
    (Circle(1), Circle(2), 1 * math.pi + 4 * math.pi),  # Сложение площадей кругов
])
def test_add_area(figure_a, figure_b, expected_area_sum):
    assert math.isclose(figure_a.add_area(figure_b), expected_area_sum, rel_tol=1e-4)


def test_invalid_triangle():
    with pytest.raises(ValueError):
        Triangle(1, 2, 3)  # Этот треугольник не существует


def test_invalid_rectangle():
    with pytest.raises(ValueError):
        Rectangle(-1, 4)  # Отрицательная ширина


def test_invalid_circle():
    with pytest.raises(ValueError):
        Circle(-1)  # Отрицательный радиус


@pytest.mark.parametrize("invalid_radius", [
    -1,
    -5,
    -10
])
def test_circle_creation_invalid_radius(invalid_radius):
    with pytest.raises(ValueError):
        Circle(invalid_radius)  # Проверяем создание круга с отрицательным радиусом
