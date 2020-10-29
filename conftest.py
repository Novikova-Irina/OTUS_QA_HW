import pytest
import requests


def pytest_addoption(parser):
    parser.addoption("--url", action="store", default="https://jsonplaceholder.typicode.com/todos")


@pytest.fixture(scope="session")
def workplace(request):
    url = request.config.getoption("--url")
    return url


@pytest.fixture(scope="session")
def create_session():
    return requests.Session()
