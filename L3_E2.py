# Реализовать функцию, принимающую несколько параметров,
# описывающих данные пользователя: имя, фамилия, год рождения,
# город проживания, email, телефон. Функция должна принимать
# параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.


def param_func(name, surname, year, city, email, phone):
    print(name, surname, year, city, email, phone)


param_func(
    name=input('Enter your name: '),
    surname=input('Enter your surname: '),
    year=input('Enter your year of birth : '),
    city=input('Enter your city : '),
    email=input('Enter your email : '),
    phone=input('Enter your phone number : ')
)
