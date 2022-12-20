# Invert a dictionary such the previous keys become values and values keys.

# initialising dictionary
init_dict = {}

# Taking input from user
values = int(input("Enter the number of values wanted to insert : "))

for i in range(values):
    key = input("Enter the key : ")
    value = input("Enter the value : ")

    init_dict[key] = value
    
# print initial dictionary
print("initial dictionary : ", str(init_dict))
  
# inverse mapping using map and reversed
inverted_dict = dict(map(reversed, init_dict.items()))
  
# print final dictionary
print("inverse mapped dictionary : ", str(inverted_dict))