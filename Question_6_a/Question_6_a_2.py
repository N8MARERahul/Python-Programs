#Create a new file...

#Create a file, if file exist returs error...
f = open("Question_6_a\Question_6_a_2.txt", "x")

#Create a file, if file does not exists...
f = open("Question_6_a\Question_6_a_3.txt", "w")

#Delete a file...
import os
if os.path.exists("Question_6_a\Question_6_a_2.txt"):
    os.remove("Question_6_a\Question_6_a_2.txt")
else:
    print("The file does not exist")