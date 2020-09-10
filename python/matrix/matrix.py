class Matrix:
    def __init__(self, matrix_string):
        split_matrix_string = (matrix_string.split('\n'))
        
        the_matrix = []
        self.the_matrix = the_matrix

        for i in range(0,len(split_matrix_string)):
            the_matrix.append(split_matrix_string[i].split())
            for j in range(0,len(the_matrix[i])):
                the_matrix[i][j] = int(the_matrix[i][j])

    def row(self, index):
        row = self.the_matrix[index-1]
        return row

    def column(self, index):
        columns = []
        for col in self.the_matrix:
            columns.append(col[index-1])
        return columns