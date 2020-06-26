# Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме: название,
# форма собственности, выручка, издержки. Пример строки файла: firm_1 ООО 10000 5000. Необходимо построчно прочитать
# файл, вычислить прибыль каждой компании, а также среднюю прибыль. Если фирма получила убытки, в расчет средней
# прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
# а также словарь со средней прибылью. Если фирма получила убытки, также добавить ее в словарь (со значением
# убытков).
#
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
#
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
#
# Пример json-объекта: [{"firm_1": 5000, "firm_2": 3000,
# "firm_3": 1000}, {"average_profit": 2000}]
#
# Подсказка: использовать менеджеры контекста.


# на вход данные:
# firm_1 ООО 10000 5000
# firm_2 ООA 11000 4000
# firm_3 ОAО 12000 3000
# firm_4 AОО 13000 2000
# firm_5 AAA 14000 1000
# firm_5 WOW 1000 11000

import json

profit = {}
pr = {}
prof = 0
prof_aver = 0
i = 0
with open('/home/alina/PycharmProjects/firm.txt', 'r', encoding='utf-8-sig') as file:
    for line in file:
        name, firm, plus, minus = line.split()
        profit[name] = int(plus) - int(minus)
        if profit.setdefault(name) >= 0:
            prof = prof + profit.setdefault(name)
            i += 1
    if i != 0:
        prof_aver = prof / i
        print(f'Average profit - {prof_aver:.2f}')
    else:
        print(f'Zero profit')
    pr = {'average profit': round(prof_aver)}
    profit.update(pr)
    print(f'Profit by firm - {profit}')

with open('firm.json', 'w') as write_js:
    json.dump(profit, write_js)

    js_str = json.dumps(profit)
    print(f'Json-file: \n '
          f' {js_str}')

# На выходе получаем:
# Average profit - 9000.00
# Profit by firm - {'firm_1': 5000, 'firm_2': 7000, 'firm_3': 9000,
# 'firm_4': 11000, 'firm_5': -10000, 'average profit': 9000}
# Json-file: {"firm_1": 5000, "firm_2": 7000,
# "firm_3": 9000, "firm_4": 11000, "firm_5": -10000, "average profit": 9000}
