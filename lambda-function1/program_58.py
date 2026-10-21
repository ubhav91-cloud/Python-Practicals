# Program 58: Count vowels in a string

count_vowels = lambda text: sum(1 for ch in text.lower() if ch in "aeiou")
print(count_vowels("education"))
