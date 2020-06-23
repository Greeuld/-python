# Представлен список чисел. Определить элементы списка,
# не имеющие повторений. Сформировать итоговый массив чисел,
# соответствующих требованию. Элементы вывести
# в порядке их следования в исходном списке.
# Для выполнения задания обязательно использовать генератор.

import random

my_list = [random.randint(0, 100) for i in range(20)]
my_new_list = [el for el in my_list if my_list.count(el) < 2]

print(f'Source list: {my_list}')
print(f'New list: {my_new_list}')
