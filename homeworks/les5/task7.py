"""
Создать (не программно) текстовый файл,
в котором каждая строка должна содержать данные о фирме: название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджеры контекста.
"""

import json

result_list = []
result_dict = {}
average = 0
firm_count = 0

with open('task7.txt', 'r', encoding='UTF-8') as file:
    firm_list = file.readlines()
    for firm in firm_list:
        [name, form, sales, spent] = [_ for _ in firm.split()]
        firm_profit = float(sales) - float(spent)
        if firm_profit >= 0:
            firm_count += 1
            average += firm_profit
        result_dict.update([(name, firm_profit)])
average_profit = round(average / firm_count, 2)
result_list.append(result_dict)
result_list.append({"average_profit": round(average_profit, 2)})
print(result_list)

with open('result_task7.json', 'w') as file2:
    json.dump(result_list, file2)
