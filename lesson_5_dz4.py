# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные. При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

with open('file4.txt', 'r') as f:
    numbers = {1: 'Один', 2: 'Два', 3: 'Три', 4: 'Четыре'}
    lines = dict((int(n), i) for i, n in (line.split(' - ') for line in f.readlines()))
    lines_rus = lines.update(numbers)
    a = [n + ' - ' + str(i) for i, n in lines.items()]
    with open('file4_1.txt', 'w') as file:
        file.write('\n'.join(a))
