# Program 42: Separate numbers into two lists by a threshold

numbers = [12, 5, 27, 9, 18, 3]
threshold = 10
small = [n for n in numbers if n < threshold]
large = [n for n in numbers if n >= threshold]
print("Below 10:", small)
print("10 or above:", large)
