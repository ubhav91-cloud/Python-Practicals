# Program 3: Count even numbers in a list

numbers = [1, 2, 3, 4, 5, 6, 8]
count = 0
for n in numbers:
    if n % 2 == 0:
        count += 1
print("Even numbers count:", count)
