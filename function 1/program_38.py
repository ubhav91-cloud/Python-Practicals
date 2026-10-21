# Function Program 38: Count Even Numbers in a List

def count_even(numbers):
    count = 0
    for n in numbers:
        if n % 2 == 0:
            count = count + 1
    return count

nums = [1, 2, 3, 4, 5, 6]
print("Even count:", count_even(nums))
