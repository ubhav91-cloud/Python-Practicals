# Program 62: Check whether a string contains a digit

has_digit = lambda text: any(ch.isdigit() for ch in text)
print(has_digit("Room7"))
