# 1. Создать список и заполнить его элементами различных типов данных. Реализовать скрипт проверки типа данных каждого элемента.
# Использовать функцию type() для проверки типа. Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.

user_list = [123, 'Привет', [1, 2, 3], {1, 2, 3}]

for i in range(len(user_list)):
    print(f'Значение {i + 1} = {type(user_list[i])}')