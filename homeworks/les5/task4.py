"""
Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""

with open('task4.txt', 'r', encoding='UTF-8') as file, open('task4_1.txt', 'w', encoding='UTF-8') as file_1:
    for line in file.readlines():
        file_1.write(line.replace('Two', 'Два').replace('One', 'Один') \
                     .replace('Three', 'Три').replace('Four', 'Четыре'))

