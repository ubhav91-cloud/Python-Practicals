# Program 44: Calculate the factorial of a number

factorial = lambda n: 1 if n <= 1 else n * __import__("math").factorial(n - 1)
print(factorial(5))
