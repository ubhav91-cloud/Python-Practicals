# Program 68: Count positive numbers in a list

numbers = [-2, 5, 0, 8, -1, 3]
result = len(list(filter(lambda n: n > 0, numbers)))
print(result)
