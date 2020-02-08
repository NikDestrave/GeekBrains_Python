# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

import random

with open('file5.txt', 'w+') as file:
    random_numbers = [random.randint(1, 100) for i in range(10)]
    file.write(' '.join(map(str, random_numbers)))
    file.seek(0)
    sum_numbers = sum(list(map(int, file.read().split())))
    print(sum_numbers)