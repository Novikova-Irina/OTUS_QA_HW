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


@pytest.mark.parametrize('field, value', [
    ('userId', 1),
    ('userId', 10),
    ('id', 1),
    ('id', TestData.TODOS_VALUE),
    ('title', 'delectus aut autem'),
    ('completed', False),
    ('completed', True)
])
def test_filtering_resource_positive(create_session, workplace, field, value):
    str_val = str(value).lower() if isinstance(value, bool) else str(value)
    response = create_session.get(url=f'{workplace}?{field}={str_val}')
    assert response.status_code == 200
    j_res = response.json()
    assert len(j_res) > 0
    for x in j_res:
        assert x[field] == value


@pytest.mark.parametrize('field, value', [
    ('userId', -1),
    ('userId', 0),
    ('userId', 11),
    ('id', -1),
    ('id', 0),
    ('id', TestData.TODOS_VALUE + 1),
    ('title', ''),
])
def test_filtering_resource_negative(create_session, workplace, field, value):
    response = create_session.get(url=f'{workplace}?{field}={value}')
    j_res = response.json()
    assert response.status_code == 200
    assert not j_res
