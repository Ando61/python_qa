import pytest
from triangle import Triangle
import math


def test_triangle_creation_valid():
    """Тест корректного создания треугольника"""
    triangle = Triangle(3, 4, 5)
    assert triangle.a == 3
    assert triangle.b == 4
    assert triangle.c == 5


def test_triangle_creation_invalid_negative_sides():
    """Тест некорректного создания треугольника с отрицательными сторонами"""
    with pytest.raises(ValueError, match="Длины сторон треугольника должны быть положительными числами"):
        Triangle(-1, 2, 3)
    with pytest.raises(ValueError, match="Длины сторон треугольника должны быть положительными числами"):
        Triangle(1, 0, 3)
    with pytest.raises(ValueError, match="Длины сторон треугольника должны быть положительными числами"):
        Triangle(1, 2, -3)


def test_triangle_creation_invalid_triangle_inequality():
    """Тест некорректного создания треугольника, который не удовлетворяет неравенству треугольника"""
    with pytest.raises(ValueError, match="Стороны не могут образовать треугольник"):
        Triangle(1, 2, 3)
    with pytest.raises(ValueError, match="Стороны не могут образовать треугольник"):
        Triangle(5, 10, 20)


def test_triangle_get_area():
    """Тест расчета площади треугольника"""
    triangle = Triangle(3, 4, 5)
    assert triangle.get_area() == 6


def test_triangle_get_perimeter():
    """Тест расчета периметра треугольника"""
    triangle = Triangle(3, 4, 5)
    assert triangle.get_perimeter() == 12


def test_triangle_area_invalid():
    """Тест некорректного расчета площади для невалидного треугольника (повторный вызов создания)"""
    with pytest.raises(ValueError, match="Стороны не могут образовать треугольник"):
        Triangle(1, 2, 3).get_area()


def test_triangle_creation_edge_cases():
    """Тест создания треугольника с минимально возможными сторонами, образующими треугольник."""
    triangle = Triangle(1, 1, 1)  # Треугольник со сторонами 1, 1, 1 (равносторонний)
    assert triangle.get_area() == (math.sqrt(3) / 4)
    assert triangle.get_perimeter() == 3
