# ✔ Пользователь вводит строку текста.
# ✔ Подсчитайте сколько раз встречается
# каждая буква в строке без использования
# метода count и с ним.
# ✔ Результат сохраните в словаре, где ключ —
# символ, а значение — частота встречи
# символа в строке.
# ✔ Обратите внимание на порядок ключей.
# Объясните почему они совпадают
# или не совпадают в ваших решениях.

import re

text = input('Введите текст: ')
text = re.sub('\W+', '', text)

my_dict = {key: text.count(key) for (value, key) in enumerate(text)}

new_dict = {}
for i in range(len(text)):
    count = 0
    value = text[i]
    for j, item in enumerate(text):
        if value == item:
            count += 1
    new_dict[text[i]] = count

print(my_dict)
print(new_dict)

# порядок ключей совпадает в обоих словарях, поскольку они добавлялись в одинаковом порядке
