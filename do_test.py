import json
from socket import *

import requests


def main():
    url = "http://localhost:5000/api"
    headers = {'content-type': 'application/json'}
    while True:
        host = 'localhost'
        port = 12345
        addre = (host, port)
        udp_socket_lis = socket(AF_INET, SOCK_DGRAM)
        udp_socket_lis.bind(addre)
        print('wait data...')
        conn, addr = udp_socket_lis.recvfrom(1024)
        get_udp = conn.decode()
        """Получение данных из файла"""
        try:
            with open(get_udp, "r", encoding="utf-8") as ff:
                for line in ff:
                    payload = {
                        "method": "do_test",
                        "params": [line[:-1]],
                        "jsonrpc": "2.0",
                        "id": 1
                    }
                    get_line = line[:-1].split(',')
                    get_file = get_udp.split('.')

                    """Обработка не корректного запроса"""
                    try:
                        response = requests.post(url, data=json.dumps(payload), headers=headers).json()
                    except BaseException as exc:
                        print(f"The request is incorrect {exc}")
                    file_name = str(get_file[0]) + str(get_line[2]) + '.txt'

                    """Запись в файл (возможно настроить запись logging)"""
                    with open(file_name, "w", encoding="utf-8") as f:
                        if response["result"] == '0':
                            print(f'{file_name}')
                            print(f"Тест {get_line[0]} с SN {get_line[2]} прошел успешно")
                            f.write(f'IP адрес: {addr[0]}, номер устройства: {addr[1]}\n'
                                    f'Тест {get_line[0]} с SN {get_line[2]} прошел успешно')
                        else:
                            print(f'{file_name}')
                            print(f"Test {get_line[0]} vs SN {get_line[2]} failed: mistakes №{response['result']}")
                            f.write(f'IP адрес: {addr[0]}, номер устройства: {addr[1]}\n'
                                    f'Тест {get_line[0]} с SN {get_line[2]} завершился ошибкой №{response["result"]}')
            udp_socket_lis.close()
        except BaseException as exc:
            print(f'Не верные данные {exc}')


if __name__ == '__main__':
    main()
