# Function Program 23: Check Palindrome Number

def is_palindrome(n):
    original = n
    reverse = 0
    while n > 0:
        reverse = reverse * 10 + n % 10
        n = n // 10
    return original == reverse

print("Is palindrome:", is_palindrome(1221))
