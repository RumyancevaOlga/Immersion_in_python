# Напишите программу, которая получает целое число и возвращает
# его шестнадцатеричное строковое представление. Функцию hex используйте
# для проверки своего результата.

hexadecimal = dict([('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'),
                    ('7', '7'), ('8', '8'), ('9', '9'), ('10', 'A'), ('11', 'B'), ('12', 'C'), ('13', 'D'),
                    ('14', 'E'), ('15', 'F')])

BASE = 16


def my_func(base: int, number: int):
    base_num = []
    while number > 0:
        base_num.append(hexadecimal.get(str(number % base)))
        number //= base
    base_num.reverse()
    for i in range(len(base_num)):
        print(base_num[i], end='')
    print()


num = int(input('Введите число: '))

my_func(BASE, num)
print(hex(num))
