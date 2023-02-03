Курсы от МФТИ, mail.ru, ФРОО на coursera.org
Функциональное программирование: замыкание, декораторы, генераторы, map/reduce/lambda,
ООП: Наследование, композиция, дескрипторы, метаклассы, дандер методы,
Exceptions, pdb, unittest,
Многопоточка и асинхронщина: threading, GIL, socket, asyncio

Неделя 1. Введение.
- Базовые типы данных и конструкции управления потоком (if, for, while)
- Модули и пакеты
- Virtualenv (установка, запуск)
- Jupiter Notebook (установка, запуск)
- Байткод (func().__code__.co_code)

Неделя 2. Структуры данных и функции.
- list, tuple, set, dict
- Функции
- Файлы
- Функциональное программирование, замыкание функции
- Декораторы
- Генераторы

Неделя 3. ООП.
- Классы и экземпляры
- Методы
- Наследование
- Композиция
- Исключения, BaseExeption, try/ except/ else/ finally, raise, exception(text, ex)

Неделя 4. Углубленный Python.
- Магические методы __methods__()
- Итераторы
- Контекстные менеджеры
- Дескрипторы классов
- Метаклассы
- pdb
- unittest

Неделя 5. Многопоточное и асинхронное программирование.
- Процесс. bash: top, strace. os.fork()
- Поток. threading.Thread()
- Очереди. queue.Queue()
- Блокировки. Threading.Rlock(), acquire(), release()
- условные переменные. threading.Condition(self._mutex)
- GIL
- socket. Создание сервера и клиента.
	- контекстный менеджер создания
	- таймауты, обработка ошибок
	- обработка нескольких соединений (socket + threading)
- Асинхронное программирование
	- select, неблокирующий ввод/ вывод без потоков, epoll (не запускал в mac os, не работает!)
	- генераторы и корутины, yield from
	- asyncio

