num1 = int(input("Enter the First number:"))

num2 = int(input("Enter the Second number:"))

print("Sum of the 2 numbers is :", (num1 + num2))

print("Product of the 2 numbers is :", (num1 * num2))

print("Difference of the 2 numbers is :", (num1 - num2))

for i in range(1,num1 and num2):
    if(num1 % i == 0 and num2 % i == 0):
        gcd = i

print("GCD of two numbers is :", gcd)