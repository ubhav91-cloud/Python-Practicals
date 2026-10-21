# Program 49: Find the shortest string in a list

words = ["apple", "watermelon", "kiwi", "banana"]
shortest = words[0]
for word in words:
    if len(word) < len(shortest):
        shortest = word
print("Shortest word:", shortest)
