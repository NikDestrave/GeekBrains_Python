'''Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять список только числами.
Класс-исключение должен контролировать типы данных элементов списка.'''

class NumError(Exception):
    def __init__(self, list):
        self.list = list

user_list = []

while True:
    try:
        value = input('Введите значение или exit для выхода: ')
        if value == 'exit':
            print(f'Программа завершена, ответ {user_list}')
            break
        elif value.isdigit() == False:
            raise NumError('Вы ввели не число')
        else:
            user_list.append(int(value))
    except NumError as err:
        print(err)




# try:
#     input_data = int(input_data)
#     if input_data < 0:
#         raise NumError('Вы ввели отрицательное число')
#     else:
#         print('Все ок')
# except NumError as err:
#     print(err)
# except ValueError:
#     print('Вы ввели не число')