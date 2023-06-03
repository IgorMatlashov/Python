# 5. Запросите у пользователя значения выручки и издержек фирмы.
# Определите, с каким финансовым результатом работает фирма
# (прибыль — выручка больше издержек, или убыток — издержки больше выручки).
# Выведите соответствующее сообщение. Если фирма отработала с прибылью,
# вычислите рентабельность выручки (соотношение прибыли к выручке).
# Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.

profit = float(input("Enter the profit of the company "))
costs = float(input("Enter the costs of the company "))

if profit > costs:
    print(f'The company operates profitably. The profitability of revenue amounted to {profit / costs:.2f}')
    workers = int(input("Enter the number of employees: "))
    print(f'Profit per employee amounted to {profit / workers:.2f}')
elif profit == costs:
    print('The company operates at zero')
else:
    print("The company operates at a loss")