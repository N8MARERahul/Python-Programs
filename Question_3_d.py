import re

#Using re.split method...
print("Using re.split method...")
txt = "I love python coding"
#Split at each white-space character
x = re.split("\s", txt)
#Split the string only at the first occurrence
y = re.split("\s", txt, 1)
print(x)
print(y)
#Using re.join method...
#print("Using re.join method...")




#Using re.search method...
print("\nUsing re.search method...")
#Search for the first white-space character in the string
a = re.search("\s", txt)
print("The first white-space character is located in position:", a.start())
#Make a search that returns a match
b = re.search("python", txt)
print(b)

#Using re.match method...
print("\nUsing re.match method...")
string1 = 'string'
string2 = 'string we are learning in python.'
print(re.match(string1, string2))