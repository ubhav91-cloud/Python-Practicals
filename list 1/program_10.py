# Program 10: Find duplicate elements

numbers = [1, 2, 3, 2, 4, 5, 1, 6]
duplicates = []
for n in numbers:
    if numbers.count(n) > 1 and n not in duplicates:
        duplicates.append(n)
print("Duplicate elements:", duplicates)
