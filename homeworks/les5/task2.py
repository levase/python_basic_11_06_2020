"""
Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""

with open('task2.txt', 'r', encoding='UTF-8') as file:
    content = file.readlines()
    print(f'Количество строк равно {len(content)}')
    for idx, string in enumerate(content, 1):
        print(f'Количество слов в строке {idx} равно {len(string.split())}')

