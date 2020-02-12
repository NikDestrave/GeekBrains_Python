# 7. Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.
# При вызове функции должен создаваться объект-генератор. Функция должна вызываться следующим образом: for el in fibo_gen().
# Функция отвечает за получение факториала числа, а в цикле необходимо выводить только первые 15 чисел.
# Подсказка: факториал числа n — произведение чисел от 1 до n. Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.

def fibo_gen(count):
    factorial = 1
    for i in range(1, count + 1):
        factorial *= i
    yield factorial

user_number = int(input('Введите число: '))

for el in fibo_gen(user_number):
    print(f'Факториал числа "{user_number}" = {el}')