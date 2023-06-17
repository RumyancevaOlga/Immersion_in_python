# Напишите функцию принимающую на вход только ключевые параметры и
# возвращающую словарь, где ключ — значение переданного аргумента, а значение —
# имя аргумента. Если ключ не хешируем, используйте его строковое представление
import typing


def func(*, arg):
    my_dict = {str(value): name for name, value in globals().items() if value == arg and not isinstance(value, typing.Hashable)}
    if len(my_dict) == 0:
        my_dict[arg] = str([name for name, value in globals().items() if value == arg][0])
    return my_dict


x = 5
print(func(arg=x))
y = [1, 2, 3]
print(func(arg=y))
