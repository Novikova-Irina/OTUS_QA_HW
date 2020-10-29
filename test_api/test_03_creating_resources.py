import pytest

from test_api.constant import TestData


@pytest.mark.parametrize('todos_id', [TestData.TODOS_VALUE])
def test_creating_a_resource(create_session, workplace, todos_id):
    response = create_session.post(url=workplace, json=TestData.DICT_UNIT_1)
    j_res = response.json()

    assert response.status_code == TestData.STATUS_CODE_201
    assert j_res['id'] == todos_id + 1
    assert j_res['userId'] == TestData.DICT_UNIT_1['userId']
    assert j_res['title'] == TestData.DICT_UNIT_1['title']
    assert j_res['completed'] is TestData.DICT_UNIT_1['completed']
