#What does this code output, and why?

def is_list_empty(my_list):
    if my_list:
        print('Not Empty')
    else:
        print('Empty')

is_list_empty([]) #If my_list is truthy, then the if branch will execute, otherwise the else branch will execute.
is_list_empty([False]) #Not Empty
is_list_empty([1, 2, 3])


