# Program 16: Find elements present only in the first list

first = [1, 2, 3, 4, 5]
second = [3, 4, 6]
result = []
for n in first:
    if n not in second:
        result.append(n)
print("Only in first list:", result)
