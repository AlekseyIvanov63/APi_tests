import pytest


def pytest_addoption(parser):
    """Параметры для тестов"""
    parser.addoption('--url',
                     default='https://ya.ru',
                     help='This is request url')

    parser.addoption('--status_code',
                     default='200',
                     help='This is response status_code')


@pytest.fixture
def base_url(request):
    """Фикстура для перадачи url"""
    return request.config.getoption('--url')


@pytest.fixture
def status_code(request):
    """Фикстура для перадачи status_code"""
    return request.config.getoption('--status_code')
