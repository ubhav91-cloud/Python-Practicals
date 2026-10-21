# Function Program 26: Least Common Multiple

def lcm(a, b):
    x, y = a, b
    while y != 0:
        x, y = y, x % y
    return (a * b) // x

print("LCM:", lcm(12, 18))
