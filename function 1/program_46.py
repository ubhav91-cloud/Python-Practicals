# Function Program 46: Multiply All Items in a List

def multiply_list(numbers):
    result = 1
    for n in numbers:
        result = result * n
    return result

nums = [2, 3, 4, 5]
print("Multiplication:", multiply_list(nums))
