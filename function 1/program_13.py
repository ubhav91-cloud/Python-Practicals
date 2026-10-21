# Function Program 13: Check Positive, Negative or Zero

def check_number(n):
    if n > 0:
        return "Positive"
    elif n < 0:
        return "Negative"
    else:
        return "Zero"

print("Number is:", check_number(-5))
