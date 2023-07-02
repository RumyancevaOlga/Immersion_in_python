# Напишите функцию, которая ищет json файлы в указанной директории и сохраняет их
# содержимое в виде одноименных pickle файлов.

import json
import pickle
import os


def my_func(dir_):
    files_json = [i for i in os.listdir(dir_) if i.endswith('.json')]
    for file in files_json:
        with (open(os.path.join(dir_, file), 'r', encoding='utf-8') as f_read,
              open(os.path.join(dir_, file.strip('.json') + '.pickle'), 'wb') as f_write
              ):
            pickle.dump(json.load(f_read), f_write)


if __name__ == '__main__':
    my_func(os.getcwd())
    with open('user.pickle', 'rb') as f_pickle:
        print(pickle.load(f_pickle))
