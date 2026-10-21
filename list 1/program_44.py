# Program 44: Transpose a matrix represented by lists

matrix = [[1, 2, 3], [4, 5, 6]]
transposed = []
for col in range(len(matrix[0])):
    new_row = []
    for row in range(len(matrix)):
        new_row.append(matrix[row][col])
    transposed.append(new_row)
print("Transposed matrix:", transposed)
