import pytest
import requests


def pytest_addoption(parser):
    parser.addoption('--url', action='store', default='https://ya.ru', help='URL to check')
    parser.addoption('--status_code', action='store', default='200', help='Expected HTTP status code')


@pytest.mark.parametrize("url, expected_status_code", [
    ("https://ya.ru", 200),
    ("https://ya.ru/sfhfh", 404)
])
def test_api_status_code(pytestconfig, url, expected_status_code):
    url_option = pytestconfig.getoption("url")
    expected_status_code_option = int(pytestconfig.getoption("status_code"))

    if url_option is not None:
        url = url_option
        expected_status_code = expected_status_code_option

    response = requests.get(url)

    assert response.status_code == expected_status_code, f"Expected {expected_status_code}, got {response.status_code}"
