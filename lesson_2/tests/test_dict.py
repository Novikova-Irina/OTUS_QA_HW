import pytest

from lesson_2.tests.constant import TestData


class TestClassDict:
    def test_validate_dict(self, case_data):
        dictionary = {
            "foo": "bar"
        }
        validation = {
            "foo": "berry"
        }

        assert validation["foo"] != dictionary["foo"]

    @pytest.mark.parametrize(
        "test_dict_1, test_dict_2",
        [
            (TestData.FIND_SERVICES_PARAMS, TestData.READ_SERVICE_PARAMS)
        ]
    )
    def test_check_if_dict_empty(self, test_dict_1, test_dict_2):
        assert test_dict_1 != test_dict_2

    @pytest.mark.parametrize(
        "dict_for_test, attribute",
        [
            (TestData.DICT_FOR_TEST_1, TestData.ADDITIONAL_ATTRIBUTE),
            (TestData.DICT_FOR_TEST_2, TestData.ADDITIONAL_ATTRIBUTE),
            (TestData.DICT_FOR_TEST_3, TestData.ADDITIONAL_ATTRIBUTE)
        ]
    )
    def test_insert_data_in_dict(self, dict_for_test, attribute):
        for x in dict_for_test:
            if attribute in dict_for_test:
                dict_for_test_modify = dict_for_test.copy()
                del dict_for_test_modify["color"]
                assert len(dict_for_test_modify) == (len(dict_for_test)) - 1
            else:
                dict_for_test_modify = dict_for_test.copy()
                dict_for_test_modify["color"] = "red"
                assert len(dict_for_test_modify) == (len(dict_for_test)) + 1
