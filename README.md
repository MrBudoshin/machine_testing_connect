# machine_testing_connect
Test requests from electronic device

##### Функционал системы:
- Тестирование данных с UPD пакета

#### Установка:
1. Клонируйте репозиторий
2. Создайте и войдите в вирутальное окружение
3. Установите зависимости:
    - `pip install -r requirements.txt`
4. Установите необходимое тестируемое устройство на server.py
5. Запустите серверы
   - `python server.py`
   - `python do_test.py`
7. Запустите в командной строке 
   - `python sender.py localhost file_name.csv `