#Without running the following code, what do you think it will do?

def foo(first, second=3, third=2):
    print(first)
    print(second)
    print(third)

foo(42, 3.141592, 2.718)

#We've defined foo with three parameters, with the second and third parameters having default values. Python ignores the
#default values in this case because we passed in specific values from the second and third argument