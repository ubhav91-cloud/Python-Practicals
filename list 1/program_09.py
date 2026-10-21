# Program 9: Remove duplicate elements

numbers = [1, 2, 2, 3, 4, 3, 5]
unique = []
for n in numbers:
    if n not in unique:
        unique.append(n)
print("List without duplicates:", unique)
