# max() and min() of key function..

# in a list->
list = ['red', 'RED', 'Yellow', 'blue', 'pink']
# Without key function,it will compare based on lexicographic order
print("List -->", list)
print("Without using key function-->")
print("Max = ", max(list))  # Output:red
print("Min = ", min(list))  # Output:RED
print("Using key function-->")
print("Max = ", max(list, key=lambda x: x.lower()))  # Output:Yellow
print("Min = ", min(list, key=lambda x: x.lower()))  # Output:Blue
print()
# in a 2D list or matrix
list_1 = [(1, 2, 3), (3, 1, 1), (8, 5, 3), (3, 4, 2)]
print("2D List -->", list_1)
# Finding the largest/smallest item based on second element in the tuple.
# lambda function returns second element in the tuple
print("Using key function-->")
print("Min = ", min(list_1, key=lambda x: x[1]))  # Output:(3, 1, 1)
print("Max = ", max(list_1, key=lambda x: x[1]))  # Output:(8, 5, 3)
print("Without using key function-->")
# Without key function
# by default it will take the first element in the tuple.
print("Min = ", min(list_1))  # Output:(1, 2, 3)
print("Max = ", max(list_1))  # Output:(8, 5, 3)
print()

#sum() using lambda 
sum = lambda x, y: x+y
print("sum() Using lambda: ", sum(4, 6))
print()

#sort using lamda
#sorting data by index value 0
list_2 = [("B", 5, "20"), ("A", 1, "5"), ("C", 6, "10")]
print("List is :", list_2)
list_2.sort(key=lambda x: x[0])
print("sort() using lambda by index value: ", list_2)