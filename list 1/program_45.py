# Program 45: Add two lists element by element

first = [1, 2, 3, 4]
second = [10, 20, 30, 40]
result = []
for i in range(len(first)):
    result.append(first[i] + second[i])
print("Element-wise sum:", result)
