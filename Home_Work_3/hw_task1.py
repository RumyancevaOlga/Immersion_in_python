# Дан список повторяющихся элементов. Вернуть список с дублирующимися
# элементами. В результирующем списке не должно быть дубликатов.

my_list = [2, 2, 5, 6, 7, 8, 3, 4, 5, 6, 1, 3, 4, 9, 8, 7, 6, 5, 15]
result = []
for item in my_list:
    if my_list.count(item) > 1:
        if item not in result:
            result.append(item)

print(result)
