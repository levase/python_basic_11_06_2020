"""
Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран
"""

with open('task5.txt', 'w', encoding='UTF-8') as file:
    for number in range(1, 101):
        print(number, end=' ', file=file)


with open('task5.txt', 'r', encoding='UTF-8') as file_2:
    result = 0
    for digit in file_2.read().split():
        digit = int(digit)
        result += digit
    print(result)
    # print(sum([int(digits) for digits in file_2.read().split()]))
