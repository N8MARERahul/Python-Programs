#Use sets to de-duplicate a list of numbers, and a string such that they contain only the unique elements...

list = []

length = int(input("Enter the number of element want to input :"))
print("Enter the elements:")
for i in range(length) :
    list.append(input())
print("The list is : ")
print(list)

duplicate_set = set()

for i in range(length):
    duplicate_set.add(list[i])
print("After removing the duplicate items from list using set :")
print(duplicate_set)