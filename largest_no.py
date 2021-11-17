# Write a Python program to get the largest number from a list
# using import modules and built in function
"""
from list.sum_all import d
print(max(d))
------------------------------------------------------------------------------------------------------------------------

# using lambda function
from functools import reduce as rd

d = [10, 20, 45, 41, 21, 32, 12]
s = rd(lambda x, y: max(x, y), d)
print(s)
------------------------------------------------------------------------------------------------------------------------

# using built in method
d = [10, 20, 45, 41, 21, 32, 12]
d.sort(reverse=True)  # d.sort()

print(d[0])  # print(d[-1])
------------------------------------------------------------------------------------------------------------------------

# i want to user input and find the maximum number in list
s = []
num = int(input("Enter how many element you want to list: "))
for i in range(1,num+1):
    d = int(input(f"Enter a {i}: "))
    s.append(d)
print(max(s))
------------------------------------------------------------------------------------------------------------------------

# using function
def maximum(d):
    max1 = d[0]
    for i in d:
        if i > max1:
            max1 = i
    return print(max1)


d1 = [10, 20, 45, 41, 21, 32, 12]
maximum(d1)
------------------------------------------------------------------------------------------------------------------------
"""
