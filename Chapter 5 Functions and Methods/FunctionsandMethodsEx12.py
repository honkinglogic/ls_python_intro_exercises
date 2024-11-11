#Without running the following code, what do you think it will do?

def foo(first, second=3, third=2):
    print(first)
    print(second)
    print(third)

foo()

#This will raise an error because no arguments are provided, we need to provide a minimum of one argument given that the
#second and third parameters have default values