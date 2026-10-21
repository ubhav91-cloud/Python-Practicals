# Function Program 42: Remove Duplicates from a List

def remove_duplicates(numbers):
    result = []
    for n in numbers:
        if n not in result:
            result.append(n)
    return result

nums = [1, 2, 2, 3, 4, 4, 5]
print("Without duplicates:", remove_duplicates(nums))
