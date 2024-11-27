my_list = [1, 2, 3, [4, 5, 6]]
another_list = list(my_list)

"""
Given the above code, answer the following questions and explain your answers:

Are the lists assigned to my_list and another_list equal? YES
Are the lists assigned to my_list and another_list the same object?
Are the nested lists at index 3 of my_list and another_list equal?
Are the nested lists at index 3 of my_list and another_list the same object?
"""

#1

print(my_list == another_list)

#yes

#2. NO, bc the list constructor function always returns a NEW list.
print(my_list is another_list)


#3 Yes, since the lists themselves are equal
print(my_list[3] == another_list[3])

#4. Shallow copies do not include nested collections; nested mutable collections
print(my_list[3] is another_list[3])
#Yes, they are the same