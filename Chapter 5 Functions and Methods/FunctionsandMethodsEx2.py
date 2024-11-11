
#What does this print?

foo = 'bar'  #global

def set_foo():
    foo = 'qux'

set_foo()
print(foo)

#The program prints bar bc the assignment on line 7 creates a new variable that is local to the function - the foo
#variable on line 7 shadows the foo variable on line 4, so line 7 doesn't change the value of foo from line 4.