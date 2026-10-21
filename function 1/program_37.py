# Function Program 37: Find the Smallest Item in a List

def smallest_item(numbers):
    smallest = numbers[0]
    for n in numbers:
        if n < smallest:
            smallest = n
    return smallest

nums = [12, 45, 7, 32, 89]
print("Smallest item:", smallest_item(nums))
