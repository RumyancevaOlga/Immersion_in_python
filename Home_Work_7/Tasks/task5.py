# ✔Создайте функцию для сортировки файлов по директориям: видео,
# изображения, текст и т.п.
# ✔Каждая группа включает файлы с несколькими расширениями.
# ✔В исходной папке должны остаться только те файлы, которые не подошли для сортировки.

__all__ = ['group']

import os

DCT = {'Video': ('mkv', 'avi', 'mp4'),
       'Image': ('png', 'jpg', 'jpeg'),
       'Doc': ('txt', 'bin'),
       }


def group(dir_):
    files = [file for file in os.listdir(dir_) if os.path.isfile(file)]
    for fold, exts in DCT.items():
        if fold not in os.listdir():
            os.mkdir(fold)
        for file in files:
            if file.split('.')[1] in exts:
                os.replace(file, os.path.join(os.getcwd(), fold, file))


if __name__ == '__main__':
    group(os.getcwd())
