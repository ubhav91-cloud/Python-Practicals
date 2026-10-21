# Function Program 53: Count a Character in a String

def count_character(text, character):
    count = 0
    for ch in text:
        if ch == character:
            count = count + 1
    return count

print("Character count:", count_character("banana", "a"))
