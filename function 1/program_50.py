# Function Program 50: Count Vowels in a String

def count_vowels(text):
    count = 0
    for ch in text.lower():
        if ch in "aeiou":
            count = count + 1
    return count

print("Vowel count:", count_vowels("Hello Python"))
