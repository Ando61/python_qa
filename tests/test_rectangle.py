import pytest
from rectangle import Rectangle


# Параметризация для корректного создания прямоугольника
@pytest.mark.parametrize("width, height", [
    (4, 5),
    (2, 3.5),
    (1, 1),
    (10, 2)
])
def test_rectangle_creation_valid(width, height):
    """Тест корректного создания прямоугольника"""
    rect = Rectangle(width, height)
    assert rect.width == width
    assert rect.height == height


# Параметризация для некорректной ширины
@pytest.mark.parametrize("width", [
    0,
    -1
])
def test_rectangle_creation_invalid_width(width):
    """Тест некорректной ширины"""
    with pytest.raises(ValueError, match="Ширина должна быть положительным числом"):
        Rectangle(width, 5)


# Параметризация для некорректной высоты
@pytest.mark.parametrize("height", [
    0,
    -1
])
def test_rectangle_creation_invalid_height(height):
    """Тест некорректной высоты"""
    with pytest.raises(ValueError, match="Высота должна быть положительным числом"):
        Rectangle(4, height)


# Параметризация для теста расчета площади
@pytest.mark.parametrize("width, height, expected_area", [
    (4, 5, 20),
    (2, 3.5, 7),
    (1, 1, 1),
    (10, 2, 20)
])
def test_get_area(width, height, expected_area):
    """Тест расчета площади прямоугольника"""
    rect = Rectangle(width, height)
    assert rect.get_area() == expected_area


# Параметризация для теста расчета периметра
@pytest.mark.parametrize("width, height, expected_perimeter", [
    (4, 5, 18),
    (2, 3.5, 11),
    (1, 1, 4),
    (10, 2, 24)
])
def test_get_perimeter(width, height, expected_perimeter):
    """Тест расчета периметра прямоугольника"""
    rect = Rectangle(width, height)
    assert rect.get_perimeter() == expected_perimeter
