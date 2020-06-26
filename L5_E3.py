# Создать текстовый файл (не программно), построчно записать
# фамилии сотрудников и величину их окладов. Определить, кто из
# сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.

# аналогично прошлому заданию, путь к файлу у Вас будет другой
f = open('/home/alina/PycharmProjects/salary.txt', 'r')

salary_sum, salary_cnt = 0, 0

for line in f:
    name, salary = line.split()
    salary = int(salary)
    salary_sum += salary
    salary_cnt += 1
    if salary < 20000:
        print(name)

print('Avg salary:', salary_sum / salary_cnt)
