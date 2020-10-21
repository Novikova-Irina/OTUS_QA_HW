class TestData(object):
    u"""Константы для работы с тестами."""

    TODOS_VALUE = 200
    TITLE = 'quae est simplex'
    DICT_UNIT_1 = {'userId': 1,
                   'title': TITLE,
                   'completed': False}

    STATUS_CODE_201 = 201


class SchemasConsts(object):
    u"""Константы для работы сo схемами."""

    DEFAULT_SETTINGS_DIRECTORY = 'schemas/'
    DEFAULT_SETTINGS_FILE = 'todos_schema.json'
    DEFAULT_SETTINGS_SCH_FILE = 'todos_schema_file.json'
    PATH_TO_SCHEMA = DEFAULT_SETTINGS_DIRECTORY + DEFAULT_SETTINGS_FILE
    PATH_TO_SCHEMA_FILE = DEFAULT_SETTINGS_DIRECTORY + DEFAULT_SETTINGS_SCH_FILE
