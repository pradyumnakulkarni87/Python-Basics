# Write a Python function that takes two lists and returns True if they have at least one common member
l1 = [10, 20, 30, 40, 50, 60]
l2 = [10, 25, 30, 55]
l3 =[]
for i in l1:
    if i in l2:
        l3.append(i)
print(l3)
if len(l3)!=0:
    print("true")
