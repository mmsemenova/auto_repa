# Глобальные перемены.
# Имеется следующие переменные, определенные в глобальной области видимости модуля:
# number = 1
# string = 'Hello'
# Напишите и вызовите функцию, которая будет изменять и возвращать эти переменные, на следующие значения:
# number = 5
# string = 'Hello, dear friend'
#

number = 1
string = 'Hello'


def global_changes():
    # С помощью global меняем глобальные переменные внутри функции
    global number
    number = 5
    global string
    string = 'Hello, dear friend'
    return number, string

# Зовем функцию, которая нам возвращает измененные глобальные переменные


global_changes()


# Ниже НИЧЕГО НЕ НАДО ИЗМЕНЯТЬ

assert number == 5, 'Переменная number должна иметь значение 5'
assert string == 'Hello, dear friend', 'Переменная number должна иметь значение Home, sweet home'
assert global_changes() == (5, 'Hello, dear friend')

print('Все ок')
