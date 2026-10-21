# Program 41: Find prime numbers in a list

numbers = [2, 3, 4, 5, 9, 11, 15, 17]
primes = []
for n in numbers:
    if n > 1:
        is_prime = True
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(n)
print("Prime numbers:", primes)
