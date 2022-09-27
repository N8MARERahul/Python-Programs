#Use list comprehension to find all the odd numbers and numbers divisible by
#3 from a list of numbers.

number_list = [1, 2, 3, 4, 5, 6 ,7]
odd_number = []
divisible_by3 = []
#finding all odd number
for i in range(len(number_list)):
    if(number_list[i] % 2 != 0):
        odd_number.append(number_list[i])
    if(number_list[i] % 3 == 0):
        divisible_by3.append(number_list[i])
print("The List is : {}".format(number_list))
print("Odd numbers are: {}".format(odd_number))
print("Dvisible by 3 numbers are: {}".format(divisible_by3))