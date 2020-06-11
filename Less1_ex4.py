# Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

number = int(input("Enter a positive integer: "))

num = number // 10
maxi = number % 10
while num > 0:
    if num % 10 > maxi:
        maxi = num % 10
    num = num // 10

print(maxi)
