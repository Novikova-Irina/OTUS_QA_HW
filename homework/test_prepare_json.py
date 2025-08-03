import json
from csv import DictReader

CSV_FILE = 'books.csv'
JSON_FILE = 'users.json'
OUTPUT_JSON_FILE_NAME = 'json_output.json'


def read_csv(file):
    """
        Преобразование csv-файла в Python-объект

    file: CSV_FILE

    return: book_value - словарь книг
    """
    book_value = {}
    with open(file) as csv_file:
        reader = DictReader(csv_file)
        for row in reader:
            for key in row:
                if key == "Title":
                    book_value.update({key: row[key]})
                elif key == "Author":
                    book_value.update({key: row[key]})
                elif key == "Height":
                    book_value.update({key: row[key]})
    return book_value


def prepare_json(json_file_name, dict_of_book):
    """
        Преобразование json-файла в Python-объект

    file: JSON_FILE

    return: dict_part_one - словарь пользователей книг
    """
    with open(json_file_name, "r") as file:
        value = json.load(file)
        # Итерируемся по данным делая из них словарь
        dict_part_one = {}
        for item in value:
            for key, value in item.items():
                if key == "name":
                    dict_part_one.update({key: value})
                elif key == "gender":
                    dict_part_one.update({key: value})
                elif key == "address":
                    dict_part_one.update({key: value})
            for _ in dict_part_one, dict_of_book:
                dict_part_one.update({"book": [dict_of_book]})
    return dict_part_one


def generate_json(dict_json):
    """ Генерация json-файла с помощью контекстного менеджера"""
    with open(OUTPUT_JSON_FILE_NAME, "w") as f:
        full_str = json.dumps(dict_json, indent=4)
        f.writelines(full_str)


def test_generate_json(suite_data, case_data):
    """ Тест формирует json-файл."""
    dict_json = prepare_json(JSON_FILE, read_csv(CSV_FILE))
    generate_json(dict_json)
