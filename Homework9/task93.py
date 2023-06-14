# Дан файл test_file/task_3.txt можно считать, что это запись покупок в магазине, где указана только цена товара
# В каждой строке файла записана цена товара.
# Покупки (т.е. несколько подряд идущих цен) разделены пустой строкой
# Нужно найти сумму трёх самых дорогих покупок, которые запишутся в переменную three_most_expensive_purchases

from pathlib import Path

with open(Path.cwd().joinpath('test_file', 'task_3.txt'), 'r', encoding='utf-8') as file:
    data = file.read()

prices_lst = data.split('\n\n')

tmpdgt = []
summas = []

for i in range(len(prices_lst)):
    tmp = prices_lst[i].split('\n')    # i-тую покупку разбиваем по '\n' на список цен
    tmpdgt = sum(list(map(int, tmp)))  # суммируем все цены i-той покупки
    summas.append(tmpdgt)              # записываем сумму цен i-той покупки в список summas

# сортируем по возрастанию список summas и считаем сумму 3-х элементов с конца
three_most_expensive_purchases = sum(sorted(summas)[-3:])

assert three_most_expensive_purchases == 202346
