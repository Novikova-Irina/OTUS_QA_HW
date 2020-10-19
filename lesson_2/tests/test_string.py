import string
import pytest

from lesson_2.tests.constant import TestData


def two_sentenses(string_data_1, string_data_2):
    for ch in string.punctuation:
        string_data_1 = string_data_1.replace(ch, " ")
        string_data_2 = string_data_2.replace(ch, " ")
    sentense_1 = string_data_1.split()
    sentense_2 = string_data_2.split()
    return sentense_1, sentense_2


def string_without_digits(str_dgt):
    for d in string.digits:
        set_of_symbols = str_dgt.replace(d, "")
    return set_of_symbols


class TestSuite:

    def test_case_1(self, case_data):
        print("      > Received from fixture datetime now is: {}".format(case_data))
        assert case_data, "DateTime dose' t present"

    @pytest.mark.parametrize(
        "string_data_1, string_data_2",
        [
            (TestData.SENTENSE_1, TestData.SENTENSE_2),
            (TestData.SENTENSE_3, TestData.SENTENSE_4)
        ]
    )
    def test_case_2(self, string_data_1, string_data_2):
        sen1, sen2 = two_sentenses(string_data_1=string_data_1, string_data_2=string_data_2)
        assert sen1 == sen2

    @pytest.mark.parametrize(
        "string_with_digits",
        [
            TestData.STRING_WITH_DIGITS_1,

            TestData.STRING_WITH_DIGITS_2
        ]
    )
    def test_case_3(self, string_with_digits):
        string_no_one_digits = string_without_digits(string_with_digits)
        assert string_no_one_digits, "No one letter"
