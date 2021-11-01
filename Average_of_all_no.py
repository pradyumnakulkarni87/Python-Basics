# Write a Python program to calculate the average value of the numbers in a given tuple of tuples.
# Original Tuple:
# ((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4))
# Average value of the numbers of the said tuple of tuples:
# [30.5, 34.25, 27.0, 23.25]

t1 = ((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4))
average = []

# for i in zip(*t1):
#     s1 = sum(i) / len(i)
#     average.append(s1)
#
# print(f"Average value of the numbers of the said tuple of tuples:\n{average}")
for j in range(0 ,len(t1)):
    average.append((t1[0][j]+t1[1][j]+t1[2][j]+t1[3][j])/4)
print(average)