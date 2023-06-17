# ✔Функция получает на вход словарь с названием компании в качестве ключа
# и списком с доходами и расходами (3-10 чисел) в качестве значения.
# ✔Вычислите итоговую прибыль или убыток каждой компании. Если все компании прибыльные,
# верните истину, а если хотя бы одна убыточная — ложь

import random

def my_func(my_dict: {str, list}) -> bool:
    result = True
    for company, balance in my_dict.items():
        my_sum = sum(balance)
        print(my_sum) #проверка
        if my_sum < 0:
            result = False
            break
    return result

list_income_expence = [100, 200, 300, 400, 55, -200, -300, -32, 900, -1000, 700, -78]
list_company = ['GeekBrains', 'Яндекс', 'Apple', 'Sony']

my_dict = {}

for i in range(len(list_company)):
    my_list = list(random.choices(list_income_expence, k=6))
    my_dict[list_company[i]] = my_list

print(my_dict) #проверка

print(my_func(my_dict))
