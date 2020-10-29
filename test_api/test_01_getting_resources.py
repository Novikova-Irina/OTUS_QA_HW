import pytest

from test_api.constant import TestData


@pytest.mark.parametrize('todos_id', [1, 2, 5, TestData.TODOS_VALUE])
def test_get_positive(workplace, create_session, todos_id):
    result = create_session.get(url=f'{workplace}/{todos_id}')
    assert result.status_code == 200
    assert result.json()['id'] == todos_id


@pytest.mark.parametrize('todos_id', [-1, 0, TestData.TODOS_VALUE + 1])
def test_get_negative(workplace, create_session, todos_id):
    result = create_session.get(url=f'{workplace}/{todos_id}')

    assert result.status_code == 404
    assert not result.json()
