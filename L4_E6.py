# Реализовать два небольших скрипта:
# а) бесконечный итератор, генерирующий целые числа,
# начиная с указанного,
# б) бесконечный итератор, повторяющий элементы
# некоторого списка, определенного заранее.
# Подсказка: использовать функцию count() и cycle()
# модуля itertools.

# Задание А

from itertools import count

for el in count(int(input('Enter start number: '))):
    print(el)

# Задание Б

from itertools import cycle

my_list = [True, 'cat', 42, None]
for el in cycle(my_list):
    print(el)
