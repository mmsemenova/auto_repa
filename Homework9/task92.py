# Напишите декоратор func_log, который может принимать аргумент file_log (Путь до файла), по умолчанию равен 'log.txt'
# Декоратор должен дозаписывать в файл имя вызываемой функции (можно получить по атрибуту __name__), дату и время вызова
# по формату:
# имя_функции вызвана %d.%m %H:%M:%S
# Для вывода времени нужно использовать модуль datetime и метод .strftime()
# https://pythonworld.ru/moduli/modul-datetime.html
# https://docs.python.org/3/library/datetime.html
#
# Например
# @func_log()
# def func1():
#     time.sleep(3)
#
# @func_log(file_log='func2.txt')
# def func2():
#     time.sleep(5)
#
# func1()
# func2()
# func1()
#
# Получим:
# в log.txt текст:
# func1 вызвана 30.05 14:12:42
# func1 вызвана 30.05 14:12:50
# в func2.txt текст:
# func2 вызвана 30.05 14:12:47


import datetime
import time


def func_log(file_log="test_file/log.txt"):

    # имя функции, дату и время дозаписывыем в файл
    def log(func):
        def wrapper(*args, **kwargs):
            with open(file_log, mode="a+", encoding="utf-8") as f:
                call_time = datetime.datetime.now().strftime("%d.%m %H:%M:%S")
                f.write(f"{func.__name__} вызвана {call_time}\n")
            res = func(*args, **kwargs)
            return res
        wrapper.__doc__ = func.__doc__
        wrapper.__name__ = func.__name__
        wrapper.__wrapped__ = func
        return wrapper
    return log


@func_log()  # навешиваем декоратор на func1, путь до файла по-умолчанию log.txt.
def func1():
    time.sleep(3)


@func_log(file_log='test_file/func2.txt')  # навешиваем декоратор на func2, передаем путь до файла.
def func2():
    time.sleep(5)


func1()
func2()
func1()
