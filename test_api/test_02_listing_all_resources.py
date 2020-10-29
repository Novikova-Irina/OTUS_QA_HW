import pytest

from test_api.constant import TestData


@pytest.mark.parametrize('todos_id', [TestData.TODOS_VALUE])
def test_listing_positive(workplace, create_session, todos_id):
    result = create_session.get(url=f'{workplace}')
    assert len(result.json()) == todos_id
