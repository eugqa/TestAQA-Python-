import os
import socket

#from src.role import Roles

class public_listener:
    def start_tcp_server(Id): #Id это адрес и порт
        Id = os.getenv('basedate') # По задумке я взял внешнюю переменную из скрипта баш
        # Создаем сокет
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
                # Привязываем сокет к адресу и порту
                server_socket.bind((Id))
                server_socket.listen()