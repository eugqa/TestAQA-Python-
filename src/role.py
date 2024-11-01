

 #скрипт для ручного выбора ролей
class Roles:

        def ParentsRoles():
            return input("Выберите роль sender или Listener")

        def Sender():
            return input("Введите имя или IP адрес сервера: ")

        def Listener():
            return input("Введите IP адрес и порт сервера приема данных: ")

        ParentsRoles = input("Выберите роль sender или Listener: ")

        role = ParentsRoles

        if role == 'sender':
            Id = Sender() #Вообще тут нужно придумать формат ввода данных, что бы потом передавать его в класс паблик сенддера .
        elif role == 'Listener':
            Id = Listener() #Вообще тут нужно придумать формат ввода данных, что бы потом передавать его в класс паблик листнера.
        else:
            Id = "Выбрана некорректная роль"


        ##print(f"Result: {Id}")



