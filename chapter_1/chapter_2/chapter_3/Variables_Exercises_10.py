#Assume that obj already has a value of 42 when the code below starts running. Which of the subsequent statements
# reassign the variable? Which statements mutate the value of the object that obj references? Which statements do
# neither? If necessary, you can read the documentation.

#First attempt

#obj = 42
obj = 'ABcd'        #reassign
obj.upper()         #mutate
obj = obj.lower()   #mutate
print(len(obj))     #neither
obj = list(obj)     #neither
obj.pop()           #mutate
obj[2] = 'X'        #mutate
obj.sort()          #mutate
set(obj)            #neither
obj = tuple(obj)    #neither

#Correct Answers
#strings and integers are immutable

#obj = '[a, b, c, d']

obj = 'ABcd'        #reassignment
obj.upper()         #Neither = we don't reassign it, obs still references the same string
obj = obj.lower()   #reassignment
print(len(obj))     #neither - just prints out
obj = list(obj)     #reassignment - bc there is an equal sign, returns a new list
obj.pop()           #mutation - this is a mutating method call
obj[2] = 'X'        #mutation
obj.sort()          #mutation
set(obj)            #neither
obj = tuple(obj)    #neither