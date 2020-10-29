import pytest

from test_api.constant import TestData


@pytest.mark.parametrize('todos_id', [TestData.TODOS_VALUE, (TestData.TODOS_VALUE - 1), (TestData.TODOS_VALUE - 50)])
def test_update_resources_put_positive(create_session, workplace, todos_id):
    response = create_session.put(url=f'{workplace}/{todos_id - 1}', json=TestData.DICT_UNIT_1)
    assert response.status_code == 200
    j_res = response.json()
    assert j_res['userId'] == TestData.DICT_UNIT_1['userId']
    assert j_res['title'] == TestData.DICT_UNIT_1['title']
    assert j_res['completed'] is TestData.DICT_UNIT_1['completed']


@pytest.mark.parametrize('todos_id', [-1, 0, (TestData.TODOS_VALUE + 1)])
def test_update_resources_put_negative(create_session, workplace, todos_id):
    response = create_session.put(url=f'{workplace}/{todos_id + 1}', json=TestData.DICT_UNIT_1)
    assert response.status_code == 500


@pytest.mark.parametrize('todos_id', [1, TestData.TODOS_VALUE])
def test_update_resources_patch_positive(create_session, workplace, todos_id):
    response = create_session.patch(url=f'{workplace}/{todos_id}', data={'title': TestData.TITLE})
    j_res = response.json()
    assert j_res['id'] == todos_id
    assert j_res['title'] == TestData.TITLE
    assert response.status_code == 200


@pytest.mark.parametrize('field, value', [
    ('userId', 50),
    ('title', 'quae est simplex'),
    ('completed', False)
])
def test_update_patch(create_session, workplace, todos_id, field, value):
    response = create_session.patch(url=f'{workplace}/{todos_id}', data={field: value})
    assert response.status_code == 200
    j_res = response.json()
    assert j_res['id'] == todos_id
    assert j_res[field] == str(value)
