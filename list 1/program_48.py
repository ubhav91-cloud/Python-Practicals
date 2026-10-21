# Program 48: Find the longest string in a list

words = ["apple", "watermelon", "kiwi", "banana"]
longest = words[0]
for word in words:
    if len(word) > len(longest):
        longest = word
print("Longest word:", longest)
