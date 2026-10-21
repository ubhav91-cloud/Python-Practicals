# Program 6: Find the second largest number

numbers = [12, 45, 7, 89, 34, 89]
unique = list(set(numbers))
unique.sort()
if len(unique) >= 2:
    print("Second largest:", unique[-2])
else:
    print("Second largest number does not exist.")
