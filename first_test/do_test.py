import requests
import json
import argparse


def main(file):
    """ Url сервиса обработки"""
    url = "http://localhost:5000/api"
    headers = {'content-type': 'application/json'}
    """Получение данных из файла"""
    with open(file, "r", encoding="utf-8") as ff:
        """Чтение файла составление запроса"""
        for line in ff:
            payload = {
                "method": "do_test",
                "params": [line[:-1]],
                "jsonrpc": "2.0",
                "id": 1
                }
            get_line = line[:-1].split(',')
            get_file = file.split('.')
            """Обработка не корректного запроса"""
            try:
                response = requests.post(url, data=json.dumps(payload), headers=headers).json()
            except BaseException as exc:
                print(f"The request is incorrect {exc}")
            file_name = str(get_file[0]) + str(get_line[2]) + '.txt'
            """Запись в файл (возможно настроить запись logging)"""
            with open(file_name, "w", encoding="utf-8") as f:
                f.write(str(response))
            if response["result"] == '0':
                print(f'{file_name}')
                print(f"Test {get_line[0]} vs SN {get_line[2]} successful")
            else:
                print(f'{file_name}')
                print(f"Test {get_line[0]} vs SN {get_line[2]} failed: mistakes №{response['result']}")


if __name__ == "__main__":
    take_file = argparse.ArgumentParser(description='Select your file to check')
    take_file.add_argument('--dir', help='name file to read')
    argument = take_file.parse_args()
    main(argument.dir)
