import pytest


class TestClassTuple(object):
    @pytest.mark.parametrize(
        "test_input",
        [
            (None, 'hello', 123),
            (1, 2, 3, 4, 5),
            (2.5, 3.9, 7.9),
            ('&', '!', '@')
        ]
    )
    def test_tuple_first(self, test_input, case_data):
        print("      > Received from fixture datetime now is: {}".format(case_data))
        test_input_not_modified = ()
        try:
            test_input[0] = 'Something'  # Попытка изменить 0 элемент кортежа
        except TypeError:
            test_input_not_modified = test_input
            return test_input_not_modified
        assert test_input == test_input_not_modified  # Проверка того, что кортеж не изменился

    def test_tuple_second(self, fixture_get_random_digit, case_data):
        print("      > Received from fixture datetime now is: {}".format(case_data))
        tuple_ran = (fixture_get_random_digit, fixture_get_random_digit + 10, fixture_get_random_digit + 20)
        assert len(tuple_ran) > 0
