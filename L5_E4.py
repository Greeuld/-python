# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую
# построчно данные. При этом английские числительные должны заменяться на
# русские. Новый блок строк должен записываться в новый текстовый файл.

import re

f1 = open('/home/alina/PycharmProjects/num.txt', 'r')
f2 = open('/home/alina/PycharmProjects/res.txt', 'w')

re_list = [(r'One', 'Один'), (r'Two', 'Два'), (r'Three', 'Три'), (r'Four', 'Четыре')]

for line in f1:
    for re1, re2 in re_list:
        line = re.sub(re1, re2, line)
    f2.write(line)

f1.close()
f2.close()
