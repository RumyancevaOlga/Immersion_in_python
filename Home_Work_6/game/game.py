# Создайте модуль с функцией внутри.
# Функция принимает на вход три целых числа: нижнюю и верхнюю границу и количество попыток.
# Внутри генерируется случайное число в указанных границах и пользователь должен угадать его
# за заданное число попыток.
# Функция выводит подсказки “больше” и “меньше”.
# Если число угадано, возвращается истина, а если попытки исчерпаны - ложь.

# Улучшаем задачу 2.
# Добавьте возможность запуска функции “угадайки” из модуля в командной строке терминала.
# Строка должна принимать от 1 до 3 аргументов: параметры вызова функции.
# Для преобразования строковых аргументов командной строки в числовые параметры используйте
# генераторное выражение.

from random import randint
from sys import argv

__all__ = ['my_game']

LOWER_LIMIT = 0
UPPER_LIMIT = 10
NUM_OF_ATTEMPTS = 3


def my_game(low=0, high=10, num_of_attempts=3):
    number = randint(low, high)
    attempt = 0
    print(
        f'Программа загадывает число от {low} до {high}. Необходимо угадать число за {attempt} попыток.')
    while attempt < num_of_attempts:
        attempt += 1
        user_number = int(input(f'Попытка номер {attempt}. Введите число: '))
        if user_number < number:
            print('Меньше')
        elif user_number > number:
            print('Больше')
        else:
            print(f'Вы отгадали с {attempt} попытки!')
            return True
    else:
        print(f'Вы использовали все {attempt} попыток и не отгадали число. Было загадано число {number}. Вы проиграли.')
        return False


if __name__ == '__main__':
    print(argv)
    _, *params = argv
    print(my_game(*map(int, params)))

#  python game.py 0 10 3
