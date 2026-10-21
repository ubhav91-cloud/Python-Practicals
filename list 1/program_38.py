# Program 38: Find the frequency of each element

numbers = [1, 2, 2, 3, 1, 4, 2]
frequency = {}
for n in numbers:
    frequency[n] = frequency.get(n, 0) + 1
print("Frequency:", frequency)
