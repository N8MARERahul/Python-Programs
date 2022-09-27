#Simulate a stack using list...
print("\nSimulate a stack using list...")
list = []
#Push some letters into list.
list.append('p')
list.append('y')
list.append('t')
list.append('h')
list.append('o')
list.append('n')
#See the list-
print(list)
#Now if we pop a letter, we should get 'n'
list_item = list.pop()
print(list_item)
#Now if we again pop a letter, we will get 'o'
list_item = list.pop()
print(list_item)
#'p', 'y', 't', 'h' remain.
print(list)

#Simulate a queue using list...
print("\nSimulate a queue using list...")
lang = []
#Enqueue some programing language name..
lang.append('C')
lang.append('C++')
lang.append('Python')
lang.append('Java')
#See the list-
print(lang)
#Now if we dequeue lang, we should get 'C'
lang_item = lang.pop(0)
print(lang_item)
#Now if we again dequeue lang, we should get 'C++'
lang_item = lang.pop(0)
print(lang_item)
#'Python' and 'Java' remain.
print(lang)