import socket
import struct


from src.constructor.listener.public import public_listener
from src.constructor.sender.protected import random_size


class protected_listener:
            server_socket = public_listener
            size = random_size
            size_data = server_socket.recv(size)

            # Декодируем размер
            size = struct.unpack('!I', size_data)[0]  # '!' - big-endian, 'I' - unsigned int
            print(f"Размер: {size}")

            # Получаем данные
            data = server_socket.recv(size)

            # Выводим первые 16 байт в hex
            hex_output = data[:16].hex()
            print(f"Данные (первые 16 байт): {hex_output}")