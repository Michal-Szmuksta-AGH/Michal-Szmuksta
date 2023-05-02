# NIESKOŃCZONE


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


def transpose(matrix: Matrix) -> Matrix:
    m, n = matrix.size()
    new_matrix = Matrix((n, m))
    for i in range(m):
        for j in range(n):
            new_matrix[j][i] = matrix[i][j]
    return new_matrix


def main():
    A = Matrix([[1, 0, 2], [-1, 3, 1]])
    A_t = transpose(A)
    print(A_t)
    B = Matrix((2, 3), 1)
    A_plus_B = A + B
    print(A_plus_B)
    C = Matrix([[3, 1], [2, 1], [1, 0]])
    A_multiplied_by_B = A * C
    print(A_multiplied_by_B)


if __name__ == "__main__":
    main()
