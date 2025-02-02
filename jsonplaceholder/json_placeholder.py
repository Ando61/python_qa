import requests
import pytest

BASE_URL = 'https://jsonplaceholder.typicode.com/posts'


def test_get_post_by_id():
    """Тестирование получения поста по ID"""
    response = requests.get(f'{BASE_URL}/1')
    json_data = response.json()
    assert response.status_code == 200, "Статус код должен быть 200"
    assert json_data['id'] == 1, "Должен вернуть пост с id 1"
    assert 'title' in json_data, "Ответ должен содержать заголовок поста"
    assert 'body' in json_data, "Ответ должен содержать тело поста"
    assert 'userId' in json_data, "Ответ должен содержать userId"


def test_list_all_posts():
    """Тестирование получения всех постов"""
    response = requests.get(BASE_URL)
    json_data = response.json()
    assert response.status_code == 200, "Статус код должен быть 200"
    assert isinstance(json_data, list), "Ответ должен быть списком"
    assert len(json_data) > 0, "Список постов не должен быть пустым"


@pytest.mark.parametrize("data, expected_user_id", [
    ({"title": "foo", "body": "bar", "userId": 1}, 1),
    ({"title": "baz", "body": "qux", "userId": 2}, 2),
])
def test_create_post(data, expected_user_id):
    """Тестирование создания поста"""
    response = requests.post(BASE_URL, json=data)
    json_data = response.json()
    assert response.status_code == 201, "Статус код должен быть 201"
    assert 'id' in json_data, "Ответ должен содержать id созданного поста"
    assert json_data['title'] == data['title'], "Заголовок должен соответствовать отправленному"
    assert json_data['userId'] == expected_user_id, "userId должен соответствовать отправленному"


@pytest.mark.parametrize("post_id, update_data", [
    (1, {"title": "updated title"}),
    (2, {"body": "updated body"}),
])
def test_update_post(post_id, update_data):
    """Тестирование обновления поста"""
    response = requests.put(f'{BASE_URL}/{post_id}', json={**{"id": post_id}, **update_data})
    json_data = response.json()
    assert response.status_code == 200, "Статус код должен быть 200"
    assert json_data['id'] == post_id, "ID поста должен остаться прежним"
    for key in update_data:
        assert json_data[key] == update_data[key], f"{key} должен быть обновлен"


def test_delete_post():
    """Тестирование удаления поста"""
    response = requests.delete(f'{BASE_URL}/1')
    assert response.status_code == 200, "Статус код должен быть 200"


def test_filter_posts_by_user():
    """Тестирование фильтрации постов по userId"""
    response = requests.get(f'{BASE_URL}?userId=1')
    json_data = response.json()
    assert response.status_code == 200, "Статус код должен быть 200"
    assert isinstance(json_data, list), "Ответ должен быть списком"
    for post in json_data:
        assert post['userId'] == 1, "Все посты должны принадлежать userId 1"
