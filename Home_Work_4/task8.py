# Создайте несколько переменных заканчивающихся и не оканчивающихся на «s».
# ✔Напишите функцию, которая при запуске заменяет содержимое переменных оканчивающихся
# на s (кроме переменной из одной буквы s) на None.
# ✔Значения не удаляются, а помещаются в одноимённые переменные без s на конце.

names = ['Jack', 'Samanta', 'Michel', 'Vivien']
s = 42
ages = [33, 43, 50, 28]
x = 256


def my_func():
    my_dict = globals()
    for key, value in my_dict.items():
        if key.endswith('s') and len(key) > 1:
            locals()[key[:-1]] = value
            my_dict[key] = None
    new_dict = locals()
    for key, item in new_dict.items():
        globals()[key] = item


my_func()
print(names, s, ages, x)
my_dict = globals()
for key, value in my_dict.items():
    if key[0] != '_':
        print(key, value)
