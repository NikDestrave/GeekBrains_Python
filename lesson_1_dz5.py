# 5. Запросите у пользователя значения выручки и издержек фирмы.
# Определите, с каким финансовым результатом работает фирма (прибыль — выручка
# больше издержек, или убыток — издержки больше выручки). Выведите соответствующее сообщение.
# Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к
# выручке). Далее запросите численность сотрудников фирмы и определите прибыль фирмы в
# расчете на одного сотрудника.

revenue = int(input('Введите сумму выручки фирмы: '))
cost = int(input('Введите сумму издержек фирмы: '))
profit = revenue - cost

if revenue > cost:
    print(f'Фирма в прибыльном состоянии. Рентабельность прибыли = {profit}')
    count_user = int(input('Количество сотрудников в фирме: '))
    profit_users = profit / count_user
    print(f'Прибыль одного сотрудника = {profit_users}')
else:
    print('Фирма в убыточном состоянии')

