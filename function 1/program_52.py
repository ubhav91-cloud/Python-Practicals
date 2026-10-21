# Function Program 52: Check String Palindrome

def is_string_palindrome(text):
    text = text.lower().replace(" ", "")
    return text == text[::-1]

print("Is palindrome:", is_string_palindrome("nurses run"))
