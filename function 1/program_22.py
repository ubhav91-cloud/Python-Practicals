# Function Program 22: Count Digits

def count_digits(n):
    if n == 0:
        return 1
    count = 0
    while n > 0:
        count = count + 1
        n = n // 10
    return count

print("Number of digits:", count_digits(58321))
