# Program 15: Find common elements in two lists

first = [1, 2, 3, 4, 5]
second = [3, 4, 5, 6, 7]
common = []
for n in first:
    if n in second and n not in common:
        common.append(n)
print("Common elements:", common)
