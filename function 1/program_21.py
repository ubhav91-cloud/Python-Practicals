# Function Program 21: Sum of Digits

def sum_digits(n):
    total = 0
    while n > 0:
        total = total + n % 10
        n = n // 10
    return total

print("Sum of digits:", sum_digits(12345))
