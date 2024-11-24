#Write Python code to create a new tuple from (1, 2, 3, 4, 5). The new tuple should be in reverse order from
# the original. It should also exclude the first and last members of the original.
# The result should be the tuple (4, 3, 2).

my_tuple = (1, 2, 3, 4, 5)


#Option 1
#Tuples are immmutable so can't reverse, but you can convert to a list - which is mutable
"""
my_list = list(my_tuple)
my_list.reverse()
print(my_list)
print(my_list[1:4])
result = tuple(my_list[1:4])
print(result)
"""

#Option 2
result = my_tuple[3:0:-1]
print(result)



tup = (1, 2, 3)
lst = [1, 2, 3]

lst[0] = 0

"""

Identify at least 2 differences between lists and tuples. 
Identify at least 2 ways that lists and tuples are similar.

Similarities: They are both ordered collections, therefore they can be referenced by index. 
They are both heterogeneous

Differences: Tuples are immutable, Lists are mutable; Tuples use square bracket syntax; Lists use parenthesis syntax ().

"""