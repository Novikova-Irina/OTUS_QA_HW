import json
import pytest
from jsonschema import validate
from test_api.constant import SchemasConsts


def assert_valid_schema(data, schema_file):
    with open(schema_file) as f:
        schema = json.load(f)
    return validate(instance=data, schema=schema)


def test_get_todos(create_session, workplace):
    res = create_session.get(url=f'{workplace}/1')
    assert_valid_schema(res.json(), SchemasConsts.PATH_TO_SCHEMA)


def test_get_todoses(create_session, workplace):
    res = create_session.get(url=workplace)
    assert_valid_schema(res.json(), SchemasConsts.PATH_TO_SCHEMA_FILE)
