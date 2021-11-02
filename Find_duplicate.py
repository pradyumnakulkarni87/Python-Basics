# Write a Python program to find the repeated items of a tuple.
t1 = (10, 20, 45, 12, 10, 63, 20, 12, 55, 41, 55)
s1 = []
s = ()
for i in t1:
    if i not in s1:
        s1.append(i)
    else:
        s += (i,)

print("Duplicate items in tuple", s)
print(s1)








