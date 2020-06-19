# Реализовать функцию my_func(), которая принимает
# три позиционных аргумента, и возвращает сумму
# наибольших двух аргументов.


def max_sum_func(a, b, c):
    user_num = [a, b, c]
    result = []

    max_1 = max(user_num)  # ищем самое макс
    result.append(max_1)  # добавляем первое макс в список
    user_num.remove(max_1)  # убираем первое макс

    max_2 = max(user_num)  # ищем второе макс
    result.append(max_2)  # добавляем второе макс в список

    print(sum(result))  # считаем сумму двух макс


max_sum_func(
    a=int(input('Enter first number: ')),
    b=int(input('Enter second number: ')),
    c=int(input('Enter third number : '))
)
