numlist = []
size = int(input("Enter size of the list: "))
for i in range(0, size):
    num = int(input("Enter elements of the list: "))
    numlist.append(num)
print(numlist)

print("The maximum element of the list is: ", max(numlist))
print("The minimum element of the list is: ", min(numlist))

pos = int(input("Enter the position to be inserted: "))
newnum = int(input("Enter the element to be inserted: "))
numlist.insert(pos, newnum)
print(numlist)

element = int(input("Enter element to be deleted: "))
numlist.remove(element)
print(numlist)

number = int(input("Enter element to be searched: "))
if number not in numlist:
    print("Element not present in list")
else:
    print("Element present in list")

