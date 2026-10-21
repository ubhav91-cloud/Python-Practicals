"""49 beginner-friendly Python list programs."""

# Program 1: Print all elements of a list
numbers = [12, 24, 36, 48, 60]
for n in numbers:
    print(n)

# Program 2: Print list elements with their indexes
numbers = [10, 20, 30, 40]
for i in range(len(numbers)):
    print("Index", i, ":", numbers[i])

# Program 3: Count even numbers in a list
numbers = [1, 2, 3, 4, 5, 6, 8]
count = 0
for n in numbers:
    if n % 2 == 0:
        count += 1
print("Even numbers count:", count)

# Program 4: Count odd numbers in a list
numbers = [1, 2, 3, 4, 5, 6, 8]
count = 0
for n in numbers:
    if n % 2 != 0:
        count += 1
print("Odd numbers count:", count)

# Program 5: Separate even and odd numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
even = []
odd = []
for n in numbers:
    if n % 2 == 0:
        even.append(n)
    else:
        odd.append(n)
print("Even numbers:", even)
print("Odd numbers:", odd)

# Program 6: Find the second largest number
numbers = [12, 45, 7, 89, 34, 89]
unique = list(set(numbers))
unique.sort()
if len(unique) >= 2:
    print("Second largest:", unique[-2])
else:
    print("Second largest number does not exist.")

# Program 7: Find the second smallest number
numbers = [12, 45, 7, 89, 34, 7]
unique = list(set(numbers))
unique.sort()
if len(unique) >= 2:
    print("Second smallest:", unique[1])
else:
    print("Second smallest number does not exist.")

# Program 8: Count positive, negative, and zero values
numbers = [-3, 0, 7, -1, 5, 0, 9]
positive = negative = zero = 0
for n in numbers:
    if n > 0:
        positive += 1
    elif n < 0:
        negative += 1
    else:
        zero += 1
print("Positive:", positive)
print("Negative:", negative)
print("Zeros:", zero)

# Program 9: Remove duplicate elements
numbers = [1, 2, 2, 3, 4, 3, 5]
unique = []
for n in numbers:
    if n not in unique:
        unique.append(n)
print("List without duplicates:", unique)

# Program 10: Find duplicate elements
numbers = [1, 2, 3, 2, 4, 5, 1, 6]
duplicates = []
for n in numbers:
    if numbers.count(n) > 1 and n not in duplicates:
        duplicates.append(n)
print("Duplicate elements:", duplicates)

# Program 11: Check whether a list is sorted
numbers = [1, 3, 5, 7, 9]
if numbers == sorted(numbers):
    print("List is sorted in ascending order.")
else:
    print("List is not sorted in ascending order.")

# Program 12: Sort a list in ascending order
numbers = [45, 12, 78, 34, 9]
numbers.sort()
print("Ascending order:", numbers)

# Program 13: Sort a list in descending order
numbers = [45, 12, 78, 34, 9]
numbers.sort(reverse=True)
print("Descending order:", numbers)

# Program 14: Merge two lists
first = [1, 2, 3]
second = [4, 5, 6]
merged = first + second
print("Merged list:", merged)

# Program 15: Find common elements in two lists
first = [1, 2, 3, 4, 5]
second = [3, 4, 5, 6, 7]
common = []
for n in first:
    if n in second and n not in common:
        common.append(n)
print("Common elements:", common)

# Program 16: Find elements present only in the first list
first = [1, 2, 3, 4, 5]
second = [3, 4, 6]
result = []
for n in first:
    if n not in second:
        result.append(n)
print("Only in first list:", result)

# Program 17: Find the union of two lists
first = [1, 2, 3, 4]
second = [3, 4, 5, 6]
union = []
for n in first + second:
    if n not in union:
        union.append(n)
print("Union:", union)

# Program 18: Find the difference between two lists
first = [1, 2, 3, 4, 5]
second = [2, 4]
difference = [n for n in first if n not in second]
print("Difference:", difference)

# Program 19: Copy a list
numbers = [10, 20, 30, 40]
copy_list = numbers.copy()
print("Original list:", numbers)
print("Copied list:", copy_list)

# Program 20: Clear all elements from a list
numbers = [10, 20, 30, 40]
numbers.clear()
print("List after clearing:", numbers)

# Program 21: Insert an element at a given position
numbers = [10, 20, 40, 50]
numbers.insert(2, 30)
print("Updated list:", numbers)

# Program 22: Append an element to a list
numbers = [10, 20, 30]
numbers.append(40)
print("Updated list:", numbers)

# Program 23: Extend a list with another list
numbers = [1, 2, 3]
more_numbers = [4, 5, 6]
numbers.extend(more_numbers)
print("Extended list:", numbers)

# Program 24: Remove an element by value
numbers = [10, 20, 30, 40, 50]
numbers.remove(30)
print("Updated list:", numbers)

# Program 25: Remove an element by index
numbers = [10, 20, 30, 40, 50]
removed = numbers.pop(2)
print("Removed element:", removed)
print("Updated list:", numbers)

# Program 26: Find the index of an element
numbers = [10, 20, 30, 40, 50]
value = 30
if value in numbers:
    print("Index:", numbers.index(value))
else:
    print("Element not found.")

# Program 27: Count occurrences of an element
numbers = [1, 2, 2, 3, 2, 4, 2]
print("Occurrences of 2:", numbers.count(2))

# Program 28: Swap the first and last elements
numbers = [10, 20, 30, 40, 50]
numbers[0], numbers[-1] = numbers[-1], numbers[0]
print("After swapping:", numbers)

# Program 29: Rotate a list one position to the left
numbers = [1, 2, 3, 4, 5]
rotated = numbers[1:] + numbers[:1]
print("Left rotation:", rotated)

# Program 30: Rotate a list one position to the right
numbers = [1, 2, 3, 4, 5]
rotated = numbers[-1:] + numbers[:-1]
print("Right rotation:", rotated)

# Program 31: Split a list into two halves
numbers = [1, 2, 3, 4, 5, 6]
mid = len(numbers) // 2
print("First half:", numbers[:mid])
print("Second half:", numbers[mid:])

# Program 32: Create a list of squares
numbers = [1, 2, 3, 4, 5]
squares = []
for n in numbers:
    squares.append(n ** 2)
print("Squares:", squares)

# Program 33: Create a list of cubes
numbers = [1, 2, 3, 4, 5]
cubes = []
for n in numbers:
    cubes.append(n ** 3)
print("Cubes:", cubes)

# Program 34: Multiply every list element by five
numbers = [1, 2, 3, 4, 5]
result = []
for n in numbers:
    result.append(n * 5)
print("Updated list:", result)

# Program 35: Find the average of list elements
numbers = [10, 20, 30, 40, 50]
if len(numbers) > 0:
    average = sum(numbers) / len(numbers)
    print("Average:", average)
else:
    print("List is empty.")

# Program 36: Find the product of all list elements
numbers = [2, 3, 4, 5]
product = 1
for n in numbers:
    product *= n
print("Product:", product)

# Program 37: Find all numbers greater than the average
numbers = [10, 20, 30, 40, 50]
average = sum(numbers) / len(numbers)
result = [n for n in numbers if n > average]
print("Numbers above average:", result)

# Program 38: Find the frequency of each element
numbers = [1, 2, 2, 3, 1, 4, 2]
frequency = {}
for n in numbers:
    frequency[n] = frequency.get(n, 0) + 1
print("Frequency:", frequency)

# Program 39: Create a list of odd numbers from a range
numbers = list(range(1, 21))
odd = [n for n in numbers if n % 2 != 0]
print("Odd numbers:", odd)

# Program 40: Create a list of multiples of seven
multiples = [n for n in range(1, 101) if n % 7 == 0]
print("Multiples of 7:", multiples)

# Program 41: Find prime numbers in a list
numbers = [2, 3, 4, 5, 9, 11, 15, 17]
primes = []
for n in numbers:
    if n > 1:
        is_prime = True
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(n)
print("Prime numbers:", primes)

# Program 42: Separate numbers into two lists by a threshold
numbers = [12, 5, 27, 9, 18, 3]
threshold = 10
small = [n for n in numbers if n < threshold]
large = [n for n in numbers if n >= threshold]
print("Below 10:", small)
print("10 or above:", large)

# Program 43: Flatten a nested list by one level
nested = [[1, 2], [3, 4], [5, 6]]
flat = []
for sublist in nested:
    for n in sublist:
        flat.append(n)
print("Flattened list:", flat)

# Program 44: Transpose a matrix represented by lists
matrix = [[1, 2, 3], [4, 5, 6]]
transposed = []
for col in range(len(matrix[0])):
    new_row = []
    for row in range(len(matrix)):
        new_row.append(matrix[row][col])
    transposed.append(new_row)
print("Transposed matrix:", transposed)

# Program 45: Add two lists element by element
first = [1, 2, 3, 4]
second = [10, 20, 30, 40]
result = []
for i in range(len(first)):
    result.append(first[i] + second[i])
print("Element-wise sum:", result)

# Program 46: Find pairs that add up to a target
numbers = [2, 4, 3, 5, 7, 8]
target = 10
pairs = []
for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] + numbers[j] == target:
            pairs.append((numbers[i], numbers[j]))
print("Pairs:", pairs)

# Program 47: Check whether two lists are equal
first = [1, 2, 3, 4]
second = [1, 2, 3, 4]
if first == second:
    print("Lists are equal.")
else:
    print("Lists are not equal.")

# Program 48: Find the longest string in a list
words = ["apple", "watermelon", "kiwi", "banana"]
longest = words[0]
for word in words:
    if len(word) > len(longest):
        longest = word
print("Longest word:", longest)

# Program 49: Find the shortest string in a list
words = ["apple", "watermelon", "kiwi", "banana"]
shortest = words[0]
for word in words:
    if len(word) < len(shortest):
        shortest = word
print("Shortest word:", shortest)
