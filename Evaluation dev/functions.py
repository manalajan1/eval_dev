def several_zeros():
    return [0] * 10

def several_zeros_custom(nb_zeros=10):
    return [0] * nb_zeros

def matrix(rows, cols):
    return [[0] * cols for _ in range(rows)]

class Matrix:
    def __init__(self, rows, cols):
        self.matrix = [[0] * cols for _ in range(rows)]

    def get_value(self, row, col):
        return self.matrix[row][col]

    def __eq__(self, other):
        if isinstance(other, Matrix):
            return self.matrix == other.matrix
        return False

if __name__ == '__main__':
  
    print(several_zeros())  
    print(several_zeros_custom(5))  
    print(matrix(4, 6))  

    m1 = Matrix(3, 4)  
    m2 = Matrix(3, 4)  
    print(m1 == m2)  
