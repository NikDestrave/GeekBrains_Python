'''Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных, вводимых пользователем.
При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.'''

class ZeroError(Exception):
    def __init__(self, txt):
        self.txt = txt

number_1 = int(input('Введите делимое: '))
number_2 = int(input('Введите делитель: '))


try:
    if number_2 == 0:
        raise ZeroError('Нельзя делить на нуль!')
    else:
        print(number_1 / number_2)
except ZeroError as err:
    print(err)
except ValueError:
    print('Вы ввели не число')