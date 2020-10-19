import random
from datetime import datetime

import pytest


@pytest.fixture
def fixture_return_rnd_number():
    return random.randint(1, 100)


@pytest.fixture
def fixture_get_random_digit(fixture_return_rnd_number):
    range_start = fixture_return_rnd_number
    range_end = fixture_return_rnd_number + 10
    return random.randint(range_start, range_end)


@pytest.fixture(scope='session', autouse=True)
def suite_data():
    print("\n> Suite setup")
    yield
    print("> Suite teardown")


@pytest.fixture(scope='function')
def case_data():
    print("   > Case setup")
    date_time = datetime.now()
    yield str(date_time)
    print("\n   > Case teardown")
