import pytest
import math
from triangle import Triangle


@pytest.mark.parametrize("sides", [
    (3, 4, 5),
    (5, 12, 13),
    (6, 8, 10),
    (7, 24, 25),
])
def test_triangle_creation_valid(sides):
    """Тест корректного создания треугольника"""
    triangle = Triangle(*sides)
    assert triangle.a == sides[0]
    assert triangle.b == sides[1]
    assert triangle.c == sides[2]


@pytest.mark.parametrize("sides", [
    (-1, 2, 3),
    (1, 0, 3),
    (1, 2, -3),
])
def test_triangle_creation_invalid_negative_sides(sides):
    """Тест некорректного создания треугольника с отрицательными сторонами"""
    with pytest.raises(ValueError, match="Длины сторон треугольника должны быть положительными числами"):
        Triangle(*sides)


@pytest.mark.parametrize("sides", [
    (1, 2, 3),
    (5, 10, 20),
])
def test_triangle_creation_invalid_triangle_inequality(sides):
    """Тест некорректного создания треугольника, который не удовлетворяет неравенству треугольника"""
    with pytest.raises(ValueError, match="Стороны не могут образовать треугольник"):
        Triangle(*sides)


@pytest.mark.parametrize("sides, expected_area", [
    ((3, 4, 5), 6),
    ((5, 12, 13), 30),
    ((6, 8, 10), 24),
])
def test_triangle_get_area(sides, expected_area):
    """Тест расчета площади треугольника"""
    triangle = Triangle(*sides)
    assert triangle.get_area() == expected_area


@pytest.mark.parametrize("sides, expected_perimeter", [
    ((3, 4, 5), 12),
    ((5, 12, 13), 30),
    ((6, 8, 10), 24),
])
def test_triangle_get_perimeter(sides, expected_perimeter):
    """Тест расчета периметра треугольника"""
    triangle = Triangle(*sides)
    assert triangle.get_perimeter() == expected_perimeter


def test_triangle_area_invalid():
    """Тест некорректного расчета площади для невалидного треугольника (повторный вызов создания)"""
    with pytest.raises(ValueError, match="Стороны не могут образовать треугольник"):
        Triangle(1, 2, 3).get_area()


def test_triangle_creation_edge_cases():
    """Тест создания треугольника с минимально возможными сторонами, образующими треугольник."""
    triangle = Triangle(1, 1, 1)  # Треугольник со сторонами 1, 1, 1 (равносторонний)
    assert triangle.get_area() == (math.sqrt(3) / 4)
    assert triangle.get_perimeter() == 3
