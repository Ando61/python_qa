import pytest
from figure import Figure
from rectangle import Rectangle


def test_rectangle_creation_valid():
    """Тест корректного создания прямоугольника"""
    rect = Rectangle(4, 5)
    assert rect.width == 4
    assert rect.height == 5


def test_rectangle_creation_invalid_width():
    """Тест некорректной ширины"""
    with pytest.raises(ValueError, match="Ширина должна быть положительным числом"):
        Rectangle(0, 5)
    with pytest.raises(ValueError, match="Ширина должна быть положительным числом"):
        Rectangle(-1, 5)


def test_rectangle_creation_invalid_height():
    """Тест некорректной высоты"""
    with pytest.raises(ValueError, match="Высота должна быть положительным числом"):
        Rectangle(4, 0)
    with pytest.raises(ValueError, match="Высота должна быть положительным числом"):
        Rectangle(4, -1)


def test_get_area():
    """Тест расчета площади прямоугольника"""
    rect = Rectangle(4, 5)
    assert rect.get_area() == 20
    rect = Rectangle(2, 3.5)
    assert rect.get_area() == 7


def test_get_perimeter():
    """Тест расчета периметра прямоугольника"""
    rect = Rectangle(4, 5)
    assert rect.get_perimeter() == 18
    rect = Rectangle(2, 3.5)
    assert rect.get_perimeter() == 11
