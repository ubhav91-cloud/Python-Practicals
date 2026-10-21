# Program 61: Check whether a string starts with a given letter

starts_with = lambda text, letter: text.lower().startswith(letter.lower())
print(starts_with("Python", "p"))
