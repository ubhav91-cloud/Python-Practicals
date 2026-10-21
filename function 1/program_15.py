# Function Program 15: Sum of Natural Numbers

def sum_natural(n):
    total = 0
    for i in range(1, n + 1):
        total = total + i
    return total

print("Sum:", sum_natural(10))
