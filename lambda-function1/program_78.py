# Program 78: Sort strings by their last character

words = ["apple", "banana", "kiwi", "grape"]
result = sorted(words, key=lambda word: word[-1])
print(result)
