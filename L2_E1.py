# Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента.
# Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя,
# а указать явно, в программе.

my_list = ['cat', False, 4.2, None, 42]


def my_type():
    for el in range(len(my_list)):
        print(type(my_list[el]))
    return


my_type()
