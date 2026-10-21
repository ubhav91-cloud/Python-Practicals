# Function Program 24: Check Armstrong Number

def is_armstrong(n):
    original = n
    total = 0
    digits = len(str(n))
    while n > 0:
        digit = n % 10
        total = total + digit ** digits
        n = n // 10
    return total == original

print("Is Armstrong:", is_armstrong(153))
