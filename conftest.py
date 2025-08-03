from datetime import datetime

import pytest


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
