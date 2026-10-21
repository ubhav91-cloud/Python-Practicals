# Function Program 35: Find the Sum of List Items

def list_sum(numbers):
    total = 0
    for n in numbers:
        total = total + n
    return total

nums = [10, 20, 30, 40]
print("Sum:", list_sum(nums))
