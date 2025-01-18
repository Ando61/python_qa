import pytest
from square import Square


# Параметризация для корректного создания квадрата
@pytest.mark.parametrize("side", [4, 2.5, 1, 3.8])
def test_square_creation_valid(side):
    """Тест корректного создания квадрата"""
    square = Square(side)
    assert square.width == side
    assert square.height == side


# Параметризация для некорректной длины стороны
@pytest.mark.parametrize("side", [0, -1, -3.5])
def test_square_creation_invalid_side(side):
    """Тест некорректной длины стороны квадрата"""
    with pytest.raises(ValueError, match="Сторона должна быть положительным числом."):
        Square(side)


# Параметризация для теста расчета площади
@pytest.mark.parametrize("side, expected_area", [
    (4, 16),
    (2.5, 6.25),
    (3, 9),
    (5, 25)
])
def test_square_get_area(side, expected_area):
    """Тест расчета площади квадрата"""
    square = Square(side)
    assert square.get_area() == expected_area


# Параметризация для теста расчета периметра
@pytest.mark.parametrize("side, expected_perimeter", [
    (4, 16),
    (2, 8),
    (3, 12),
    (1.5, 6)
])
def test_square_get_perimeter(side, expected_perimeter):
    """Тест расчета периметра квадрата"""
    square = Square(side)
    assert square.get_perimeter() == expected_perimeter
