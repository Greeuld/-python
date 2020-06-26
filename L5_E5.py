# Создать (программно) текстовый файл, записать в него программно набор чисел,
# разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и
# выводить ее на экран.

import random

f = open('/home/alina/PycharmProjects/numbers.txt', 'w')
f.write(' '.join([str(random.randint(0, 10)) for i in range(20)]))
f.close()

f = open('/home/alina/PycharmProjects/numbers.txt', 'r')
print(sum(map(int, f.read().split())))
f.close()
