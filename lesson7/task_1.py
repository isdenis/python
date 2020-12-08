class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        a = ""
        for i in self.matrix:
            for j in i:
                a = a + " " + str(j)
            a = a + '\n'
        return a

    def __add__(self, other):
        c = []
        for i in range(len(self.matrix)):
            c.append([])
            for j in range(len(self.matrix[i])):
                c[i].append(self.matrix[i][j] + other.matrix[i][j])
        return Matrix(c)


matrix_1 = Matrix([[1, 2], [3, 4], [5, 6]])
matrix_2 = Matrix([[1, 2], [3, 4], [5, 6]])

print(matrix_1 + matrix_2)
