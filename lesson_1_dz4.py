# 4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

user_numbers = input('Введите положительное число: ')
max_number = 0

for number in user_numbers:
    number = int(number)
    if number > max_number:
        max_number = number
    else:
        continue

print(f'Максимальная цифра из числа {user_numbers} = {max_number}')