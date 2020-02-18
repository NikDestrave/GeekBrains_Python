'''Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год и
преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года
(например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.'''


class Date:
    def __init__(self, date):
        self.date = str(date)

    @classmethod
    def date_int(cls, date):
        str_date = [int(i) for i in str(date).split('-')]
        print(str_date)
        return str_date

    @staticmethod
    def date_valid(date):
        str_date = [int(i) for i in str(date).split('-')]
        day = '' if str_date[0] >= 1 and str_date[0] <= 31 else 'День введен неверно'
        month = '' if str_date[1] >= 1 and str_date[1] <= 12 else 'Месяц введен неверно'
        year = '' if len(list(str(str_date[2]))) == 4 else 'Год введен неверно'
        print(f'{day}{month}{year}')

date = '23-02-2020'
Date.date_int(date)
Date.date_valid(date)