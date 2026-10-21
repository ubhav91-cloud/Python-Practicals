# Program 69: Filter numbers divisible by four

numbers = [4, 7, 8, 12, 15, 16, 20]
result = list(filter(lambda n: n % 4 == 0, numbers))
print(result)
