# Для списка реализовать обмен значений соседних элементов, т.е.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().

quan = int(input("Enter the number of items: "))

my_list = []
i = 0
while i < quan:
    my_list.append(input("Enter the following item value: "))
    i += 1

el = 0
for elem in range(int(len(my_list) / 2)):
    my_list[el], my_list[el + 1] = my_list[el + 1], my_list[el]
    el += 2

print(my_list)
