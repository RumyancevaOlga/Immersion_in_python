# Вспоминаем задачу 3 из прошлого семинара. Мы сформировали текстовый файл с псевдо именами
# и произведением чисел.
# Напишите функцию, которая создаёт из созданного ранее файла новый с данными в формате JSON.
# Имена пишите с большой буквы.
# Каждую пару сохраняйте с новой строки.

import json


def new_json_file(file_name: str):
    my_dict = {}

    with open(file_name, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines:
            key, value = line.strip().title().split(' ')
            my_dict[key] = value

    with open('results.json', 'w', encoding='utf-8') as f_json:
        json.dump(my_dict, f_json, indent=2, ensure_ascii=False)


new_json_file('results.txt')
