# Function Program 20: Reverse a Number

def reverse_number(n):
    reverse = 0
    while n > 0:
        digit = n % 10
        reverse = reverse * 10 + digit
        n = n // 10
    return reverse

print("Reversed number:", reverse_number(1234))
