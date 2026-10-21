# Function Program 36: Find the Largest Item in a List

def largest_item(numbers):
    largest = numbers[0]
    for n in numbers:
        if n > largest:
            largest = n
    return largest

nums = [12, 45, 7, 32, 89]
print("Largest item:", largest_item(nums))
