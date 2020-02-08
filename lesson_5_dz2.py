# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.

with open('file2.txt', 'r') as f:
    print(f'Количество строк = {len(f.readlines())}')
    f.seek(0)
    count = [len(line.split()) for line in f]
    print(count)
    print(f'Количество слов = {sum(count)}')
