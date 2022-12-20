# Write a function to generate the Fibonacci numbers in 
# (a) exponential time using the naïve algorithm...
# (b) in linear time using dynamic programming (memorization) with a dictionary...

# Using Naive algorithm...
def fib(n):
    if n < 2:
        return n
    else:
        return fib(n - 1) + fib(n - 2)

# Using dynamic program...
def fibo(n):
    Dict={0:0, 1:1}
    def fibonacci(n):
        if n not in Dict:
            val=fibonacci(n-1)+fibonacci(n-2)
            Dict[n]=val
        return Dict[n]  
    return fibonacci(n)

num = int(input("Enter the value of n : "))

print("1. Using Naive Algorithm ...")
print("2. Using Dynamic Programming...")
choice = int(input("Enter your choice : "))

if choice == 1:
    print(fib(num))
elif choice == 2:
    print(fibo(num))
else :
    print("Wrong Choice...")