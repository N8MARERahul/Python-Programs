#Generate Prime Numbers in a Given range...
lower_range = int(input("Enter the Lower range: "))
upper_range = int(input("Enter the Upper range: "))
print("Prime Numbers between {} and {} -->".format(lower_range, upper_range))
for i in range(lower_range, upper_range):
    flag = 0
    for j in range(2, (i // 2 + 1)):
        if(i % j == 0):
            flag = 1
    if(flag == 0):
        print(i)