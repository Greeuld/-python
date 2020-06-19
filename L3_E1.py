# Реализовать функцию, принимающую два числа (позиционные аргументы)
# и выполняющую их деление. Числа запрашивать у пользователя,
# предусмотреть обработку ситуации деления на ноль.


def div_func(n, d):
    try:
        result = n / d
        return result
    except ZeroDivisionError:
        return "The denominator shouldn't be zero"


print(div_func(int(input("Enter the numerator: ")), int(input("Enter the denominator: "))))
