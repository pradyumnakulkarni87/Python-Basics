# program to find second largest number in a list
l1 = [10, 20, 40, 54, 12, 4, 21, 9, 1, -1]
l1.sort()
# print(l1)
print(f"second largest number is: {l1[-2]}")

l1.sort(reverse=True)

print(f"second largest number is: {l1[1]}")

l1.sort()
print(l1.pop(-2))


