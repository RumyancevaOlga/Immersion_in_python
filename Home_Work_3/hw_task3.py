# Создайте словарь со списком вещей для похода в качестве ключа и их массой
# в качестве значения. Определите какие вещи влезут в рюкзак передав его максимальную
# грузоподъёмность. Достаточно вернуть один допустимый вариант.

import itertools

CAPACITY = 2
LOW_LIMIT = 1.9

dict_items = {'спички': 0.02, 'палатка': 2, 'кружка': 0.1, 'котелок': 1, 'консервы': 0.5, 'бумага': 0.3, 'топорик': 1.5, 'перчатки': 0.05, 'ложка': 0.07, 'ножик': 0.1}

whole_backpack = 0
dict_backpack = {}

for key, item in dict_items.items():
    if whole_backpack + item <= CAPACITY:
        dict_backpack[key] = item
        whole_backpack += item

print(dict_backpack)

# *Верните все возможные варианты комплектации рюкзака.

list_item = list(dict_items.keys())
list_whole = list(dict_items.values())
list_backpack = []

comb = itertools.chain(itertools.combinations(list_whole, r=n) for n in range(1, len(list_whole) + 1))

sum_item = 0
for item in comb:
    for i in item:
        if isinstance(i, int):
            sum_item = i
        else:
            sum_item = sum(i)
        if LOW_LIMIT <= sum_item <= CAPACITY:
            print(i) # из-за похожих комбинаций появляются повторы, победить не удалось
            for key, elem in dict_items.items():
                for j in range(len(i)):
                    if elem == i[j] and key not in list_backpack:
                        list_backpack.append(key)
        if len(list_backpack) > 0:
            print(list_backpack)
            list_backpack.clear()

