# Спортсмен занимается ежедневными пробежками.
# В первый день его результат составил a километров.
# Каждый день спортсмен увеличивал результат
# на 10 % относительно предыдущего.
# Требуется определить номер дня, на который
# общий результат спортсмена составить не менее b километров.
# Программа должна принимать значения параметров a и b
# и выводить одно натуральное число — номер дня.

a = int(input("Enter the result of the first day: "))
b = int(input("Enter the desired result: "))

if a >= b:
    print("Congratulations, you have reached the goal!")
else:
    i = 1
    while a < b:
        a = a + a / 10
        i += 1
    print(f"You will achieve your goal in {i} days!")
