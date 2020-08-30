'''3. Реализовать программу работы с органическими клетками. Необходимо создать класс Клетка.
В его конструкторе инициализировать параметр, соответствующий количеству клеток (целое число).
В классе должны быть реализованы методы перегрузки арифметических операторов: сложение (add()), вычитание (sub()), умножение (mul()), деление (truediv()).
Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение, умножение и обычное (не целочисленное) деление клеток, соответственно.
В методе деления должно осуществляться округление значения до целого числа.'''


class Cell:
    def __init__(self, cell_1, cell_2):
        self.cell_1 = cell_1
        self.cell_2 = cell_2

    def __add__(self, other):
        return Cell(self.cell_1 + other.cell_1, self.cell_2 + other.cell_2)

    def __sub__(self, other):
        return Cell(self.cell_1 - other.cell_1, self.cell_2 - other.cell_2)

    def __mul__(self, other):
        pass

    def __truediv__(self, other):
        pass

    def __str__(self):
        return f'{self.cell_1} {self.cell_2}'


a = Cell([1, 1], [1, 1])
b = Cell([1, 1], [1, 1])
print(a + b)
c = Cell([1, 1, 1, 1], [1, 1])
d = Cell([1, 1], [1, 1])
print(c - d)
