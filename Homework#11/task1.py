# Task1
''
"""
Погружение в Python (семинары)
Урок 11. ООП. Особенности Python

Решить задания, которые не успели решить на семинаре. (решили все)

Добавьте ко всем задачам с семинара строки документации и методы вывода информации на печать.

Создайте класс Матрица. Добавьте методы для: - вывода на печать,
сравнения,
сложения,
*умножения матриц
"""


class Matrix:
    def __init__(self, rows, columns):
        """
        Принимает на вход
        :param rows: Ряды
        :param columns: Столбцы
        """
        self.rows = rows
        self.columns = columns
        self.matrix = [[0 for j in range(columns)] for i in range(rows)]  # Пробегаем по ним

    def __str__(self):
        """
        print
        :return: Вывод пользователю
        """
        return '\\n'.join([' '.join([str(elem) for elem in row]) for row in self.matrix])

    def __eq__(self, other):
        """
        Сравнение
        :param other:
        :return:
        """
        if isinstance(other, Matrix):
            if self.rows == other.rows and self.columns == other.columns:
                for i in range(self.rows):
                    for j in range(self.columns):
                        if self.matrix[i][j] != other.matrix[i][j]:
                            return False
                return True
            else:
                return False
        else:
            return False

    def __add__(self, other):
        """
        Сложение
        :param other:
        :return:
        """
        if isinstance(other, Matrix):
            if self.rows == other.rows and self.columns == other.columns:
                result = Matrix(self.rows, self.columns)
                for i in range(self.rows):
                    for j in range(self.columns):
                        result.matrix[i][j] = self.matrix[i][j] + other.matrix[i][j]
                return result
            else:
                return None
        else:
            return None

    def __mul__(self, other):
        """
        Умножение
        :param other:
        :return:
        """
        if isinstance(other, Matrix):
            if self.columns == other.rows:
                result = Matrix(self.rows, other.columns)
                for i in range(self.rows):
                    for j in range(other.columns):
                        for k in range(self.columns):
                            result.matrix[i][j] += self.matrix[i][k] * other.matrix[k][j]
                return result
            else:
                return None
        else:
            return None


if __name__ == '__main__':
    # создание матриц
    matrix1 = Matrix(2, 3)
    matrix2 = Matrix(2, 3)
    matrix3 = Matrix(3, 2)

    # Заполнение матриц
    matrix1.matrix = [[1, 2, 3], [4, 5, 6]]
    matrix2.matrix = [[1, 2, 3], [4, 5, 6]]
    matrix3.matrix = [[1, 2], [3, 4], [5, 6]]

    # Print матриц
    print("Matrix 1:\\n", matrix1)
    print("Matrix 2:\\n", matrix2)
    print("Matrix 3:\\n", matrix3)

    # Сравнение матриц
    print("Matrix 1 == Matrix 2:", matrix1 == matrix2)
    print("Matrix 1 == Matrix 3:", matrix1 == matrix3)

    # Сложение матриц
    matrix_sum = matrix1 + matrix2
    print("Matrix 1 + Matrix 2:\\n", matrix_sum)

    # Умножение матриц
    matrix_product = matrix1 * matrix3
    print("Matrix 1 * Matrix 3:\\n", matrix_product)
