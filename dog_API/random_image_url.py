import requests
import pytest

BASE_URL = 'https://dog.ceo/api/breeds/image/random'
BASE_URL_1 = "https://dog.ceo/api/breed/hound/images"
BASE_URL_HOUND_IMAGES = "https://dog.ceo/api/breed/hound/images"


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


def test_get_images_count():
    response = requests.get(BASE_URL_1)
    data = response.json()
    assert len(data['message']) >= 0, "The number of images should be non-negative."


@pytest.mark.parametrize("expected_status", ["success"])
def test_random_image_url(expected_status):
    """Проверка, что ответ содержит корректный URL изображения"""
    response = requests.get(BASE_URL)
    json_data = response.json()
    assert json_data["status"] == expected_status, "Статус должен быть 'success'"
    assert json_data["message"].startswith("http"), "Должен вернуть корректный URL изображения"
    assert 'jpg' in json_data["message"] or 'png' in json_data[
        "message"], "URL изображения должен содержать 'jpg' или 'png'"


@pytest.mark.parametrize("parameters", [
    BASE_URL,
    BASE_URL_HOUND_IMAGES
])
def test_parametrized_requests(parameters):
    """Проверка различных вызовов API"""
    response = requests.get(parameters)
    assert response.ok, "Запрос должен быть успешным"
    json_data = response.json()
    assert "message" in json_data and "status" in json_data, "Ответ должен содержать нужные ключи"
    assert json_data["status"] == "success", "Статус должен быть 'success'"


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
    assert response.status_code == 200, "Должен вернуть статус 200"
    json_data = response.json()
    assert "message" in json_data, "Ответ должен содержать ключ 'message'"
    assert "status" in json_data, "Ответ должен содержать ключ 'status'"
    assert isinstance(json_data["message"], str), "'message' должен быть строкой"


def test_get_hound_images_count():
    """Проверка количества изображений для породы hound"""
    response = requests.get(BASE_URL_HOUND_IMAGES)
    json_data = response.json()
    assert response.status_code == 200, "Должен вернуть статус 200"
    assert json_data["status"] == "success", "Статус должен быть 'success'"
    assert "message" in json_data, "Ответ должен содержать ключ 'message'"
    assert isinstance(json_data["message"], list), "'message' должен быть списком"
    assert len(json_data["message"]) >= 0, "Количество изображений должно быть ненегативным"

    # Дополнительно проверим, что в каждом элементе списка есть корректный URL изображения
    for image_url in json_data["message"]:
        assert image_url.startswith("http"), "Каждое изображение должно быть URL"
        assert 'jpg' in image_url or 'png' in image_url, "URL изображения должен содержать 'jpg' или 'png'"
