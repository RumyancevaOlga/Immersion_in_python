# ✔Напишите функцию, которая генерирует псевдоимена.
# ✔Имя должно начинаться с заглавной буквы, состоять из 4-7 букв,
# среди которых обязательно должны быть гласные.
# ✔Полученные имена сохраните в файл.

__all__ = ['my_func_1']

from random import sample, randint, choice
import os

MIN_VALUE = 4
MAX_VALUE = 7
VOWELS = 'eyuioa'
LITERALS = 'qwertyuiopasdfghjklzxcvbnm'


def my_func_1(count_names: int, file_name: str, dir_name: str):
    file_path = os.path.join(dir_name, file_name)
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)
    if not os.path.exists(file_path):
        with open(file_path, 'a', encoding='utf-8') as f:
            for _ in range(count_names):
                name = sample(LITERALS, randint(MIN_VALUE, MAX_VALUE))
                if not set(name) & set(VOWELS):
                    name[0] = choice(VOWELS)
                name = ''.join(name).title()
                f.write(f'{name}\n')


if __name__ == '__main__':
    my_func_1(7, 'file_5.txt', r'/Home_Work_7/Doc')
