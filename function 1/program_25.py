# Function Program 25: Greatest Common Divisor

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

print("GCD:", gcd(24, 36))
