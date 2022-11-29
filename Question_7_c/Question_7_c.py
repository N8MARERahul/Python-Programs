# Open the file in read mode
text = open("Question_7_c\Question_7_c.txt", "r")
  
# Create an empty dictionary
occ_word = dict()
occ_letter = dict()

# Loop through each line of the file
for line in text:
    # Remove the leading spaces and newline character
    line = line.strip()
  
    # Convert the characters in line to
    # lowercase to avoid case mismatch
    line = line.lower()
  
    # Split the line into words
    words = line.split()

    # Remove the space from the text
    letters = line.replace(" ", "")
                         
  
    # Iterate over each word in line
    for word in words:
        # Check if the word is already in dictionary
        if word in occ_word:
            # Increment count of word by 1
            occ_word[word] = occ_word[word] + 1
        else:
            # Add the word to dictionary with count 1
            occ_word[word] = 1
    # Iterate over each word in line
    for letter in letters:
        # Check if the letter is already in dictionary
        if letter in occ_letter:
            # Increment count of letter by 1
            occ_letter[letter] = occ_letter[letter] + 1
        else:
            # Add the letter to dictionary with count 1
            occ_letter[letter] = 1

print("Occurence of the words : ")  
# Print the contents of dictionary
for key in list(occ_word.keys()):
    print(key, ":", occ_word[key])

print("\nOccurence of the letters :")
# Print the contents of dictionary
for key in list(occ_letter.keys()):
    print(key, ":", occ_letter[key])