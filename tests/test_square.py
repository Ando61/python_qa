import pytest
from square import Square


def test_square_creation_valid():
    """Тест корректного создания квадрата"""
    square = Square(4)
    assert square.width == 4
    assert square.height == 4


def test_square_creation_invalid_side():
    """Тест некорректной длины стороны квадрата"""
    with pytest.raises(ValueError, match="Сторона должна быть положительным числом."):
        Square(0)
    with pytest.raises(ValueError, match="Сторона должна быть положительным числом."):
        Square(-1)


def test_square_get_area():
    """Тест расчета площади квадрата"""
    square = Square(4)
    assert square.get_area() == 16
    square = Square(2.5)
    assert square.get_area() == 6.25


def test_square_get_perimeter():
    """Тест расчета периметра квадрата"""
    square = Square(4)
    assert square.get_perimeter() == 16
    square = Square(2)
    assert square.get_perimeter() == 8
