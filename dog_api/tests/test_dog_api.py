import requests
import pytest


@pytest.mark.parametrize("param1,param2", [
    ('Content-Type', "application/json"),
    ('Server', "cloudflare"),
    ("Cf-Cache-Status", 'DYNAMIC')
])
def test_header(param1, param2, base_url):
    """Проверка headers запроса"""
    response = requests.get(f'{base_url}/breeds/image/random')
    assert response.status_code == 200
    assert response.headers[param1] == param2


@pytest.mark.parametrize("expected", ['success'])
def test_status(base_url, expected):
    """Проверка значения ключа status"""
    response = requests.get(f'{base_url}/breed/hound/afghan/images/random')
    assert response.status_code == 200
    status = response.json()['status']
    assert status == expected


@pytest.mark.parametrize("expected", [239])
def test_list_count_breeds(base_url, expected):
    """Проверка количества картинок породы afghan"""
    response = requests.get(f'{base_url}/breed/hound/afghan/images')
    assert response.status_code == 200
    dict_breeds = response.json()['message']
    assert len(dict_breeds) == expected


@pytest.mark.parametrize("expected", [0])
def test_image(base_url, expected):
    """Проверка непустого ответа на запрос картинки"""
    response = requests.get(f'{base_url}/breed/Akita/images/random')
    assert response.status_code == 200
    assert len(response.content) != expected


@pytest.mark.parametrize("expected", [
    (["afghan",
      "basset",
      "blood",
      "english",
      "ibizan",
      "plott",
      "walker"
      ])])
def test_body(base_url, expected):
    """Проверка ожидаемого месседжа"""
    response = requests.get(f'{base_url}/breed/hound/list')
    assert response.status_code == 200
    json_dict = response.json()['message']
    assert json_dict == expected
