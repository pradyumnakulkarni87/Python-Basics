# Write a Python program to replace last value of tuples in a list. Go to the editor
# Sample list: [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
# Expected Output: [(10, 20, 100), (40, 50, 100), (70, 80, 100)]
t1 = [(10, 20, 40), (40, 50, 60), (70, 80, 90),(100,)]
for i in range(len(t1)):
    t1[i] = t1[i] + (100,)

print(t1)
