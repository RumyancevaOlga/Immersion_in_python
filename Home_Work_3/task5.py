# ✔ Создайте вручную список с повторяющимися целыми числами.
# ✔ Сформируйте список с порядковыми номерами
# нечётных элементов исходного списка.
# ✔ Нумерация начинается с единицы.

my_list = [2, 2, 5, 6, 7, 8, 3, 4, 5, 6, 1, 3, 4, 9, 8, 7, 6, 5]
new_list = []

# for i in range(len(my_list)):
#     if my_list[i] % 2 > 0:
#         new_list.append(my_list.index(my_list[i], i) + 1)
#
# print(new_list)
# new_list.clear()

for i, item in enumerate(my_list):
    if item % 2 > 0:
        new_list.append(my_list.index(item, i) + 1)

print(new_list)
