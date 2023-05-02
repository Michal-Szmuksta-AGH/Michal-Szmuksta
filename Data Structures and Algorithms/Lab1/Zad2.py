# NIESKOŃCZONE
import copy


class Matrix:
    def __init__(self, parameter, filler=0):
        if isinstance(parameter, tuple):
            matrix = []
            m, n = parameter
            for i in range(m):
                matrix.append([filler] * n)
            self.__matrix = matrix
        elif isinstance(parameter, list):
            self.__matrix = parameter
        else:
            raise TypeError

    def size(self):
        return len(self.__matrix), len(self.__matrix[0])

    def __add__(self, other):
        if self.size() == other.size():
            result = []
            for s, o in zip(self.__matrix, other.__matrix):
                value = []
                for i, j in zip(s, o):
                    value.append(i + j)
                result.append(value)
            return Matrix(result)
        else:
            raise ArithmeticError

    def __mul__(self, other):
        a, b = self.size()
        c, d = other.size()
        if b == c:
            result = []
            for row in range(a):
                value = []
                for col in range(d):
                    sum = 0
                    for s, o in zip(self.__matrix[row], other.__matrix):
                        sum = sum + s * o[col]
                    value.append(sum)
                result.append(value)
            return Matrix(result)
        else:
            raise ArithmeticError

    def __getitem__(self, item):
        return self.__matrix[item]

    def __str__(self):
        string = ''
        for i in self.__matrix:
            string = string + str(i) + ''
            string = string + '\n'
        return string


def chio(matrix: Matrix) -> int:
    matrix_copy = copy.deepcopy(matrix)
    m, n = matrix_copy.size()
    if m == 2 and n == 2:
        return matrix_copy[0][0] * matrix_copy[1][1] - matrix_copy[0][1] * matrix_copy[1][0]

    elif m == n:
        sem = 1
        if matrix_copy[0][0] == 0:
            for i in range(1, m):
                if matrix_copy[i][0] != 0:
                    row = [j for j in matrix_copy[i]]
                    for k in range(m):
                        matrix_copy[i][k] = matrix_copy[0][k]
                    for h in range(m):
                        matrix_copy[0][h] = row[h]
                    sem = -1
                    break
            if sem == 1:
                return 0

        reduced_matrix = Matrix((m - 1, m - 1))
        for i in range(m - 1):
            for j in range(m - 1):
                auxiliary_matrix = Matrix(
                    [[matrix_copy[0][0], matrix_copy[0][j + 1]], [matrix_copy[i + 1][0], matrix_copy[i + 1][j + 1]]])
                reduced_matrix[i][j] = chio(auxiliary_matrix)
        return 1 / (matrix_copy[0][0] ** (m - 2)) * chio(reduced_matrix) * sem

    else:
        raise TypeError


def main():
    M = Matrix([
        [5, 1, 1, 2, 3],
        [4, 2, 1, 7, 3],
        [2, 1, 2, 4, 7],
        [9, 1, 0, 7, 0],
        [1, 4, 7, 2, 2]
    ])
    N = Matrix([
        [0, 1, 1, 2, 3],
        [4, 2, 1, 7, 3],
        [2, 1, 2, 4, 7],
        [9, 1, 0, 7, 0],
        [1, 4, 7, 2, 2]
    ])
    print(chio(M))
    print(chio(N))


if __name__ == "__main__":
    main()
