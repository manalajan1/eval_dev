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
    
def mysort(mylist: [int]) -> [int]:
    listcopy = mylist[:]

    list_length = len(list_copy)

    for i in range(list_length):
        for j in range(list_length - i - 1):
            if list_copy[j] > list_copy[j + 1]:
                list_copy[j], list_copy[j + 1] = list_copy[j + 1], list_copy[j]

    return list_copy

if __name == '__main':
    my_list = [17, 19, 8, 40, 1, 7, 22]
    sorted_list = my_sort(my_list)
    print("Liste triée :", sorted_list)

