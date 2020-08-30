# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.

with open('file3.txt', 'r') as file:
    result = [i for i, n in (line.split(' ') for line in file.readlines()) if int(n) < 20000]
    print('\n'.join(result))
    file.seek(0)
    sum_result = [int(n) for i, n in (line.split(' ') for line in file.readlines())]
    print(f'Средний заработок {len(sum_result)} сотрудников = {sum(sum_result) / len(sum_result)}')