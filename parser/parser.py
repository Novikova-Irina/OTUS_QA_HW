from collections import Counter
from operator import itemgetter
import argparse
import re
import sys
import json


def parser_init():
    """
    Парсер параметров
    """
    parser = argparse.ArgumentParser(description='Process access.log')
    parser.add_argument('-f', '--file', type=str, dest='file', help='Path to logfile')
    parser.add_argument('-d', '--directory', type=str, dest="directory", help='Path to directory')
    args = parser.parse_args()
    return args


def read_file(input_file, output_file):
    """

    input_file : str
        Path to logs file.
    output_file : str
        Path to file  results.
    """

    requests_count = 0

    post_requests_count = 0
    get_requests_count = 0
    put_requests_count = 0
    delete_requests_count = 0

    requests_list = []
    ip_list = []

    # Открытие файла с логами и чтение line by line
    try:
        with open(input_file, 'r', encoding='utf-8') as log:
            for line in log:

                # Счетчик HTTP методов:
                requests_count += 1

                if re.search('POST', line):
                    http_method = 'POST'
                    post_requests_count += 1
                elif re.search('GET', line):
                    http_method = 'GET'
                    get_requests_count += 1
                elif re.search('PUT', line):
                    http_method = 'PUT'
                    put_requests_count += 1
                elif re.search('DELETE', line):
                    http_method = 'DELETE'
                    delete_requests_count += 1

                # Использование регулярных выражений для поиска информации:
                request_ip = re.match(
                    r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', line
                )
                request_duration = re.search(r'(\d)*$', line)
                request_url = re.search(r'(/\D*) HTTP', line)
                request_status_code = re.search(r'(\d{3}) ', line)

                if request_ip and request_duration \
                        and request_url and request_status_code:
                    requests_list.append(
                        [
                            request_ip.group(0),
                            request_duration.group(0),
                            http_method,
                            request_url.group(1),
                            request_status_code.group(1)
                        ]
                    )
                    ip_list.append(request_ip.group(0))

    # Возникает, когда файл не указан при вызове из командной строки:
    except TypeError:
        sys.exit('Необходимо указать имя файла в командной строке "--file=filename"')

    # Возникает, когда запрашиваемый файл не существует:
    except FileNotFoundError:
        sys.exit('Невозможно найти файл. Файл не существует.')

    # Топ-10 IP-адресов, с которых поступали запросы:
    top_requests = list(
        sorted(Counter(ip_list).items(), key=lambda x: x[1], reverse=True)
    )[:9]

    # Топ-10 IP-адресов, по продолжительности запросов:
    top_duration = sorted(requests_list, key=itemgetter(1), reverse=True)[:9]

    # Топ-10 запросов с ошибками клиента (4**):
    top_client_error = [x for x in requests_list if x[4].startswith('4')][:9]

    # Топ-10 запросов с ошибками сервера (5**):
    top_server_error = [x for x in requests_list if x[4].startswith('5')][:9]

    # Формируем структуру файла с результатами:
    result = {
        'requests':
            {
                'all': requests_count,
                'post_requests_count': post_requests_count,
                'get_requests_count': get_requests_count,
                'put_requests_count': put_requests_count,
                'delete_requests_count': delete_requests_count,
             },
        'top_requests': top_requests,
        'top_duration': top_duration,
        'top_client_error': top_client_error,
        'top_server_error': top_server_error
    }

    # Создаем файл с результатами и записываем данные c двойнным отступом:
    try:
        with open(output_file, 'w+') as output:
            json.dump(result, output, indent=2)
    except Exception as exc:
        sys.exit(f'Невозможно записать файл: {exc}')


def read_dir(directory):
    """
    directory : str
        Path to directory with logs files
    """
    read_file('d:/Git/lesson_19/parser/logs/access.log', f'output.json')


def main():
    """
    Точка входа
    """
    args = parser_init()
    read_dir(args.directory)
    read_file(args.file, output_file='output.json')


if __name__ == '__main__':
    main()
