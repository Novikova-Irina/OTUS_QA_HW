import pytest


class TestClassList:

    @pytest.mark.parametrize(
        "test_input",
        [
            [None, 'hello', 123],
            [1, 2, 3, 4, 5],
            ['I', 'live', 'in', 'Russia']
        ]
    )
    def test_one(self, test_input):
        for i in test_input:
            if i is None:
                assert i is None
            else:
                assert("TRUE" if i else "FALSE") == "TRUE"

    @pytest.mark.parametrize(
        "test_input",
        [
            [None, 'hello', 123],
            [1, 2, 3, 4, 5]
        ]
    )
    def test_two(self, test_input):
        print(test_input)
        assert len([i for i in test_input if i is not None]) > 0
