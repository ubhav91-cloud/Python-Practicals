# Program 17: Find the union of two lists

first = [1, 2, 3, 4]
second = [3, 4, 5, 6]
union = []
for n in first + second:
    if n not in union:
        union.append(n)
print("Union:", union)
