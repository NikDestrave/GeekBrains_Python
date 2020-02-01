# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух аргументов.

def my_func(num1, num2, num3):
    min_number = min(num1, num2, num3)
    return num1 + num2 + num3 - min_number

print(my_func(int(input('Введите 1 число: ')), int(input('Введите 2 число: ')), int(input('Введите 3 число: '))))