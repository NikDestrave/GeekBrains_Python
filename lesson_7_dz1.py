'''Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()), который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.'''


class Matrix:
    def __init__(self, matrix_1, matrix_2):
        self.matrix_1 = matrix_1
        self.matrix_2 = matrix_2
        self.result = []

    def __add__(self, other):
        super().__init__(self.result)
        for i in range(len(self.matrix_1)):
            for j in range(len(self.matrix_1[0])):
                sum_result = self.matrix_1[i][j] + self.matrix_2[i][j]
                self.result.append(sum_result)

    def __str__(self):
        return f'{self.result}'


matrixes = Matrix([[31, 22], [37, 43], [51, 86]],
                  [[8, 5], [10, 7], [5, 20]])

print(matrixes)
