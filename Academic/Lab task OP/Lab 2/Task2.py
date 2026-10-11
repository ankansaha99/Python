def t_m(matrix):
    r, c = len(matrix), len(matrix[0])
    transposed = [[0] * r for _ in range(c)]
    for i in range(r):
        for j in range(c):
            transposed[j][i] = matrix[i][j]
    return transposed

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

transposed_m = t_m(matrix)

for row in transposed_m:
    print(row)
