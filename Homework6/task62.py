# Нелокальные изменения
# Имеется функция global_function с локальной переменной msg = 1
# Ваша задача дополнить логику функции global_function следующим образом:
# global_function должна содержать в себе функцию local_function
# local_function должна изменить значение переменной msg на значение 2

def global_function():
    msg = 1

    def local_function():

        # Используем nonlocal для изменения переменной глобальной функции внутри локальной
        nonlocal msg
        msg = 2

    # Зовем сначала локальную функцию внутри глобальной
    local_function()

    return msg

# Зовем глобальную функцию


global_function()

assert global_function() == 2, 'Значение переменной msg должно быть равно 2'
print('Все ок')
