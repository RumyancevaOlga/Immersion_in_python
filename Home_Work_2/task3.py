# Напишите программу, которая принимает две строки вида “a/b” -
# дробь с числителем и знаменателем. Программа должна возвращать сумму и
# произведение* дробей. Для проверки своего кода используйте модуль fractions.

import fractions

frac_1 = input('Введите первую дробь: ')
frac_2 = input('Введите вторую дробь: ')


def multi(num_1: int, num_2: int) -> str:
    for i in range(num_1, 1, -1):
        if num_1 % i == num_2 % i == 0:
            num_1 /= i
            num_2 /= i
    if num_1 / num_2 == 1:
        res = '1'
    else:
        res = str(int(num_1)) + '/' + str(int(num_2))
    return res


def sum(num_1: str, num_2: str) -> str:
    res = 0
    fra_res = ''
    fra_1 = num_1.split('/')
    fra_2 = num_2.split('/')
    if fra_1[1] == fra_2[1]:
        res = int(fra_1[0]) + int(fra_2[0])
        fra_res = multi(int(res), int(fra_1[1]))
    elif int(fra_1[1]) % int(fra_2[1]) == 0:
        res = int(fra_1[0]) + int(fra_2[0]) * (int(fra_1[1]) // int(fra_2[1]))
        fra_res = multi(int(res), int(fra_1[1]))
    elif int(fra_2[1]) % int(fra_1[1]) == 0:
        res = int(fra_2[0]) + int(fra_1[0]) * (int(fra_2[1]) // int(fra_1[1]))
        fra_res = multi(int(res), int(fra_2[1]))
    else:
        res = (int(fra_1[0]) * int(fra_2[1])) + (int(fra_2[0]) * int(fra_1[1]))
        fra_res = multi(int(res), int(fra_2[1]) * int(fra_1[1]))
    return fra_res


def product(num_1: str, num_2: str) -> str:
    fra_res = ''
    fra_1 = num_1.split('/')
    fra_2 = num_2.split('/')
    fra_res = multi(int(fra_1[0]) * int(fra_2[0]), int(fra_1[1]) * int(fra_2[1]))
    return  fra_res

num_1 = fractions.Fraction(frac_1)
num_2 = fractions.Fraction(frac_2)

print('сумма равна:', sum(frac_1, frac_2))
print('проверка', num_1 + num_2)

print('произведение равно:', product(frac_1, frac_2))
print('проверка', num_1 * num_2)