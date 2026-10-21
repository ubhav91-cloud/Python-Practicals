# Program 50: Calculate compound amount

amount = lambda p, r, t: p * (1 + r / 100) ** t
print(round(amount(1000, 5, 2), 2))
