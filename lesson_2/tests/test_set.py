import pytest

from lesson_2.tests.constant import TestData


class TestClassSet:

    @pytest.mark.parametrize(
        "test_set_1, test_set_2",
        [
            (TestData.SET_1, TestData.SET_2),
            (TestData.SET_11, TestData.SET_22)
        ]
    )
    def test_one(self, test_set_1, test_set_2):
        old_value_test_set_1 = test_set_1.copy()
        test_set_1.update(test_set_2)
        assert len(test_set_1) == len(old_value_test_set_1) + len(test_set_2)

    @pytest.mark.parametrize(
        "test_set",
        [
            TestData.SET_1,
            TestData.SET_2,
            TestData.SET_11,
            TestData.SET_22
        ]
    )
    def test_two(self, test_set, case_data):
        old_value_test_set_1 = test_set.copy()
        test_set.add(case_data)
        print(test_set)
        assert len(test_set) == len(old_value_test_set_1) + 1
