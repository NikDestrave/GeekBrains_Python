# 1. Поработайте с переменными, создайте несколько, выведите на экран,
# запросите у пользователя несколько чисел и строк и сохраните в переменные,
# выведите на экран.

print('Введите ваши данные:')

name = input('Имя: ')
surname = input('Фамилию: ')
age = int(input('Возраст: '))
weight = int(input('Вес: '))

print(f'{name} {surname}, возраст {age} лет, весом {weight} кг.')