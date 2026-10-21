# Function Program 43: Search for an Item in a List

def search_item(numbers, target):
    for n in numbers:
        if n == target:
            return True
    return False

nums = [10, 20, 30, 40]
print("Item found:", search_item(nums, 30))
