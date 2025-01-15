import pytest
from src.circle import Circle
import math


def test_circle_creation_valid():
    """Тест корректного создания окружности с позитивным радиусом."""
    circle = Circle(5)
    assert circle.radius == 5


def test_circle_creation_invalid_radius():
    """Тест на создание окружности с невалидным радиусом."""
    with pytest.raises(ValueError, match="Радиус должен быть положительным числом"):
        Circle(0)
    with pytest.raises(ValueError, match="Радиус должен быть положительным числом"):
        Circle(-3)


def test_circle_area():
    """Тест расчета площади окружности."""
    circle = Circle(5)
    expected_area = math.pi * (5 ** 2)
    assert circle.get_area() == pytest.approx(expected_area, rel=1e-5)


def test_circle_perimeter():
    """Тест расчета периметра окружности."""
    circle = Circle(5)
    expected_perimeter = 2 * math.pi * 5
    assert circle.get_perimeter() == pytest.approx(expected_perimeter, rel=1e-5)