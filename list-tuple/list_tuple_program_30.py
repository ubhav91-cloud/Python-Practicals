# List-Tuple Program 30: Remove duplicate list items
numbers = [1, 2, 2, 3, 4, 4, 5]
unique = list(dict.fromkeys(numbers))
print(unique)
