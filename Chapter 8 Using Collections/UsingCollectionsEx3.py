#Write Python code to create a new tuple from (1, 2, 3, 4, 5). The new tuple should be in reverse order from the original.
# It should also exclude the first and last members of the original. The result should be the tuple (4, 3, 2).
from audioop import reverse

#Method 1:
# my_tuple = (1, 2, 3, 4, 5)
# my_list = list(my_tup)
# my_list.reverse()
#
#
# print(my_list[1:4])
# result = tuple(my_list[1:4])
# print(result)


#Method 2:
my_tuple = (1, 2, 3, 4, 5)
result = my_tuple[3:0:-1]
print(result)

#Method 3:
my_tuple = (1, 2, 3, 4, 5)
result = my_tuple[-2:0:-1]
print(result)