# Ways to find length of list
# built in function len()
l_1 = [10, 20, 30, 40, 50, 60, 71, 12]
print(len(l_1))

# using for loop
s = 0
for i in l_1:
    s += 1
print(s)


# using built in modules

from operator import length_hint as len

l2 = len(l_1)
# print(len(l_1))
print(l2)

