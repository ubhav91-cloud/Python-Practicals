# Function Program 44: Count Occurrences in a List

def count_occurrences(numbers, target):
    count = 0
    for n in numbers:
        if n == target:
            count = count + 1
    return count

nums = [2, 3, 2, 4, 2, 5]
print("Occurrences:", count_occurrences(nums, 2))
