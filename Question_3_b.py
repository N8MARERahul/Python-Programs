list = ['I' ,'You' ,'Love' , 'Are' ,'Python' , 'Cute']

even = " ".join(list[0:1] + list[2:3] +list[4:5])
odd = " ".join(list[1:2] + list[3:4] +list[5:6])
print("The list is : {}".format(list))
print("Even Position words: {}".format(even))
print("\nOdd Position words: {}".format(odd))