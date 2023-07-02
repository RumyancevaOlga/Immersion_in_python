# Прочитайте созданный в прошлом задании csv файл без использования csv.DictReader.
# Дополните id до 10 цифр незначащими нулями.
# В именах первую букву сделайте прописной.
# Добавьте поле хеш на основе имени и идентификатора.
# Получившиеся записи сохраните в json файл, где каждая строка csv файла представлена
# как отдельный json словарь.
# Имя исходного и конечного файлов передавайте как аргументы функции.

import json
import csv


def my_func(file_csv, file_json):
    with(open(file_csv, 'r', encoding='utf-8') as f_read,
         open(file_json, 'w', encoding='utf-8') as f_write
         ):
        file = [*csv.reader(f_read)]
        header = file[0]
        my_list = []
        for id_person, name, level in file[1:]:
            my_list.append({header[0]: id_person, header[1]: name, header[2]: level})

        json.dump(my_list, f_write, ensure_ascii=False, indent=2)


if __name__ == '__main__':
    my_func('users.csv', 'users.json')
