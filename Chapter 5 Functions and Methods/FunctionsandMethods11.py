#Without running the following code, what do you think it will do?

def foo(first, second=3, third=2):
    print(first)
    print(second)
    print(third)

foo(42)

#We've defined foo with 3 parameters, with a default parameter for the second and third parameters. We've passed the
#function one argument, so Python uses the default value for the last two parameters.