from itertools import permutations as perm, combinations_with_replacement as comb, combinations


def check_queen(coordinates: list) -> bool:
    for item in coordinates:
        for j in range(coordinates.index(item) + 1, len(coordinates)):
            # проверка диагоналей, затем горизонтали и вертикали
            if item[0] - item[1] == coordinates[j][0] - coordinates[j][1] or \
                    item[0] + item[1] == coordinates[j][0] + coordinates[j][1] or \
                    item[0] == coordinates[j][0] or item[1] == coordinates[j][1]:
                return False
    return True


def generator_and_print():
    variants = sorted(list(set(list(comb(range(1, 9), 2)) + list(perm(range(1, 9), 2)))))
    i = 1
    for item in combinations(variants, 8):
        if check_queen(item):
            print(f'{i}: {item}')
            i += 1
        if i == 93:
            break


my_coordinates = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8]]
print(check_queen(my_coordinates))

generator_and_print()
