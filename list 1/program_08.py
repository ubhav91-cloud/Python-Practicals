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
