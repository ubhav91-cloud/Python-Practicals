# Program 39: Create a list of odd numbers from a range

numbers = list(range(1, 21))
odd = [n for n in numbers if n % 2 != 0]
print("Odd numbers:", odd)
