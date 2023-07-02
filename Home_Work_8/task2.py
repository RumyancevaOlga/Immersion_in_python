# Напишите функцию, которая в бесконечном цикле запрашивает имя, личный идентификатор и
# уровень доступа (от 1 до 7).
# После каждого ввода добавляйте новую информацию в JSON файл.
# Пользователи группируются по уровню доступа.
# Идентификатор пользователя выступает ключём для имени.
# Убедитесь, что все идентификаторы уникальны независимо от уровня доступа.
# При перезапуске функции уже записанные в файл данные должны сохраняться.

__all__ = ['code']


import json
import os


def code(filename):
    if os.path.exists(filename):
        with open(filename, "r", encoding="utf-8") as f:
            my_dict = json.load(f)
    else:
        my_dict = {str(key): {} for key in range(1, 8)}
    # print(my_dict)
    while True:
        data = input("Введите Имя, Личный идентификатор,уровень доступа через пробел:")
        if not data:
            break
        name, id_person, level, *_ = data.split()
        if id_person not in my_dict[level]:
            my_dict[level].update({id_person: name})
        else:
            print('Идентификатор не уникален')
    print(my_dict)

    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_dict, f, indent=1)


if __name__ == '__main__':
    filename = 'file.json'
    code(filename)
