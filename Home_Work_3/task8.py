# ✔ Три друга взяли вещи в поход. Сформируйте
# словарь, где ключ — имя друга, а значение —
# кортеж вещей. Ответьте на вопросы:
# ✔ Какие вещи взяли все три друга
# ✔ Какие вещи уникальны, есть только у одного друга
# ✔ Какие вещи есть у всех друзей кроме одного
# и имя того, у кого данная вещь отсутствует
# ✔ Для решения используйте операции
# с множествами. Код должен расширяться
# на любое большее количество друзей.

import random

list_friends = ['Петя', 'Вася', 'Коля']
list_items = ['спички', 'палатка', 'кружка', 'котелок', 'консервы', 'бумага', 'топорик', 'перчатки', 'ложка', 'ножик']

my_dict = {}
for i in range(len(list_friends)):
    my_tuple = frozenset(random.choices(list_items, k=5))
    my_dict[list_friends[i]] = my_tuple

print(my_dict)

# в условии написано, используйте операции со множествами, при этом написано про кортежи, использовала frozenset
# какие вещи взяли все три друга

everyone = set()

for i in range(len(list_friends) - 1):
    everyone = set(my_dict[list_friends[i]] & my_dict[list_friends[i + 1]])

if len(everyone) > 0:
    print('У всех есть' + str(everyone))

# ✔ Какие вещи уникальны, есть только у одного друга
list_all_item = []
for i in range(len(list_friends)):
    for j, item in enumerate(my_dict[list_friends[i]]):
        list_all_item.append(item)

for i, item in enumerate(list_all_item):
    if list_all_item.count(item) == 1:
        print('Уникальная вещь: ' + str(item))

# Какие вещи есть у всех друзей кроме одного и имя того, у кого данная вещь отсутствует

check_list = []
for i, item in enumerate(list_all_item):
    if list_all_item.count(item) == len(list_friends) - 1:
        for key, value in my_dict.items():
            if item not in value and item not in check_list:
                check_list.append(item)
                print(item, 'нет только у', key)
# улучшать грамотность вывода нет времени
