#Can you write some code to change the value 'bye' in the following tuple to 'goodbye'?

# stuff = ('hello', 'world', 'bye', 'now')
#
# print(stuff[0:2] + stuff[0:2])
#
# stuff = list(stuff)
# stuff[2] = 'goodbye'
# stuff = tuple(stuff)
#
# #Tuples are immutable
# #[lists are immutable
#
# #First change it into a list (mutable), and then change it back into a Tuple)
#

# my_str = "Launch School"
# print(my_str[4:10])

numbers = [1, 2, 3, 4, 5]
squares = []
squares2 = []

# for number in numbers:
#     squares.append(number * number)

squares = [(number * number) for number in numbers]
print(squares)
print(squares2)