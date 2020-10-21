import pytest

from test_api.constant import TestData


@pytest.mark.parametrize('todos_id', [1, 2])
def test_filtering_resource_positive(create_session, workplace, todos_id):
    response = create_session.get(url=f'{workplace}?userId={todos_id}')
    j_res = response.json()
    assert response.status_code == 200
    for x in j_res:
        assert x['userId'] == todos_id


@pytest.mark.parametrize('todos_id', [TestData.TODOS_VALUE, (TestData.TODOS_VALUE + 1), (TestData.TODOS_VALUE + 3)])
def test_filtering_resource_negative(create_session, workplace, todos_id):
    response = create_session.get(url=f'{workplace}?userId={todos_id}')
    j_res = response.json()
    assert response.status_code == 200
    assert not j_res
