# ✔Функция получает на вход список чисел и два индекса.
# ✔Вернуть сумму чисел между между переданными индексами.
# ✔Если индекс выходит за пределы списка, сумма считается до конца
# и/или начала списка.

def my_func(my_list_a: list, start_a: int, end_a: int) -> int:
    if start_a > end_a:
        start_a, end_a = end_a, start_a
    if start_a < 0:
        start_a = 0
    if end_a >= len(my_list_a):
        end_a = len(my_list_a) - 1
    # использую срез в функции sum
    my_sum = sum(my_list_a[start_a:end_a + 1])
    return my_sum


my_list = [2, 5, 7, 9, 1, 3, 4, 5, 2, 6, 1, 8, 4]
start = 4
end = 100

print(my_func(my_list, end, start))
