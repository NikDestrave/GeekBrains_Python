from itertools import count, cycle

def salary(prod, rate, prize):
    user_zp = int(prod) * float(rate) + float(prize)
    print(f'Заработная плата сотрудника: {user_zp}р.')


def list_numbers(user_list):
    new_list = [int(i) for i in user_list.split()]
    result = [new_list[q] for q in range(len(new_list)) if new_list[q] > new_list[q - 1]]
    print(result)


def numbers(min, max):
    print(list(q for q in range(min, max) if q % 20 == 0 or q % 21 == 0))


def numbers_2(user_list):
    list_2 = [int(i) for i in user_list.split()]
    result = [q for q in list_2 if list_2.count(q) == 1]
    print(result)

def func_reduce(num_1, num_2):
    return num_1 + num_2

def script_1(num):
    for i in count(num):
        if i > 50:
            break
        else:
            print(i)

def script_2(list):
    list_2 = [i for i in list.split()]
    count = 0
    for i in cycle(list_2):
        if count > 10:
            break
        print(i)
        count += 1

if __name__ == '__main__':
    salary(5, 50, 2500)
    list_numbers('1 5 3 8 6 5')
    numbers()
    numbers_2(input('Введите числа через пробел: '))
    func_reduce()