revenue = input('Введите числовое значение выручки: ')
cost = input('Введите числовое значение издержек: ')
revenue = int(revenue)
cost = int(cost)

while revenue > cost:
    print('Вы работаете с прибылью')
    profit = revenue - cost
    profitability = revenue / profit
    print(f'Рентабельность выручки равна {profitability:.2f}')
    staff = input('Введите количество сотрудников: ')
    staff = int(staff)
    staff_profit = profit / staff
    print(f'Прибыль фирмы в расчете на одного сотрудника равна {staff_profit:.2f}')
    break
else:
    print('Вы работаете в убыток')