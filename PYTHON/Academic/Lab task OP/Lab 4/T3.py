def sum_diagonal_elements(matrix):
    diagonal_sum = 0
    for i in range(min(len(matrix), len(matrix[0]))):
        diagonal_sum += matrix[i][i]
    return diagonal_sum

matrix = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]

result = sum_diagonal_elements(matrix)
print("Sum of Diagonal Elements:", result)
