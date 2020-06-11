#  Запросите у пользователя значения выручки и издержек фирмы.
#  Определите, с каким финансовым результатом работает фирма
#  (прибыль — выручка больше издержек, или убыток — издержки больше выручки).
#  Выведите соответствующее сообщение.
#  Если фирма отработала с прибылью, вычислите рентабельность выручки
#  (соотношение прибыли к выручке).
#  Далее запросите численность сотрудников фирмы и определите прибыль
#  фирмы в расчете на одного сотрудника.

revenue = int(input("Enter revenue value: "))
cost = int(input("Enter cost value: "))

# Если фирма приносит доход
if revenue > cost:
    print("Your company makes a profit!")

    profit_margin = revenue / cost
    print(f"Revenue stability is {profit_margin:.2f}")

    employees = int(input("Enter the number of employees: "))
    profit_per_employees = (revenue - cost) / employees
    print(profit_per_employees)
# Если фирма убыточная или выходит в ноль
else:
    print("Your company is unprofitable.")

