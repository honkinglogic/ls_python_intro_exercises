#Write a comprehension that creates a dict object whose keys are strings and whose values are the length of the
#corresponding key. Only keys with odd lengths should be in the dict. Use the set given by my_set as the source of strings.

my_set = {
    'Fluffy',
    'Butterscotch',
    'Pudding',
    'Cheddar',
    'Cocoa',
}
#

result = { name: len(name)
           for name in my_set
           if len(name) % 2 != 0}
print(result)


#[expression for value in iterable if condition]
#dictionary = {key: expression for (key, value) in iterable}

# # { key: value for item in collection
# #        if condition}
# #my_dict = {xxx for x in my_set}
#
# #   With a regular for loop:
# # result = {}
# # for key in my_set:
# #     if len(key) % 2 != 0:
# #         result[key] = len(key)
# # print(result)
#
# #With a comprehension:
# result = { name: len(name)
#            for name in my_set
#            if len(name) % 2 != 0}
# print(result)