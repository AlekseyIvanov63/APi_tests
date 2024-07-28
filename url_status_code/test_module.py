import requests


def test_url_and_status_code(base_url, status_code):
    """Проверка статуса кода"""
    response = requests.get(base_url)
    assert response.status_code == int(status_code)
