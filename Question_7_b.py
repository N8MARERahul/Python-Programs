#Use the set union and intersection operations to implement the Jaccard and Cosine similarity of two sets. 

#Jaccard similarity-->
def jaccard_similarity(set_1, set_2):
    #Find intersection of two sets
    intersection = set_1.intersection(set_2)
    #Find union of two sets
    union = set_1.union(set_2)
    #Take the ratio of sizes
    similarity = len(intersection)/len(union)
    print("Jaccard similarity between the sets is --> ", similarity)

#Cosine similarities -->
def cosine_similarity(set_1, set_2):
    from numpy import dot
    from numpy.linalg import norm
    cosine_similarity = dot(set_1, set_2) / (norm(set_1) * norm(set_2))
    print("Cosine similarity between the sets is --> ", cosine_similarity)


user_input_1 = input("Enter space-separated integers for 1st set : ")

set_1 = set(int(item) for item in user_input_1.split())

user_input_2 = input("Enter space-separated integers for 2nd set : ")

set_2 = set(int(item) for item in user_input_2.split())

print("First set is --> ", set_1)
print("Second set is -->", set_2)

print("Press 1 for Jaccard similarity.")
print("Press 2 for Cosine similarity.")
choice = int(input("Enter your choice : "))

if (choice == 1):
    jaccard_similarity(set_1, set_2)
elif (choice == 2):
    cosine_similarity(set_1, set_2)
else:
    print("Wrong choice!!")