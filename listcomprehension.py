from functools import reduce
numlist =[]
size = int(input("Enter size of the list"))
for i in range(0, size):
    num = int(input("Enter list elements:"))
    numlist.append(num)

newlist = []
for i in numlist:
    a = 3*i
    newlist.append(a)

print("The original list is:", numlist)
print("The modified list is:", newlist)

sum = reduce(lambda a,b:a+b, numlist)
print("The sum of original list: ", sum)

newsum = reduce(lambda a,b:a+b, newlist)
print("The sum of modified list: ", newsum)