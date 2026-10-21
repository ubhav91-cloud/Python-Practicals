# Program 43: Flatten a nested list by one level

nested = [[1, 2], [3, 4], [5, 6]]
flat = []
for sublist in nested:
    for n in sublist:
        flat.append(n)
print("Flattened list:", flat)
