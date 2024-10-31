import socket
import time

from src.constructor.sender.protected import random_size
from src.role import Roles


class public_sender:
    random_byte = random_size()
    size = random_size()
    def create_tcp(Id):  #Типо переменная Id это сервер и хост
        Id = Roles()
        attempt = 3
        for i in range(attempt):
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((Id))
                print("Соединение успешно установлено!")
                return s
            except (socket.error, ConnectionRefusedError) as e:
                print(f"Попытка {i + 1} не удалась: {e}")
                if i < attempt - 1:
                    print("Повторная попытка через 10 секунд...")
                    time.sleep(10)
        print("Не удалось установить соединение после 3 попыток.")
        return None

        # Форматируем сообщение: <размер><данные>
        message = size + random_byte # По идее мы получили уже и размер и данные
        # Отправляем сообщение
        s.sendall(message)

# Пример использования
#tcp = create_tcp("example.com", 80) можно упростить переменную....наверное