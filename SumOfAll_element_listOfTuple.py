#  Write a Python program to compute the sum of all the elements of each tuple stored inside a list of tuples
"""
l1 = [(1, 2), (2, 3), (3, 4)]
l2 = []
for i in l1:
    l2.append(sum(i))
print(l2)
------------------------------------------------------------------------------------------------------------------------

# using list comprehension
l1 = [(1, 2), (2, 3), (3, 4)]
l2 = [sum(x) for x in l1]
print(l2)

------------------------------------------------------------------------------------------------------------------------
"""
# using 
l1 = [(1, 2), (2, 3), (3, 4)]
