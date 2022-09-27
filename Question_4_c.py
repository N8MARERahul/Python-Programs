#calculate factorial of a number...
#Testing For loop...
num = int(input("Enter the Number: "))
print("Testing For Loop->>")
fact_for = 1
for i in range(1, num + 1):
    fact_for *= i
print("{}! = {}".format(num, fact_for))

#Testing while loop...
print("\ntesting while Loop->>")
fact_while, i = 1, 1
while(i <= num):
    fact_while *= i
    i += 1
print("{}! = {}".format(num, fact_while))