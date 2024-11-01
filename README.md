Тестовое задание (решение предоставляется перед собеседованием ссылкой на проект на github):

•	программа должна понимать параметры командной строки:
o	роль - определяет будет ли приложение отправлять данные или принимать данные
o	имя сервера - полное имя сервера или ip-адрес сервера с которым программа будет взаимодействовать (используется только для роли отправляющей данные)
o	ip-адрес и порт на котором будет запущен сервис приема данных (используется только для роли принимающей данные)

•	программа должна включать один package в котором:
o	создан класс MySender и:
	конструктор, принимающий на вход реквизиты сервера для подключения
	protected метод который генерирует случайную последовательность байт размером до 8 ГБ, максимальный размер устанавливается константой
	public метод который создает tcp-соединение с переданным через конструктор сервером 
(в случае если соединение установить не получилось из-за недоступности сервера, делается еще 2 попытки с интервалом 10с)
и отправляет случайную последовательность байт по tcp в формате <размер><данные>, при этом <размер> должен занимать минимальное необходимое количество байт и корректно декодироваться на принимающей стороне
o	создан класс MyListener и:
	конструктор, принимающий на вход реквизиты интерфейса на котором должен работать сервис
	public метод который запускает tcp-сервис на переданных через конструктор ip-адресе и порту
	protected метод который получает последовательность байт по tcp в формате <размер><данные> декодирует их и выводит в stdout размер в виде целого числа и первые 16 байт (не более 16 байт) в hex-формате блока данных
o	в функции main 
	для роли отправителя с использованием класса MySender выполняется одна отправка
	для роли принимающей стороны с использованием класса MyListener поднимается tcp-сервис и ожидает/обрабатывает подключения

•	для приложения должен быть написан bash-скрипт в котором:
o	получается список сетевых интерфейсов для которых установлен адрес ipv4, включая локальный, извлекается его ipv4-адрес и добавляется в список ILIST
o	объявляется переменная MIN_PORT в которой указывается целочисленное значение, например, 60000, используемое в качестве номера порта
o	для каждого элемента SERVER_IP массива в переменной ILIST:
	запускается приложение в роли принимающей стороны, ожидающее подключения на IP-адресе SERVER_IP и порту который вычисляется как MIN_PORT + <порядковый номер элемента массива>, stdout каждого приложения перенаправляется в отдельный временный файл 
	запускается приложение в роли отправителя, подключающееся по IP-адресу SERVER_IP и порту который вычисляется как MIN_PORT + <порядковый номер элемента массива>
o	после запуска приложений для каждого элемента массива и завершения отправки данных выводится сообщение "Done. Press any key to exit." и ожидается нажатие клавиши
o	после нажатия клавиши в скрипте выполняется
	явное принудительное завершение всех процессов приложения, запущенных в роли принимающей стороны, с выводом PID завершаемого процесса
	удаление всех временных файлов 

