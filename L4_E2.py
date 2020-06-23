# Представлен список чисел. Необходимо вывести элементы
# исходного списка, значения которых больше предыдущего элемента.
# Подсказка: элементы, удовлетворяющие условию, оформить
# в виде списка. Для формирования списка использовать генератор.

import random

my_list = [random.randint(0, 100) for i in range(10)]
my_new_list = [el for num, el in enumerate(my_list) if my_list[num - 1] < my_list[num]]

print(f'Source list: {my_list}')
print(f'New list: {my_new_list}')
