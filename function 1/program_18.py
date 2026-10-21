# Function Program 18: Print Prime Numbers in a Range

def primes(start, end):
    for n in range(start, end + 1):
        if n > 1:
            prime = True
            for i in range(2, n):
                if n % i == 0:
                    prime = False
                    break
            if prime:
                print(n, end=" ")

primes(1, 30)
