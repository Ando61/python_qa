from abc import ABC, abstractmethod
import pytest
import math
from rectangle import Rectangle
from square import Square
from triangle import Triangle
from circle import Circle


class Figure(ABC):
    @abstractmethod
    def get_area(self):
        pass

    @abstractmethod
    def get_perimeter(self):
        pass

    def add_area(self, figure):
        if not isinstance(figure, Figure):
            raise ValueError("Неверный тип: ожидаем объект класса 'Figure'")
        return self.get_area() + figure.get_area()


@pytest.mark.parametrize("fig1, fig2, expected_area", [
    (Triangle(3, 4, 5), Triangle(5, 12, 13), 36),  # 6 + 30
    (Rectangle(2, 3), Triangle(3, 4, 5), 12),  # 6 + 6
    (Triangle(6, 8, 10), Rectangle(2, 3), 30),  # 24 + 6
])
def test_add_area_valid(fig1, fig2, expected_area):
    """Тест корректного добавления площадей двух фигур"""
    assert fig1.add_area(fig2) == expected_area


@pytest.mark.parametrize("fig1, not_a_figure", [
    (Triangle(3, 4, 5), "строка"),
    (Rectangle(2, 3), 5),
    (Triangle(6, 8, 10), None),
])
def test_add_area_invalid_type(fig1, not_a_figure):
    """Тест обработки ошибки при передаче неверного типа"""
    with pytest.raises(ValueError, match="Неверный тип: ожидаем объект класса 'Figure'"):
        fig1.add_area(not_a_figure)
