#!/bin/bash

# Инициализируем массив для хранения IPv4 адресов
ILIST=()
MIN_PORT=60000

# Получаем список сетевых интерфейсов с установленными IPv4 адресами
interfaces=$(ip -o -f inet addr show | awk '{print $2}' | sort -u)

# Проходим по каждому интерфейсу
for iface in $interfaces; do
    # Получаем IPv4 адрес для текущего интерфейса
    ipaddr=$(ip -f inet addr show "$iface" | grep -oP '(?<=inet\s)\d{1,3}(\.\d{1,3}){3}') #Не уверен

    # Добавляем адрес в массив ILIST
    ILIST+=("$ipaddr")
done

#Записываем переменные полученные айпишник в массиве в переменную
export basedate=ILIST

python3 main.py

#Тут я запустил вроде как приложение, но его же надо объявлять его в переменную для простановки порта..

apps=("main.py")

for i in "${!apps[@]}"; do
    PORT=$((MIN_PORT + i))
    TEMP_FILE="/tmp/${apps[i]}_output.log"

    # Запуск приложения в фоновом режиме
    "${apps[i]}" -s "$SERVER_IP" -p "$PORT" > "$TEMP_FILE" 2>&1 &

    echo "Запущено приложение ${apps[i]} на порту $PORT, вывод в $TEMP_FILE"
done

./apps --ip "$SERVER_IP" --port "$port" &

wait

echo "Done. Press any key to exit."
read -n 1 -s

# Завершение всех процессов принимающей стороны и вывод PIDs
for pid in $(jobs -p); do
    echo "Terminating process with PID: $pid"
    kill "$pid"
done

# Удаление временных файлов
rm -f $temp_dir/*_output.log

echo "Temporary files deleted."