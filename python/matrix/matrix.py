class Matrix:
    def __init__(self, matrix_string):
        self.matrix = matrix_string.split('\n')

        for i in range(0,len(self.matrix)):
            self.matrix[i] = self.matrix[i].split()

    def row(self, index):
        return [int(row) for row in self.matrix[index-1]]

    def column(self, index):
        return [int(col[index-1]) for col in self.matrix]
