#Write a function called increment_counter that increments a counter variable every time it is called.
# You can test your code with the following:

counter = 0
def increment_counter():
    global counter  #otherwise it assumes it's initalizing a local variable that is local to that function (which is undefined at this point)
    counter += 1


print(counter)                # 0

increment_counter()
print(counter)                # 1

increment_counter()
print(counter)                # 2

counter = 100
increment_counter()
print(counter)                # 101

#If we want to change the global variable in ANY way, you must explicitly write the global keyword