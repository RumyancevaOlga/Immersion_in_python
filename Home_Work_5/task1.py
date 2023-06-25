# Напишите функцию, которая принимает на вход строку - абсолютный путь
# до файла. Функция возвращает кортеж из трёх элементов: путь, имя файла,
# расширение файла.

def path_name_extension(path: str) -> tuple:
    path, name = path.rsplit('\\', 1)
    name, extension = name.split('.')
    res = [path, name, extension]
    return tuple(res)


path_to_file = r'G:\Домашнее задание GeekBrains\Immersion_in_python\Home_Work_5\task1.py'
print(path_name_extension(path_to_file))
