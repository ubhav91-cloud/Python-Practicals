# Program 7: Find the second smallest number

numbers = [12, 45, 7, 89, 34, 7]
unique = list(set(numbers))
unique.sort()
if len(unique) >= 2:
    print("Second smallest:", unique[1])
else:
    print("Second smallest number does not exist.")
