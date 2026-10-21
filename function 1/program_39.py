# Function Program 39: Count Odd Numbers in a List

def count_odd(numbers):
    count = 0
    for n in numbers:
        if n % 2 != 0:
            count = count + 1
    return count

nums = [1, 2, 3, 4, 5, 6]
print("Odd count:", count_odd(nums))
