# gaussian addition 
number_list = [1,2,3,4,5,6,7,8,9]
left_number = 0 
result = 0
i=0
if(len(number_list) % 2 != 0):
    middle = ((len(number_list) ) // 2) 
    left_number = number_list[middle]

while(i <(len(number_list)//2)):
    sum_row = number_list[i] + number_list[::-1][i]
    result += sum_row
    print("{} + {} = {}".format(number_list[i] , number_list[::-1][i] , sum_row))
    i+=1

if(left_number != 0):
    result += left_number
    print("{} + 0 = {}".format(left_number, left_number))

print("The sum is: {}".format(result))