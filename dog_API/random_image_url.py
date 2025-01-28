import requests
import pytest

BASE_URL = 'https://dog.ceo/api/breeds/image/random'


@pytest.mark.parametrize("expected_status", ["success"])
def test_random_image_url(expected_status):
    """Проверка, что ответ содержит корректный URL изображения"""
    response = requests.get(BASE_URL)
    json_data = response.json()
    assert json_data["status"] == expected_status, "Статус должен быть 'success'"
    assert json_data["message"].startswith("http"), "Должен вернуть корректный URL изображения"


@pytest.mark.parametrize("parameters", [
    "https://dog.ceo/api/breeds/image/random",
    "https://dog.ceo/api/breeds/image/random",
])
def test_parametrized_requests(parameters):
    """Проверка различных вызовов API"""
    response = requests.get(parameters)
    assert response.ok, "Запрос должен быть успешным"
    json_data = response.json()
    assert "message" in json_data and "status" in json_data, "Ответ должен содержать нужные ключи"


def test_random_image_response_status():
    """Проверка успешного ответа сервиса"""
    response = requests.get(BASE_URL)
    assert response.status_code == 200, "Должен вернуть статус 200"


def test_random_image_status():
    """Проверка, что статус ответа равен 'success'"""
    response = requests.get(BASE_URL)
    json_data = response.json()
    assert json_data["status"] == "success", "Статус должен быть 'success'"


def test_random_image_response_structure():
    """Проверка структуры JSON ответа"""
    response = requests.get(BASE_URL)
    assert response.status_code == 200
    json_data = response.json()
    assert "message" in json_data, "Ответ должен содержать ключ 'message'"
    assert "status" in json_data, "Ответ должен содержать ключ 'status'"
