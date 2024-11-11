#Without running the following code, what do you think it will do?

def foo(first, second=3, third):
    print(first)
    print(second)
    print(third)

foo(42)

#This will raise a Syntax error, whenever you have a default values it must be followed by more default values. Default
#values can only be put at the end
