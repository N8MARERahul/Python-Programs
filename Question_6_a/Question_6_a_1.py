#Basic file operations. Explore the different file modes.

#Open an existing file and read it...
file = open("Question_6_a\Question_6_a_1.txt", "r")
print(file.read())
file.close()

#Open an existing file and append content to the file...
file = open("Question_6_a\Question_6_a_1.txt", "a")
file.write("\nThe file has oppend as append mode.")
file.close()
#open and read the file after the appending:
file = open("Question_6_a\Question_6_a_1.txt", "r")
print(file.read())
file.close()

#Open an existing file and overwrite the content:
f = open("Question_6_a\Question_6_a_!.txt", "w")
f.write("\n\nI have deleted the content of the file!!!")
f.close()
#open and read the file after the writing:
file = open("Question_6_a\Question_6_a_1.txt", "r")
print(file.read())
file.close()