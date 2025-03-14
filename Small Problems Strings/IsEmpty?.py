#Write a function that checks whether a string is empty or not. For example:

def is_empty(s):
    return s == ''

print(is_empty('mars'))  # False
print(is_empty('  '))    # False
print(is_empty(''))      # True

#Incorrectly uses print here rather than return
# def is_empty(a):
#     if len(a) > 0:
#         return print('False')
#     else:
#         return print('True')

#Other solutions:

def is_empty(s):
    return len(s) == 0

#most pythonic:
def is_empty(s):
    return not s