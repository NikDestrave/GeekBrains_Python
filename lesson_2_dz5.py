#5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел. У пользователя необходимо запрашивать
# новый элемент рейтинга. Если в рейтинге существуют элементы с одинаковыми значениями, то новый элемент с тем же значением должен разместиться
# после них.
# Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
# Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
# Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
# Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
# Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].

user_value = int(input('Введите значение: '))
my_list = [7, 5, 3, 3, 2]

for el in my_list:
    if my_list.count(user_value) > 0:
        my_list.insert(my_list.index(user_value) + my_list.count(user_value), user_value)
        break
    else:
        if user_value > el:
            my_list.insert(my_list.index(el), user_value)
            break
        elif user_value < my_list[len(my_list) - 1]:
            my_list.append(user_value)

print(my_list)