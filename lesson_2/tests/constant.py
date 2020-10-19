

class TestData(object):
    u"""Константы для работы с тестами."""

    TUPLE_ONE = ()
    READ_SERVICE_PARAMS = {
        'branchId': 'sim', 'serviceIds': 'cd', 'contractIds': 'sim', 'xpath': 'sim',
        'parameterContext': 'sp', 'serviceId': 'sim', 'serviceName': 'sim'
    }

    FIND_SERVICES_PARAMS = {
        'branchId': 'sim', 'serviceTypeName': 'sim', 'xpath': 'sim', 'serviceStatus': 'sim', 'namespace': 'sim',
        'serviceName': 'sim', 'integer': 'sim', 'serviceCriteria': 'sp', 'concreteServiceCriteria': 'sp',
        'serviceContent': 'sp', 'extension': 'sp', 'VIDIMOST_V_DOSTUPNYKH_YESNO': 'sip', 'tariff': 'pccd',
        'instance': 'pccd', 'tariffId': 'pccd', 'serviceIds': 'cd', 'rule': 'sip',
        'link_systemName_vidimost_v_dostupnykh_yesNo_in': 'sip', 'serviceId': 'sim'
    }

    DICT_FOR_TEST_1 = {
     "brand": "Ford",
     "model": "Mustang",
     "year": 1964
    }

    DICT_FOR_TEST_2 = {
     "brand": "WV",
     "model": "Passat",
     "year": 2000,
     "color": "blue"
    }

    DICT_FOR_TEST_3 = {
     "brand": "Lada",
     "model": "Kalina",
     "year": 1999,
     "color": "red"
    }

    ADDITIONAL_ATTRIBUTE = 'color'

    SENTENSE_1 = "One;two,&three:four* five"
    SENTENSE_2 = "One:,two,three,@four%*_five"
    SENTENSE_3 = "last;second,&first:%&*(*^^"
    SENTENSE_4 = "*!@^#:,last,**(^second,@first%"
    STRING_WITH_DIGITS_1 = "dfgsfshw3443	3tqt34th43gb44y6576867"
    STRING_WITH_DIGITS_2 = "Ghegjhewehk vjwwjhrwhhe"
    SET_1 = {'NN', 'hello', '123'}
    SET_2 = {'1', '2', '3', '4', '5'}
    SET_11 = {1, 2, 3}
    SET_22 = {6, 6, '3', '4', '5'}