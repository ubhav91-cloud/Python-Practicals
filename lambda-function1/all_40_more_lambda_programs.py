"""40 more beginner-friendly Python lambda function examples (Programs 41-80)."""

# Program 41: Find the first number in a list
numbers = [11, 22, 33, 44]
first = lambda items: items[0]
print(first(numbers))

# Program 42: Find the last number in a list
numbers = [11, 22, 33, 44]
last = lambda items: items[-1]
print(last(numbers))

# Program 43: Find the sum of three numbers
total = lambda a, b, c: a + b + c
print(total(4, 5, 6))

# Program 44: Calculate the factorial of a number
factorial = lambda n: 1 if n <= 1 else n * __import__("math").factorial(n - 1)
print(factorial(5))

# Program 45: Check whether a number is odd
is_odd = lambda n: n % 2 != 0
print(is_odd(9))

# Program 46: Check whether a number is divisible by three
check = lambda n: "Yes" if n % 3 == 0 else "No"
print(check(18))

# Program 47: Find the smaller of three numbers
smallest = lambda a, b, c: min(a, b, c)
print(smallest(8, 3, 12))

# Program 48: Return the square root of a number
square_root = lambda n: n ** 0.5
print(square_root(81))

# Program 49: Calculate the hypotenuse of a right triangle
hypotenuse = lambda a, b: (a ** 2 + b ** 2) ** 0.5
print(hypotenuse(3, 4))

# Program 50: Calculate compound amount
amount = lambda p, r, t: p * (1 + r / 100) ** t
print(round(amount(1000, 5, 2), 2))

# Program 51: Convert meters to centimeters
centimeters = lambda m: m * 100
print(centimeters(4))

# Program 52: Convert hours to minutes
minutes = lambda hours: hours * 60
print(minutes(3))

# Program 53: Convert minutes to seconds
seconds = lambda minutes: minutes * 60
print(seconds(5))

# Program 54: Calculate the volume of a cube
volume = lambda side: side ** 3
print(volume(4))

# Program 55: Calculate the perimeter of a rectangle
perimeter = lambda length, width: 2 * (length + width)
print(perimeter(8, 3))

# Program 56: Calculate the area of a triangle
area = lambda base, height: 0.5 * base * height
print(area(10, 6))

# Program 57: Get the final two characters of a string
last_two = lambda text: text[-2:]
print(last_two("Python"))

# Program 58: Count vowels in a string
count_vowels = lambda text: sum(1 for ch in text.lower() if ch in "aeiou")
print(count_vowels("education"))

# Program 59: Remove spaces from a string
remove_spaces = lambda text: text.replace(" ", "")
print(remove_spaces("hello python"))

# Program 60: Capitalize the first letter of a string
capitalize = lambda text: text.capitalize()
print(capitalize("python programming"))

# Program 61: Check whether a string starts with a given letter
starts_with = lambda text, letter: text.lower().startswith(letter.lower())
print(starts_with("Python", "p"))

# Program 62: Check whether a string contains a digit
has_digit = lambda text: any(ch.isdigit() for ch in text)
print(has_digit("Room7"))

# Program 63: Get the middle character of an odd-length string
middle = lambda text: text[len(text) // 2]
print(middle("hello"))

# Program 64: Repeat a string three times
repeat = lambda text: text * 3
print(repeat("Hi "))

# Program 65: Find the sum of a list
numbers = [2, 4, 6, 8]
total = lambda items: sum(items)
print(total(numbers))

# Program 66: Find the maximum number in a list
numbers = [12, 5, 27, 9]
maximum = lambda items: max(items)
print(maximum(numbers))

# Program 67: Find the minimum number in a list
numbers = [12, 5, 27, 9]
minimum = lambda items: min(items)
print(minimum(numbers))

# Program 68: Count positive numbers in a list
numbers = [-2, 5, 0, 8, -1, 3]
result = len(list(filter(lambda n: n > 0, numbers)))
print(result)

# Program 69: Filter numbers divisible by four
numbers = [4, 7, 8, 12, 15, 16, 20]
result = list(filter(lambda n: n % 4 == 0, numbers))
print(result)

# Program 70: Filter numbers less than zero
numbers = [-5, 3, -2, 8, 0, -1]
result = list(filter(lambda n: n < 0, numbers))
print(result)

# Program 71: Filter words that contain letter e
words = ["red", "blue", "cat", "green"]
result = list(filter(lambda word: "e" in word, words))
print(result)

# Program 72: Convert each word to uppercase
words = ["apple", "banana", "cherry"]
result = list(map(lambda word: word.upper(), words))
print(result)

# Program 73: Get the first letter of each word
words = ["apple", "banana", "cherry"]
result = list(map(lambda word: word[0], words))
print(result)

# Program 74: Add corresponding items from two lists
a = [1, 2, 3]
b = [10, 20, 30]
result = list(map(lambda x, y: x + y, a, b))
print(result)

# Program 75: Find the remainder of each number divided by two
numbers = [10, 11, 12, 13, 14]
result = list(map(lambda n: n % 2, numbers))
print(result)

# Program 76: Sort words alphabetically
words = ["mango", "apple", "banana", "grape"]
result = sorted(words, key=lambda word: word.lower())
print(result)

# Program 77: Sort people by age
people = [("Asha", 22), ("Ravi", 19), ("Neha", 25)]
result = sorted(people, key=lambda person: person[1])
print(result)

# Program 78: Sort strings by their last character
words = ["apple", "banana", "kiwi", "grape"]
result = sorted(words, key=lambda word: word[-1])
print(result)

# Program 79: Calculate total price after tax
total_price = lambda price, tax: price + (price * tax / 100)
print(total_price(800, 5))

# Program 80: Get the absolute difference between two numbers
difference = lambda a, b: abs(a - b)
print(difference(17, 9))

# Program 81: Check whether a year is a leap year
is_leap = lambda year: "Leap year" if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0) else "Not a leap year"
print(is_leap(2024))
