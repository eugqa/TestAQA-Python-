import os

class random_size:
        def random_line(size):
            if size > 1 * 1024 ** 3:
                raise ValueError("Максимальный размер - 8 ГБ.")

            line = os.urandom(size)
            return line


            # Ввод кол-ва байтов
        size = 1 * 1024 ** 3
        #random_byte = random_line(size)

#print(f"Сгенерировано {len(random_byte)} байт.")