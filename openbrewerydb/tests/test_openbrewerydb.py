import pytest
import requests
from jsonschema import validate
from openbrewerydb.json_schema.json_schema_openbrewerydb import SCHEMA_META


@pytest.mark.parametrize("expected", ['b54b16e1-ac3b-4bff-a11f-f7ae9ddc27e0'])
def test_key_id(base_url, expected):
    """Проверка значения ключа id"""
    response = requests.get(f'{base_url}/{expected}')
    assert response.status_code == 200
    assert response.json()['id'] == expected


@pytest.mark.parametrize("expected", ['San Diego'])
def test_city_in_response(base_url, expected):
    """Проверяем что по запросу на San Diego в ответах отображается только San Diego"""
    response = requests.get(f'{base_url}?by_city=san_diego&per_page=3')
    assert response.status_code == 200
    json_dict = response.json()
    for i in json_dict:
        assert i["city"] == expected


@pytest.mark.parametrize('expected', [15])
def test_number_breweries(base_url, expected):
    """Проверка максимального количества возвращенных пивоварен — 15"""
    response = requests.get(f'{base_url}/autocomplete?query=san%20diego')
    assert response.status_code == 200
    json_dict = response.json()
    assert len(json_dict) <= expected


@pytest.mark.parametrize('expected', ['61'])
def test_show_breweries_in_south_korea(base_url, expected):
    """Проверка количества пивоварен в Южной Корее"""
    response = requests.get(f'{base_url}/meta?by_country=south_korea')
    assert response.status_code == 200
    assert response.json()['total'] == expected


@pytest.mark.parametrize('expected', ['micro'])
def test_brewery_type(base_url, expected):
    """Проверка типа brewery при фильтрации"""
    response = requests.get(f'{base_url}?by_type={expected}&per_page=3')
    assert response.status_code == 200
    json_dict = response.json()
    for i in json_dict:
        assert i["brewery_type"] == expected


def test_total_breweries(base_url):
    """Проверка общего количества breweries"""
    response = requests.get(f'{base_url}/meta')
    assert response.status_code == 200
    validate(instance=response.json(), schema=SCHEMA_META)
    assert response.json()['total'] == "8257"
