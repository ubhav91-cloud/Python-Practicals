# Program 37: Find all numbers greater than the average

numbers = [10, 20, 30, 40, 50]
average = sum(numbers) / len(numbers)
result = [n for n in numbers if n > average]
print("Numbers above average:", result)
