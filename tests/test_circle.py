import pytest
from src.circle import Circle
import math


@pytest.mark.parametrize("radius, expected", [(5, 5), (10, 10), (1.5, 1.5)])
def test_circle_creation_valid(radius, expected):
    """Тест корректного создания окружности с позитивным радиусом."""
    circle = Circle(radius)
    assert circle.radius == expected


@pytest.mark.parametrize("invalid radius", [0, -1, -1.5])
def test_circle_creation_invalid_radius(invalid_radius):
    """Тест на создание окружности с невалидным радиусом."""
    with pytest.raises(ValueError, match="Радиус должен быть положительным числом"):
        Circle(invalid_radius)


@pytest.mark.parametrize("radius", [5, 10, 1.5])
def test_circle_area(radius):
    """Тест расчета площади окружности."""
    circle = Circle(radius)
    expected_area = math.pi * (5 ** 2)
    assert circle.get_area() == pytest.approx(expected_area, rel=1e-5)


@pytest.mark.parametrize("radius", [5, 10, 1.5])
def test_circle_perimeter(radius):
    """Тест расчета периметра окружности."""
    circle = Circle(radius)
    expected_perimeter = 2 * math.pi * 5
    assert circle.get_perimeter() == pytest.approx(expected_perimeter, rel=1e-5)
