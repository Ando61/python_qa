import requests
import pytest

BASE_URL = 'https://api.openbrewerydb.org/v1/breweries/'


def get_brewery_by_id(brewery_id):
    response = requests.get(f"{BASE_URL}{brewery_id}")
    return response


def test_existing_brewery():
    """Получение списка пивоварен и выбора существующих ID"""
    response = requests.get(BASE_URL)
    assert response.status_code == 200, "Failed to fetch breweries"
    breweries = response.json()

    assert len(breweries) > 0, "No breweries found"
    brewery_id = breweries[0]['id']  # Используйте ID первой пивоварни из списка
    response = get_brewery_by_id(brewery_id)

    assert response.status_code == 200, f"Expected status code 200 but got {response.status_code}"
    data = response.json()
    assert 'id' in data, "Response does not contain 'id'"
    assert data['id'] == brewery_id, "The brewery ID in the response does not match the requested ID"


def test_non_existing_brewery():
    """Несуществующий идентификатор"""
    brewery_id = 'nonexistent-id'
    response = get_brewery_by_id(brewery_id)

    assert response.status_code == 404, f"Expected status code 404 but got {response.status_code}"
    message = response.json().get('message', '')
    assert "can't access" in message, "Expected error message not found"


state_min_breweries = {
    "California": 25,
    "Texas": 20,
    "New York": 15
}


@pytest.mark.parametrize("state, expected_status_code, expected_length", [
    ("California", 200, None),
    ("Texas", 200, None),
    ("New York", 200, None),
    ("NonExistentState", 200, 0)
])
def test_filter_breweries_by_state(state, expected_status_code, expected_length):
    params = {'by_state': state.replace(" ", "%20")}
    response = requests.get(BASE_URL, params=params)

    assert response.status_code == expected_status_code, f'Expected status code {expected_status_code} but got {response.status_code}'

    breweries = response.json() if expected_status_code == 200 else []

    assert len(breweries) >= 0, "Breweries count should not be negative"
    print(f"Received {len(breweries)} breweries in {state}")

    if expected_length is None:
        print(f"Received breweries in {state}: {breweries}")

    min_breweries = state_min_breweries.get(state)
    if min_breweries is not None:
        assert len(breweries) >= min_breweries, f"Expected at least {min_breweries} breweries in {state}"
    elif expected_length is not None:
        assert len(breweries) == expected_length, f"Expected exactly {expected_length} breweries in {state}"


@pytest.mark.parametrize("brewery_type, expected_status_code, expected_min_length", [
    ("micro", 200, 1),
    ("brewpub", 200, 1),
    ("contract", 200, 1),
    ("NonExistentType", 400, 0)
])
def test_filter_breweries_by_type(brewery_type, expected_status_code, expected_min_length):
    params = {'by_type': brewery_type.replace(" ", "%20")}
    response = requests.get(BASE_URL, params=params)

    assert response.status_code == expected_status_code, f"Expected status code {expected_status_code} but got {response.status_code}"

    if expected_status_code == 200:
        breweries = response.json()
        assert len(
            breweries) >= expected_min_length, f"Expected at least {expected_min_length} breweries of type {brewery_type}, but got {len(breweries)}"
