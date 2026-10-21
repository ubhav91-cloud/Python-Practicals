# List-Tuple Program 32: Flatten a simple nested list
matrix = [[1, 2], [3, 4], [5, 6]]
flat = [item for row in matrix for item in row]
print(flat)
