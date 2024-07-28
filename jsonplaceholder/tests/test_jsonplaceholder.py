import pytest
import requests
from jsonplaceholder.json_schema.json_schema_jsonplaceholder import POST_1


@pytest.mark.parametrize('expected', [100])
def test_number_albums(base_url, expected):
    """Проверка количества альбомов"""
    response = requests.get(f'{base_url}/albums')
    assert response.status_code == 200
    json_dict = response.json()
    assert len(json_dict) == expected


@pytest.mark.parametrize("expected", [1])
def test_postid_in_comments(base_url, expected):
    """Проверяем что в комментариях к посту отображаются только комментарии с номером указанного поста"""
    response = requests.get(f'{base_url}/posts/1/comments')
    assert response.status_code == 200
    json_dict = response.json()
    for i in json_dict:
        assert i["postId"] == expected


@pytest.mark.parametrize('expected', [10])
def test_number_user(base_url, expected):
    """Проверка количества пользователей"""
    response = requests.get(f'{base_url}/users')
    assert response.status_code == 200
    json_dict = response.json()
    assert len(json_dict) == expected


@pytest.mark.parametrize("expected", [None])
def test_delete_comments(base_url, expected):
    """Проверка удаления комментариев к посту"""
    response = requests.get(f'{base_url}/posts/1/comments')
    assert response.status_code == 200
    json_dict = response.json()
    assert json_dict.clear() == expected


def test_get_post_1(base_url):
    """Проверка первого поста"""
    response = requests.get(f'{base_url}/posts/1')
    assert response.status_code == 200
    json_dict = response.json()
    assert json_dict == POST_1
