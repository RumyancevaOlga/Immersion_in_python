# Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток. Программа
# должна подсказывать «больше» или «меньше» после каждой попытки. Для генерации случайного
# числа используйте код:
# from random import randint
# num = randint(LOWER_LIMIT, UPPER_LIMIT)

from random import randint

LOWER_LIMIT = 0
UPPER_LIMIT = 100

num = randint(LOWER_LIMIT, UPPER_LIMIT)

user_num = int(input('Угадай число, которое я загадала '))

for i in range (0, 10):
    if user_num == num:
        print('Молодец! Угадал!')
        break
    elif user_num > num:
        print('Неверно, бери меньше')
    elif user_num < num:
        print('Неверно, бери больше')
    user_num = int(input('Попробуй еще раз '))

if user_num != num:
    print('Попытки закончились! Ты проиграл!')
