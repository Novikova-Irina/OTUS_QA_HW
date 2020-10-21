import pytest

from test_api.constant import TestData


@pytest.mark.parametrize('todos_id', [TestData.TODOS_VALUE, (TestData.TODOS_VALUE - 2), (TestData.TODOS_VALUE - 33)])
def test_delete_resource_positive(create_session, workplace, todos_id):
    response = create_session.delete(url=f'{workplace}/{todos_id}')
    assert response.status_code == 200
    assert not response.json()
