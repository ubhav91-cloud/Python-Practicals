# Program 77: Sort people by age

people = [("Asha", 22), ("Ravi", 19), ("Neha", 25)]
result = sorted(people, key=lambda person: person[1])
print(result)
